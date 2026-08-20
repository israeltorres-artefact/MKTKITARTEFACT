# Manual Maestro de Marca e Identidad Visual — Artefact (Noviembre 2024)

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
