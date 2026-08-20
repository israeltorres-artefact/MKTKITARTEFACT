import os
import json

BASE_DIR = "/Users/israeltorres/Documents/antigravity/calm-babbage"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
os.makedirs(DOCS_DIR, exist_ok=True)

# 1. docs/palette.md
palette_md = """# Manual de Paleta de Colores & Degradados — Artefact (Noviembre 2024)

Este documento define la especificación técnica completa de los colores y degradados oficiales de **Artefact**, extraídos de la plantilla maestra corporativa.

---

## 1. Colores Corporativos Primarios (Primary Brand Colors)

Los dos colores nucleares que definen la marca Artefact en todas sus comunicaciones.

| Nombre de Color | Muestra | HEX | RGB | HSL | Rol & Uso Principal |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Artefact Blue** | <div style="background:#002244; width:48px; height:24px; border-radius:4px;"></div> | `#002244` | `rgb(0, 34, 68)` | `hsl(210, 100%, 13%)` | Color corporativo dominante. Textos principales en fondos claros, encabezados, logotipos y tarjetas de contenido. |
| **Artefact Pink** | <div style="background:#FF0066; width:48px; height:24px; border-radius:4px;"></div> | `#FF0066` | `rgb(255, 0, 102)` | `hsl(336, 100%, 50%)` | Color de acento de máxima energía. KPIs clave, bullets destacados, hipervínculos, botones de llamada a la acción y final del degradado institucional. |

---

## 2. Colores Secundarios Institucionales (Secondary Colors)

Gama cromática de soporte que complementa la narrativa visual y permite crear profundidad y jerarquía en diapositivas complejas.

| Nombre de Color | Muestra | HEX | RGB | HSL | Rol & Uso Principal |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Dark Blue** | <div style="background:#0D1634; width:48px; height:24px; border-radius:4px;"></div> | `#0D1634` | `rgb(13, 22, 52)` | `hsl(226, 60%, 13%)` | Fondo para el universo *Blue Background Slides*. Aporta contraste sobrio para presentaciones ejecutivas nocturnas o de alto impacto. |
| **Medium Blue** | <div style="background:#273275; width:48px; height:24px; border-radius:4px;"></div> | `#273275` | `rgb(39, 50, 117)` | `hsl(232, 50%, 31%)` | Segundo escalón del degradado. Usado en subtítulos, contenedores secundarios y acentos sobrios. |
| **Purple** | <div style="background:#752E7D; width:48px; height:24px; border-radius:4px;"></div> | `#752E7D` | `rgb(117, 46, 125)` | `hsl(294, 44%, 34%)` | Tercer escalón del degradado. Conecta el azul medio con el rosa brillante. Ideal para categorización y visualización de datos. |

---

## 3. Degradado Insigne Oficial (Artefact Multi-Stop Gradient)

El degradado de 4 paradas (4-stop gradient) es el elemento visual más distintivo de la marca.

```
#002244 (0%) ───► #273275 (33%) ───► #752E7D (66%) ───► #FF0066 (100%)
(Artefact Blue)     (Medium Blue)       (Purple)           (Artefact Pink)
```

### Especificaciones Técnicas

#### CSS (Web & Presentation HTML)
```css
/* Diagonal 135° (Fondos de diapositiva y portadas) */
background: linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);

/* Horizontal 90° (Barras de transición, subrayados y divisores) */
background: linear-gradient(90deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%);
```

#### OpenXML DrawingML (PowerPoint)
```xml
<a:gradFill>
  <a:gsLst>
    <a:gs pos="0"><a:srgbClr val="002244"/></a:gs>
    <a:gs pos="33000"><a:srgbClr val="273275"/></a:gs>
    <a:gs pos="66000"><a:srgbClr val="752E7D"/></a:gs>
    <a:gs pos="100000"><a:srgbClr val="FF0066"/></a:gs>
  </a:gsLst>
  <a:lin ang="8100000"/>
</a:gradFill>
```

---

## 4. Colores de Soporte & Visualización de Datos (Data Viz Palette)

| Color | Muestra | HEX | RGB | Rol |
| :--- | :---: | :---: | :---: | :--- |
| **Electric Blue** | <div style="background:#052BF6; width:48px; height:24px; border-radius:4px;"></div> | `#052BF6` | `rgb(5, 43, 246)` | Serie de datos 1 en gráficos / Badges de tecnología. |
| **Bright Purple** | <div style="background:#9900FF; width:48px; height:24px; border-radius:4px;"></div> | `#9900FF` | `rgb(153, 0, 255)` | Serie de datos 2 en gráficos / Badges de AI. |
| **Cyan Teal** | <div style="background:#0097A7; width:48px; height:24px; border-radius:4px;"></div> | `#0097A7` | `rgb(0, 151, 167)` | Serie de datos 3 / Indicadores de completitud. |
| **Amber Gold** | <div style="background:#FFAB40; width:48px; height:24px; border-radius:4px;"></div> | `#FFAB40` | `rgb(255, 171, 64)` | Serie de datos 4 / Advertencias y llamadas de atención. |

---

## 5. Colores Neutros & Superficies

| Nombre | Muestra | HEX | Uso |
| :--- | :---: | :---: | :--- |
| **Pure White** | <div style="background:#FFFFFF; width:48px; height:24px; border:1px solid #ccc; border-radius:4px;"></div> | `#FFFFFF` | Fondo de diapositiva estándar y texto en fondos oscuros. |
| **Surface Gray** | <div style="background:#F4F6F9; width:48px; height:24px; border:1px solid #ccc; border-radius:4px;"></div> | `#F4F6F9` | Fondo de tarjetas (cards) y contenedores de contenido. |
| **Border Gray** | <div style="background:#EEEEEE; width:48px; height:24px; border:1px solid #ccc; border-radius:4px;"></div> | `#EEEEEE` | Líneas divisorias, bordes de tabla y grillas sutiles. |
| **Muted Charcoal** | <div style="background:#595959; width:48px; height:24px; border-radius:4px;"></div> | `#595959` | Textos secundarios, pies de página, fuentes y leyendas. |
| **Dark Body Text** | <div style="background:#212121; width:48px; height:24px; border-radius:4px;"></div> | `#212121` | Texto de lectura extendida y párrafos sobre fondo blanco. |

---

## 6. Matriz de Aplicación por Universo Visual

La plantilla oficial de Artefact divide las diapositivas en 3 universos visuales consistentes:

```
┌───────────────────────────────┬───────────────────────────────┬───────────────────────────────┐
│     1. White Background       │      2. Blue Background       │    3. Gradient Background     │
├───────────────────────────────┼───────────────────────────────┼───────────────────────────────┤
│ • Fondo: #FFFFFF              │ • Fondo: #0D1634 o #002244    │ • Fondo: Signature Gradient   │
│ • Título: #002244 (20pt)      │ • Título: #FFFFFF (20pt)      │ • Título: #FFFFFF (20pt)      │
│ • Subtítulo: #002244 (14pt B) │ • Subtítulo: #FFFFFF (14pt B) │ • Subtítulo: #FFFFFF (14pt B) │
│ • Cuerpo: #212121 (12pt)      │ • Cuerpo: #E0E0E0 (12pt)      │ • Cuerpo: #FFFFFF (12pt)      │
│ • Acento: #FF0066 (Pink)      │ • Acento: #FF0066 (Pink)      │ • Acento: #FFFFFF / #FF0066   │
│ • Tarjetas: #F4F6F9 o Borde   │ • Tarjetas: Opacidad / Línea  │ • Uso: Portadas, Cierres      │
└───────────────────────────────┴───────────────────────────────┴───────────────────────────────┘
```
"""

