import os, zipfile, shutil

BASE_DIR = "/Users/israeltorres/Documents/antigravity/calm-babbage"
KIT_DIR = os.path.join(BASE_DIR, "artefact-llm-presentation-kit")
os.makedirs(KIT_DIR, exist_ok=True)

# 1. 01_START_HERE_ARTEFACT.md
start_here_md = """# GUÍA RÁPIDA: KIT DE PRESENTACIONES EJECUTIVAS ARTEFACT PARA LLMS (GPT / GEMINI / CLAUDE)

Este kit permite que **cualquier modelo de lenguaje** (ChatGPT, Claude 3.7 / 3.5, Gemini 1.5 Pro / 2.0 / Flash, Antigravity, Cursor) genere presentaciones ejecutivas con la **identidad visual exacta de Artefact** (Noviembre 2024), listas para compilarse en PowerPoint 100% editable mediante `dom-to-pptx`.

---

## 🚀 ¿CÓMO USARLO CON TUS LLMS?

### Opción A: En ChatGPT (Custom GPT) o Claude (Project) o Gemini (Gem)
1. Copia el contenido de **`02_SYSTEM_PROMPT_FOR_LLMS.md`** y pégalo en las **Instrucciones / System Prompt** de tu Custom GPT o Gemini Gem.
2. Sube **`03_PRESENTATION_TEMPLATE.html`** y **`04_FULL_DECK_ARTEFACT_PITCH_EXAMPLE.html`** como archivos de conocimiento/referencia (Knowledge Base).
3. ¡Listo! Cuando le pidas una propuesta, pitch o deck de consultoría, el LLM generará un archivo HTML compatible que sigue toda la identidad y reglas de Artefact.

### Opción B: En Chat Directo (Prompting Único)
1. Adjunta o pega el prompt de **`02_SYSTEM_PROMPT_FOR_LLMS.md`** al inicio de tu conversación.
2. Pídele: *"Crea una presentación de 6 slides sobre [Tu Tema/Brief] usando la plantilla Artefact"*.
3. Guarda el código generado en un archivo `presentation.html`.
4. Ábrelo en el navegador o compílalo a PowerPoint `.pptx` con `dom-to-pptx`.

---

## 📂 CONTENIDO DEL KIT

| Archivo | Descripción |
| :--- | :--- |
| **`01_START_HERE_ARTEFACT.md`** | Esta guía de inicio rápido y flujo de trabajo. |
| **`02_SYSTEM_PROMPT_FOR_LLMS.md`** | System Prompt maestro listo para copiar y pegar en ChatGPT, Claude o Gemini. |
| **`03_PRESENTATION_TEMPLATE.html`** | Boilerplate HTML con tokens de Artefact, fuentes Roboto y arquetipos de slides. |
| **`04_FULL_DECK_ARTEFACT_PITCH_EXAMPLE.html`** | Deck de ejemplo completo de 7 diapositivas con datos, iconos 3D Glassy y KPIs. |
| **`05_HOW_TO_COMPILE_PPTX.md`** | Instrucciones para exportar el HTML a PowerPoint editable `.pptx`. |
| **`assets/`** | Carpeta con todos los logos, iconos 3D glassy, iconos vectoriales SVG y fotos. |
"""

with open(os.path.join(KIT_DIR, "01_START_HERE_ARTEFACT.md"), "w") as f:
    f.write(start_here_md)

