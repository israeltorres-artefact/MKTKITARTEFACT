import zipfile, os
from xml.etree import ElementTree as ET

ns = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main"
}

def drawingml_path_to_svg_d(path_elem, w, h, off_x=0, off_y=0):
    pw = float(path_elem.attrib.get("w", w or 1))
    ph = float(path_elem.attrib.get("h", h or 1))
    scale_x = float(w) / pw if pw else 1.0
    scale_y = float(h) / ph if ph else 1.0
    
    d = []
    for cmd in path_elem:
        tag = cmd.tag.split("}")[-1]
        if tag == "moveTo":
            pt = cmd.find("a:pt", ns)
            if pt is not None:
                x = off_x + float(pt.attrib["x"]) * scale_x
                y = off_y + float(pt.attrib["y"]) * scale_y
                d.append(f"M {x:.2f} {y:.2f}")
        elif tag == "lnTo":
            pt = cmd.find("a:pt", ns)
            if pt is not None:
                x = off_x + float(pt.attrib["x"]) * scale_x
                y = off_y + float(pt.attrib["y"]) * scale_y
                d.append(f"L {x:.2f} {y:.2f}")
        elif tag == "cubicBezTo":
            pts = cmd.findall("a:pt", ns)
            coords = []
            for pt in pts:
                x = off_x + float(pt.attrib["x"]) * scale_x
                y = off_y + float(pt.attrib["y"]) * scale_y
                coords.append(f"{x:.2f} {y:.2f}")
            c_str = " ".join(coords)
            d.append(f"C {c_str}")
        elif tag == "close":
            d.append("Z")
    return " ".join(d)

def convert_group_to_svg(group_elem, group_idx, slide_idx):
    grp_pr = group_elem.find("p:grpSpPr", ns)
    xfrm = grp_pr.find("a:xfrm", ns) if grp_pr is not None else None
    
    ch_off = xfrm.find("a:chOff", ns) if xfrm is not None else None
    ch_ext = xfrm.find("a:chExt", ns) if xfrm is not None else None
    
    ch_x = float(ch_off.attrib.get("x", 0)) if ch_off is not None else 0
    ch_y = float(ch_off.attrib.get("y", 0)) if ch_off is not None else 0
    ch_w = float(ch_ext.attrib.get("cx", 100)) if ch_ext is not None else 100
    ch_h = float(ch_ext.attrib.get("cy", 100)) if ch_ext is not None else 100
    
    if ch_w <= 0: ch_w = 100
    if ch_h <= 0: ch_h = 100
    
    paths_data = []
    for sp in group_elem.findall(".//p:sp", ns):
        sp_pr = sp.find("p:spPr", ns)
        if sp_pr is None:
            continue
        sp_xfrm = sp_pr.find("a:xfrm", ns)
        sp_off = sp_xfrm.find("a:off", ns) if sp_xfrm is not None else None
        sp_ext = sp_xfrm.find("a:ext", ns) if sp_xfrm is not None else None
        
        sp_x = float(sp_off.attrib.get("x", 0)) if sp_off is not None else 0
        sp_y = float(sp_off.attrib.get("y", 0)) if sp_off is not None else 0
        sp_w = float(sp_ext.attrib.get("cx", ch_w)) if sp_ext is not None else ch_w
        sp_h = float(sp_ext.attrib.get("cy", ch_h)) if sp_ext is not None else ch_h
        
        # Color fill
        fill_clr = "#002244"
        solid_fill = sp_pr.find("a:solidFill", ns)
        if solid_fill is not None:
            srgb = solid_fill.find("a:srgbClr", ns)
            if srgb is not None:
                fill_clr = f"#{srgb.attrib.get('val')}"
            else:
                scheme = solid_fill.find("a:schemeClr", ns)
                if scheme is not None:
                    sval = scheme.attrib.get("val")
                    if sval in ("accent3", "lt2"): fill_clr = "#FF0066"
                    elif sval in ("accent1",): fill_clr = "#273275"
                    elif sval in ("accent2",): fill_clr = "#752E7D"
                    else: fill_clr = "#002244"
        elif sp_pr.find("a:noFill", ns) is not None:
            fill_clr = "none"
            
        stroke_clr = "none"
        stroke_w = 0
        ln = sp_pr.find("a:ln", ns)
        if ln is not None:
            w_attr = ln.attrib.get("w")
            stroke_w = max(1.0, float(w_attr)/12700.0) if w_attr else 1.5
            ln_srgb = ln.find(".//a:srgbClr", ns)
            if ln_srgb is not None:
                stroke_clr = f"#{ln_srgb.attrib.get('val')}"
            else:
                stroke_clr = fill_clr if fill_clr != "none" else "#002244"

        cust_geom = sp_pr.find("a:custGeom", ns)
        if cust_geom is not None:
            path_lst = cust_geom.find("a:pathLst", ns)
            if path_lst is not None:
                for path in path_lst.findall("a:path", ns):
                    d = drawingml_path_to_svg_d(path, sp_w, sp_h, sp_x, sp_y)
                    if d:
                        paths_data.append((d, fill_clr, stroke_clr, stroke_w))
                        
    if not paths_data:
        return None
        
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{ch_x} {ch_y} {ch_w} {ch_h}" width="100%" height="100%">'
    ]
    for d, f, s, sw in paths_data:
        s_attr = f' stroke="{s}" stroke-width="{sw}"' if s != "none" else ""
        svg_lines.append(f'  <path d="{d}" fill="{f}"{s_attr} />')
    svg_lines.append('</svg>')
    
    return "\n".join(svg_lines)

pptx_path = "/Users/israeltorres/Downloads/NEW Official GSlides Template - Artefact - November 2024.pptx"
with zipfile.ZipFile(pptx_path, "r") as z:
    count = 0
    for s_idx in [90, 91, 92, 93]:
        s_file = f"ppt/slides/slide{s_idx}.xml"
        tree = ET.fromstring(z.read(s_file))
        groups = tree.findall(".//p:grpSp", ns)
        for i, g in enumerate(groups):
            svg = convert_group_to_svg(g, i, s_idx)
            if svg:
                out_path = f"/Users/israeltorres/Documents/antigravity/calm-babbage/assets/icons/vector_svg/vector_icon_s{s_idx}_{i+1:02d}.svg"
                with open(out_path, "w") as f:
                    f.write(svg)
                count += 1
    print(f"Successfully exported {count} SVG vector icons!")