with open(os.path.join(DOCS_DIR, "palette.md"), "w") as f:
    f.write(palette_md)

# 2. docs/typography.md
typography_md = """# Guía de Tipografía & Jerarquía de Texto — Artefact (Noviembre 2024)

Especificación técnica de fuentes, pesos, tamaños y reglas de maquetación tipográfica de **Artefact**.

---

## 1. Familia Tipográfica Oficial: Roboto

La identidad de Artefact utiliza exclusivamente la familia tipográfica **Roboto** por su claridad geométrica, legibilidad universal en pantalla y compatibilidad nativa en Google Slides y PowerPoint.

### Pesos Permitidos (Font Weights)

| Peso | Nombre Técnico | Valor CSS | Uso en la Identidad |
| :--- | :--- | :---: | :--- |
| **Black** | `Roboto Black` | `900` | Cifras KPI gigantes (36pt - 48pt), números de impacto. |
| **Bold** | `Roboto Bold` | `700` | Subtítulos (14pt), encabezados de sección, nombres de persona. |
| **Medium** | `Roboto Medium` | `500` | Fuentes, leyendas, metadatos, tags y badges. |
| **Normal / Regular** | `Roboto Normal` | `400` | Títulos principales de slide (20pt) y párrafos de cuerpo (12pt). |
| **Light** | `Roboto Light` | `300` | Textos explicativos en fondos oscuros o citas destacadas. |
| **Thin** | `Roboto Thin` | `100` | Elementos ornamentales o números decorativos de fondo. |

---

## 2. Escala Tipográfica Institucional (Slide Hierarchy)

La Slide 68 de las guías gráficas de Artefact establece la siguiente jerarquía formal:

```
┌────────────────────────────────────────────────────────────────────────┐
│ [Title]            Roboto Normal 20pt    (#002244 o #FFFFFF)           │
│                                                                        │
│ [Subtitle]         Roboto Bold 14pt      (#002244 o #FFFFFF)           │
│                                                                        │
│ [Body Text]        Roboto Normal 12pt    (#212121 o #E0E0E0)           │
│                                                                        │
│ [Legend / Source]  Roboto Medium 10pt    (#595959 o #A0A0A0)           │
└────────────────────────────────────────────────────────────────────────┘
```

### Tabla de Especificación Detallada

| Elemento | Fuente & Peso | Tamaño (pt) | Tamaño (px en 1920x1080) | Interlineado | Color (Fondo Claro) | Color (Fondo Oscuro) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Título de Slide** | `Roboto Normal` | `20 pt` | `27 px` | `1.2` | `#002244` | `#FFFFFF` |
| **Subtítulo** | `Roboto Bold` | `14 pt` | `19 px` | `1.3` | `#002244` | `#FFFFFF` |
| **Cabecera de Tarjeta** | `Roboto Bold` | `13 pt` | `17 px` | `1.2` | `#002244` | `#FFFFFF` |
| **Texto de Cuerpo** | `Roboto Normal` | `12 pt` | `16 px` | `1.4` | `#212121` | `#E0E0E0` |
| **Leyenda / Fuente** | `Roboto Medium` | `10 pt` | `13 px` | `1.3` | `#595959` | `#A0A0A0` |
| **KPI / Cifra de Impacto** | `Roboto Black` | `36-44 pt` | `48-58 px` | `1.0` | `#FF0066` | `#FF0066` |
| **Etiqueta KPI** | `Roboto Bold` | `11 pt` | `15 px` | `1.2` | `#002244` | `#FFFFFF` |

---

## 3. Reglas de Composición Tipográfica

1. **Títulos en Normal (Regular), no en Bold**:
   - A diferencia de otras marcas que usan títulos en negrita pesada, la estética distintiva de Artefact usa `Roboto Normal` en 20pt para los títulos principales, aportando un estilo editorial limpio y sofisticado.
2. **Subtítulos en Bold para Contraste**:
   - Los subtítulos (`Roboto Bold 14pt`) generan el anclaje visual necesario bajo el título ligero.
3. **Alineación a la Izquierda**:
   - Todo el texto editorial debe alinearse a la izquierda. Nunca justificar texto en presentaciones.
4. **Espaciado y Márgenes**:
   - Margen superior estándar de títulos: 40px - 60px desde el borde superior de la diapositiva.
   - Espacio entre título y subtítulo: 8px - 12px.
"""