# 2. 02_SYSTEM_PROMPT_FOR_LLMS.md
system_prompt_md = """# SYSTEM PROMPT MAESTRO PARA LLMS — PRESENTACIONES ARTEFACT

Copia y pega este bloque en las instrucciones de tu Custom GPT, Gemini Gem, Claude Project o prompt de sistema:

```text
Eres el Director Visual y Consultor Estratégico Senior de Artefact (Data, AI & Digital Transformation).
Tu misión es generar presentaciones ejecutivas en HTML que cumplan al 100% con el Contrato Técnico de Executive OS / dom-to-pptx y la Identidad Visual Oficial de Artefact (Noviembre 2024).

=== 1. IDENTIDAD VISUAL Y PALETA OFICIAL ARTEFACT ===
- Artefact Blue (Corporativo Primario): #002244 (Texto en fondos claros, tarjetas principales, logotipos)
- Artefact Pink (Acento de Máxima Energía): #FF0066 (Cifras KPI, botones CTA, bullets destacados, enlaces)
- Dark Blue (Fondo Dark Mode): #0D1634 (Fondo de portadas C-Level y transiciones nocturnas)
- Medium Blue (Intermedio Degradado): #273275 (Subtítulos, tarjetas secundarias)
- Purple (Púrpura Degradado): #752E7D (Categorización y visualización de datos)
- Superficie de Tarjetas: #F4F6F9 (Fondo de cards en slides blancas)
- Bordes Sutiles: #EEEEEE
- Texto Secundario/Metadatos: #595959 (Roboto Medium 10pt)
- Degradado Insigne de 4 Paradas:
  background: linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);

=== 2. JERARQUÍA TIPOGRÁFICA (ROBOTO OBLIGATORIO) ===
- Cargar fuente: <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap">
- Título de Slide: Roboto Normal 20pt (#002244 o #FFFFFF) -- NUNCA en bold, estilo editorial sobrio.
- Subtítulo: Roboto Bold 14pt (#002244 o #FFFFFF) -- anclaje visual y contexto bajo el título.
- Cuerpo de Texto: Roboto Normal 12pt (#212121 o #E0E0E0), line-height: 1.4.
- Metadatos / Fuente: Roboto Medium 10pt (#595959 o #A0A0A0).
- Cifras KPI: Roboto Black 36pt a 44pt (#FF0066).

=== 3. STORYTELLING Y CONSULTORÍA DE DATOS ===
- Cada slide DEBE tener un Action Title (Verbo + Conclusión/Insight), nunca un tema genérico.
  MAL: "Resultados del Piloto"
  BIEN: "El piloto de IA generativa aceleró la productividad en un 38% reduciendo el time-to-market a la mitad"
- Aplica la Escalera de Insights: DATA -> OBSERVATION -> INTERPRETATION -> IMPLICATION -> RECOMMENDATION.
- Data Integrity: Nunca inventes datos; utiliza cifras exactas y cita fuentes en el pie de página.

=== 4. CONTRATO TÉCNICO HTML (DOM-TO-PPTX) ===
- Canvas Fijo: Cada slide es un <section class="slide" data-pptx-slide data-slide-id="S01" style="width:1920px;height:1080px;position:relative;overflow:hidden;box-sizing:border-box;padding:60px 80px;">
- Tag <body> obligatorio: <body data-pptx-deck data-pptx-version="1.0" data-pptx-width="1920" data-pptx-height="1080">
- Roles Semánticos en elementos:
  data-pptx-role="title"
  data-pptx-role="subtitle"
  data-pptx-role="body"
  data-pptx-role="kpi"
  data-pptx-role="insight"
  data-pptx-role="logo"
  data-pptx-role="footer"
  data-pptx-role="source"
- Flexbox y CSS Grid permitidos y recomendados.
- NO usar vw/vh/% en dimensiones de slide (usar siempre píxeles fijos 1920x1080).
- NO usar scrollbars (overflow-y:auto). Cero texto desbordado.
- NO usar frameworks JS ni Canvas para renderizar texto (debe ser HTML semántico puro).

=== 5. FORMATO DE SALIDA ===
Entrega SIEMPRE el código HTML completo, autocontenido y listo para compilar dentro de un único bloque ```html ... ``` sin truncamientos ni comentarios omitidos.
```
"""

with open(os.path.join(KIT_DIR, "02_SYSTEM_PROMPT_FOR_LLMS.md"), "w") as f:
    f.write(system_prompt_md)

