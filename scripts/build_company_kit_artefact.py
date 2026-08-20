import os, json, shutil

BASE_DIR = "/Users/israeltorres/Documents/antigravity/calm-babbage"
KITS_ROOT = os.path.join(BASE_DIR, "company-kits")
ARTEFACT_KIT = os.path.join(KITS_ROOT, "artefact")

os.makedirs(ARTEFACT_KIT, exist_ok=True)
os.makedirs(os.path.join(ARTEFACT_KIT, "tokens"), exist_ok=True)
os.makedirs(os.path.join(ARTEFACT_KIT, "guidelines"), exist_ok=True)
os.makedirs(os.path.join(ARTEFACT_KIT, "llm"), exist_ok=True)
os.makedirs(os.path.join(ARTEFACT_KIT, "templates"), exist_ok=True)

# 1. Manifest JSON
manifest = {
    "$schema": "https://presentation-os.internal/schemas/company-kit.json",
    "id": "artefact",
    "name": "Artefact",
    "fullName": "Artefact — Data & AI Consulting",
    "version": "1.0.0",
    "templateRelease": "November 2024",
    "description": "Kit oficial de identidad corporativa, tokens, reglas de maquetación HTML y assets de presentación para Artefact.",
    "brandColors": {
        "primary": "#002244",
        "accent": "#FF0066",
        "darkBackground": "#0D1634",
        "secondaryBlue": "#273275",
        "purple": "#752E7D",
        "gradient": "linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%)"
    },
    "typography": {
        "primaryFamily": "Roboto",
        "weights": ["100", "300", "400", "500", "700", "900"],
        "hierarchy": {
            "slideTitle": "Roboto Normal 20pt",
            "slideSubtitle": "Roboto Bold 14pt",
            "bodyText": "Roboto Normal 12pt",
            "legendSource": "Roboto Medium 10pt",
            "kpiMetric": "Roboto Black 36-44pt"
        }
    },
    "assetCounts": {
        "logos": 11,
        "glassy3dIcons": 12,
        "uiFlatIcons": 39,
        "symbolBanners": 16,
        "vectorSvgIcons": 171,
        "cutouts": 9,
        "photography": 89
    },
    "files": {
        "context": "context.md",
        "guidelines": "guidelines/brand_guidelines.md",
        "palette": "guidelines/palette_guide.md",
        "typography": "guidelines/typography_guide.md",
        "iconsCatalog": "guidelines/icons_catalog.md",
        "slideTaxonomy": "guidelines/slide_taxonomy.md",
        "systemPrompt": "llm/system_prompt.md",
        "skill": "llm/skill.md",
        "template": "templates/template.html",
        "fullDeckExample": "templates/full_deck_example.html",
        "tokensCss": "tokens/theme.css",
        "tokensColorsJson": "tokens/colors.json",
        "tokensTypographyJson": "tokens/typography.json"
    }
}