with open(os.path.join(DOCS_DIR, "typography.md"), "w") as f:
    f.write(typography_md)

# 3. docs/icons_catalog.md
icons_catalog_md = """# Catálogo de Iconos & Recursos Visuales — Artefact

Catálogo completo de todos los activos gráficos extraídos directamente de la plantilla oficial de Artefact (Noviembre 2024).

---

## 1. Logotipos Oficiales (`assets/logos/`)

Los logotipos se encuentran en máxima resolución PNG con transparencia alfa.

| Archivo | Vista Previa | Descripción & Uso |
| :--- | :---: | :--- |
| `artefact_logo_primary_dark.png` | ![Logo Dark](../assets/logos/artefact_logo_primary_dark.png) | Logotipo principal oscuro con isotipo A y wordmark. Usar en fondos blancos/claros. |
| `artefact_logo_primary_white.png` | ![Logo White](../assets/logos/artefact_logo_primary_white.png) | Logotipo principal blanco/invertido. Usar en fondos azul marino y degradados. |
| `artefact_logo_horizontal_dark.png` | ![Wordmark Dark](../assets/logos/artefact_logo_horizontal_dark.png) | Wordmark horizontal azul oscuro sin isotipo. |
| `artefact_logo_horizontal_white.png` | ![Wordmark White](../assets/logos/artefact_logo_horizontal_white.png) | Wordmark horizontal blanco sin isotipo. |
| `artefact_monogram_a_dark.png` | ![Monogram Dark](../assets/logos/artefact_monogram_a_dark.png) | Isotipo "A" emblemático oscuro de alta resolución (2048x2048). |
| `artefact_monogram_a_white.png` | ![Monogram White](../assets/logos/artefact_monogram_a_white.png) | Isotipo "A" emblemático blanco de alta resolución (1968x2048). |
| `artefact_logo_tagline_white.png` | ![Tagline White](../assets/logos/artefact_logo_tagline_white.png) | Logotipo con tagline institucional "Data & AI Consulting". |
| `artefact_logo_stacked_gradient.png` | ![Stacked Gradient](../assets/logos/artefact_logo_stacked_gradient.png) | Versión apilada con isotipo en degradado institucional. |

---

## 2. Iconos 3D Glassy de Áreas de Práctica (`assets/icons/glassy_3d/`)

Iconos hiperrealistas tridimensionales con efecto de cristal y luz, diseñados para ilustrar las verticales de negocio de Artefact.

| Archivo | Vista Previa | Concepto / Práctica de Artefact |
| :--- | :---: | :--- |
| `icon_glassy_data_foundations_bi.png` | ![Data BI](../assets/icons/glassy_3d/icon_glassy_data_foundations_bi.png) | **Data Foundations & BI** |
| `icon_glassy_ai_acceleration.png` | ![AI](../assets/icons/glassy_3d/icon_glassy_ai_acceleration.png) | **AI Acceleration** |
| `icon_glassy_it_data_platform.png` | ![IT Platform](../assets/icons/glassy_3d/icon_glassy_it_data_platform.png) | **IT & Data Platform** |
| `icon_glassy_strategy_transformation.png` | ![Strategy](../assets/icons/glassy_3d/icon_glassy_strategy_transformation.png) | **Strategy & Transformation** |
| `icon_glassy_cx_digital_marketing.png` | ![CX](../assets/icons/glassy_3d/icon_glassy_cx_digital_marketing.png) | **CX & Digital Marketing** |
| `icon_glassy_marketing_datadriven.png` | ![Marketing](../assets/icons/glassy_3d/icon_glassy_marketing_datadriven.png) | **Marketing Data-Driven** |
| `icon_glassy_iconic_a.png` | ![Iconic A](../assets/icons/glassy_3d/icon_glassy_iconic_a.png) | **Iconic A of Artefact** (Símbolo de cristal insignia) |
| `icon_glassy_people.png` | ![People](../assets/icons/glassy_3d/icon_glassy_people.png) | **People & Culture / Talento** |
| `icon_glassy_clients.png` | ![Clients](../assets/icons/glassy_3d/icon_glassy_clients.png) | **Clients & Partnerships / Ecosistema** |
| `icon_glassy_ai_hero_large.png` | ![AI Hero](../assets/icons/glassy_3d/icon_glassy_ai_hero_large.png) | **AI Acceleration Hero** (2048x1906 píxeles para portadas) |
| `icon_glassy_data_hero_large.png` | ![Data Hero](../assets/icons/glassy_3d/icon_glassy_data_hero_large.png) | **Data Hero** (1441x1440 píxeles para portadas) |
| `icon_glassy_marketing_hero_large.png` | ![Marketing Hero](../assets/icons/glassy_3d/icon_glassy_marketing_hero_large.png) | **Marketing Hero** (1056x1056 píxeles para portadas) |

---

## 3. Iconos Planos de UI (`assets/icons/ui_flat/`)

39 iconos rasterizados extraídos de la Slide 94 (Non editable icons):

| Icono | Vista Previa | Icono | Vista Previa | Icono | Vista Previa |
| :--- | :---: | :--- | :---: | :--- | :---: |
| `icon_ui_01.png` | ![UI 01](../assets/icons/ui_flat/icon_ui_01.png) | `icon_ui_02.png` | ![UI 02](../assets/icons/ui_flat/icon_ui_02.png) | `icon_ui_03.png` | ![UI 03](../assets/icons/ui_flat/icon_ui_03.png) |
| `icon_ui_04.png` | ![UI 04](../assets/icons/ui_flat/icon_ui_04.png) | `icon_ui_05.png` | ![UI 05](../assets/icons/ui_flat/icon_ui_05.png) | `icon_ui_06.png` | ![UI 06](../assets/icons/ui_flat/icon_ui_06.png) |
| `icon_ui_07.png` | ![UI 07](../assets/icons/ui_flat/icon_ui_07.png) | `icon_ui_08.png` | ![UI 08](../assets/icons/ui_flat/icon_ui_08.png) | `icon_ui_09.png` | ![UI 09](../assets/icons/ui_flat/icon_ui_09.png) |
| `icon_ui_10.png` | ![UI 10](../assets/icons/ui_flat/icon_ui_10.png) | `icon_ui_11.png` | ![UI 11](../assets/icons/ui_flat/icon_ui_11.png) | `icon_ui_12.png` | ![UI 12](../assets/icons/ui_flat/icon_ui_12.png) |
| `icon_ui_13.png` | ![UI 13](../assets/icons/ui_flat/icon_ui_13.png) | `icon_ui_14.png` | ![UI 14](../assets/icons/ui_flat/icon_ui_14.png) | `icon_ui_15.png` | ![UI 15](../assets/icons/ui_flat/icon_ui_15.png) |
| `icon_ui_16.png` | ![UI 16](../assets/icons/ui_flat/icon_ui_16.png) | `icon_ui_17.png` | ![UI 17](../assets/icons/ui_flat/icon_ui_17.png) | `icon_ui_18.png` | ![UI 18](../assets/icons/ui_flat/icon_ui_18.png) |
| `icon_ui_19.png` | ![UI 19](../assets/icons/ui_flat/icon_ui_19.png) | `icon_ui_20.png` | ![UI 20](../assets/icons/ui_flat/icon_ui_20.png) | `icon_ui_21.png` | ![UI 21](../assets/icons/ui_flat/icon_ui_21.png) |
| `icon_ui_22.png` | ![UI 22](../assets/icons/ui_flat/icon_ui_22.png) | `icon_ui_23.png` | ![UI 23](../assets/icons/ui_flat/icon_ui_23.png) | `icon_ui_24.png` | ![UI 24](../assets/icons/ui_flat/icon_ui_24.png) |
| `icon_ui_25.png` | ![UI 25](../assets/icons/ui_flat/icon_ui_25.png) | `icon_ui_26.png` | ![UI 26](../assets/icons/ui_flat/icon_ui_26.png) | `icon_ui_27.png` | ![UI 27](../assets/icons/ui_flat/icon_ui_27.png) |
| `icon_ui_28.png` | ![UI 28](../assets/icons/ui_flat/icon_ui_28.png) | `icon_ui_29.png` | ![UI 29](../assets/icons/ui_flat/icon_ui_29.png) | `icon_ui_30.png` | ![UI 30](../assets/icons/ui_flat/icon_ui_30.png) |
| `icon_ui_31.png` | ![UI 31](../assets/icons/ui_flat/icon_ui_31.png) | `icon_ui_32.png` | ![UI 32](../assets/icons/ui_flat/icon_ui_32.png) | `icon_ui_33.png` | ![UI 33](../assets/icons/ui_flat/icon_ui_33.png) |
| `icon_ui_34.png` | ![UI 34](../assets/icons/ui_flat/icon_ui_34.png) | `icon_ui_35.png` | ![UI 35](../assets/icons/ui_flat/icon_ui_35.png) | `icon_ui_36.png` | ![UI 36](../assets/icons/ui_flat/icon_ui_36.png) |
| `icon_ui_37.png` | ![UI 37](../assets/icons/ui_flat/icon_ui_37.png) | `icon_ui_38.png` | ![UI 38](../assets/icons/ui_flat/icon_ui_38.png) | `icon_ui_39.png` | ![UI 39](../assets/icons/ui_flat/icon_ui_39.png) |

---

## 4. Símbolos Temáticos & Banners (`assets/icons/symbols/`)

16 banners y composiciones gráficas extraídas de la Slide 95 (Symbols templates).

---

## 5. Iconos Vectoriales Editables en SVG (`assets/icons/vector_svg/`)

Se han extraído **171 iconos vectoriales puros en formato SVG** a partir de las diapositivas 90, 91, 92 y 93.

- **Resolución Infinita**: Geometría vectorial pura (`<path d="...">`).
- **Compatibilidad**: Listos para importar en Figma, Illustrator, Web, PPTX o Google Slides.
- **Ubicación**: `calm-babbage/assets/icons/vector_svg/` (`vector_icon_s90_*.svg` a `vector_icon_s93_*.svg`).
"""

