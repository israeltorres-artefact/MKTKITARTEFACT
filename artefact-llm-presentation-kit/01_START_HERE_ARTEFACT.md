# GUÍA RÁPIDA: KIT DE PRESENTACIONES EJECUTIVAS ARTEFACT PARA LLMS (GPT / GEMINI / CLAUDE)

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