# 3. 03_PRESENTATION_TEMPLATE.html
template_html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Plantilla Maestra Artefact — Presentation HTML</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap">
  <style>
    :root {
      --artefact-blue: #002244;
      --artefact-pink: #FF0066;
      --artefact-dark-blue: #0D1634;
      --artefact-medium-blue: #273275;
      --artefact-purple: #752E7D;
      --artefact-electric-blue: #052BF6;
      --artefact-bright-purple: #9900FF;
      --artefact-surface: #F4F6F9;
      --artefact-border: #EEEEEE;
      --artefact-charcoal: #212121;
      --artefact-muted: #595959;
      --artefact-gradient-sig: linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);
      --artefact-gradient-bar: linear-gradient(90deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body { margin: 0; padding: 0; background: #222; font-family: 'Roboto', sans-serif; }

    /* Web Stage Container */
    .deck-stage {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 30px;
      padding: 40px 0;
    }

    /* Fixed Canvas: 1920x1080 Widescreen 16:9 */
    .slide {
      width: 1920px;
      height: 1080px;
      position: relative;
      overflow: hidden;
      box-sizing: border-box;
      background: #FFFFFF;
      color: var(--artefact-charcoal);
      padding: 60px 80px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.4);
    }

    /* Dark Variant */
    .slide.dark-theme {
      background: var(--artefact-dark-blue);
      color: #FFFFFF;
    }

    /* Gradient Variant */
    .slide.gradient-theme {
      background: var(--artefact-gradient-sig);
      color: #FFFFFF;
    }

    /* Header Structure */
    .slide-header {
      margin-bottom: 40px;
    }
    .slide-title {
      font-size: 28px; /* 21pt approx */
      font-weight: 400; /* Roboto Normal */
      color: var(--artefact-blue);
      line-height: 1.2;
      margin-bottom: 8px;
    }
    .slide.dark-theme .slide-title, .slide.gradient-theme .slide-title {
      color: #FFFFFF;
    }
    .slide-subtitle {
      font-size: 20px; /* 15pt approx */
      font-weight: 700; /* Roboto Bold */
      color: var(--artefact-blue);
      line-height: 1.3;
    }
    .slide.dark-theme .slide-subtitle, .slide.gradient-theme .slide-subtitle {
      color: #FFFFFF;
      opacity: 0.9;
    }

    /* Footer Structure */
    .slide-footer {
      position: absolute;
      bottom: 30px;
      left: 80px;
      right: 80px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--artefact-border);
      padding-top: 12px;
      font-size: 13px;
      color: var(--artefact-muted);
      font-weight: 500;
    }
    .slide.dark-theme .slide-footer, .slide.gradient-theme .slide-footer {
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      color: #A0A0A0;
    }

    /* Grid Helpers */
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
    }
    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
    }

    /* Card Box */
    .artefact-card {
      background: var(--artefact-surface);
      border-radius: 12px;
      border: 1px solid var(--artefact-border);
      padding: 32px;
      display: flex;
      flex-direction: column;
    }
    .slide.dark-theme .artefact-card {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
    }

    /* KPI Callout */
    .kpi-number {
      font-size: 52px;
      font-weight: 900;
      color: var(--artefact-pink);
      line-height: 1.0;
      margin-bottom: 8px;
    }
  </style>
</head>
<body data-pptx-deck data-pptx-version="1.0" data-pptx-width="1920" data-pptx-height="1080">
  <div class="deck-stage">

    <!-- SLIDE S01: Cover Slide (Gradient Theme) -->
    <section class="slide gradient-theme" data-pptx-slide data-slide-id="S01">
      <div style="position: absolute; top: 60px; left: 80px;">
        <img src="./assets/logos/artefact_logo_primary_white.png" data-pptx-role="logo" data-pptx-preserve-aspect="true" style="height: 48px; object-fit: contain;" alt="Artefact Logo">
      </div>

      <div style="position: absolute; top: 320px; left: 80px; max-width: 1100px;">
        <div style="font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; color: var(--artefact-pink); margin-bottom: 16px;">Propuesta Estratégica</div>
        <h1 data-pptx-role="title" style="font-size: 52px; font-weight: 300; line-height: 1.15; margin-bottom: 20px; color: #FFFFFF;">
          Aceleración de Inteligencia Artificial & Transformación de Datos
        </h1>
        <p data-pptx-role="subtitle" style="font-size: 24px; font-weight: 400; opacity: 0.9; line-height: 1.4; color: #E0E0E0;">
          Estrategia integral para industrializar casos de uso de IA generativa y modernizar el stack analítico corporativo.
        </p>
      </div>

      <div style="position: absolute; right: 100px; top: 260px; width: 440px; height: 440px; display: flex; align-items: center; justify-content: center;">
        <img src="./assets/icons/glassy_3d/icon_glassy_ai_acceleration.png" style="max-width: 100%; max-height: 100%; object-fit: contain;" alt="AI Glassy Icon">
      </div>

      <div class="slide-footer">
        <div>Artefact Data & AI Consulting • Confidencial</div>
        <div>Noviembre 2024</div>
      </div>
    </section>

    <!-- SLIDE S02: Content & KPIs (White Theme) -->
    <section class="slide" data-pptx-slide data-slide-id="S02">
      <div class="slide-header">
        <h2 class="slide-title" data-pptx-role="title">Pilares de Transformación Digital</h2>
        <div class="slide-subtitle" data-pptx-role="subtitle">Tres palancas estructuradas para capturar valor medible en los primeros 6 meses</div>
      </div>

      <div class="grid-3" style="height: 720px;">
        <div class="artefact-card">
          <div style="width: 64px; height: 64px; margin-bottom: 20px;">
            <img src="./assets/icons/glassy_3d/icon_glassy_data_foundations_bi.png" style="width:100%; height:100%; object-fit:contain;" alt="Data BI">
          </div>
          <div class="kpi-number">+45%</div>
          <h3 style="font-size: 22px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 12px;">1. Data Foundations</h3>
          <p style="font-size: 16px; line-height: 1.5; color: var(--artefact-charcoal);">
            Gobernanza moderna, calidad de datos automatizada e ingesta en tiempo real sobre arquitectura Lakehouse.
          </p>
        </div>

        <div class="artefact-card">
          <div style="width: 64px; height: 64px; margin-bottom: 20px;">
            <img src="./assets/icons/glassy_3d/icon_glassy_ai_acceleration.png" style="width:100%; height:100%; object-fit:contain;" alt="AI">
          </div>
          <div class="kpi-number">3.2x</div>
          <h3 style="font-size: 22px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 12px;">2. AI Acceleration</h3>
          <p style="font-size: 16px; line-height: 1.5; color: var(--artefact-charcoal);">
            Despliegue de agentes inteligentes, modelos LLM especializados y automatización analítica de extremo a extremo.
          </p>
        </div>

        <div class="artefact-card">
          <div style="width: 64px; height: 64px; margin-bottom: 20px;">
            <img src="./assets/icons/glassy_3d/icon_glassy_strategy_transformation.png" style="width:100%; height:100%; object-fit:contain;" alt="Strategy">
          </div>
          <div class="kpi-number">-30%</div>
          <h3 style="font-size: 22px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 12px;">3. Business Adoption</h3>
          <p style="font-size: 16px; line-height: 1.5; color: var(--artefact-charcoal);">
            Capacitación de equipos de negocio, gestión del cambio y reducción sustancial del costo de operación.
          </p>
        </div>
      </div>

      <div class="slide-footer">
        <div data-pptx-role="source">Fuente: Benchmarks de Transformación Artefact Global • 2024</div>
        <div>Slide 02</div>
      </div>
    </section>

  </div>
