import os
import io
import json
import zipfile
import shutil
from xml.etree import ElementTree as ET
from PIL import Image

PPTX_PATH = "/Users/israeltorres/Downloads/NEW Official GSlides Template - Artefact - November 2024.pptx"
BASE_DIR = "/Users/israeltorres/Documents/antigravity/calm-babbage"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
TOKENS_DIR = os.path.join(BASE_DIR, "tokens")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

ns = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships"
}

def extract_raster_media(z):
    print("--- Extracting Raster Media Assets ---")
    
    # 1. Logos
    logos_map = {
        "ppt/media/image12.png": "artefact_logo_primary_dark.png",
        "ppt/media/image57.png": "artefact_logo_primary_white.png",
        "ppt/media/image21.png": "artefact_logo_horizontal_dark.png",
        "ppt/media/image3.png": "artefact_logo_horizontal_white.png",
        "ppt/media/image61.png": "artefact_monogram_a_dark.png",
        "ppt/media/image4.png": "artefact_monogram_a_white.png",
        "ppt/media/image10.png": "artefact_logo_tagline_white.png",
        "ppt/media/image27.png": "artefact_logo_white_square_tagline.png",
        "ppt/media/image23.png": "artefact_wordmark_large_gradient.png",
        "ppt/media/image26.png": "artefact_wordmark_outline.png",
        "ppt/media/image31.png": "artefact_logo_stacked_gradient.png"
    }
    
    target_logos_dir = os.path.join(ASSETS_DIR, "logos")
    os.makedirs(target_logos_dir, exist_ok=True)
    for src, dst in logos_map.items():
        if src in z.namelist():
            with open(os.path.join(target_logos_dir, dst), "wb") as f:
                f.write(z.read(src))
    print(f"Logos extracted: {len(logos_map)}")

    # 2. 3D Glassy Icons (Slide 69)
    glassy_map = {
        "ppt/media/image67.png": "icon_glassy_data_foundations_bi.png",
        "ppt/media/image68.png": "icon_glassy_ai_acceleration.png",
        "ppt/media/image69.png": "icon_glassy_it_data_platform.png",
        "ppt/media/image74.png": "icon_glassy_strategy_transformation.png",
        "ppt/media/image76.png": "icon_glassy_cx_digital_marketing.png",
        "ppt/media/image80.png": "icon_glassy_marketing_datadriven.png",
        "ppt/media/image73.png": "icon_glassy_iconic_a.png",
        "ppt/media/image85.png": "icon_glassy_people.png",
        "ppt/media/image84.png": "icon_glassy_clients.png",
        "ppt/media/image17.png": "icon_glassy_ai_hero_large.png",
        "ppt/media/image20.png": "icon_glassy_data_hero_large.png",
        "ppt/media/image24.png": "icon_glassy_marketing_hero_large.png"
    }
    
    target_glassy_dir = os.path.join(ASSETS_DIR, "icons", "glassy_3d")
    os.makedirs(target_glassy_dir, exist_ok=True)
    for src, dst in glassy_map.items():
        if src in z.namelist():
            with open(os.path.join(target_glassy_dir, dst), "wb") as f:
                f.write(z.read(src))
    print(f"Glassy 3D icons extracted: {len(glassy_map)}")

    # 3. Non-editable UI Icons (Slide 94)
    slide94_rels = get_slide_rels(z, 94)
    s94_tree = ET.fromstring(z.read("ppt/slides/slide94.xml"))
    target_ui_dir = os.path.join(ASSETS_DIR, "icons", "ui_flat")
    os.makedirs(target_ui_dir, exist_ok=True)
    
    ui_icons = []
    idx = 1
    for pic in s94_tree.findall(".//p:pic", ns):
        blip = pic.find(".//a:blip", ns)
        if blip is not None:
            embed = blip.attrib.get(f"{{{ns['r']}}}embed")
            target = slide94_rels.get(embed)
            if target:
                media_path = "ppt/" + target.replace("../", "")
                if media_path in z.namelist():
                    out_name = f"icon_ui_{idx:02d}.png"
                    with open(os.path.join(target_ui_dir, out_name), "wb") as f:
                        f.write(z.read(media_path))
                    ui_icons.append((out_name, media_path))
                    idx += 1
    print(f"UI flat icons extracted: {len(ui_icons)}")

    # 4. Symbol Templates (Slide 95)
    slide95_rels = get_slide_rels(z, 95)
    s95_tree = ET.fromstring(z.read("ppt/slides/slide95.xml"))
    target_symbols_dir = os.path.join(ASSETS_DIR, "icons", "symbols")
    os.makedirs(target_symbols_dir, exist_ok=True)
    
    symbol_icons = []
    idx = 1
    for pic in s95_tree.findall(".//p:pic", ns):
        blip = pic.find(".//a:blip", ns)
        if blip is not None:
            embed = blip.attrib.get(f"{{{ns['r']}}}embed")
            target = slide95_rels.get(embed)
            if target:
                media_path = "ppt/" + target.replace("../", "")
                if media_path in z.namelist():
                    out_name = f"symbol_banner_{idx:02d}.png"
                    with open(os.path.join(target_symbols_dir, out_name), "wb") as f:
                        f.write(z.read(media_path))
                    symbol_icons.append((out_name, media_path))
                    idx += 1
    print(f"Symbol banners extracted: {len(symbol_icons)}")

    # 5. Trimmed PNG Cutouts (Slide 70)
    slide70_rels = get_slide_rels(z, 70)
    s70_tree = ET.fromstring(z.read("ppt/slides/slide70.xml"))
    target_cutouts_dir = os.path.join(ASSETS_DIR, "cutouts")
    os.makedirs(target_cutouts_dir, exist_ok=True)
    
    cutouts = []
    idx = 1
    for pic in s70_tree.findall(".//p:pic", ns):
        blip = pic.find(".//a:blip", ns)
        if blip is not None:
            embed = blip.attrib.get(f"{{{ns['r']}}}embed")
            target = slide70_rels.get(embed)
            if target:
                media_path = "ppt/" + target.replace("../", "")
                if media_path in z.namelist():
                    out_name = f"cutout_{idx:02d}.png"
                    with open(os.path.join(target_cutouts_dir, out_name), "wb") as f:
                        f.write(z.read(media_path))
                    cutouts.append((out_name, media_path))
                    idx += 1
    print(f"Cutouts extracted: {len(cutouts)}")

    # 6. Photography by Industry & Sustainability (Slides 71-84)
    target_photo_dir = os.path.join(ASSETS_DIR, "photography")
    os.makedirs(target_photo_dir, exist_ok=True)
    
    photo_count = 0
    for s_idx in range(71, 85):
        s_rels = get_slide_rels(z, s_idx)
        s_file = f"ppt/slides/slide{s_idx}.xml"
        if s_file in z.namelist():
            stree = ET.fromstring(z.read(s_file))
            for pic in stree.findall(".//p:pic", ns):
                blip = pic.find(".//a:blip", ns)
                if blip is not None:
                    embed = blip.attrib.get(f"{{{ns['r']}}}embed")
                    target = s_rels.get(embed)
                    if target:
                        media_path = "ppt/" + target.replace("../", "")
                        if media_path in z.namelist():
                            ext = os.path.splitext(media_path)[1].lower()
                            out_name = f"photo_slide{s_idx}_{os.path.basename(media_path)}"
                            with open(os.path.join(target_photo_dir, out_name), "wb") as f:
                                f.write(z.read(media_path))
                            photo_count += 1
    print(f"Industry & Sustainability photos extracted: {photo_count}")

