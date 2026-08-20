import os, glob, json, shutil
from PIL import Image

BASE_DIR = "/Users/israeltorres/Documents/antigravity/calm-babbage"
DESKTOP_DIR = "/Users/israeltorres/Desktop/SKILL PPT"

# Collect all assets with metadata
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
        desc = "Logotipo institucional en versión oscura para fondos claros." if not is_white else "Logotipo institucional en versión blanca para fondos oscuros o degradados."
        if "monogram" in bname: desc = "Isotipo 'A' emblemático de máxima resolución (2048x2048)."
        elif "horizontal" in bname: desc = "Wordmark horizontal para barras de navegación o encabezados compactos."
        elif "tagline" in bname: desc = "Logotipo con tagline institucional 'Data & AI Consulting'."
        elif "gradient" in bname: desc = "Logotipo estilizado con isotipo en degradado corporativo."
        
        assets_db["logos"].append({
            "name": bname,
            "title": bname.replace("artefact_", "").replace(".png", "").replace("_", " ").title(),
            "category": "Logotipos",
            "rel_path": f"assets/logos/{bname}",
            "width": w,
            "height": h,
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": is_white,
            "desc": desc,
            "tags": ["logo", "branding", "wordmark", "monogram", "artefact"]
        })

    # 2. 3D Glassy Icons
    glassy_meta = {
        "icon_glassy_ai_acceleration.png": {"title": "AI Acceleration", "topic": "Inteligencia Artificial, LLMs, GenAI, Agentes Cognitivos, Machine Learning, Automatización Predictiva."},
        "icon_glassy_data_foundations_bi.png": {"title": "Data Foundations & BI", "topic": "Data Lakehouse, Gobierno de Datos, Calidad, BI Dashboards, Data Mesh, ETL/ELT."},
        "icon_glassy_strategy_transformation.png": {"title": "Strategy & Transformation", "topic": "Estrategia de Negocio, Data Operating Model, ROI, Priorización de Casos de Uso."},
        "icon_glassy_it_data_platform.png": {"title": "IT & Data Platform", "topic": "Infraestructura Cloud (GCP, AWS, Azure, Databricks, Snowflake), MLOps, CI/CD."},
        "icon_glassy_cx_digital_marketing.png": {"title": "CX & Digital Marketing", "topic": "Customer Experience, Customer 360, CDP, Personalización Omnicanal, CRM."},
        "icon_glassy_marketing_datadriven.png": {"title": "Marketing Data-Driven", "topic": "Media Mix Modeling (MMM), Atribución, AdTech, Optimización de Inversión en Medios."},
        "icon_glassy_iconic_a.png": {"title": "Iconic A of Artefact", "topic": "Símbolo emblemático de la marca, Metodología Propietaria, Cierre Institucional."},
        "icon_glassy_people.png": {"title": "People & Culture", "topic": "Talento, AI Literacy, Cultura Data-Driven, Gestión del Cambio, Habilitación de Equipos."},
        "icon_glassy_clients.png": {"title": "Clients & Partnerships", "topic": "Ecosistema de Partners, Clientes, Benchmarks de Mercado, Portafolio."},
        "icon_glassy_ai_hero_large.png": {"title": "AI Hero (High Res)", "topic": "Gráfico principal tridimensional gigante (2048px) para portadas de alto impacto."},
        "icon_glassy_data_hero_large.png": {"title": "Data Hero (High Res)", "topic": "Gráfico principal de datos gigante (1440px) para portadas analíticas."},
        "icon_glassy_marketing_hero_large.png": {"title": "Marketing Hero (High Res)", "topic": "Gráfico principal de marketing gigante (1056px) para propuestas de medios."}
    }
    for f in sorted(glob.glob(os.path.join(BASE_DIR, "assets/icons/glassy_3d/*.png"))):
        bname = os.path.basename(f)
        meta = glassy_meta.get(bname, {"title": bname.replace("icon_glassy_", "").replace(".png", "").replace("_", " ").title(), "topic": "Icono 3D Glassy institucional de Artefact."})
        size_kb = os.path.getsize(f) / 1024
        try:
            im = Image.open(f)
            w, h = im.size
        except:
            w, h = 0, 0
        assets_db["glassy"].append({
            "name": bname,
            "title": meta["title"],
            "category": "Iconos 3D Glassy",
            "rel_path": f"assets/icons/glassy_3d/{bname}",
            "width": w,
            "height": h,
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": False,
            "desc": meta["topic"],
            "tags": ["3d", "glassy", "icon", meta["title"].lower(), "artefact"]
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
            "width": w,
            "height": h,
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": False,
            "desc": "Icono plano transparente para viñetas, tarjetas y tablas (Slide 94).",
            "tags": ["ui", "flat", "icon", "bullet", "interface"]
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
            "width": "Vector",
            "height": "Vector",
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": True,
            "desc": "Icono vectorial nativo de precisión matemática en SVG (Slides 90-93). Escalable al infinito.",
            "svg_data": svg_content,
            "tags": ["vector", "svg", "editable", "shapes", "icon"]
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
            "width": w,
            "height": h,
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": False,
            "desc": "Recorte fotográfico transparente (PNG alfa) listo para superponer en tarjetas o fondos (Slide 70).",
            "tags": ["cutout", "transparent", "photo", "trimmed", "overlay"]
        })

    # 6. Photography by Industry
    vertical_map = {
        "slide71": ("Conceptos Visuales & Fondos Hero", "Imágenes de impacto general para portadas y transiciones."),
        "slide72": ("Retail & E-commerce", "Supermercados, pasarelas de pago, carritos y tiendas online."),
        "slide73": ("FMCG, Bienes de Consumo & Lujo", "Alimentos, bebidas, manufactura y cosmética premium."),
        "slide74": ("Banca, Finanzas & Pagos", "Terminales POS, tarjetas de crédito, transacciones y finanzas."),
        "slide75": ("Salud, Farma & Biotecnología", "Laboratorios limpios, microscopía y diagnóstico clínico."),
        "slide76": ("Salud & Ciencias Aplicadas", "Investigación clínica y biotecnología avanzada."),
        "slide77": ("Energía, Renovables & Utilities", "Parques eólicos marinos y redes eléctricas inteligentes."),
        "slide78": ("Energía Solar & Movilidad Eléctrica", "Paneles solares y estaciones de carga EV."),
        "slide79": ("Telecomunicaciones & Redes 5G", "Torres de telecomunicaciones, fibra y conectividad."),
        "slide80": ("Infraestructura Digital & Data Centers", "Racks de servidores, hardware y nube."),
        "slide81": ("Transformación Digital & Analítica", "Visualización de datos y entornos colaborativos."),
        "slide82": ("Inteligencia Artificial & Automatización", "Flujos de trabajo aumentados por IA."),
        "slide83": ("Equipos & Colaboración Empresarial", "Liderazgo, talleres de trabajo y personas."),
        "slide84": ("Sostenibilidad & Medio Ambiente (ESG)", "Huella de carbono, reciclaje, bosques y tecnología verde.")
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
            "width": w,
            "height": h,
            "size_kb": f"{size_kb:.1f} KB",
            "is_dark_bg": False,
            "desc": vert_desc,
            "tags": ["photo", "industry", s_tag, vert_title.lower(), "stock"]
        })

    return assets_db

