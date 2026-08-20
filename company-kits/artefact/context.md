# CONTEXTO INTERNO DEL KIT ARTEFACT — DATA & AI CONSULTING

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
