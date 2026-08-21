import os, glob, json, shutil
from PIL import Image

BASE_DIR = "/Users/israeltorres/Documents/antigravity/calm-babbage"
DESKTOP_DIR = "/Users/israeltorres/Desktop/SKILL PPT"
KIT_DIR = os.path.join(BASE_DIR, "company-kits", "artefact")
CDN_BASE = "https://israeltorres-artefact.github.io/MKTKITARTEFACT/assets/"
GITHUB_REPO_URL = "https://github.com/israeltorres-artefact/MKTKITARTEFACT"

def scan_assets():
    assets_db = {
        "logos": [],
        "glassy": [],
        "svg": [],
        "ui_flat": [],
        "cutouts": [],
        "photography": []
    }
    
    # 1. Logos
    for f in sorted(glob.glob(os.path.join(BASE_DIR, "assets/logos/*.png"))):
        bname = os.path.basename(f)
        size_kb = os.path.getsize(f) / 1024
        try:
            im = Image.open(f)
            w, h = im.size
        except:
            w, h = 0, 0
        is_white = "white" in bname
        desc = "Logotipo oficial en versión oscura para fondos blancos o claros." if not is_white else "Logotipo oficial en versión blanca para fondos oscuros o degradados."
        if "monogram" in bname: desc = "Isotipo 'A' emblemático en máxima resolución ultra-nítida (2048x2048)."
        elif "horizontal" in bname: desc = "Wordmark horizontal ideal para barras de navegación superiores y cabeceras."
        elif "tagline" in bname: desc = "Logotipo con tagline institucional 'Data & AI Consulting'."
        elif "gradient" in bname: desc = "Logotipo apilado con símbolo en degradado institucional."
        
        assets_db["logos"].append({
            "name": bname,
            "title": bname.replace("artefact_", "").replace(".png", "").replace("_", " ").title(),
            "category": "Logotipos",
            "rel_path": f"assets/logos/{bname}",
            "cdn_url": f"{CDN_BASE}logos/{bname}",
            "width": w,
            "height": h,
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": is_white,
            "desc": desc,
            "tags": ["logo", "branding", "wordmark", "monogram", "artefact", "identidad"]
        })

    # 2. 3D Glassy Icons
    glassy_meta = {
        "icon_glassy_ai_acceleration.png": {
            "title": "AI Acceleration",
            "practice": "Inteligencia Artificial & GenAI",
            "topic": "Agentes Cognitivos, LLMs empresariales, RAG, Machine Learning predictivo y automatización inteligente.",
            "color": "#FF0066"
        },
        "icon_glassy_data_foundations_bi.png": {
            "title": "Data Foundations & BI",
            "practice": "Data Platform & Lakehouse",
            "topic": "Arquitectura Lakehouse, Gobierno y Linaje de Datos, Calidad, Data Mesh y Dashboards de alto impacto.",
            "color": "#002244"
        },
        "icon_glassy_strategy_transformation.png": {
            "title": "Strategy & Transformation",
            "practice": "Estrategia & ROI",
            "topic": "Data Operating Model, Priorización de Casos de Uso por ROI, Adopción y Modelos de Negocio.",
            "color": "#273275"
        },
        "icon_glassy_it_data_platform.png": {
            "title": "IT & Data Platform",
            "practice": "Cloud & MLOps",
            "topic": "Infraestructura Cloud (GCP, AWS, Azure, Databricks, Snowflake), CI/CD, MLOps y Seguridad.",
            "color": "#752E7D"
        },
        "icon_glassy_cx_digital_marketing.png": {
            "title": "CX & Digital Marketing",
            "practice": "Customer 360 & CDP",
            "topic": "Customer Data Platforms (CDP), Hiper-personalización omnicanal, CRM y Fidelización.",
            "color": "#FF0066"
        },
        "icon_glassy_marketing_datadriven.png": {
            "title": "Marketing Data-Driven",
            "practice": "Media Mix & Attribution",
            "topic": "Media Mix Modeling (MMM), Atribución Multitáctil, AdTech y Optimización del Retorno Publicitario (ROAS).",
            "color": "#052BF6"
        },
        "icon_glassy_iconic_a.png": {
            "title": "Iconic A of Artefact",
            "practice": "Marca & Metodología",
            "topic": "Símbolo emblemático de cristal insignia. Usado en portadas hero, manifiestos y cierres de agradecimiento.",
            "color": "#FF0066"
        },
        "icon_glassy_people.png": {
            "title": "People & Culture",
            "practice": "Talento & AI Literacy",
            "topic": "Capacitación en Inteligencia Artificial, Cultura Data-Driven, Gestión del Cambio y Habilitación de Equipos.",
            "color": "#273275"
        },
        "icon_glassy_clients.png": {
            "title": "Clients & Ecosystem",
            "practice": "Partnerships & Casos",
            "topic": "Ecosistema de partners tecnológicos, portafolio de clientes globales y credenciales.",
            "color": "#752E7D"
        },
        "icon_glassy_ai_hero_large.png": {
            "title": "AI Hero (2048px Ultra HD)",
            "practice": "Portada Principal",
            "topic": "Gráfico tridimensional gigante en máxima definición para portadas ejecutivas de Data & AI.",
            "color": "#FF0066"
        },
        "icon_glassy_data_hero_large.png": {
            "title": "Data Hero (1440px Ultra HD)",
            "practice": "Portada Analítica",
            "topic": "Gráfico tridimensional gigante para portadas de modernización de datos y plataformas.",
            "color": "#002244"
        },
        "icon_glassy_marketing_hero_large.png": {
            "title": "Marketing Hero (1056px Ultra HD)",
            "practice": "Portada Marketing",
            "topic": "Gráfico tridimensional gigante para propuestas de marketing de precisión y medios.",
            "color": "#052BF6"
        }
    }
    for f in sorted(glob.glob(os.path.join(BASE_DIR, "assets/icons/glassy_3d/*.png"))):
        bname = os.path.basename(f)
        meta = glassy_meta.get(bname, {
            "title": bname.replace("icon_glassy_", "").replace(".png", "").replace("_", " ").title(),
            "practice": "Consultoría Especializada",
            "topic": "Icono 3D Glassy institucional de Artefact.",
            "color": "#002244"
        })
        size_kb = os.path.getsize(f) / 1024
        try:
            im = Image.open(f)
            w, h = im.size
        except:
            w, h = 0, 0
        assets_db["glassy"].append({
            "name": bname,
            "title": meta["title"],
            "practice": meta["practice"],
            "category": "Iconos 3D Glassy",
            "rel_path": f"assets/icons/glassy_3d/{bname}",
            "cdn_url": f"{CDN_BASE}icons/glassy_3d/{bname}",
            "width": w,
            "height": h,
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": False,
            "desc": meta["topic"],
            "badge_color": meta["color"],
            "tags": ["3d", "glassy", "icon", meta["title"].lower(), meta["practice"].lower(), "artefact"]
        })

    # 3. UI Flat Icons
    for f in sorted(glob.glob(os.path.join(BASE_DIR, "assets/icons/ui_flat/*.png"))):
        bname = os.path.basename(f)
        size_kb = os.path.getsize(f) / 1024
        try:
            im = Image.open(f)
            w, h = im.size
        except:
            w, h = 0, 0
        assets_db["ui_flat"].append({
            "name": bname,
            "title": bname.replace(".png", "").replace("_", " ").title(),
            "category": "Iconos Planos UI",
            "rel_path": f"assets/icons/ui_flat/{bname}",
            "cdn_url": f"{CDN_BASE}icons/ui_flat/{bname}",
            "width": w,
            "height": h,
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": False,
            "desc": "Icono plano transparente para viñetas, tarjetas modulares, tablas y pasos de proceso (Slide 94).",
            "tags": ["ui", "flat", "icon", "bullet", "interface", "minimal"]
        })

    # 4. SVG Vector Icons
    for f in sorted(glob.glob(os.path.join(BASE_DIR, "assets/icons/vector_svg/*.svg"))):
        bname = os.path.basename(f)
        size_kb = os.path.getsize(f) / 1024
        with open(f, "r") as s_file:
            svg_content = s_file.read()
        assets_db["svg"].append({
            "name": bname,
            "title": bname.replace(".svg", "").replace("_", " ").title(),
            "category": "Iconos Vectoriales SVG",
            "rel_path": f"assets/icons/vector_svg/{bname}",
            "cdn_url": f"{CDN_BASE}icons/vector_svg/{bname}",
            "width": "Vector",
            "height": "Vector",
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": True,
            "desc": "Geometría vectorial matemática pura en SVG extraída de las diapositivas 90 a 93. Admite cambio dinámico de color.",
            "svg_data": svg_content,
            "tags": ["vector", "svg", "editable", "shapes", "icon", "drawingml"]
        })

    # 5. Cutouts
    for f in sorted(glob.glob(os.path.join(BASE_DIR, "assets/cutouts/*.png"))):
        bname = os.path.basename(f)
        size_kb = os.path.getsize(f) / 1024
        try:
            im = Image.open(f)
            w, h = im.size
        except:
            w, h = 0, 0
        assets_db["cutouts"].append({
            "name": bname,
            "title": bname.replace(".png", "").replace("_", " ").title(),
            "category": "Recortes Transparentes",
            "rel_path": f"assets/cutouts/{bname}",
            "cdn_url": f"{CDN_BASE}cutouts/{bname}",
            "width": w,
            "height": h,
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": False,
            "desc": "Recorte fotográfico transparente (PNG alfa) listo para superponer en tarjetas o fondos (Slide 70).",
            "tags": ["cutout", "transparent", "photo", "trimmed", "overlay", "device"]
        })

    # 6. Photography by Industry
    vertical_map = {
        "slide71": ("Conceptos Visuales & Fondos Hero", "Imágenes de impacto general para portadas y transiciones."),
        "slide72": ("Retail & E-commerce", "Supermercados, pasarelas de pago móvil, carritos y logística urbana."),
        "slide73": ("FMCG & Lujo", "Alimentos, bebidas, manufactura automatizada y cosmética premium."),
        "slide74": ("Banca & Finanzas", "Terminales POS, chips de tarjetas contactless y rascacielos financieros."),
        "slide75": ("Salud & Farma", "Laboratorios limpios, microscopía digital y diagnóstico clínico."),
        "slide76": ("Ciencias Aplicadas", "Investigación biotecnológica y analítica médica."),
        "slide77": ("Energía & Utilities", "Parques eólicos marinos y redes de distribución inteligente."),
        "slide78": ("Energía Solar & EV", "Paneles solares industriales y estaciones de recarga eléctrica."),
        "slide79": ("Telecom & 5G", "Torres de telecomunicaciones, fibra óptica y conectividad."),
        "slide80": ("Infraestructura & Nube", "Racks de servidores, hardware de centros de datos y cloud."),
        "slide81": ("Transformación Digital", "Visualización de datos y entornos de trabajo colaborativo."),
        "slide82": ("Inteligencia Artificial", "Flujos automatizados aumentados con IA."),
        "slide83": ("Liderazgo & Equipos", "Talleres de trabajo, consultoría y personas."),
        "slide84": ("Sostenibilidad ESG", "Huella de carbono, energías limpias y reciclaje circular.")
    }

    for f in sorted(glob.glob(os.path.join(BASE_DIR, "assets/photography/*"))):
        bname = os.path.basename(f)
        size_kb = os.path.getsize(f) / 1024
        try:
            im = Image.open(f)
            w, h = im.size
        except:
            w, h = 0, 0
        parts = bname.split("_")
        s_tag = parts[1] if len(parts) > 1 else "general"
        vert_title, vert_desc = vertical_map.get(s_tag, ("Fotografía General", "Imagen institucional."))
        
        assets_db["photography"].append({
            "name": bname,
            "title": f"{vert_title} ({parts[-1].split('.')[0]})",
            "category": "Fotografía por Industria",
            "vertical": vert_title,
            "rel_path": f"assets/photography/{bname}",
            "cdn_url": f"{CDN_BASE}photography/{bname}",
            "width": w,
            "height": h,
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": False,
            "desc": vert_desc,
            "tags": ["photo", "industry", s_tag, vert_title.lower(), "stock", "fotografia"]
        })

    return assets_db