def get_slide_rels(z, slide_idx):
    rels_file = f"ppt/slides/_rels/slide{slide_idx}.xml.rels"
    rels = {}
    if rels_file in z.namelist():
        tree = ET.fromstring(z.read(rels_file))
        for elem in tree.findall(f"{{{ns['rel']}}}Relationship"):
            rels[elem.attrib.get("Id")] = elem.attrib.get("Target")
    return rels

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
    
    # Normalize coordinate origin to (0,0) by subtracting ch_x, ch_y
    paths_data = []
    for sp in group_elem.findall(".//p:sp", ns):
        sp_pr = sp.find("p:spPr", ns)
        if sp_pr is None:
            continue
        sp_xfrm = sp_pr.find("a:xfrm", ns)
        sp_off = sp_xfrm.find("a:off", ns) if sp_xfrm is not None else None
        sp_ext = sp_xfrm.find("a:ext", ns) if sp_xfrm is not None else None
        
        sp_x = (float(sp_off.attrib.get("x", ch_x)) - ch_x) if sp_off is not None else 0
        sp_y = (float(sp_off.attrib.get("y", ch_y)) - ch_y) if sp_off is not None else 0
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
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ch_w:.2f} {ch_h:.2f}" width="100%" height="100%">'
    ]
    for d, f, s, sw in paths_data:
        s_attr = f' stroke="{s}" stroke-width="{sw}"' if s != "none" else ""
        svg_lines.append(f'  <path d="{d}" fill="{f}"{s_attr} />')
    svg_lines.append('</svg>')
    
    return "\n".join(svg_lines)