assets_db = scan_assets()
db_json_str = json.dumps(assets_db)

html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Artefact Brand System & Asset Explorer</title>
  <link rel="stylesheet" href="tokens/artefact_theme.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary-gradient: linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);
      --bg-page: #F8F9FB;
      --card-bg: #FFFFFF;
      --text-main: #212121;
      --text-muted: #595959;
      --border-color: #E6E8EC;
      --accent-pink: #FF0066;
      --artefact-blue: #002244;
      --dark-navy: #0D1634;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: var(--bg-page);
      color: var(--text-main);
      line-height: 1.5;
      padding-bottom: 80px;
    }}

    /* Top Sticky Navigation Bar */
    .top-bar {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      padding: 12px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}
    .brand-logo-nav {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--artefact-blue);
      font-weight: 700;
      font-size: 16px;
    }}
    .brand-logo-nav img {{
      height: 28px;
    }}
    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .btn-action {{
      padding: 8px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      border: none;
    }}
    .btn-primary {{
      background: var(--accent-pink);
      color: white;
    }}
    .btn-primary:hover {{
      background: #E0005A;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(255,0,102,0.3);
    }}
    .btn-secondary {{
      background: #F0F2F5;
      color: var(--artefact-blue);
    }}
    .btn-secondary:hover {{
      background: #E4E7EB;
    }}

    /* Hero Banner */
    .hero-header {{
      background: var(--primary-gradient);
      color: white;
      padding: 60px 40px 50px 40px;
      margin: 24px auto;
      max-width: 1400px;
      border-radius: 20px;
      box-shadow: 0 16px 40px rgba(0, 34, 68, 0.2);
      position: relative;
      overflow: hidden;
    }}
    .hero-header h1 {{
      font-size: 40px;
      font-weight: 300;
      letter-spacing: -0.5px;
      margin-bottom: 10px;
    }}
    .hero-header p {{
      font-size: 17px;
      opacity: 0.92;
      max-width: 800px;
      line-height: 1.6;
      margin-bottom: 24px;
    }}
    .stats-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .stat-badge {{
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      backdrop-filter: blur(8px);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    /* Main Container */
    .main-container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* Search & Filter Toolbar */
    .toolbar {{
      background: white;
      padding: 16px 24px;
      border-radius: 14px;
      border: 1px solid var(--border-color);
      margin-bottom: 28px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.03);
    }}
    .search-box {{
      position: relative;
      flex: 1;
      min-width: 280px;
      max-width: 500px;
    }}
    .search-box input {{
      width: 100%;
      padding: 12px 16px 12px 42px;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      font-size: 14px;
      font-family: inherit;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }}
    .search-box input:focus {{
      border-color: var(--accent-pink);
      box-shadow: 0 0 0 3px rgba(255,0,102,0.12);
    }}
    .search-icon {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: #999;
      font-size: 16px;
    }}

    /* Tabs Filter Bar */
    .filter-tabs {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 30px;
    }}
    .tab-btn {{
      padding: 10px 20px;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      background: white;
      color: var(--text-main);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .tab-btn:hover {{
      background: #F4F6F9;
      border-color: #D0D4DC;
    }}
    .tab-btn.active {{
      background: var(--artefact-blue);
      color: white;
      border-color: var(--artefact-blue);
      box-shadow: 0 4px 12px rgba(0, 34, 68, 0.2);
    }}
    .tab-count {{
      background: rgba(0,0,0,0.08);
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 11px;
    }}
    .tab-btn.active .tab-count {{
      background: rgba(255,255,255,0.25);
    }}

    /* Sub-filter chips */
    .subfilter-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
    }}
    .chip-btn {{
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 500;
      background: #EBF0F5;
      color: var(--artefact-blue);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .chip-btn:hover {{
      background: #DFE5ED;
    }}
    .chip-btn.active {{
      background: var(--accent-pink);
      color: white;
      box-shadow: 0 2px 8px rgba(255,0,102,0.3);
    }}

    /* Section Headings */
    .section-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin: 36px 0 18px 0;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--border-color);
    }}
    .section-title {{
      font-size: 22px;
      font-weight: 700;
      color: var(--artefact-blue);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .section-desc {{
      font-size: 13px;
      color: var(--text-muted);
    }}

    /* Grid of Asset Cards */
    .asset-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 20px;
      margin-bottom: 40px;
    }}
    .asset-card {{
      background: white;
      border: 1px solid var(--border-color);
      border-radius: 14px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
      cursor: pointer;
      position: relative;
    }}
    .asset-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 12px 28px rgba(0,0,0,0.08);
      border-color: #CBD0DB;
    }}
    .asset-preview-box {{
      height: 160px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      background: #FAFAFB;
      position: relative;
    }}
    .asset-preview-box.dark-bg {{
      background: var(--dark-navy);
    }}
    .asset-preview-box img, .asset-preview-box svg {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      transition: transform 0.2s;
    }}
    .asset-card:hover .asset-preview-box img, .asset-card:hover .asset-preview-box svg {{
      transform: scale(1.05);
    }}
    .asset-info {{
      padding: 16px;
      display: flex;
      flex-direction: column;
      flex: 1;
      justify-content: space-between;
    }}
    .asset-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--artefact-blue);
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .asset-meta {{
      font-size: 11px;
      color: var(--text-muted);
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
    }}
    .asset-actions {{
      display: flex;
      gap: 8px;
    }}
    .btn-card {{
      flex: 1;
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 600;
      border: 1px solid var(--border-color);
      background: #F6F7F9;
      color: var(--artefact-blue);
      cursor: pointer;
      text-align: center;
      transition: all 0.15s;
    }}
    .btn-card:hover {{
      background: var(--artefact-blue);
      color: white;
      border-color: var(--artefact-blue);
    }}

    /* Color Swatches Grid */
    .color-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 16px;
      margin-bottom: 30px;
    }}
    .color-box {{
      background: white;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.2s;
    }}
    .color-box:hover {{
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    }}
    .color-fill {{
      height: 90px;
      width: 100%;
    }}
    .color-details {{
      padding: 14px;
    }}
    .color-name {{
      font-weight: 700;
      font-size: 14px;
      color: var(--artefact-blue);
      margin-bottom: 2px;
    }}
    .color-code {{
      font-family: monospace;
      font-size: 12px;
      color: var(--text-muted);
    }}

    /* Modal Viewer */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(0, 15, 35, 0.7);
      backdrop-filter: blur(6px);
      z-index: 1000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease;
    }}
    .modal-backdrop.open {{
      opacity: 1;
      pointer-events: auto;
    }}
    .modal-dialog {{
      background: white;
      width: 100%;
      max-width: 800px;
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 24px 60px rgba(0,0,0,0.3);
      display: flex;
      flex-direction: column;
      max-height: 90vh;
      animation: modalPop 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    @keyframes modalPop {{
      from {{ transform: scale(0.95); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}
    .modal-header {{
      padding: 20px 28px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .modal-header h3 {{
      font-size: 18px;
      color: var(--artefact-blue);
      font-weight: 700;
    }}
    .btn-close-modal {{
      background: none;
      border: none;
      font-size: 22px;
      color: #888;
      cursor: pointer;
    }}
    .modal-body {{
      padding: 28px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    .modal-preview-stage {{
      background: #F4F6F9;
      border-radius: 14px;
      padding: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 240px;
      position: relative;
    }}
    .modal-preview-stage.dark-bg {{
      background: var(--dark-navy);
    }}
    .modal-preview-stage img, .modal-preview-stage svg {{
      max-height: 200px;
      max-width: 100%;
      object-fit: contain;
    }}
    .code-snippet-box {{
      background: #181E29;
      color: #E2E8F0;
      padding: 16px;
      border-radius: 10px;
      font-family: monospace;
      font-size: 12px;
      position: relative;
      overflow-x: auto;
    }}
    .btn-copy-code {{
      position: absolute;
      top: 10px;
      right: 10px;
      background: rgba(255,255,255,0.15);
      color: white;
      border: none;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11px;
      cursor: pointer;
    }}
    .btn-copy-code:hover {{
      background: var(--accent-pink);
    }}

    /* Toast notification */
    .toast {{
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #111827;
      color: white;
      padding: 12px 24px;
      border-radius: 30px;
      font-size: 13px;
      font-weight: 500;
      box-shadow: 0 10px 30px rgba(0,0,0,0.25);
      z-index: 9999;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toast.show {{
      transform: translateX(-50%) translateY(0);
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation -->
  <header class="top-bar">
    <a href="#" class="brand-logo-nav">
      <img src="assets/logos/artefact_logo_primary_dark.png" alt="Artefact">
      <span>Brand System & Asset Explorer</span>
    </a>
    <div class="nav-actions">
      <a href="docs/ELEMENTS_AND_CONTEXT_PLAYBOOK.md" class="btn-action btn-secondary" target="_blank">📖 Playbook de Uso</a>
      <a href="/Users/israeltorres/Downloads/artefact-llm-presentation-kit-v1.zip" class="btn-action btn-primary" download>📦 Descargar ZIP Kit</a>
    </div>
  </header>

  <!-- Hero Header -->
  <div class="main-container">
    <div class="hero-header">
      <div style="font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; color: #FF0066; margin-bottom: 8px;">Official Master Release • November 2024</div>
      <h1>Artefact Executive Design System</h1>
      <p>Catálogo interactivo de activos visuales, logotipos, iconos 3D glassy, vectores SVG puros, banco de imágenes por industrias y tokens oficiales para generación de presentaciones ejecutivas.</p>
      
      <div class="stats-bar">
        <span class="stat-badge">🏷️ 11 Logotipos HD</span>
        <span class="stat-badge">🔮 12 Iconos 3D Glassy</span>
        <span class="stat-badge">📐 171 Vectores SVG</span>
        <span class="stat-badge">📱 39 Iconos UI</span>
        <span class="stat-badge">📸 89 Fotos por Industria</span>
        <span class="stat-badge">✂️ 9 Recortes PNG</span>
      </div>
    </div>

    <!-- Search & Filter Toolbar -->
    <div class="toolbar">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" placeholder="Buscar por nombre, industria (Retail, AI, Banca), formato o etiqueta..." oninput="onSearchChange()">
      </div>
      <div style="font-size: 13px; color: var(--text-muted);" id="resultsCount">
        Mostrando todos los activos
      </div>
    </div>

    <!-- Category Filter Tabs -->
    <div class="filter-tabs" id="categoryTabs">
      <button class="tab-btn active" onclick="setCategory('all')">🌈 Todos <span class="tab-count" id="countAll">0</span></button>
      <button class="tab-btn" onclick="setCategory('colors')">🎨 Paleta & Tokens</button>
      <button class="tab-btn" onclick="setCategory('logos')">🏷️ Logotipos <span class="tab-count" id="countLogos">11</span></button>
      <button class="tab-btn" onclick="setCategory('glassy')">🔮 Iconos 3D Glassy <span class="tab-count" id="countGlassy">12</span></button>
      <button class="tab-btn" onclick="setCategory('svg')">📐 Iconos Vectoriales SVG <span class="tab-count" id="countSvg">171</span></button>
      <button class="tab-btn" onclick="setCategory('ui_flat')">📱 Iconos Planos UI <span class="tab-count" id="countUi">39</span></button>
      <button class="tab-btn" onclick="setCategory('photography')">📸 Fotografía por Industria <span class="tab-count" id="countPhotos">89</span></button>
      <button class="tab-btn" onclick="setCategory('cutouts')">✂️ Recortes Transparentes <span class="tab-count" id="countCutouts">9</span></button>
      <button class="tab-btn" onclick="setCategory('typography')">✍️ Tipografía Roboto</button>
    </div>

    <!-- Subfilter chips for photography -->
    <div class="subfilter-bar" id="photoSubfilters" style="display: none;">
      <button class="chip-btn active" onclick="setPhotoVertical('all')">Todas las Industrias</button>
      <button class="chip-btn" onclick="setPhotoVertical('Retail')">🛒 Retail & E-commerce</button>
      <button class="chip-btn" onclick="setPhotoVertical('FMCG')">📦 FMCG & Lujo</button>
      <button class="chip-btn" onclick="setPhotoVertical('Banca')">💳 Banca & Finanzas</button>
      <button class="chip-btn" onclick="setPhotoVertical('Salud')">🔬 Salud & Farma</button>
      <button class="chip-btn" onclick="setPhotoVertical('Energía')">⚡ Energía & Utilities</button>
      <button class="chip-btn" onclick="setPhotoVertical('Telecom')">📡 Telecom & 5G</button>
      <button class="chip-btn" onclick="setPhotoVertical('Transformación')">🤖 IA & Tech</button>
      <button class="chip-btn" onclick="setPhotoVertical('Sostenibilidad')">🌱 Sostenibilidad ESG</button>
    </div>

    <!-- Color Palette Section (Dynamic / Toggleable) -->
    <div id="colorsSection">
      <div class="section-header">
        <div class="section-title">🎨 Paleta Oficial de Colores & Degradado Insigne</div>
        <div class="section-desc">Haz clic en cualquier muestra para copiar su código HEX al portapapeles</div>
      </div>
      
      <div style="height: 50px; border-radius: 12px; background: var(--primary-gradient); margin-bottom: 20px; box-shadow: 0 4px 14px rgba(0,0,0,0.1); cursor: pointer;" onclick="copyToClipboard('linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%)', 'CSS del Degradado')" title="Copiar CSS de Degradado"></div>

      <div class="color-grid">
        <div class="color-box" onclick="copyToClipboard('#002244', 'Artefact Blue')">
          <div class="color-fill" style="background:#002244;"></div>
          <div class="color-details">
            <div class="color-name">Artefact Blue</div>
            <div class="color-code">#002244 • Corporativo Primario</div>
          </div>
        </div>
        <div class="color-box" onclick="copyToClipboard('#FF0066', 'Artefact Pink')">
          <div class="color-fill" style="background:#FF0066;"></div>
          <div class="color-details">
            <div class="color-name">Artefact Pink</div>
            <div class="color-code">#FF0066 • Acento / KPIs</div>
          </div>
        </div>
        <div class="color-box" onclick="copyToClipboard('#0D1634', 'Dark Blue')">
          <div class="color-fill" style="background:#0D1634;"></div>
          <div class="color-details">
            <div class="color-name">Dark Blue</div>
            <div class="color-code">#0D1634 • Fondo Dark Mode</div>
          </div>
        </div>
        <div class="color-box" onclick="copyToClipboard('#273275', 'Medium Blue')">
          <div class="color-fill" style="background:#273275;"></div>
          <div class="color-details">
            <div class="color-name">Medium Blue</div>
            <div class="color-code">#273275 • Degradado Paso 2</div>
          </div>
        </div>
        <div class="color-box" onclick="copyToClipboard('#752E7D', 'Purple')">
          <div class="color-fill" style="background:#752E7D;"></div>
          <div class="color-details">
            <div class="color-name">Purple</div>
            <div class="color-code">#752E7D • Degradado Paso 3</div>
          </div>
        </div>
        <div class="color-box" onclick="copyToClipboard('#052BF6', 'Electric Blue')">
          <div class="color-fill" style="background:#052BF6;"></div>
          <div class="color-details">
            <div class="color-name">Electric Blue</div>
            <div class="color-code">#052BF6 • Gráficos Serie 1</div>
          </div>
        </div>
        <div class="color-box" onclick="copyToClipboard('#9900FF', 'Bright Purple')">
          <div class="color-fill" style="background:#9900FF;"></div>
          <div class="color-details">
            <div class="color-name">Bright Purple</div>
            <div class="color-code">#9900FF • Gráficos Serie 2</div>
          </div>
        </div>
        <div class="color-box" onclick="copyToClipboard('#F4F6F9', 'Surface Light')">
          <div class="color-fill" style="background:#F4F6F9; border-bottom:1px solid #eee;"></div>
          <div class="color-details">
            <div class="color-name">Surface Light</div>
            <div class="color-code">#F4F6F9 • Tarjetas y Paneles</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Typography Section (Toggleable) -->
    <div id="typographySection" style="display: none; margin-bottom: 40px;">
      <div class="section-header">
        <div class="section-title">✍️ Jerarquía Tipográfica Institucional — Roboto</div>
        <div class="section-desc">Escala exacta para presentaciones en formato 16:9 (1920x1080)</div>
      </div>
      <div style="background: white; border: 1px solid var(--border-color); border-radius: 14px; padding: 32px;">
        <div style="margin-bottom: 24px; padding-bottom: 20px; border-bottom: 1px solid var(--border-color);">
          <div style="font-size: 28px; font-weight: 400; color: var(--artefact-blue); line-height: 1.2;">
            Título de Diapositiva: La modernización hacia un Lakehouse unificado reduce los costos en un 40%
          </div>
          <div style="font-size: 12px; color: var(--text-muted); margin-top: 6px;">
            <code>Roboto Normal (400) • 20pt (28px)</code> • Regla de Oro: En estilo regular ligero para elegancia editorial.
          </div>
        </div>

        <div style="margin-bottom: 24px; padding-bottom: 20px; border-bottom: 1px solid var(--border-color);">
          <div style="font-size: 20px; font-weight: 700; color: var(--artefact-blue); line-height: 1.3;">
            Subtítulo / Contexto: Tres fases estructuradas para capturar valor y acelerar casos de uso con IA
          </div>
          <div style="font-size: 12px; color: var(--text-muted); margin-top: 6px;">
            <code>Roboto Bold (700) • 14pt (20px)</code> • Anclaje visual inmediato bajo el título principal.
          </div>
        </div>

        <div style="margin-bottom: 24px; padding-bottom: 20px; border-bottom: 1px solid var(--border-color);">
          <div style="font-size: 16px; font-weight: 400; color: var(--text-main); line-height: 1.5; max-width: 900px;">
            <strong>Gobernanza activa:</strong> Implementación de catálogo automatizado con linaje de datos de extremo a extremo para asegurar cumplimiento ético y disponibilidad de modelos.
          </div>
          <div style="font-size: 12px; color: var(--text-muted); margin-top: 6px;">
            <code>Roboto Normal (400) • 12pt (16px)</code> con lead-in en <code>Roboto Bold</code> para lectura rápida.
          </div>
        </div>

        <div style="display: flex; gap: 40px; align-items: baseline;">
          <div>
            <div style="font-size: 56px; font-weight: 900; color: var(--accent-pink); line-height: 1;">+35% ROI</div>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 4px;"><code>Roboto Black (900) • 44pt</code> (Métrica KPI Gigante)</div>
          </div>
          <div>
            <div style="font-size: 13px; font-weight: 500; color: var(--text-muted);">Fuente: Artefact Data & AI Assessment • 2024</div>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 4px;"><code>Roboto Medium (500) • 10pt</code> (Pie de página / Fuente)</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Asset Cards Grid (Populated dynamically) -->
    <div id="assetsGridContainer">
      <div class="section-header">
        <div class="section-title" id="gridSectionTitle">📦 Activos Visuales</div>
        <div class="section-desc">Haz clic en cualquier tarjeta para abrir el inspector y copiar snippets</div>
      </div>
      <div class="asset-grid" id="assetCardsGrid"></div>
    </div>

  </div>

  <!-- Modal Inspector Dialog -->
  <div class="modal-backdrop" id="modalBackdrop" onclick="closeModal(event)">
    <div class="modal-dialog" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3 id="modalTitle">Detalles del Activo</h3>
        <button class="btn-close-modal" onclick="closeModalDirect()">✕</button>
      </div>
      <div class="modal-body">
        <div class="modal-preview-stage" id="modalPreviewStage"></div>
        <div>
          <h4 style="font-size: 14px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 4px;" id="modalAssetName"></h4>
          <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5;" id="modalAssetDesc"></p>
        </div>
        <div>
          <div style="font-size: 12px; font-weight: 700; margin-bottom: 6px; color: var(--artefact-blue);">Código HTML para Presentation HTML (dom-to-pptx):</div>
          <div class="code-snippet-box">
            <button class="btn-copy-code" onclick="copySnippetFromModal('html')">Copiar</button>
            <code id="modalSnippetHtml"></code>
          </div>
        </div>
        <div>
          <div style="font-size: 12px; font-weight: 700; margin-bottom: 6px; color: var(--artefact-blue);">Ruta relativa local / CDN:</div>
          <div class="code-snippet-box">
            <button class="btn-copy-code" onclick="copySnippetFromModal('path')">Copiar</button>
            <code id="modalSnippetPath"></code>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Element -->
  <div class="toast" id="toastBox">
    <span>✅</span> <span id="toastMsg">Copiado al portapapeles</span>
  </div>

  <script>
    const assetsData = {db_json_str};
    let currentCategory = 'all';
    let currentPhotoVertical = 'all';
    let currentSearchTerm = '';
    let currentModalItem = null;

    // Initialize counts
    document.getElementById('countAll').innerText = 
      assetsData.logos.length + assetsData.glassy.length + assetsData.svg.length + 
      assetsData.ui_flat.length + assetsData.cutouts.length + assetsData.photography.length;
    document.getElementById('countLogos').innerText = assetsData.logos.length;
    document.getElementById('countGlassy').innerText = assetsData.glassy.length;
    document.getElementById('countSvg').innerText = assetsData.svg.length;
    document.getElementById('countUi').innerText = assetsData.ui_flat.length;
    document.getElementById('countPhotos').innerText = assetsData.photography.length;
    document.getElementById('countCutouts').innerText = assetsData.cutouts.length;

    function renderGrid() {{
      const grid = document.getElementById('assetCardsGrid');
      const colorsSec = document.getElementById('colorsSection');
      const typoSec = document.getElementById('typographySection');
      const photoSub = document.getElementById('photoSubfilters');
      const titleElem = document.getElementById('gridSectionTitle');

      // Visibility toggles
      colorsSec.style.display = (currentCategory === 'all' || currentCategory === 'colors') ? 'block' : 'none';
      typoSec.style.display = (currentCategory === 'all' || currentCategory === 'typography') ? 'block' : 'none';
      photoSub.style.display = (currentCategory === 'photography') ? 'flex' : 'none';

      if (currentCategory === 'colors' || currentCategory === 'typography') {{
        document.getElementById('assetsGridContainer').style.display = 'none';
        return;
      }} else {{
        document.getElementById('assetsGridContainer').style.display = 'block';
      }}

      // Aggregate list
      let list = [];
      if (currentCategory === 'all') {{
        list = [...assetsData.logos, ...assetsData.glassy, ...assetsData.svg.slice(0, 48), ...assetsData.ui_flat, ...assetsData.cutouts, ...assetsData.photography.slice(0, 36)];
        titleElem.innerText = '📦 Vista General de Activos (Muestra Representativa)';
      }} else if (currentCategory === 'logos') {{
        list = assetsData.logos;
        titleElem.innerText = '🏷️ Logotipos Oficiales Artefact (' + list.length + ')';
      }} else if (currentCategory === 'glassy') {{
        list = assetsData.glassy;
        titleElem.innerText = '🔮 Iconos 3D Glassy de Áreas de Práctica (' + list.length + ')';
      }} else if (currentCategory === 'svg') {{
        list = assetsData.svg;
        titleElem.innerText = '📐 Iconos Vectoriales SVG Puros (' + list.length + ')';
      }} else if (currentCategory === 'ui_flat') {{
        list = assetsData.ui_flat;
        titleElem.innerText = '📱 Iconos Planos UI Transparentes (' + list.length + ')';
      }} else if (currentCategory === 'cutouts') {{
        list = assetsData.cutouts;
        titleElem.innerText = '✂️ Recortes Transparentes / Cutouts (' + list.length + ')';
      }} else if (currentCategory === 'photography') {{
        list = assetsData.photography;
        if (currentPhotoVertical !== 'all') {{
          list = list.filter(item => item.vertical.toLowerCase().includes(currentPhotoVertical.toLowerCase()));
        }}
        titleElem.innerText = '📸 Banco de Fotografía por Industria (' + list.length + ')';
      }}

      // Apply search filter
      if (currentSearchTerm.trim() !== '') {{
        const q = currentSearchTerm.toLowerCase();
        list = list.filter(item => 
          item.name.toLowerCase().includes(q) || 
          item.title.toLowerCase().includes(q) ||
          item.desc.toLowerCase().includes(q) ||
          item.tags.some(t => t.toLowerCase().includes(q))
        );
      }}

      document.getElementById('resultsCount').innerText = 'Mostrando ' + list.length + ' activos';

      // Build HTML
      if (list.length === 0) {{
        grid.innerHTML = '<div style="grid-column: 1/-1; padding: 40px; text-align: center; color: #888;">No se encontraron activos para esta búsqueda.</div>';
        return;
      }}

      let cardsHtml = '';
      list.forEach((item, index) => {{
        const darkClass = item.is_dark_bg ? 'dark-bg' : '';
        const previewContent = item.svg_data 
          ? `<div style="width:72px;height:72px;display:flex;align-items:center;justify-content:center;">${{item.svg_data}}</div>`
          : `<img src="${{item.rel_path}}" alt="${{item.name}}" loading="lazy">`;

        cardsHtml += `
          <div class="asset-card" onclick="openModalByIndex('${{item.category}}', '${{item.name}}')">
            <div class="asset-preview-box ${{darkClass}}">
              ${{previewContent}}
            </div>
            <div class="asset-info">
              <div>
                <div class="asset-title" title="${{item.title}}">${{item.title}}</div>
                <div class="asset-meta">
                  <span>${{item.width}}x${{item.height}}</span>
                  <span>${{item.size_kb}}</span>
                </div>
              </div>
              <div class="asset-actions">
                <button class="btn-card" onclick="event.stopPropagation(); copyToClipboard('${{item.rel_path}}', '${{item.name}}')">Copiar Ruta</button>
                <button class="btn-card" onclick="event.stopPropagation(); openModalByIndex('${{item.category}}', '${{item.name}}')">Detalles</button>
              </div>
            </div>
          </div>
        `;
      }});

      grid.innerHTML = cardsHtml;
    }}

    function setCategory(cat) {{
      currentCategory = cat;
      const tabs = document.querySelectorAll('#categoryTabs .tab-btn');
      tabs.forEach(t => t.classList.remove('active'));
      event.currentTarget.classList.add('active');
      renderGrid();
    }}

    function setPhotoVertical(vert) {{
      currentPhotoVertical = vert;
      const chips = document.querySelectorAll('#photoSubfilters .chip-btn');
      chips.forEach(c => c.classList.remove('active'));
      event.currentTarget.classList.add('active');
      renderGrid();
    }}

    function onSearchChange() {{
      currentSearchTerm = document.getElementById('searchInput').value;
      renderGrid();
    }}

    function openModalByIndex(cat, name) {{
      // find item
      let all = [...assetsData.logos, ...assetsData.glassy, ...assetsData.svg, ...assetsData.ui_flat, ...assetsData.cutouts, ...assetsData.photography];
      let item = all.find(i => i.name === name);
      if (!item) return;

      currentModalItem = item;
      document.getElementById('modalTitle').innerText = item.title;
      document.getElementById('modalAssetName').innerText = item.name + ' (' + item.width + 'x' + item.height + ' • ' + item.size_kb + ')';
      document.getElementById('modalAssetDesc').innerText = item.desc;
      
      const preview = document.getElementById('modalPreviewStage');
      preview.className = 'modal-preview-stage ' + (item.is_dark_bg ? 'dark-bg' : '');
      if (item.svg_data) {{
        preview.innerHTML = `<div style="width:120px;height:120px;">${{item.svg_data}}</div>`;
      }} else {{
        preview.innerHTML = `<img src="${{item.rel_path}}" alt="${{item.name}}">`;
      }}

      // Snippets
      document.getElementById('modalSnippetHtml').innerText = `<img src="./${{item.rel_path}}" data-pptx-role="${{item.category === 'Logotipos' ? 'logo' : 'image'}}" alt="${{item.title}}">`;
      document.getElementById('modalSnippetPath').innerText = item.rel_path;

      document.getElementById('modalBackdrop').classList.add('open');
    }}

    function closeModal(e) {{
      if (e.target.id === 'modalBackdrop') {{
        document.getElementById('modalBackdrop').classList.remove('open');
      }}
    }}

    function closeModalDirect() {{
      document.getElementById('modalBackdrop').classList.remove('open');
    }}

    function copySnippetFromModal(type) {{
      if (!currentModalItem) return;
      if (type === 'html') {{
        copyToClipboard(`<img src="./${{currentModalItem.rel_path}}" data-pptx-role="${{currentModalItem.category === 'Logotipos' ? 'logo' : 'image'}}" alt="${{currentModalItem.title}}">`, 'HTML Snippet');
      }} else if (type === 'path') {{
        copyToClipboard(currentModalItem.rel_path, 'Ruta del Activo');
      }}
    }}

    function copyToClipboard(text, label) {{
      navigator.clipboard.writeText(text).then(() => {{
        showToast('Copiado: ' + label);
      }}).catch(() => {{
        showToast('Copiado: ' + text);
      }});
    }}

    function showToast(msg) {{
      const toast = document.getElementById('toastBox');
      document.getElementById('toastMsg').innerText = msg;
      toast.classList.add('show');
      setTimeout(() => {{
        toast.classList.remove('show');
      }}, 2400);
    }}

    // Initial render
    renderGrid();
  </script>
</body>
</html>
"""

# Write to root index.html
with open(os.path.join(BASE_DIR, "index.html"), "w") as f:
    f.write(html_template)

# Write to company-kits/artefact/index.html
with open(os.path.join(BASE_DIR, "company-kits", "artefact", "index.html"), "w") as f:
    f.write(html_template)

# Mirror to Desktop
os.makedirs(os.path.join(DESKTOP_DIR, "company-kits", "artefact"), exist_ok=True)
with open(os.path.join(DESKTOP_DIR, "company-kits", "artefact", "index.html"), "w") as f:
    f.write(html_template)

print("Comprehensive Asset Explorer Hub (index.html) successfully generated in all locations!")
