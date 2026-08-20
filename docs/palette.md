# Manual de Paleta de Colores & Degradados — Artefact (Noviembre 2024)

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