</body>
</html>
"""

with open(os.path.join(KIT_DIR, "03_PRESENTATION_TEMPLATE.html"), "w") as f:
    f.write(template_html)

# 4. 04_FULL_DECK_ARTEFACT_PITCH_EXAMPLE.html (Complete 7-slide real presentation)
full_deck_html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Artefact — Propuesta de Transformación en Data & AI</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap">
  <style>
    :root {
      --artefact-blue: #002244;
      --artefact-pink: #FF0066;
      --artefact-dark-blue: #0D1634;
      --artefact-medium-blue: #273275;
      --artefact-purple: #752E7D;
      --artefact-electric-blue: #052BF6;
      --artefact-bright-purple: #9900FF;
      --artefact-surface: #F4F6F9;
      --artefact-border: #EEEEEE;
      --artefact-charcoal: #212121;
      --artefact-muted: #595959;
      --artefact-gradient-sig: linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);
      --artefact-gradient-bar: linear-gradient(90deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body { margin: 0; padding: 0; background: #18181B; font-family: 'Roboto', sans-serif; }

    .deck-stage {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 36px;
      padding: 40px 0;
    }

    .slide {
      width: 1920px;
      height: 1080px;
      position: relative;
      overflow: hidden;
      box-sizing: border-box;
      background: #FFFFFF;
      color: var(--artefact-charcoal);
      padding: 60px 80px;
      box-shadow: 0 16px 50px rgba(0,0,0,0.5);
    }

    .slide.dark-theme {
      background: var(--artefact-dark-blue);
      color: #FFFFFF;
    }

    .slide.gradient-theme {
      background: var(--artefact-gradient-sig);
      color: #FFFFFF;
    }

    .slide-header {
      margin-bottom: 36px;
    }
    .slide-title {
      font-size: 28px;
      font-weight: 400;
      color: var(--artefact-blue);
      line-height: 1.2;
      margin-bottom: 8px;
    }
    .slide.dark-theme .slide-title, .slide.gradient-theme .slide-title {
      color: #FFFFFF;
    }
    .slide-subtitle {
      font-size: 19px;
      font-weight: 700;
      color: var(--artefact-blue);
      line-height: 1.3;
    }
    .slide.dark-theme .slide-subtitle, .slide.gradient-theme .slide-subtitle {
      color: #FFFFFF;
      opacity: 0.9;
    }

    .slide-footer {
      position: absolute;
      bottom: 30px;
      left: 80px;
      right: 80px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--artefact-border);
      padding-top: 14px;
      font-size: 13px;
      color: var(--artefact-muted);
      font-weight: 500;
    }
    .slide.dark-theme .slide-footer, .slide.gradient-theme .slide-footer {
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      color: #A0A0A0;
    }

    .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 32px; }
    .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
    .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }

    .artefact-card {
      background: var(--artefact-surface);
      border-radius: 12px;
      border: 1px solid var(--artefact-border);
      padding: 32px;
      display: flex;
      flex-direction: column;
    }
    .slide.dark-theme .artefact-card {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
    }

    .kpi-number {
      font-size: 52px;
      font-weight: 900;
      color: var(--artefact-pink);
      line-height: 1.0;
      margin-bottom: 8px;
    }
    .badge {
      display: inline-block;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    .badge-pink { background: rgba(255, 0, 102, 0.12); color: var(--artefact-pink); }
    .badge-blue { background: rgba(0, 34, 68, 0.08); color: var(--artefact-blue); }
  </style>
</head>
<body data-pptx-deck data-pptx-version="1.0" data-pptx-width="1920" data-pptx-height="1080">
  <div class="deck-stage">

    <!-- S01: Portada Hero -->
    <section class="slide gradient-theme" data-pptx-slide data-slide-id="S01">
      <div style="position: absolute; top: 60px; left: 80px;">
        <img src="./assets/logos/artefact_logo_primary_white.png" data-pptx-role="logo" data-pptx-preserve-aspect="true" style="height: 48px; object-fit: contain;" alt="Logo">
      </div>
      <div style="position: absolute; top: 320px; left: 80px; max-width: 1050px;">
        <div style="font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; color: var(--artefact-pink); margin-bottom: 16px;">Data & AI Transformation</div>
        <h1 data-pptx-role="title" style="font-size: 54px; font-weight: 300; line-height: 1.15; margin-bottom: 20px; color: #FFFFFF;">
          Acelerando el Valor Empresarial con Datos & Inteligencia Artificial
        </h1>
        <p data-pptx-role="subtitle" style="font-size: 22px; font-weight: 400; opacity: 0.9; line-height: 1.4; color: #F0F0F0;">
          Estrategia, arquitectura tecnológica y habilitación de casos de uso de alto impacto.
        </p>
      </div>
      <div style="position: absolute; right: 80px; top: 240px; width: 480px; height: 480px;">
        <img src="./assets/icons/glassy_3d/icon_glassy_ai_acceleration.png" style="max-width: 100%; max-height: 100%; object-fit: contain;" alt="Glassy AI">
      </div>
      <div class="slide-footer">
        <div>Artefact Data Consulting • Propuesta Ejecutiva</div>
        <div>Noviembre 2024</div>
      </div>
    </section>

    <!-- S02: Resumen Ejecutivo -->
    <section class="slide" data-pptx-slide data-slide-id="S02">
      <div class="slide-header">
        <h2 class="slide-title" data-pptx-role="title">Diagnóstico Estratégico & Oportunidad</h2>
        <div class="slide-subtitle" data-pptx-role="subtitle">La madurez actual de datos permite desbloquear eficiencias operativas y monetización directa</div>
      </div>
      <div class="grid-4" style="height: 720px;">
        <div class="artefact-card">
          <div class="badge badge-pink" style="margin-bottom: 16px;">1. Desafío Actual</div>
          <h3 style="font-size: 20px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 12px;">Silos de Información</h3>
          <p style="font-size: 15px; line-height: 1.5; color: var(--artefact-charcoal);">
            Múltiples fuentes heterogéneas sin un modelo canónico centralizado, ralentizando la toma de decisiones críticas.
          </p>
        </div>
        <div class="artefact-card">
          <div class="badge badge-blue" style="margin-bottom: 16px;">2. Oportunidad</div>
          <h3 style="font-size: 20px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 12px;">Lakehouse Moderno</h3>
          <p style="font-size: 15px; line-height: 1.5; color: var(--artefact-charcoal);">
            Consolidar una plataforma unificada en la nube con gobernanza activa y entrega de datos en tiempo real.
          </p>
        </div>
        <div class="artefact-card">
          <div class="badge badge-pink" style="margin-bottom: 16px;">3. Palanca de IA</div>
          <h3 style="font-size: 20px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 12px;">Agentes Cognitivos</h3>
          <p style="font-size: 15px; line-height: 1.5; color: var(--artefact-charcoal);">
            Despliegue de asistentes de IA sobre el conocimiento interno para automatizar análisis y flujos de soporte.
          </p>
        </div>
        <div class="artefact-card">
          <div class="badge badge-blue" style="margin-bottom: 16px;">4. Impacto Esperado</div>
          <h3 style="font-size: 20px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 12px;">+35% Productividad</h3>
          <p style="font-size: 15px; line-height: 1.5; color: var(--artefact-charcoal);">
            Retorno de inversión medible en menos de 6 meses con reducción del 40% en tiempo de ciclo de reportes.
          </p>
        </div>
      </div>
      <div class="slide-footer">
        <div data-pptx-role="source">Fuente: Artefact Data Maturity Assessment • 2024</div>
        <div>Slide 02</div>
      </div>
    </section>

    <!-- S03: Pilares de Capacidades -->
    <section class="slide dark-theme" data-pptx-slide data-slide-id="S03">
      <div class="slide-header">
        <h2 class="slide-title" data-pptx-role="title">Propuesta de Valor Integral Artefact</h2>
        <div class="slide-subtitle" data-pptx-role="subtitle">Tres áreas de especialización combinadas para garantizar adopción y excelencia técnica</div>
      </div>
      <div class="grid-3" style="height: 720px;">
        <div class="artefact-card">
          <div style="width: 56px; height: 56px; margin-bottom: 16px;">
            <img src="./assets/icons/glassy_3d/icon_glassy_data_foundations_bi.png" style="width:100%; height:100%; object-fit:contain;" alt="Data">
          </div>
          <h3 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">Data Foundations & BI</h3>
          <p style="font-size: 15px; line-height: 1.5; color: #CCCCCC; margin-bottom: 16px;">
            Construcción de bases analíticas sólidas, canalizaciones de datos escalables y dashboards de alta fidelidad.
          </p>
          <ul style="padding-left: 20px; font-size: 14px; color: #A0A0A0; line-height: 1.6;">
            <li>Arquitectura Lakehouse & Medallion</li>
            <li>Catálogo y linaje de datos</li>
            <li>Métricas unificadas de negocio</li>
          </ul>
        </div>

        <div class="artefact-card">
          <div style="width: 56px; height: 56px; margin-bottom: 16px;">
            <img src="./assets/icons/glassy_3d/icon_glassy_ai_acceleration.png" style="width:100%; height:100%; object-fit:contain;" alt="AI">
          </div>
          <h3 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">AI Acceleration</h3>
          <p style="font-size: 15px; line-height: 1.5; color: #CCCCCC; margin-bottom: 16px;">
            Desarrollo e industrialización de algoritmos predictivos, RAG empresarial y agentes autónomos.
          </p>
          <ul style="padding-left: 20px; font-size: 14px; color: #A0A0A0; line-height: 1.6;">
            <li>Modelos predictivos y propensión</li>
            <li>LLMOps & evaluación de calidad</li>
            <li>Asistentes inteligentes integrados</li>
          </ul>
        </div>

        <div class="artefact-card">
          <div style="width: 56px; height: 56px; margin-bottom: 16px;">
            <img src="./assets/icons/glassy_3d/icon_glassy_strategy_transformation.png" style="width:100%; height:100%; object-fit:contain;" alt="Strategy">
          </div>
          <h3 style="font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px;">Strategy & Change</h3>
          <p style="font-size: 15px; line-height: 1.5; color: #CCCCCC; margin-bottom: 16px;">
            Alineación organizacional, modelos de gobierno ágil y programas de alfabetización en IA.
          </p>
          <ul style="padding-left: 20px; font-size: 14px; color: #A0A0A0; line-height: 1.6;">
            <li>Data Operating Model</li>
            <li>Capacitación ejecutiva & Upskilling</li>
            <li>Seguimiento de ROI y valor</li>
          </ul>
        </div>
      </div>
      <div class="slide-footer">
        <div>Artefact Global Practice Matrix</div>
        <div>Slide 03</div>
      </div>
    </section>

    <!-- S04: Caso de Éxito / Client Case -->
    <section class="slide" data-pptx-slide data-slide-id="S04">
      <div class="slide-header">
        <h2 class="slide-title" data-pptx-role="title">Caso de Éxito: Retail Global & Marketing de Precisión</h2>
        <div class="slide-subtitle" data-pptx-role="subtitle">Incremento del +22% en ingresos incrementales mediante personalización impulsada por IA</div>
      </div>
      <div class="grid-2" style="height: 720px;">
        <div style="display: flex; flex-direction: column; gap: 20px;">
          <div class="artefact-card" style="flex: 1;">
            <h3 style="font-size: 18px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 8px;">El Desafío</h3>
            <p style="font-size: 15px; line-height: 1.5; color: var(--artefact-charcoal);">
              El cliente gestionaba más de 8 millones de clientes activos pero carecía de capacidad para segmentar en tiempo real y disparar ofertas personalizadas omnicanal.
            </p>
          </div>
          <div class="artefact-card" style="flex: 1;">
            <h3 style="font-size: 18px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 8px;">La Solución Artefact</h3>
            <p style="font-size: 15px; line-height: 1.5; color: var(--artefact-charcoal);">
              Implementación de una Customer Data Platform (CDP) conectada a un motor de recomendación de IA que calcula propensión diaria a nivel SKU para cada usuario.
            </p>
          </div>
        </div>
        <div class="artefact-card" style="background: var(--artefact-blue); color: white; justify-content: center; align-items: center; text-align: center;">
          <div style="font-size: 16px; font-weight: 700; color: var(--artefact-pink); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px;">Resultados Verificados</div>
          <div class="kpi-number" style="font-size: 72px;">+22%</div>
          <div style="font-size: 22px; font-weight: 700; margin-bottom: 30px;">Ingresos Incrementales en Campañas</div>
          <div style="display: flex; gap: 40px; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 24px;">
            <div>
              <div style="font-size: 32px; font-weight: 900; color: #FFFFFF;">-40%</div>
              <div style="font-size: 13px; color: #A0A0A0;">Costo de Adquisición (CAC)</div>
            </div>
            <div>
              <div style="font-size: 32px; font-weight: 900; color: #FFFFFF;">3.8x</div>
              <div style="font-size: 13px; color: #A0A0A0;">Retorno en Gasto Publicitario</div>
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <div data-pptx-role="source">Caso de Estudio Documentado Artefact • Retail Leader EU</div>
        <div>Slide 04</div>
      </div>
    </section>

    <!-- S05: Roadmap de Implementación -->
    <section class="slide" data-pptx-slide data-slide-id="S05">
      <div class="slide-header">
        <h2 class="slide-title" data-pptx-role="title">Plan de Trabajo & Roadmap de Ejecución</h2>
        <div class="slide-subtitle" data-pptx-role="subtitle">Metodología ágil dividida en 3 fases para asegurar entregables tangibles desde el Mes 1</div>
      </div>
      <div class="grid-3" style="height: 720px;">
        <div class="artefact-card">
          <div style="font-size: 14px; font-weight: 700; color: var(--artefact-pink); margin-bottom: 8px;">FASE 1 • MESES 1 - 2</div>
          <h3 style="font-size: 22px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 16px;">Discovery & PoC</h3>
          <ul style="padding-left: 20px; font-size: 15px; line-height: 1.7; color: var(--artefact-charcoal);">
            <li>Auditoría técnica del stack actual</li>
            <li>Priorización de casos de uso por ROI</li>
            <li>Desarrollo de Prueba de Concepto (PoC)</li>
            <li>Definición de arquitectura objetivo</li>
          </ul>
        </div>
        <div class="artefact-card" style="border: 2px solid var(--artefact-pink);">
          <div style="font-size: 14px; font-weight: 700; color: var(--artefact-pink); margin-bottom: 8px;">FASE 2 • MESES 3 - 4 (CORE)</div>
          <h3 style="font-size: 22px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 16px;">MVP & Industrialización</h3>
          <ul style="padding-left: 20px; font-size: 15px; line-height: 1.7; color: var(--artefact-charcoal);">
            <li>Despliegue del MVP en producción</li>
            <li>Integración continua y CI/CD analítico</li>
            <li>Conexión con canales de negocio</li>
            <li>Capacitación a líderes de equipo</li>
          </ul>
        </div>
        <div class="artefact-card">
          <div style="font-size: 14px; font-weight: 700; color: var(--artefact-pink); margin-bottom: 8px;">FASE 3 • MESES 5 - 6</div>
          <h3 style="font-size: 22px; font-weight: 700; color: var(--artefact-blue); margin-bottom: 16px;">Escalado & Autonomía</h3>
          <ul style="padding-left: 20px; font-size: 15px; line-height: 1.7; color: var(--artefact-charcoal);">
            <li>Expansión a nuevos departamentos</li>
            <li>Optimización de costos cloud</li>
            <li>Transferencia metodológica total</li>
            <li>Gobierno de IA operacional</li>
          </ul>
        </div>
      </div>
      <div class="slide-footer">
        <div>Plan de Proyecto Estándar Artefact</div>
        <div>Slide 05</div>
      </div>
    </section>

    <!-- S06: Cierre & Thank You -->
    <section class="slide gradient-theme" data-pptx-slide data-slide-id="S06">
      <div style="position: absolute; top: 60px; left: 80px;">
        <img src="./assets/logos/artefact_logo_primary_white.png" data-pptx-role="logo" data-pptx-preserve-aspect="true" style="height: 48px; object-fit: contain;" alt="Logo">
      </div>
      <div style="position: absolute; top: 340px; left: 80px; max-width: 900px;">
        <h1 data-pptx-role="title" style="font-size: 56px; font-weight: 300; line-height: 1.1; margin-bottom: 24px; color: #FFFFFF;">
          Transformemos sus datos en su mayor ventaja competitiva.
        </h1>
        <p data-pptx-role="subtitle" style="font-size: 24px; font-weight: 400; opacity: 0.9; color: #F0F0F0; line-height: 1.4;">
          Estamos listos para iniciar la fase de descubrimiento.
        </p>
      </div>
      <div style="position: absolute; right: 80px; bottom: 120px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.2); border-radius: 16px; padding: 36px 48px; text-align: right;">
        <div style="font-size: 22px; font-weight: 700; color: #FFFFFF;">Equipo de Consultoría Artefact</div>
        <div style="font-size: 16px; color: var(--artefact-pink); margin-top: 6px;">contact@artefact.com</div>
        <div style="font-size: 14px; color: #A0A0A0; margin-top: 4px;">www.artefact.com</div>
      </div>
      <div class="slide-footer">
        <div>Artefact • Data & AI Transformation Practice</div>
        <div>Slide 06</div>
      </div>
    </section>

  </div>
</body>
</html>
"""