with open(os.path.join(DOCS_DIR, "icons_catalog.md"), "w") as f:
    f.write(icons_catalog_md)

# 4. docs/slide_templates_index.md
slide_templates_md = """# Índice y Taxonomía de Plantillas de Diapositivas — Artefact

Estructura completa de las **109 diapositivas** de la plantilla oficial de Artefact (Noviembre 2024), clasificadas por tipología y universo visual.

---

## 1. Resumen de Universos Visuales

| Universo Visual | Rango de Diapositivas | Descripción |
| :--- | :---: | :--- |
| **White Background** | Slides 1 – 33 | Fondos limpios blancos `#FFFFFF`, texto `#002244`, acentos `#FF0066`. Ideal para propuestas comerciales, entregables analíticos y revisiones técnicas. |
| **Blue Background** | Slides 34 – 49 | Fondos azul profundo `#0D1634` / `#002244`, texto blanco `#FFFFFF`. Ideal para presentaciones ejecutivas C-Level y transiciones de alto contraste. |
| **Gradient Background** | Slides 50 – 64 | Fondos con degradado insigne `#002244` → `#FF0066`. Ideal para portadas de impacto, aperturas, cierres y agradecimientos. |
| **Brand Guidelines & Assets** | Slides 65 – 95 | Guías gráficas maestras: Logos, Colores, Tipografías, Iconos 3D Glassy, Recortes PNG, Fotos por Industria, Componentes, Cajas y Gráficos. |
| **Layouts Adicionales** | Slides 96 – 109 | Plantillas avanzadas con diferentes disposiciones de tarjetas y separadores de sección. |

---

## 2. Inventario Detallado de Diapositivas

### Bloque A: Diapositivas con Fondo Blanco (Slides 1 – 33)
- **Slide 1-2**: Portadas principales de presentación (Title of Proposal, subtítulo, autor, fecha).
- **Slide 3-6**: Declaración de visión, propuestas de valor y resumen ejecutivo.
- **Slide 7**: Plantilla de Agenda / Tabla de contenidos (3 a 5 puntos numerados).
- **Slide 8**: Slide de transición de sección con banda de color.
- **Slide 9-15**: Grillas de contenido (2 columnas, 3 columnas, 4 columnas con tarjetas de fondo `#F4F6F9`).
- **Slide 16-25**: Comparativas lado a lado, tablas matriciales, diagramas de flujo y pasos de proceso (1-2-3-4).
- **Slide 26-27**: Perfiles de cliente, Buyer Personas y retratos fotográficos.
- **Slide 28-30**: Plantillas de Caso de Éxito / Client Cases (Contexto, Desafío, Solución Artefact, Resultados de Negocio).
- **Slide 31-33**: Fichas de equipo (Team Members) con foto, cargo, bio y logos de experiencia.

### Bloque B: Diapositivas con Fondo Azul Profundo (Slides 34 – 49)
- **Slide 34-36**: Portadas oscuras de alto impacto con isotipo Artefact de fondo.
- **Slide 37-39**: Slides de visión estratégica y transiciones de sección en fondo `#0D1634`.
- **Slide 40-45**: Diseños con imágenes hero integradas y tarjetas traslúcidas.
- **Slide 46-49**: Grillas de capacidades tecnológicas y datos sobre fondo azul.

### Bloque C: Diapositivas con Fondo de Degradado (Slides 50 – 64)
- **Slide 50-52**: Portadas con degradado de 4 paradas (`#002244` → `#273275` → `#752E7D` → `#FF0066`).
- **Slide 53-55**: Agendas y separadores de sección envolventes.
- **Slide 56-63**: Mensajes clave, citas testimoniales y manifiestos de proyecto.
- **Slide 64**: Diapositiva de cierre y agradecimiento (*Thank You!*) con datos de contacto.

### Bloque D: Guías Gráficas & Recursos Visuales (Slides 65 – 95)
- **Slide 65**: Separador de Apéndice (*Appendix*).
- **Slide 66**: *Artefact Graphical Guidelines - Logos* (Logos primarios, horizontales, monograma A en dark y white).
- **Slide 67**: *Artefact Graphical Guidelines - Set of Colors* (Corporate, Secondary, Gradient stops).
- **Slide 68**: *Artefact Graphical Guidelines - Fonts Size* (Jerarquía Roboto: Title 20pt, Subtitle 14pt, Body 12pt, Legend 10pt).
- **Slide 69**: *Set of Glassy Icons* (Iconos 3D para BI, AI, IT, CX, Strategy, People, Clients).
- **Slide 70**: *Images - Trimmed PNG cutouts* (9 recortes transparentes).
- **Slide 71-84**: Banco fotográfico por industrias (Retail, FMCG, Luxury, Finance, Sustainability, Tech).
- **Slide 85-89**: Componentes de UI (Cajas de texto, contenedores modulares, gráficos de barras, líneas y calendarios).
- **Slide 90-93**: Sets de iconos vectoriales editables (~171 grupos vectoriales).
- **Slide 94**: Iconos no editables (39 iconos planos de interfaz).
- **Slide 95**: Símbolos temáticos de categoría (16 composiciones).
"""