assets_db = scan_assets()
db_json_str = json.dumps(assets_db)

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Artefact Brand System & Official Asset Hub</title>
  <link rel="stylesheet" href="tokens/artefact_theme.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary-gradient: linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);
      --gradient-horizontal: linear-gradient(90deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);
      --bg-body: #0A0F1D;
      --bg-surface: #111827;
      --bg-card: #1F2937;
      --text-light: #F9FAFB;
      --text-muted: #9CA3AF;
      --border-dark: #374151;
      --accent-pink: #FF0066;
      --artefact-blue: #002244;
      --medium-blue: #273275;
      --purple: #752E7D;
      --electric-blue: #052BF6;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: var(--bg-body);
      color: var(--text-light);
      line-height: 1.5;
      min-height: 100vh;
      overflow-x: hidden;
      padding-bottom: 60px;
    }

    .ambient-glow {
      position: fixed;
      top: -200px;
      left: 50%;
      transform: translateX(-50%);
      width: 1000px;
      height: 600px;
      background: radial-gradient(circle, rgba(255, 0, 102, 0.16) 0%, rgba(39, 50, 117, 0.15) 50%, transparent 80%);
      filter: blur(80px);
      z-index: 0;
      pointer-events: none;
    }

    .navbar {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(10, 15, 29, 0.88);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding: 14px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .nav-brand {
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
      color: white;
    }
    .nav-brand img {
      height: 32px;
      object-fit: contain;
    }
    .nav-brand-text {
      font-size: 15px;
      font-weight: 500;
      display: flex;
      flex-direction: column;
    }
    .nav-brand-text span:first-child {
      font-weight: 700;
      color: white;
    }
    .nav-brand-text span:last-child {
      font-size: 11px;
      color: var(--accent-pink);
      text-transform: uppercase;
      letter-spacing: 1.5px;
    }
    .nav-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .btn-nav {
      padding: 9px 18px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      border: 1px solid transparent;
    }
    .btn-nav-primary {
      background: var(--accent-pink);
      color: white;
      box-shadow: 0 4px 14px rgba(255, 0, 102, 0.35);
    }
    .btn-nav-primary:hover {
      background: #FF1A75;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(255, 0, 102, 0.5);
    }
    .btn-nav-secondary {
      background: rgba(255, 255, 255, 0.08);
      color: white;
      border-color: rgba(255, 255, 255, 0.15);
    }
    .btn-nav-secondary:hover {
      background: rgba(255, 255, 255, 0.15);
    }

    .container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 24px;
      position: relative;
      z-index: 1;
    }

    .hero {
      padding: 50px 0 36px 0;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      border-radius: 30px;
      background: rgba(255, 0, 102, 0.12);
      border: 1px solid rgba(255, 0, 102, 0.3);
      color: var(--accent-pink);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 18px;
    }
    .hero-title {
      font-size: 46px;
      font-weight: 300;
      line-height: 1.15;
      max-width: 960px;
      margin-bottom: 14px;
      color: white;
    }
    .hero-title strong {
      font-weight: 700;
      background: var(--gradient-horizontal);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
      font-size: 17px;
      color: var(--text-muted);
      max-width: 760px;
      margin-bottom: 36px;
      line-height: 1.6;
    }

    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      width: 100%;
      max-width: 1200px;
      margin-bottom: 40px;
    }
    .stat-card {
      background: rgba(31, 41, 55, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(12px);
      border-radius: 16px;
      padding: 18px;
      text-align: center;
      transition: all 0.25s;
      cursor: pointer;
    }
    .stat-card:hover {
      transform: translateY(-4px);
      border-color: rgba(255, 0, 102, 0.4);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }
    .stat-number {
      font-size: 30px;
      font-weight: 900;
      color: white;
      margin-bottom: 4px;
    }
    .stat-number.pink { color: var(--accent-pink); }
    .stat-label {
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .sticky-toolbar {
      position: sticky;
      top: 72px;
      z-index: 900;
      background: rgba(17, 24, 39, 0.95);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 18px;
      padding: 14px 20px;
      margin-bottom: 28px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
    }
    .search-wrapper {
      flex: 1;
      min-width: 280px;
      position: relative;
    }
    .search-input {
      width: 100%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 12px;
      padding: 12px 18px 12px 44px;
      color: white;
      font-size: 14px;
      font-family: inherit;
      outline: none;
      transition: all 0.2s;
    }
    .search-input:focus {
      background: rgba(255, 255, 255, 0.1);
      border-color: var(--accent-pink);
      box-shadow: 0 0 0 3px rgba(255, 0, 102, 0.2);
    }
    .search-icon {
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 16px;
    }

    .tabs-nav {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 28px;
    }
    .tab-pill {
      padding: 10px 18px;
      border-radius: 30px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .tab-pill:hover {
      background: rgba(255, 255, 255, 0.1);
      color: white;
    }
    .tab-pill.active {
      background: var(--accent-pink);
      color: white;
      border-color: var(--accent-pink);
      box-shadow: 0 4px 14px rgba(255, 0, 102, 0.4);
    }
    .tab-badge {
      background: rgba(0, 0, 0, 0.3);
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 11px;
    }

    .subfilter-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 24px;
      padding: 16px;
      background: rgba(255, 255, 255, 0.03);
      border-radius: 14px;
      border: 1px solid rgba(255, 255, 255, 0.06);
    }
    .chip-btn {
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 500;
      background: rgba(255, 255, 255, 0.07);
      color: #D1D5DB;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s;
    }
    .chip-btn:hover { background: rgba(255, 255, 255, 0.15); }
    .chip-btn.active {
      background: white;
      color: var(--bg-body);
      font-weight: 700;
      box-shadow: 0 2px 8px rgba(255, 255, 255, 0.2);
    }

    .section-title-box {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin: 40px 0 20px 0;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .section-title-text {
      font-size: 24px;
      font-weight: 700;
      color: white;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .section-subtitle-text {
      font-size: 13px;
      color: var(--text-muted);
    }

    .color-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 20px;
      margin-bottom: 40px;
    }
    .color-card-item {
      background: var(--bg-surface);
      border: 1px solid var(--border-dark);
      border-radius: 16px;
      overflow: hidden;
      cursor: pointer;
      transition: all 0.2s;
      position: relative;
    }
    .color-card-item:hover {
      transform: translateY(-4px);
      border-color: rgba(255, 255, 255, 0.3);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
    }
    .color-swatch-box {
      height: 110px;
      width: 100%;
      position: relative;
      display: flex;
      align-items: flex-end;
      justify-content: flex-end;
      padding: 12px;
    }
    .copy-pill {
      background: rgba(0, 0, 0, 0.6);
      backdrop-filter: blur(4px);
      color: white;
      font-size: 11px;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 8px;
      opacity: 0;
      transition: opacity 0.2s;
    }
    .color-card-item:hover .copy-pill { opacity: 1; }
    .color-meta {
      padding: 16px;
    }
    .color-title {
      font-size: 15px;
      font-weight: 700;
      color: white;
      margin-bottom: 4px;
    }
    .color-hex {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: var(--accent-pink);
    }
    .color-role {
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 6px;
      line-height: 1.4;
    }

    .asset-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 20px;
      margin-bottom: 48px;
    }
    .asset-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-dark);
      border-radius: 16px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      position: relative;
    }
    .asset-card:hover {
      transform: translateY(-5px);
      border-color: rgba(255, 0, 102, 0.5);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5);
    }
    .asset-stage {
      height: 180px;
      background: #1A2234;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      position: relative;
      overflow: hidden;
    }
    .asset-stage.white-stage {
      background: #F3F4F6;
    }
    .asset-stage img, .asset-stage svg {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      transition: transform 0.3s;
    }
    .asset-card:hover .asset-stage img, .asset-card:hover .asset-stage svg {
      transform: scale(1.08);
    }
    .asset-content {
      padding: 18px;
      display: flex;
      flex-direction: column;
      flex: 1;
      justify-content: space-between;
    }
    .asset-name-text {
      font-size: 14px;
      font-weight: 700;
      color: white;
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .asset-category-tag {
      font-size: 11px;
      color: var(--accent-pink);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
    }
    .asset-footer-info {
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      color: var(--text-muted);
      padding-top: 12px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }

    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(5, 10, 20, 0.85);
      backdrop-filter: blur(12px);
      z-index: 2000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }
    .modal-overlay.open {
      opacity: 1;
      pointer-events: auto;
    }
    .modal-box {
      background: var(--bg-surface);
      border: 1px solid var(--border-dark);
      border-radius: 20px;
      width: 100%;
      max-width: 860px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.6);
      display: flex;
      flex-direction: column;
    }
    .modal-head {
      padding: 22px 28px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .modal-title-heading {
      font-size: 20px;
      font-weight: 700;
      color: white;
    }
    .btn-modal-close {
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 24px;
      cursor: pointer;
      transition: color 0.2s;
    }
    .btn-modal-close:hover { color: white; }
    .modal-content-area {
      padding: 28px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }
    .modal-visual-preview {
      height: 260px;
      border-radius: 16px;
      background: #182236;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 40px;
      position: relative;
    }
    .modal-visual-preview.white-bg {
      background: #F3F4F6;
    }
    .modal-visual-preview.gradient-bg {
      background: var(--primary-gradient);
    }
    .bg-switcher {
      position: absolute;
      top: 14px;
      right: 14px;
      display: flex;
      gap: 6px;
      background: rgba(0, 0, 0, 0.4);
      padding: 4px;
      border-radius: 8px;
    }
    .bg-switch-btn {
      padding: 4px 8px;
      font-size: 11px;
      color: white;
      border: none;
      border-radius: 6px;
      background: transparent;
      cursor: pointer;
    }
    .bg-switch-btn.active { background: var(--accent-pink); }

    .code-block {
      background: #090E17;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 16px;
      position: relative;
    }
    .code-block code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: #38BDF8;
      word-break: break-all;
    }
    .btn-copy-code {
      position: absolute;
      top: 12px;
      right: 12px;
      background: var(--accent-pink);
      color: white;
      border: none;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-copy-code:hover {
      background: #FF1A75;
    }

    .toast-popup {
      position: fixed;
      bottom: 36px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: white;
      color: var(--bg-body);
      padding: 14px 28px;
      border-radius: 40px;
      font-size: 14px;
      font-weight: 700;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .toast-popup.show {
      transform: translateX(-50%) translateY(0);
    }
  </style>
</head>
<body>

  <div class="ambient-glow"></div>

  <!-- Navbar -->
  <header class="navbar">
    <a href="#" class="nav-brand">
      <img src="assets/logos/artefact_logo_primary_white.png" alt="Artefact">
      <div class="nav-brand-text">
        <span>Artefact Brand System</span>
        <span>Official Asset & Design Hub</span>
      </div>
    </a>
    <div class="nav-actions">
      <button class="btn-nav btn-nav-secondary" onclick="setCategory('colors')">🎨 Paleta de Colores</button>
      <button class="btn-nav btn-nav-secondary" onclick="setCategory('glassy')">🔮 Iconos 3D</button>
      <a href="""" + GITHUB_REPO_URL + """" class="btn-nav btn-nav-primary" target="_blank">⭐ Repositorio GitHub</a>
    </div>
  </header>

  <div class="container">

    <!-- Hero -->
    <section class="hero">
      <div class="hero-badge">Artefact Brand Identity • Official Asset Library • November 2024</div>
      <h1 class="hero-title">
        El Sistema de Marca & Recursos Visuales de <strong>Artefact</strong>
      </h1>
      <p class="hero-subtitle">
        Biblioteca oficial de logotipos corporativos, iconos 3D glassy por especialidad, vectores SVG de alta precisión, banco de fotografía por industrias y tokens de color para equipos y consultores de Artefact.
      </p>

      <!-- Stats Grid -->
      <div class="stats-grid">
        <div class="stat-card" onclick="setCategory('logos')">
          <div class="stat-number pink" id="statLogos">11</div>
          <div class="stat-label">Logotipos HD</div>
        </div>
        <div class="stat-card" onclick="setCategory('glassy')">
          <div class="stat-number" id="statGlassy">12</div>
          <div class="stat-label">Iconos 3D Glassy</div>
        </div>
        <div class="stat-card" onclick="setCategory('svg')">
          <div class="stat-number pink" id="statSvg">171</div>
          <div class="stat-label">Vectores SVG</div>
        </div>
        <div class="stat-card" onclick="setCategory('ui_flat')">
          <div class="stat-number" id="statUi">39</div>
          <div class="stat-label">Iconos Planos UI</div>
        </div>
        <div class="stat-card" onclick="setCategory('photography')">
          <div class="stat-number" id="statPhotos">89</div>
          <div class="stat-label">Fotos por Industria</div>
        </div>
        <div class="stat-card" onclick="setCategory('cutouts')">
          <div class="stat-number pink" id="statCutouts">9</div>
          <div class="stat-label">Recortes PNG</div>
        </div>
      </div>
    </section>

    <!-- Sticky Toolbar -->
    <div class="sticky-toolbar">
      <div class="search-wrapper">
        <span class="search-icon">🔍</span>
        <input type="text" class="search-input" id="globalSearch" placeholder="Buscar activo por nombre, industria (Retail, AI, Banca, Farma, ESG) o etiqueta..." oninput="onSearchInput()">
      </div>
      <div style="font-size: 13px; color: var(--text-muted);" id="counterText">
        Mostrando todos los activos
      </div>
    </div>

    <!-- Category Tabs -->
    <div class="tabs-nav" id="categoryTabs">
      <button class="tab-pill active" onclick="setCategory('all')">✨ Todos <span class="tab-badge" id="badgeAll">0</span></button>
      <button class="tab-pill" onclick="setCategory('colors')">🎨 Paleta & Degradados</button>
      <button class="tab-pill" onclick="setCategory('logos')">🏷️ Logotipos <span class="tab-badge">11</span></button>
      <button class="tab-pill" onclick="setCategory('glassy')">🔮 Iconos 3D Glassy <span class="tab-badge">12</span></button>
      <button class="tab-pill" onclick="setCategory('svg')">📐 Vectores SVG <span class="tab-badge">171</span></button>
      <button class="tab-pill" onclick="setCategory('ui_flat')">📱 Iconos Planos UI <span class="tab-badge">39</span></button>
      <button class="tab-pill" onclick="setCategory('photography')">📸 Fotografía <span class="tab-badge">89</span></button>
      <button class="tab-pill" onclick="setCategory('cutouts')">✂️ Recortes PNG <span class="tab-badge">9</span></button>
      <button class="tab-pill" onclick="setCategory('typography')">✍️ Tipografía Roboto</button>
    </div>

    <!-- Photo Sub-filters -->
    <div class="subfilter-bar" id="photoSubfilters" style="display: none;">
      <button class="chip-btn active" onclick="setPhotoVertical('all')">Todas las Industrias (89)</button>
      <button class="chip-btn" onclick="setPhotoVertical('Retail')">🛒 Retail & E-commerce</button>
      <button class="chip-btn" onclick="setPhotoVertical('FMCG')">📦 FMCG & Lujo</button>
      <button class="chip-btn" onclick="setPhotoVertical('Banca')">💳 Banca & Finanzas</button>
      <button class="chip-btn" onclick="setPhotoVertical('Salud')">🔬 Salud & Farma</button>
      <button class="chip-btn" onclick="setPhotoVertical('Energía')">⚡ Energía & Utilities</button>
      <button class="chip-btn" onclick="setPhotoVertical('Telecom')">📡 Telecom & 5G</button>
      <button class="chip-btn" onclick="setPhotoVertical('Transformación')">🤖 IA & Transformación</button>
      <button class="chip-btn" onclick="setPhotoVertical('Sostenibilidad')">🌱 Sostenibilidad ESG</button>
    </div>

    <!-- Color Palette Section -->
    <div id="colorsSection">
      <div class="section-title-box">
        <div class="section-title-text">🎨 Paleta Oficial de Colores & Degradado de 4 Paradas</div>
        <div class="section-subtitle-text">Haz clic en cualquier tarjeta para copiar su valor al portapapeles</div>
      </div>

      <div style="height: 60px; border-radius: 14px; background: var(--primary-gradient); margin-bottom: 24px; box-shadow: 0 8px 25px rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: space-between; padding: 0 24px; cursor: pointer;" onclick="copyValue('linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%)', 'CSS del Degradado Insigne')">
        <span style="font-weight: 700; font-size: 14px; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">Signature Multi-Stop Gradient (4 Paradas)</span>
        <span style="font-size: 12px; background: rgba(0,0,0,0.4); padding: 4px 10px; border-radius: 6px;">Click para copiar CSS</span>
      </div>

      <div class="color-grid">
        <div class="color-card-item" onclick="copyValue('#002244', 'Artefact Blue')">
          <div class="color-swatch-box" style="background:#002244;">
            <span class="copy-pill">Copiar HEX</span>
          </div>
          <div class="color-meta">
            <div class="color-title">Artefact Blue</div>
            <div class="color-hex">#002244</div>
            <div class="color-role">Color corporativo primario. Textos en fondo claro, logotipos y tarjetas.</div>
          </div>
        </div>

        <div class="color-card-item" onclick="copyValue('#FF0066', 'Artefact Pink')">
          <div class="color-swatch-box" style="background:#FF0066;">
            <span class="copy-pill">Copiar HEX</span>
          </div>
          <div class="color-meta">
            <div class="color-title">Artefact Pink</div>
            <div class="color-hex">#FF0066</div>
            <div class="color-role">Acento de máxima energía. Cifras KPI gigantes, enlaces y botones CTA.</div>
          </div>
        </div>

        <div class="color-card-item" onclick="copyValue('#0D1634', 'Dark Blue')">
          <div class="color-swatch-box" style="background:#0D1634;">
            <span class="copy-pill">Copiar HEX</span>
          </div>
          <div class="color-meta">
            <div class="color-title">Dark Blue</div>
            <div class="color-hex">#0D1634</div>
            <div class="color-role">Fondo nocturno para portadas C-Level y slides oscuras.</div>
          </div>
        </div>

        <div class="color-card-item" onclick="copyValue('#273275', 'Medium Blue')">
          <div class="color-swatch-box" style="background:#273275;">
            <span class="copy-pill">Copiar HEX</span>
          </div>
          <div class="color-meta">
            <div class="color-title">Medium Blue</div>
            <div class="color-hex">#273275</div>
            <div class="color-role">Azul real intermedio. Segundo escalón del degradado.</div>
          </div>
        </div>

        <div class="color-card-item" onclick="copyValue('#752E7D', 'Purple')">
          <div class="color-swatch-box" style="background:#752E7D;">
            <span class="copy-pill">Copiar HEX</span>
          </div>
          <div class="color-meta">
            <div class="color-title">Purple</div>
            <div class="color-hex">#752E7D</div>
            <div class="color-role">Púrpura berenjena. Tercer escalón del degradado.</div>
          </div>
        </div>

        <div class="color-card-item" onclick="copyValue('#052BF6', 'Electric Blue')">
          <div class="color-swatch-box" style="background:#052BF6;">
            <span class="copy-pill">Copiar HEX</span>
          </div>
          <div class="color-meta">
            <div class="color-title">Electric Blue</div>
            <div class="color-hex">#052BF6</div>
            <div class="color-role">Visualización de datos. Serie 1 en gráficos de barras y badges.</div>
          </div>
        </div>

        <div class="color-card-item" onclick="copyValue('#9900FF', 'Bright Purple')">
          <div class="color-swatch-box" style="background:#9900FF;">
            <span class="copy-pill">Copiar HEX</span>
          </div>
          <div class="color-meta">
            <div class="color-title">Bright Purple</div>
            <div class="color-hex">#9900FF</div>
            <div class="color-role">Visualización de datos. Serie 2 en gráficos y badges de IA.</div>
          </div>
        </div>

        <div class="color-card-item" onclick="copyValue('#F4F6F9', 'Surface Light')">
          <div class="color-swatch-box" style="background:#F4F6F9; border-bottom: 1px solid #333;">
            <span class="copy-pill" style="background: rgba(0,0,0,0.8);">Copiar HEX</span>
          </div>
          <div class="color-meta">
            <div class="color-title">Surface Light</div>
            <div class="color-hex">#F4F6F9</div>
            <div class="color-role">Superficie estándar de tarjetas modulares en fondos claros.</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Typography Section -->
    <div id="typographySection" style="display: none; margin-bottom: 40px;">
      <div class="section-title-box">
        <div class="section-title-text">✍️ Jerarquía Tipográfica Institucional — Roboto</div>
        <div class="section-subtitle-text">Escala oficial de fuentes para documentos y presentaciones corporativas</div>
      </div>

      <div style="background: var(--bg-surface); border: 1px solid var(--border-dark); border-radius: 18px; padding: 36px;">
        <div style="margin-bottom: 28px; padding-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.08);">
          <div style="font-size: 30px; font-weight: 400; color: white; line-height: 1.2;">
            Título de Diapositiva: La modernización hacia un Lakehouse unificado reduce los costos en un 40%
          </div>
          <div style="font-size: 13px; color: var(--accent-pink); margin-top: 8px;">
            <code>Roboto Normal (400) • 20pt (28px)</code> • Regla de Oro: En estilo regular ligero para elegancia editorial.
          </div>
        </div>

        <div style="margin-bottom: 28px; padding-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.08);">
          <div style="font-size: 20px; font-weight: 700; color: white; line-height: 1.3;">
            Subtítulo / Contexto: Tres fases estructuradas para capturar valor y acelerar casos de uso con IA
          </div>
          <div style="font-size: 13px; color: var(--accent-pink); margin-top: 8px;">
            <code>Roboto Bold (700) • 14pt (20px)</code> • Anclaje visual inmediato bajo el título principal.
          </div>
        </div>

        <div style="margin-bottom: 28px; padding-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.08);">
          <div style="font-size: 16px; font-weight: 400; color: #D1D5DB; line-height: 1.5; max-width: 900px;">
            <strong style="color:white;">Gobernanza activa:</strong> Implementación de catálogo automatizado con linaje de datos de extremo a extremo para asegurar cumplimiento ético y disponibilidad de modelos.
          </div>
          <div style="font-size: 13px; color: var(--text-muted); margin-top: 8px;">
            <code>Roboto Normal (400) • 12pt (16px)</code> con lead-in en <code>Roboto Bold</code> para lectura rápida.
          </div>
        </div>

        <div style="display: flex; gap: 48px; align-items: baseline; flex-wrap: wrap;">
          <div>
            <div style="font-size: 64px; font-weight: 900; color: var(--accent-pink); line-height: 1;">+35% ROI</div>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 6px;"><code>Roboto Black (900) • 44pt</code> (Métrica KPI Gigante)</div>
          </div>
          <div>
            <div style="font-size: 14px; font-weight: 500; color: var(--text-muted);">Fuente: Artefact Data & AI Assessment • 2024</div>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 6px;"><code>Roboto Medium (500) • 10pt</code> (Pie de página / Atribución)</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Asset Cards Grid -->
    <div id="assetsGridSection">
      <div class="section-title-box">
        <div class="section-title-text" id="gridTitle">📦 Galería de Activos</div>
        <div class="section-subtitle-text">Haz clic en cualquier tarjeta para ver detalles y copiar enlaces directos</div>
      </div>

      <div class="asset-grid" id="assetGridContainer"></div>
    </div>

  </div>

  <!-- Modal Inspector -->
  <div class="modal-overlay" id="modalOverlay" onclick="closeModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div class="modal-head">
        <div class="modal-title-heading" id="mTitle">Detalles del Activo</div>
        <button class="btn-modal-close" onclick="closeModalDirect()">✕</button>
      </div>
      <div class="modal-content-area">
        
        <div class="modal-visual-preview" id="mPreviewStage">
          <div class="bg-switcher">
            <button class="bg-switch-btn active" onclick="setModalBg('dark')">Dark</button>
            <button class="bg-switch-btn" onclick="setModalBg('white')">White</button>
            <button class="bg-switch-btn" onclick="setModalBg('gradient')">Gradient</button>
          </div>
          <div id="mVisualHolder" style="max-width: 100%; max-height: 100%; display: flex; align-items: center; justify-content: center;"></div>
        </div>

        <div>
          <h4 style="font-size: 16px; font-weight: 700; color: white; margin-bottom: 6px;" id="mName"></h4>
          <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5;" id="mDesc"></p>
        </div>

        <div>
          <div style="font-size: 12px; font-weight: 700; margin-bottom: 8px; color: var(--accent-pink); text-transform: uppercase;">URL Pública Directa en la Nube (GitHub Pages):</div>
          <div class="code-block">
            <button class="btn-copy-code" onclick="copySnippet('url')">Copiar URL</button>
            <code id="mSnippetUrl"></code>
          </div>
        </div>

        <div>
          <div style="font-size: 12px; font-weight: 700; margin-bottom: 8px; color: var(--accent-pink); text-transform: uppercase;">Código HTML Estándar:</div>
          <div class="code-block">
            <button class="btn-copy-code" onclick="copySnippet('html')">Copiar HTML</button>
            <code id="mSnippetHtml"></code>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- Toast Alert -->
  <div class="toast-popup" id="toastAlert">
    <span>✨</span> <span id="toastText">Copiado al portapapeles</span>
  </div>

  <script>
    const db = """ + db_json_str + """;
    let currentCat = 'all';
    let currentPhotoVert = 'all';
    let searchQuery = '';
    let selectedItem = null;

    document.getElementById('badgeAll').innerText = 
      db.logos.length + db.glassy.length + db.svg.length + db.ui_flat.length + db.photography.length + db.cutouts.length;

    function renderAssets() {
      const grid = document.getElementById('assetGridContainer');
      const colorsSection = document.getElementById('colorsSection');
      const typoSection = document.getElementById('typographySection');
      const photoSub = document.getElementById('photoSubfilters');
      const gridTitle = document.getElementById('gridTitle');
      const gridSec = document.getElementById('assetsGridSection');

      colorsSection.style.display = (currentCat === 'all' || currentCat === 'colors') ? 'block' : 'none';
      typoSection.style.display = (currentCat === 'all' || currentCat === 'typography') ? 'block' : 'none';
      photoSub.style.display = (currentCat === 'photography') ? 'flex' : 'none';

      if (['colors', 'typography'].includes(currentCat)) {
        gridSec.style.display = 'none';
        return;
      } else {
        gridSec.style.display = 'block';
      }

      let items = [];
      if (currentCat === 'all') {
        items = [...db.logos, ...db.glassy, ...db.svg.slice(0, 48), ...db.ui_flat, ...db.cutouts, ...db.photography.slice(0, 32)];
        gridTitle.innerText = '📦 Galería Panorámica de Activos';
      } else if (currentCat === 'logos') {
        items = db.logos;
        gridTitle.innerText = '🏷️ Logotipos Oficiales Artefact (' + items.length + ')';
      } else if (currentCat === 'glassy') {
        items = db.glassy;
        gridTitle.innerText = '🔮 Iconos 3D Glassy de Áreas de Práctica (' + items.length + ')';
      } else if (currentCat === 'svg') {
        items = db.svg;
        gridTitle.innerText = '📐 Vectores SVG Puros (' + items.length + ')';
      } else if (currentCat === 'ui_flat') {
        items = db.ui_flat;
        gridTitle.innerText = '📱 Iconos Planos de UI (' + items.length + ')';
      } else if (currentCat === 'cutouts') {
        items = db.cutouts;
        gridTitle.innerText = '✂️ Recortes Transparentes (' + items.length + ')';
      } else if (currentCat === 'photography') {
        items = db.photography;
        if (currentPhotoVert !== 'all') {
          items = items.filter(i => i.vertical.toLowerCase().includes(currentPhotoVert.toLowerCase()));
        }
        gridTitle.innerText = '📸 Banco Fotográfico por Industria (' + items.length + ')';
      }

      if (searchQuery.trim() !== '') {
        const q = searchQuery.toLowerCase();
        items = items.filter(i => 
          i.name.toLowerCase().includes(q) || 
          i.title.toLowerCase().includes(q) ||
          i.desc.toLowerCase().includes(q) ||
          (i.practice && i.practice.toLowerCase().includes(q)) ||
          i.tags.some(t => t.toLowerCase().includes(q))
        );
      }

      document.getElementById('counterText').innerText = 'Mostrando ' + items.length + ' activos';

      if (items.length === 0) {
        grid.innerHTML = '<div style="grid-column: 1/-1; padding: 60px; text-align: center; color: var(--text-muted);">No se encontraron activos para esta búsqueda.</div>';
        return;
      }

      let html = '';
      items.forEach(item => {
        const isWhiteStage = (item.category === 'Logotipos' && !item.is_dark_bg) || (item.category === 'Iconos Planos UI');
        const stageClass = isWhiteStage ? 'white-stage' : '';
        const preview = item.svg_data 
          ? `<div style="width:72px;height:72px;display:flex;align-items:center;justify-content:center;">${item.svg_data}</div>`
          : `<img src="${item.cdn_url}" alt="${item.name}" loading="lazy">`;

        html += `
          <div class="asset-card" onclick="openModal('${item.name}')">
            <div class="asset-stage ${stageClass}">
              ${preview}
            </div>
            <div class="asset-content">
              <div>
                <div class="asset-category-tag">${item.practice || item.category}</div>
                <div class="asset-name-text" title="${item.title}">${item.title}</div>
              </div>
              <div class="asset-footer-info">
                <span>${item.width}x${item.height}</span>
                <span>${item.size_kb}</span>
              </div>
            </div>
          </div>
        `;
      });

      grid.innerHTML = html;
    }

    function setCategory(cat) {
      currentCat = cat;
      const pills = document.querySelectorAll('#categoryTabs .tab-pill');
      pills.forEach(p => p.classList.remove('active'));
      event.currentTarget.classList.add('active');
      renderAssets();
    }

    function setPhotoVertical(vert) {
      currentPhotoVert = vert;
      const chips = document.querySelectorAll('#photoSubfilters .chip-btn');
      chips.forEach(c => c.classList.remove('active'));
      event.currentTarget.classList.add('active');
      renderAssets();
    }

    function onSearchInput() {
      searchQuery = document.getElementById('globalSearch').value;
      renderAssets();
    }

    function openModal(name) {
      const all = [...db.logos, ...db.glassy, ...db.svg, ...db.ui_flat, ...db.cutouts, ...db.photography];
      const item = all.find(i => i.name === name);
      if (!item) return;

      selectedItem = item;
      document.getElementById('mTitle').innerText = item.title;
      document.getElementById('mName').innerText = item.name + ' (' + item.width + 'x' + item.height + ' • ' + item.size_kb + ')';
      document.getElementById('mDesc').innerText = item.desc;

      const visualHolder = document.getElementById('mVisualHolder');
      if (item.svg_data) {
        visualHolder.innerHTML = `<div style="width:140px;height:140px;">${item.svg_data}</div>`;
      } else {
        visualHolder.innerHTML = `<img src="${item.cdn_url}" style="max-height:180px; max-width:100%;" alt="${item.name}">`;
      }

      document.getElementById('mSnippetHtml').innerText = `<img src="${item.cdn_url}" alt="${item.title}">`;
      document.getElementById('mSnippetUrl').innerText = item.cdn_url;

      document.getElementById('modalOverlay').classList.add('open');
    }

    function setModalBg(type) {
      const stage = document.getElementById('mPreviewStage');
      const btns = document.querySelectorAll('.bg-switch-btn');
      btns.forEach(b => b.classList.remove('active'));
      event.currentTarget.classList.add('active');
      stage.className = 'modal-visual-preview ' + (type === 'white' ? 'white-bg' : (type === 'gradient' ? 'gradient-bg' : ''));
    }

    function closeModal(e) {
      if (e.target.id === 'modalOverlay') {
        document.getElementById('modalOverlay').classList.remove('open');
      }
    }

    function closeModalDirect() {
      document.getElementById('modalOverlay').classList.remove('open');
    }

    function copySnippet(type) {
      if (!selectedItem) return;
      if (type === 'html') {
        copyValue(`<img src="${selectedItem.cdn_url}" alt="${selectedItem.title}">`, 'Snippet HTML');
      } else if (type === 'url') {
        copyValue(selectedItem.cdn_url, 'URL Directa');
      }
    }

    function copyValue(val, label) {
      navigator.clipboard.writeText(val).then(() => {
        showToast('Copiado: ' + label);
      }).catch(() => {
        showToast('Copiado');
      });
    }

    function showToast(msg) {
      const t = document.getElementById('toastAlert');
      document.getElementById('toastText').innerText = msg;
      t.classList.add('show');
      setTimeout(() => { t.classList.remove('show'); }, 2400);
    }

    renderAssets();
  </script>
</body>
</html>
"""

# Write to root index.html
with open(os.path.join(BASE_DIR, "index.html"), "w") as f:
    f.write(html_content)

# Write to company kit index.html
with open(os.path.join(KIT_DIR, "index.html"), "w") as f:
    f.write(html_content)

# Mirror to Desktop
with open(os.path.join(DESKTOP_DIR, "company-kits", "artefact", "index.html"), "w") as f:
    f.write(html_content)

print("Clean Public Hub (index.html) successfully generated!")