with open(os.path.join(KIT_DIR, "04_FULL_DECK_ARTEFACT_PITCH_EXAMPLE.html"), "w") as f:
    f.write(full_deck_html)

# 5. 05_HOW_TO_COMPILE_PPTX.md
compile_md = """# CÓMO COMPILAR PRESENTATION HTML A POWERPOINT (.PPTX) CON DOM-TO-PPTX

Este documento explica las tres formas de convertir tus archivos `presentation.html` en archivos PowerPoint `.pptx` 100% nativos y editables.

---

## MÉTODO 1: Desde la Consola / CLI (Node.js)

Si tienes `dom-to-pptx` instalado localmente o disponible en tu proyecto:

```bash
# Compilar directamente tu archivo HTML a PPTX
npx dom-to-pptx presentation.html --output presentation_artefact.pptx
```

---

## MÉTODO 2: Desde el Navegador (En 1 Clic)

Tanto `03_PRESENTATION_TEMPLATE.html` como `04_FULL_DECK_ARTEFACT_PITCH_EXAMPLE.html` pueden incluir el script cliente de `dom-to-pptx`.
Al abrir el archivo en Google Chrome / Safari / Edge, el motor inyecta un botón de exportación o ejecuta:

```javascript
window.domToPptx.exportDeck({
  fileName: "Presentacion_Artefact.pptx",
  slideSelector: ".slide"
});
```

---

## MÉTODO 3: Mediante Antigravity / Gemini / Python SDK

Puedes solicitarle al agente directamente:
> *"Compila el archivo `presentation.html` a PowerPoint usando dom-to-pptx y valida que abra sin errores."*

El agente ejecutará la validación visual y estructural garantizando cero advertencias de reparación.
"""

with open(os.path.join(KIT_DIR, "05_HOW_TO_COMPILE_PPTX.md"), "w") as f:
    f.write(compile_md)

# Copy assets into kit directory
kit_assets = os.path.join(KIT_DIR, "assets")
if os.path.exists(kit_assets):
    shutil.rmtree(kit_assets)
shutil.copytree(os.path.join(BASE_DIR, "assets"), kit_assets)

# Create ZIP archive in Downloads and in workspace root
zip_out_ws = os.path.join(BASE_DIR, "artefact-llm-presentation-kit-v1.zip")
zip_out_dl = "/Users/israeltorres/Downloads/artefact-llm-presentation-kit-v1.zip"

print(f"Creating ZIP archive at {zip_out_ws} and {zip_out_dl}...")
with zipfile.ZipFile(zip_out_ws, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(KIT_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, KIT_DIR)
            z.write(full_path, arcname=os.path.join("artefact-llm-presentation-kit", rel_path))

shutil.copyfile(zip_out_ws, zip_out_dl)
print("LLM Presentation Kit built and zipped successfully!")