with open(os.path.join(ARTEFACT_KIT, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=2)

# 2. Registry JSON for multi-brand architecture
registry = {
    "version": "1.0.0",
    "defaultKit": "artefact",
    "kits": [
        {
            "id": "artefact",
            "name": "Artefact",
            "path": "artefact/manifest.json",
            "status": "active",
            "description": "Data & AI Consulting Master Template (Nov 2024)"
        },
        {
            "id": "bch",
            "name": "Banco de Chile",
            "path": "bch/manifest.json",
            "status": "available",
            "description": "Banco de Chile Executive Presentation Engine"
        }
    ]
}

with open(os.path.join(KITS_ROOT, "REGISTRY.json"), "w") as f:
    json.dump(registry, f, indent=2)

# 3. README for the entire company-kits directory
kits_readme = """# 🏢 COMPANY PRESENTATION KITS — MULTI-BRAND ARCHITECTURE

Este directorio almacena los **Kits de Presentación Específicos por Empresa / Marca** para el motor de generación y compilación de presentaciones ejecutivas (`dom-to-pptx`).

Cada kit encapsula de forma aislada:
- **Tokens de Diseño**: Colores HEX/RGB, gradientes, tipografías y variables CSS.
- **Activos Oficiales**: Logotipos, iconos 3D glassy, iconos planos, vectores SVG y banco de imágenes.
- **Reglas de Storytelling & Consultoría**: Estructura de diapositivas, Action Titles y jerarquía.
- **Prompts & Skills para LLMs**: System Prompts y definiciones de Skill para ChatGPT, Claude, Gemini y Antigravity.
- **Plantillas HTML**: Boilerplates pre-maquetados en resolución 1920x1080 listos para compilar.

---

## 📋 Catálogo de Kits Disponibles

| Kit ID | Empresa / Marca | Vertical / Enfoque | Estado |
| :--- | :--- | :--- | :---: |
| **`artefact`** | **Artefact** | Consultoría en Data, AI & Transformación Digital | 🟢 **Activo & Completo (Nov 2024)** |
| **`bch`** | **Banco de Chile** | Banca, Medios de Pago & Presentaciones C-Level | 🟢 **Disponible** |

---

## 🧩 Estructura Estándar de un Kit de Empresa

```text
company-kits/[kit-id]/
├── manifest.json              # Metadatos estructurados del kit
├── context.md                 # Contexto de negocio y filosofía de diseño
├── tokens/                    # Tokens de color, tipografía y CSS
├── guidelines/                # Manuales de marca, paleta, tipografía y catálogo
├── llm/                       # System prompt y skill para modelos de lenguaje
├── templates/                 # Boilerplates HTML 1920x1080 compatibles con dom-to-pptx
└── assets/                    # Logos, iconos 3D, SVG y fotografías
```
"""

with open(os.path.join(KITS_ROOT, "README.md"), "w") as f:
    f.write(kits_readme)

# 4. Context MD inside artefact kit
context_md = """# CONTEXTO INTERNO DEL KIT ARTEFACT — DATA & AI CONSULTING

Este documento proporciona el **contexto maestro** para cualquier agente, LLM o desarrollador que necesite generar o mantener presentaciones con la identidad de **Artefact**.

---

## 1. Identidad & Misión de la Compañía
- **Empresa**: Artefact (Consultora Global de Data, AI, Marketing Digital y Transformación Tecnológica).
- **Filosofía Visual**: Precisión analítica e ingenieril combinada con sofisticación editorial y dinamismo tecnológico.
- **Mantra de Comunicación**: *Insight First* — cada diapositiva responde a una pregunta de negocio, comunica una decisión y sustenta la evidencia con datos irrebatibles.

---

## 2. Pilares de la Identidad Visual

### A. Paleta de Colores
1. **Artefact Blue (`#002244`)**: Azul corporativo oscuro primario. Representa rigor, estructura y confianza. Usado para textos en fondo blanco, cabeceras y logotipos.
2. **Artefact Pink (`#FF0066`)**: Rosa vibrante de alta energía. Representa innovación, diferenciación y dinamismo. Usado para cifras KPI gigantes, botones CTA y bullets destacados.
3. **Dark Blue (`#0D1634`)**: Azul noche profundo. Usado como fondo para portadas de alto impacto y presentaciones en modo oscuro.
4. **Medium Blue (`#273275`)** & **Purple (`#752E7D`)**: Tonos de transición que completan el degradado insigne de 4 paradas.
5. **Degradado Insigne (Signature Gradient)**:
   `linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%)`

### B. Tipografía Exclusiva: Roboto
- **Títulos de Slide**: `Roboto Normal 20pt` (estilo editorial sobrio, no en negrita).
- **Subtítulos**: `Roboto Bold 14pt` (anclaje de peso visual bajo el título).
- **Cuerpo de Texto**: `Roboto Normal 12pt` (lectura cómoda, interlineado 1.4).
- **Metadatos y Leyendas**: `Roboto Medium 10pt`.
- **Cifras KPI**: `Roboto Black 36-44pt` (`#FF0066`).

### C. Iconografía Oficial
- **Iconos 3D Glassy**: Elementos tridimensionales con textura de cristal para representar las áreas de práctica: *Data Foundations & BI*, *AI Acceleration*, *IT Platform*, *Strategy & Transformation*, *CX & Marketing*, *People*, *Clients* e *Iconic A*.
- **Iconos Planos de UI**: 39 iconos transparentes para viñetas, tarjetas y tablas.
- **Iconos Vectoriales SVG**: 171 formas vectoriales puras en SVG.

---

## 3. Contrato Técnico con el Compilador (dom-to-pptx)
Para garantizar que cualquier slide exporte limpiamente a PowerPoint `.pptx` 100% editable:
- **Dimensiones de Slide**: `1920px × 1080px` fijas (16:9 Widescreen).
- **Contenedor**: `<body data-pptx-deck data-pptx-version="1.0" data-pptx-width="1920" data-pptx-height="1080">`
- **Sección de Slide**: `<section class="slide" data-pptx-slide data-slide-id="S01">`
- **Roles Semánticos**: `data-pptx-role="title"`, `data-pptx-role="subtitle"`, `data-pptx-role="kpi"`, `data-pptx-role="body"`, `data-pptx-role="logo"`.
- **Cero desbordes**: Altura de línea y padding controlados para evitar texto recortado.
"""

with open(os.path.join(ARTEFACT_KIT, "context.md"), "w") as f:
    f.write(context_md)

# Copy tokens
shutil.copyfile(os.path.join(BASE_DIR, "tokens", "colors.json"), os.path.join(ARTEFACT_KIT, "tokens", "colors.json"))
shutil.copyfile(os.path.join(BASE_DIR, "tokens", "typography.json"), os.path.join(ARTEFACT_KIT, "tokens", "typography.json"))
shutil.copyfile(os.path.join(BASE_DIR, "tokens", "artefact_theme.css"), os.path.join(ARTEFACT_KIT, "tokens", "theme.css"))

# Copy guidelines
shutil.copyfile(os.path.join(BASE_DIR, "docs", "brand_guidelines_artefact.md"), os.path.join(ARTEFACT_KIT, "guidelines", "brand_guidelines.md"))
shutil.copyfile(os.path.join(BASE_DIR, "docs", "palette.md"), os.path.join(ARTEFACT_KIT, "guidelines", "palette_guide.md"))
shutil.copyfile(os.path.join(BASE_DIR, "docs", "typography.md"), os.path.join(ARTEFACT_KIT, "guidelines", "typography_guide.md"))
shutil.copyfile(os.path.join(BASE_DIR, "docs", "icons_catalog.md"), os.path.join(ARTEFACT_KIT, "guidelines", "icons_catalog.md"))
shutil.copyfile(os.path.join(BASE_DIR, "docs", "slide_templates_index.md"), os.path.join(ARTEFACT_KIT, "guidelines", "slide_taxonomy.md"))

# Copy LLM prompts
shutil.copyfile(os.path.join(BASE_DIR, "artefact-llm-presentation-kit", "02_SYSTEM_PROMPT_FOR_LLMS.md"), os.path.join(ARTEFACT_KIT, "llm", "system_prompt.md"))
shutil.copyfile(os.path.join(os.path.expanduser("~"), ".gemini/config/skills/presentaciones-ejecutivas-artefact/SKILL.md"), os.path.join(ARTEFACT_KIT, "llm", "skill.md"))

# Copy templates
shutil.copyfile(os.path.join(BASE_DIR, "artefact-llm-presentation-kit", "03_PRESENTATION_TEMPLATE.html"), os.path.join(ARTEFACT_KIT, "templates", "template.html"))
shutil.copyfile(os.path.join(BASE_DIR, "artefact-llm-presentation-kit", "04_FULL_DECK_ARTEFACT_PITCH_EXAMPLE.html"), os.path.join(ARTEFACT_KIT, "templates", "full_deck_example.html"))

# Copy assets
kit_assets = os.path.join(ARTEFACT_KIT, "assets")
if os.path.exists(kit_assets):
    shutil.rmtree(kit_assets)
shutil.copytree(os.path.join(BASE_DIR, "assets"), kit_assets)

print("Company kit for Artefact successfully assembled at:", ARTEFACT_KIT)
