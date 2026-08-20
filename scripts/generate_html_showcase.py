import os, glob

BASE_DIR = "/Users/israeltorres/Documents/antigravity/calm-babbage"

svg_files = sorted(glob.glob(os.path.join(BASE_DIR, "assets/icons/vector_svg/*.svg")))
glassy_files = sorted(glob.glob(os.path.join(BASE_DIR, "assets/icons/glassy_3d/*.png")))
ui_files = sorted(glob.glob(os.path.join(BASE_DIR, "assets/icons/ui_flat/*.png")))
logo_files = sorted(glob.glob(os.path.join(BASE_DIR, "assets/logos/*.png")))
cutout_files = sorted(glob.glob(os.path.join(BASE_DIR, "assets/cutouts/*.png")))

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Artefact Brand System & Asset Library (Nov 2024)</title>
  <link rel="stylesheet" href="tokens/artefact_theme.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: var(--font-family-artefact);
      background: #F8F9FA;
      color: var(--artefact-charcoal);
      line-height: 1.5;
      padding: 40px 20px;
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
    }}
    header {{
      background: var(--artefact-gradient-signature);
      color: white;
      padding: 40px;
      border-radius: 16px;
      margin-bottom: 40px;
      box-shadow: 0 10px 30px rgba(0, 34, 68, 0.15);
    }}
    header h1 {{
      font-size: 32pt;
      font-weight: 300;
      margin-bottom: 8px;
    }}
    header p {{
      font-size: 14pt;
      opacity: 0.9;
    }}
    .section-title {{
      font-size: 20pt;
      font-weight: 700;
      color: var(--artefact-blue);
      margin: 40px 0 20px 0;
      border-bottom: 2px solid var(--artefact-gray-border);
      padding-bottom: 8px;
    }}
    .grid-colors {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 20px;
      margin-bottom: 30px;
    }}
    .color-card {{
      background: white;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
      border: 1px solid var(--artefact-gray-border);
    }}
    .color-swatch {{
      height: 100px;
      width: 100%;
    }}
    .color-info {{
      padding: 14px;
    }}
    .color-name {{
      font-weight: 700;
      font-size: 11pt;
      color: var(--artefact-blue);
      margin-bottom: 4px;
    }}
    .color-hex {{
      font-family: monospace;
      font-size: 10pt;
      color: var(--artefact-gray-muted);
    }}
    .gradient-bar {{
      height: 60px;
      border-radius: 12px;
      background: var(--artefact-gradient-signature);
      margin-bottom: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    .grid-assets {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
      gap: 16px;
      margin-bottom: 30px;
    }}
    .asset-card {{
      background: white;
      border: 1px solid var(--artefact-gray-border);
      border-radius: 12px;
      padding: 16px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .asset-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }}
    .asset-card img, .asset-card svg {{
      max-width: 100px;
      max-height: 100px;
      object-fit: contain;
      margin-bottom: 12px;
    }}
    .asset-card.dark-bg {{
      background: var(--artefact-dark-blue);
      color: white;
    }}
    .asset-name {{
      font-size: 9pt;
      font-weight: 500;
      word-break: break-word;
      color: var(--artefact-gray-muted);
    }}
    .asset-card.dark-bg .asset-name {{
      color: #E0E0E0;
    }}
    .typography-demo {{
      background: white;
      padding: 24px;
      border-radius: 12px;
      border: 1px solid var(--artefact-gray-border);
      margin-bottom: 30px;
    }}
    .type-row {{
      margin-bottom: 16px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--artefact-gray-border);
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>Artefact Brand System</h1>
      <p>Biblioteca de Identidad Visual, Paleta Cromática y Catálogo de Iconos — Noviembre 2024</p>
    </header>

    <h2 class="section-title">1. Paleta de Colores & Degradados</h2>
    <div class="gradient-bar"></div>
    <div class="grid-colors">
      <div class="color-card">
        <div class="color-swatch" style="background:#002244;"></div>
        <div class="color-info">
          <div class="color-name">Artefact Blue</div>
          <div class="color-hex">#002244</div>
        </div>
      </div>
      <div class="color-card">
        <div class="color-swatch" style="background:#FF0066;"></div>
        <div class="color-info">
          <div class="color-name">Artefact Pink</div>
          <div class="color-hex">#FF0066</div>
        </div>
      </div>
      <div class="color-card">
        <div class="color-swatch" style="background:#0D1634;"></div>
        <div class="color-info">
          <div class="color-name">Dark Blue</div>
          <div class="color-hex">#0D1634</div>
        </div>
      </div>
      <div class="color-card">
        <div class="color-swatch" style="background:#273275;"></div>
        <div class="color-info">
          <div class="color-name">Medium Blue</div>
          <div class="color-hex">#273275</div>
        </div>
      </div>
      <div class="color-card">
        <div class="color-swatch" style="background:#752E7D;"></div>
        <div class="color-info">
          <div class="color-name">Purple</div>
          <div class="color-hex">#752E7D</div>
        </div>
      </div>
    </div>

    <h2 class="section-title">2. Logotipos Oficiales ({len(logo_files)})</h2>
    <div class="grid-assets">
"""

for lf in logo_files:
    rel_path = os.path.relpath(lf, BASE_DIR)
    bname = os.path.basename(lf)
    is_dark = "white" in bname
    dark_class = "dark-bg" if is_dark else ""
    html += f"""      <div class="asset-card {dark_class}">
        <img src="{rel_path}" alt="{bname}">
        <span class="asset-name">{bname}</span>
      </div>
"""

html += f"""    </div>

    <h2 class="section-title">3. Iconos 3D Glassy de Áreas de Práctica ({len(glassy_files)})</h2>
    <div class="grid-assets">
"""

for gf in glassy_files:
    rel_path = os.path.relpath(gf, BASE_DIR)
    bname = os.path.basename(gf)
    html += f"""      <div class="asset-card">
        <img src="{rel_path}" alt="{bname}">
        <span class="asset-name">{bname.replace('icon_glassy_', '').replace('.png', '').replace('_', ' ').title()}</span>
      </div>
"""

html += f"""    </div>

    <h2 class="section-title">4. Iconos Planos de UI ({len(ui_files)})</h2>
    <div class="grid-assets">
"""

for uf in ui_files:
    rel_path = os.path.relpath(uf, BASE_DIR)
    bname = os.path.basename(uf)
    html += f"""      <div class="asset-card">
        <img src="{rel_path}" alt="{bname}">
        <span class="asset-name">{bname}</span>
      </div>
"""

html += f"""    </div>

    <h2 class="section-title">5. Iconos Vectoriales SVG Editables ({len(svg_files)})</h2>
    <div class="grid-assets">
"""

for sf in svg_files[:60]: # showcase first 60 SVGs in main grid
    rel_path = os.path.relpath(sf, BASE_DIR)
    bname = os.path.basename(sf)
    html += f"""      <div class="asset-card" style="background:#002244; color:white;">
        <img src="{rel_path}" alt="{bname}" style="filter: brightness(0) invert(1);">
        <span class="asset-name" style="color:#A0A0A0;">{bname}</span>
      </div>
"""

html += f"""    </div>
    <p style="text-align:center; color:var(--artefact-gray-muted); margin-bottom:40px;">Mostrando primeros 60 de {len(svg_files)} iconos vectoriales SVG disponibles en <code>assets/icons/vector_svg/</code>.</p>

    <h2 class="section-title">6. Jerarquía Tipográfica (Roboto)</h2>
    <div class="typography-demo">
      <div class="type-row">
        <div style="font-size:20pt; font-weight:400; color:var(--artefact-blue);">Título de Diapositiva — Roboto Normal 20pt</div>
        <div style="font-size:9pt; color:var(--artefact-gray-muted);">Uso: Título principal de cada lámina.</div>
      </div>
      <div class="type-row">
        <div style="font-size:14pt; font-weight:700; color:var(--artefact-blue);">Subtítulo de Diapositiva — Roboto Bold 14pt</div>
        <div style="font-size:9pt; color:var(--artefact-gray-muted);">Uso: Contexto y anclaje bajo el título principal.</div>
      </div>
      <div class="type-row">
        <div style="font-size:12pt; font-weight:400; color:var(--artefact-charcoal);">Cuerpo de texto y descripción analítica — Roboto Normal 12pt. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
        <div style="font-size:9pt; color:var(--artefact-gray-muted);">Uso: Párrafos de lectura extendida y contenido de tarjetas.</div>
      </div>
      <div class="type-row">
        <div style="font-size:10pt; font-weight:500; color:var(--artefact-gray-muted);">Fuente: Artefact Data & AI Consulting — Roboto Medium 10pt</div>
        <div style="font-size:9pt; color:var(--artefact-gray-muted);">Uso: Metadatos, notas al pie y referencias.</div>
      </div>
      <div class="type-row" style="border-bottom:none;">
        <div style="font-size:36pt; font-weight:900; color:var(--artefact-pink); line-height:1;">+145% ROI</div>
        <div style="font-size:11pt; font-weight:700; color:var(--artefact-blue);">Cifra de Impacto / KPI — Roboto Black 36pt con etiqueta Roboto Bold 11pt</div>
      </div>
    </div>

  </div>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w") as f:
    f.write(html)

print(f"Generated index.html showcase with {len(logo_files)} logos, {len(glassy_files)} glassy icons, {len(ui_files)} ui icons, and {len(svg_files)} SVGs!")