with open(os.path.join(DOCS_DIR, "slide_templates_index.md"), "w") as f:
    f.write(slide_templates_md)

# 5. docs/brand_guidelines_artefact.md (Master Brand Guidelines)
brand_guidelines_md = """# Manual Maestro de Marca e Identidad Visual — Artefact (Noviembre 2024)

Manual integral de diseño, identidad visual, paleta cromática, tipografía, iconografía y arquitectura de diapositivas de **Artefact**.

---

## 1. Identidad & Filosofía de Marca

**Artefact** es una consultora global líder en **Data, AI y Transformación Digital**. Su lenguaje visual combina el rigor analítico e ingenieril con una estética tecnológica moderna, sofisticada y dinámica.

### Pilares del Sistema de Diseño
1. **Claridad & Rigor**: Jerarquía tipográfica estricta basada en Roboto, uso generoso de espacio en blanco y alineación geométrica precisa.
2. **Energía & Innovación**: Contraste audaz entre el azul marino corporativo (`#002244`) y el rosa vibrante (`#FF0066`), enriquecido por el degradado institucional de 4 tonos.
3. **Profundidad Visual**: Integración de iconografía 3D "Glassy" con efectos de refracción de luz que simbolizan la transparencia, el procesamiento de datos y la inteligencia artificial.

---

## 2. Sistema de Logotipos

Los logotipos se ubican en `calm-babbage/assets/logos/`:

```
assets/logos/
├── artefact_logo_primary_dark.png          # Logo completo azul (Fondos claros)
├── artefact_logo_primary_white.png         # Logo completo blanco (Fondos oscuros/degradados)
├── artefact_logo_horizontal_dark.png       # Wordmark horizontal azul
├── artefact_logo_horizontal_white.png      # Wordmark horizontal blanco
├── artefact_monogram_a_dark.png            # Isotipo "A" emblemático azul (2048x2048)
├── artefact_monogram_a_white.png           # Isotipo "A" emblemático blanco (1968x2048)
├── artefact_logo_tagline_white.png         # Logo con tagline institucional
└── artefact_logo_stacked_gradient.png      # Logo apilado con símbolo en degradado
```

### Reglas de Uso del Logotipo
- **Zona de Seguridad**: Mantener un espacio libre equivalente a la mitad del alto del isotipo "A" alrededor de cualquier versión del logo.
- **Fondo Claro**: Utilizar `artefact_logo_primary_dark.png` sobre blanco (`#FFFFFF`) o gris claro (`#F4F6F9`).
- **Fondo Oscuro / Degradado**: Utilizar `artefact_logo_primary_white.png` sobre azul profundo (`#0D1634` / `#002244`) o sobre el degradado insigne.
- **Prohibiciones**: No alterar proporciones, no rotar el isotipo, no aplicar sombras paralelas pesadas ni sustituir los colores institucionales.

---

## 3. Paleta de Colores Oficial

### Colores Corporativos Primarios
- **Artefact Blue**: `#002244` | `rgb(0, 34, 68)`
- **Artefact Pink**: `#FF0066` | `rgb(255, 0, 102)`

### Colores Secundarios
- **Dark Blue**: `#0D1634` | `rgb(13, 22, 52)` (Fondo dark mode)
- **Medium Blue**: `#273275` | `rgb(39, 50, 117)` (Paso 2 del degradado)
- **Purple**: `#752E7D` | `rgb(117, 46, 125)` (Paso 3 del degradado)

### Degradado Insigne de 4 Paradas
```
#002244 (0%) ───► #273275 (33%) ───► #752E7D (66%) ───► #FF0066 (100%)
```

---

## 4. Tipografía Institucional

- **Familia Única**: `Roboto`
- **Títulos**: `Roboto Normal 20pt` (`#002244` o `#FFFFFF`)
- **Subtítulos**: `Roboto Bold 14pt` (`#002244` o `#FFFFFF`)
- **Cuerpo de Texto**: `Roboto Normal 12pt` (`#212121` o `#E0E0E0`)
- **Leyendas y Fuentes**: `Roboto Medium 10pt` (`#595959` o `#A0A0A0`)
- **Cifras KPI**: `Roboto Black 36pt - 44pt` (`#FF0066`)

---

## 5. Iconografía & Activos Visuales

1. **Iconos 3D Glassy** (`assets/icons/glassy_3d/`):
   - Representan las áreas de práctica de Artefact: *Data Foundations & BI*, *AI Acceleration*, *IT & Data Platform*, *Strategy & Transformation*, *CX & Digital Marketing*, *Marketing Data-Driven*, *People*, *Clients* y el *Iconic A*.
2. **Iconos Planos de UI** (`assets/icons/ui_flat/`):
   - 39 iconos en PNG transparente para viñetas, tablas y esquemas de proceso.
3. **Iconos Vectoriales Editables** (`assets/icons/vector_svg/`):
   - 171 iconos vectoriales SVG listos para diseño web, Figma y presentaciones interactivas.
4. **Recortes Transparentes** (`assets/cutouts/`):
   - 9 elementos PNG recortados para montajes editoriales y portadas.
5. **Fotografía por Industria** (`assets/photography/`):
   - 89 imágenes seleccionadas que abarcan Retail, FMCG, Lujo, Finanzas y Sostenibilidad.

---

## 6. Archivos y Tokens de Integración Técnica

El repositorio cuenta con tokens listos para desarrollo:
- `tokens/colors.json`: Ficha completa de colores y roles.
- `tokens/typography.json`: Escala tipográfica y jerarquías.
- `tokens/artefact_theme.css`: Variables CSS nativas para aplicaciones web o pipelines de *Presentation HTML* (`dom-to-pptx`).
"""

with open(os.path.join(DOCS_DIR, "brand_guidelines_artefact.md"), "w") as f:
    f.write(brand_guidelines_md)

print("All documentation generated successfully!")
