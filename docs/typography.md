# Guía de Tipografía & Jerarquía de Texto — Artefact (Noviembre 2024)

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