def extract_vector_icons(z):
    print("--- Extracting Vector Icons as SVG ---")
    target_vec_dir = os.path.join(ASSETS_DIR, "icons", "vector_svg")
    os.makedirs(target_vec_dir, exist_ok=True)
    
    total_svg = 0
    for s_idx in [90, 91, 92, 93]:
        s_file = f"ppt/slides/slide{s_idx}.xml"
        if s_file in z.namelist():
            tree = ET.fromstring(z.read(s_file))
            groups = tree.findall(".//p:grpSp", ns)
            for i, g in enumerate(groups):
                svg = convert_group_to_svg(g, i, s_idx)
                if svg:
                    out_name = f"vector_icon_s{s_idx}_{i+1:02d}.svg"
                    with open(os.path.join(target_vec_dir, out_name), "w") as f:
                        f.write(svg)
                    total_svg += 1
    print(f"Total SVG vector icons extracted: {total_svg}")

def generate_tokens():
    print("--- Generating Design Tokens ---")
    os.makedirs(TOKENS_DIR, exist_ok=True)
    
    colors_data = {
        "brand": {
            "name": "Artefact",
            "version": "November 2024",
            "description": "Artefact Brand Design System Tokens"
        },
        "corporate_colors": {
            "artefact_blue": {
                "hex": "#002244",
                "rgb": "rgb(0, 34, 68)",
                "hsl": "hsl(210, 100%, 13%)",
                "role": "Primary Corporate Dark Blue / Main text and branding"
            },
            "artefact_pink": {
                "hex": "#FF0066",
                "rgb": "rgb(255, 0, 102)",
                "hsl": "hsl(336, 100%, 50%)",
                "role": "Primary Corporate Accent / Hyperlink & Highlights"
            }
        },
        "secondary_colors": {
            "dark_blue": {
                "hex": "#0D1634",
                "rgb": "rgb(13, 22, 52)",
                "hsl": "hsl(226, 60%, 13%)",
                "role": "Deep Midnight Background / Dark Mode Slide Background"
            },
            "medium_blue": {
                "hex": "#273275",
                "rgb": "rgb(39, 50, 117)",
                "hsl": "hsl(232, 50%, 31%)",
                "role": "Secondary Royal Indigo Blue / Accent 1"
            },
            "purple": {
                "hex": "#752E7D",
                "rgb": "rgb(117, 46, 125)",
                "hsl": "hsl(294, 44%, 34%)",
                "role": "Secondary Aubergine Magenta / Accent 2"
            }
        },
        "data_visualization_and_accents": {
            "electric_blue": {
                "hex": "#052BF6",
                "rgb": "rgb(5, 43, 246)",
                "role": "Vibrant Electric Blue (Accent 4 / Data Series 1)"
            },
            "bright_purple": {
                "hex": "#9900FF",
                "rgb": "rgb(153, 0, 255)",
                "role": "Vibrant Purple (Accent 5 / Data Series 2)"
            },
            "cyan_teal": {
                "hex": "#0097A7",
                "rgb": "rgb(0, 151, 167)",
                "role": "Teal / Link hover"
            },
            "amber_gold": {
                "hex": "#FFAB40",
                "rgb": "rgb(255, 171, 64)",
                "role": "Amber Accent"
            }
        },
        "neutral_colors": {
            "white": {
                "hex": "#FFFFFF",
                "rgb": "rgb(255, 255, 255)",
                "role": "Light background & high-contrast dark-mode text"
            },
            "light_gray_bg": {
                "hex": "#F4F6F9",
                "rgb": "rgb(244, 246, 249)",
                "role": "Card container backgrounds"
            },
            "card_border": {
                "hex": "#EEEEEE",
                "rgb": "rgb(238, 238, 238)",
                "role": "Subtle borders and dividers"
            },
            "medium_gray_text": {
                "hex": "#595959",
                "rgb": "rgb(89, 89, 89)",
                "role": "Secondary body text / legends"
            },
            "dark_gray_text": {
                "hex": "#212121",
                "rgb": "rgb(33, 33, 33)",
                "role": "Neutral dark body copy"
            }
        },
        "gradients": {
            "artefact_signature_gradient": {
                "css": "linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%)",
                "stops": [
                    {"offset": "0%", "color": "#002244", "name": "Artefact Blue"},
                    {"offset": "33%", "color": "#273275", "name": "Medium Blue"},
                    {"offset": "66%", "color": "#752E7D", "name": "Purple"},
                    {"offset": "100%", "color": "#FF0066", "name": "Artefact Pink"}
                ],
                "role": "Hero presentation slides, section dividers, cover backgrounds"
            },
            "blue_depth_gradient": {
                "css": "linear-gradient(180deg, #0D1634 0%, #002244 100%)",
                "stops": [
                    {"offset": "0%", "color": "#0D1634"},
                    {"offset": "100%", "color": "#002244"}
                ],
                "role": "Dark slide backgrounds"
            }
        }
    }
    
    with open(os.path.join(TOKENS_DIR, "colors.json"), "w") as f:
        json.dump(colors_data, f, indent=2)
        
    typography_data = {
        "font_family": {
            "primary": "Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
            "weights": {
                "thin": 100,
                "light": 300,
                "regular": 400,
                "medium": 500,
                "bold": 700,
                "black": 900
            }
        },
        "hierarchy": {
            "slide_title": {
                "font_weight": "Roboto Normal (400)",
                "font_size_pt": 20,
                "font_size_px": 27,
                "line_height": 1.2,
                "color_light_bg": "#002244",
                "color_dark_bg": "#FFFFFF"
            },
            "slide_subtitle": {
                "font_weight": "Roboto Bold (700)",
                "font_size_pt": 14,
                "font_size_px": 19,
                "line_height": 1.3,
                "color_light_bg": "#002244",
                "color_dark_bg": "#FFFFFF"
            },
            "section_header": {
                "font_weight": "Roboto Bold (700)",
                "font_size_pt": 16,
                "font_size_px": 21,
                "line_height": 1.3
            },
            "body_text": {
                "font_weight": "Roboto Normal (400)",
                "font_size_pt": 12,
                "font_size_px": 16,
                "line_height": 1.4,
                "color_light_bg": "#212121",
                "color_dark_bg": "#E0E0E0"
            },
            "legend_source": {
                "font_weight": "Roboto Medium (500)",
                "font_size_pt": 10,
                "font_size_px": 13,
                "line_height": 1.3,
                "color_light_bg": "#595959",
                "color_dark_bg": "#A0A0A0"
            },
            "kpi_metric": {
                "font_weight": "Roboto Black (900)",
                "font_size_pt": 36,
                "font_size_px": 48,
                "line_height": 1.0,
                "color": "#FF0066"
            }
        }
    }
    
    with open(os.path.join(TOKENS_DIR, "typography.json"), "w") as f:
        json.dump(typography_data, f, indent=2)
        
    css_content = """/* Artefact Brand Design System Tokens - Official November 2024 */
:root {
  /* Corporate Colors */
  --artefact-blue: #002244;
  --artefact-pink: #FF0066;
  
  /* Secondary Colors */
  --artefact-dark-blue: #0D1634;
  --artefact-medium-blue: #273275;
  --artefact-purple: #752E7D;
  
  /* Accents & Data Viz */
  --artefact-electric-blue: #052BF6;
  --artefact-bright-purple: #9900FF;
  --artefact-teal: #0097A7;
  --artefact-amber: #FFAB40;
  
  /* Neutrals */
  --artefact-white: #FFFFFF;
  --artefact-gray-light: #F4F6F9;
  --artefact-gray-border: #EEEEEE;
  --artefact-gray-muted: #595959;
  --artefact-charcoal: #212121;
  
  /* Gradients */
  --artefact-gradient-signature: linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);
  --artefact-gradient-horizontal: linear-gradient(90deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);
  --artefact-gradient-dark: linear-gradient(180deg, #0D1634 0%, #002244 100%);
  
  /* Typography */
  --font-family-artefact: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  
  /* Font Sizes */
  --fs-title: 20pt;
  --fs-subtitle: 14pt;
  --fs-body: 12pt;
  --fs-legend: 10pt;
  --fs-kpi: 36pt;
  
  /* Font Weights */
  --fw-thin: 100;
  --fw-light: 300;
  --fw-normal: 400;
  --fw-medium: 500;
  --fw-bold: 700;
  --fw-black: 900;
}
"""
    with open(os.path.join(TOKENS_DIR, "artefact_theme.css"), "w") as f:
        f.write(css_content)

def main():
    print(f"Reading PPTX archive from {PPTX_PATH}...")
    with zipfile.ZipFile(PPTX_PATH, "r") as z:
        extract_raster_media(z)
        extract_vector_icons(z)
        generate_tokens()
    print("Done extracting assets & tokens!")

if __name__ == "__main__":
    main()
