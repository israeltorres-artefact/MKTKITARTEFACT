# GUÍA MAESTRA DE FORMATO, COMPONENTES & CONTEXTO VISUAL — ARTEFACT (Noviembre 2024)

Este documento detalla todas las reglas de formato, biblioteca de componentes de UI, estilos de cajas, tipos de gráficos, perfiles de equipo, casos de cliente y la taxonomía de imágenes por industria extraídas de la plantilla oficial de **Artefact** (109 diapositivas).

---

## 1. ANATOMÍA Y SISTEMA DE GRILLA (CANVAS CONTRACT)

- **Canvas de Diapositiva**: `1920px × 1080px` (16:9 Widescreen Standard).
- **Márgenes y Área Segura**:
  - Margen Superior: `60px` a `80px`.
  - Margen Lateral (Izquierdo / Derecho): `80px` (fijo para alineación perfecta en todo el deck).
  - Margen Inferior / Zona de Footer: `40px` a `60px` (con línea divisoria a `30px` del fondo).
- **Estructura del Encabezado (Header)**:
  - **Action Title**: `Roboto Normal 20pt - 24pt` (`font-weight: 400`), `#002244` en fondo claro / `#FFFFFF` en fondo oscuro. Debe ser una conclusión activa con verbo + métrica/impacto.
  - **Subtitle / Contexto**: `Roboto Bold 14pt - 15pt` (`font-weight: 700`), `#002244` en fondo claro / `#FFFFFF` en fondo oscuro. Anclaje visual inmediato.
- **Estructura del Pie de Página (Footer)**:
  - Izquierda: `data-pptx-role="source"` con fuente de datos o metadatos en `Roboto Medium 10pt` (`#595959` / `#A0A0A0`).
  - Derecha: Número de slide o confidencialidad institucional.

---

## 2. BIBLIOTECA DE COMPONENTES & ESTILOS DE CAJAS (SLIDE 86)

Artefact utiliza 5 estilos estándar de cajas modulares para estructurar información compleja:

### Estilo 1: Tarjeta de Superficie (Surface Container Card)
- **Uso**: Contenedor estándar para columnas de contenido, pilares y listas de bullets.
- **CSS**:
  ```css
  background: #F4F6F9;
  border: 1px solid #EEEEEE;
  border-radius: 12px;
  padding: 32px;
  ```

### Estilo 2: Tarjeta con Borde de Acento (Highlight Border Card)
- **Uso**: Destacar la fase activa en un roadmap, el pilar central o la opción recomendada.
- **CSS**:
  ```css
  background: #FFFFFF;
  border: 2px solid #FF0066; /* o #273275 */
  border-radius: 12px;
  padding: 32px;
  box-shadow: 0 8px 24px rgba(255, 0, 102, 0.08);
  ```

### Estilo 3: Tarjeta con Franja Lateral (Accent Left Strip)
- **Uso**: Bloques de llamada de atención, citas ejecutivas o hallazgos críticos.
- **CSS**:
  ```css
  background: #F4F6F9;
  border-left: 6px solid #FF0066;
  border-radius: 0 12px 12px 0;
  padding: 24px 28px;
  ```

### Estilo 4: Tarjeta Hero Nocturna (Dark Glass Card)
- **Uso**: Bloques de resultados en slides azules o sobre degradados.
- **CSS**:
  ```css
  background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 12px;
  padding: 32px;
  color: #FFFFFF;
  ```

### Estilo 5: Badges y Pastillas (Pill Badges)
- **Uso**: Identificadores de fase, estado de proyectos, etiquetas de tecnología.
- **CSS**:
  ```css
  display: inline-block;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  ```

---

## 3. ESTILOS DE GRÁFICOS & VISUALIZACIÓN DE DATOS (SLIDES 87-89)

1. **Gráficos de Barras / Columnas**:
   - Barras de contexto en `#002244` o `#273275`.
   - **Barra de foco / Hallazgo clave siempre en `#FF0066` (Artefact Pink)**.
   - Valores numéricos en `Roboto Bold` en la parte superior o interior de la barra.
2. **Gráficos de Dona / Anillo (Donut Charts)**:
   - Diámetro interior (agujero): `65%` a `75%`.
   - Paleta de sectores: `#002244` (Serie 1), `#273275` (Serie 2), `#752E7D` (Serie 3), `#FF0066` (Serie 4 / Destacada).
   - Prohibido amontonar etiquetas en el hoyo central; leyenda estructurada a la derecha o inferior a `10pt`.
3. **Bloques KPI Gigantes**:
   - Cifra de impacto: `Roboto Black 44pt - 64pt` en color `#FF0066`.
   - Etiqueta descriptiva superior o inferior: `Roboto Bold 12pt - 14pt` en `#002244` o `#FFFFFF`.
   - Delta comparativo (`+35% YoY`, `3.2x ROI`) en pastilla con fondo suave.
4. **Líneas de Tiempo & Calendarios (Slide 88)**:
   - Grillas mensuales / trimestrales con cabeceras `JANUARY`, `FEBRUARY`, etc., en `Roboto Bold 11pt`.
   - Barras de tarea horizontales en degradado o `#273275` con hitos destacados en `#FF0066`.

---

## 4. BANCO DE IMÁGENES POR INDUSTRIA & CONTEXTO VISUAL (SLIDES 71-84)

La plantilla oficial de Artefact clasifica su fotografía institucional en 8 verticales temáticas:

| Vertical / Industria | Diapositivas | Tipología de Fotografía & Contexto Recomendado |
| :--- | :---: | :--- |
| **Retail & E-commerce** | Slides 72-73 | Carritos de compra, lineales de supermercado, pasarelas de pago móvil, paquetería y logística urbana. Usar en casos de omnicanalidad y CDP. |
| **FMCG & Bienes de Consumo** | Slide 73 | Plantas de embotellado, líneas de producción automatizadas, gestión de inventario en almacenes de alta tecnología. |
| **Lujo, Cosmética & Moda** | Slide 73-74 | Frascos de perfume sobre fondos oscuros, cosméticos minimalistas, tiendas boutique de alta gama. Usar en propuestas de personalización VIP y CX. |
| **Banca, Finanzas & Fintech** | Slide 74-75 | Terminales POS, chips de tarjetas contactless, aplicaciones de banca móvil, rascacielos financieros. Usar en fraud detection y credit scoring. |
| **Salud, Farma & Biotecnología** | Slides 75-76 | Científicos en laboratorios limpios, microscopía digital, secuenciación genética y tablets clínicas. Usar en drug discovery y optimización clínica. |
| **Energía, Utilities & Smart Grid** | Slides 77-78 | Turbinas eólicas en alta mar, paneles solares industriales, estaciones de carga EV y medidores inteligentes. |
| **Telecomunicaciones & Medios** | Slides 79-80 | Torres 5G, racks de servidores en data centers, fibra óptica brillante y streaming en pantallas interactivas. |
| **Sostenibilidad & ESG** | Slide 84 | Energías renovables, huella de carbono digital, reciclaje circular, bosques y tecnología verde. Usar en reportes de sostenibilidad y optimización de nube. |
| **Recortes Transparentes (Cutouts)** | Slide 70 | 9 personas y dispositivos con fondo recortado (PNG alfa), listos para superponer sobre fondos de color o tarjetas con degradado. |

---

## 5. MATRIZ DE USO DE ICONOGRAFÍA

| Tipo de Icono | Carpeta de Assets | Cuándo Usarlo | Cuándo NO Usarlo |
| :--- | :--- | :--- | :--- |
| **Iconos 3D Glassy** | `assets/icons/glassy_3d/` | Portadas, cabeceras de pilares estratégicos, tarjetas hero de Data/AI/Strategy. | Viñetas pequeñas de texto o tablas densas. |
| **Iconos Planos de UI** | `assets/icons/ui_flat/` | Listas de viñetas, pasos de procesos (1-2-3-4), tarjetas de características secundarias. | Elementos gigantes de portada. |
| **Iconos Vectoriales SVG** | `assets/icons/vector_svg/` | Diseños donde se requiera cambio dinámico de color (`currentColor`), alta precisión geométrica o fondos invertidos. | Cuando se requiera realismo 3D. |
| **Símbolos / Banners** | `assets/icons/symbols/` | Franjas decorativas superiores, separadores de sección y portadillas de capítulo. | Iconos individuales de lista. |

---

## 6. PLANTILLAS DE ARQUETIPOS CLAVE

### A. Plantilla de Ficha de Equipo (Team Member Card — Slides 31-33)
```text
┌──────────────────────────────────────────────────────────┐
│ [ Foto Cuadrada con esquinas 12px ]                      │
│                                                          │
│ Julien HO-TONG                  (Roboto Bold 16pt #002244)│
│ Partner — AI & Data Platform     (Roboto Medium 12pt #FF0066)
│                                                          │
│ Ex-Google Brain, +12 años liderando programas de         │
│ modernización de datos en Retail y Telecom.              │
│                                 (Roboto Normal 11pt #595959)
│                                                          │
│ [ Logotipos de experiencia previa en escala de grises ]  │
└──────────────────────────────────────────────────────────┘
```

### B. Plantilla de Caso de Éxito (Client Case — Slides 28-30)
```text
┌─────────────────────────────────────────────────────────────────────────┐
│ CLIENT CASE: RETAIL GLOBAL • PERSONALIZACIÓN OMNICANAL                  │
├───────────────────────────────────┬─────────────────────────────────────┤
│ 1. Contexto & Desafío             │ 3. Resultados Cuantitativos         │
│ • 8M de clientes activos.         │                                     │
│ • Falta de segmentación dinámica. │         +22% ROI en Campañas        │
│                                   │          3.8x Retorno ROAS          │
│ 2. Solución Artefact              │         -40% Costo Adquisición      │
│ • CDP + Motor de Recomendación IA │                                     │
│ • Ingesta en tiempo real.         │ (Card Azul Marino #002244 con cifras│
│                                   │  gigantes en Rosa #FF0066)          │
└───────────────────────────────────┴─────────────────────────────────────┘
```

---

## 7. QA FORMATTING CHECKLIST PARA PRESENTACIONES ARTEFACT

- [ ] Margen lateral exacto de `80px` mantenido en todas las diapositivas.
- [ ] Título de slide redactado como **Action Title** (Conclusión + Impacto).
- [ ] Jerarquía tipográfica respetada: Título en `Roboto Normal` (regular), Subtítulo en `Roboto Bold`.
- [ ] Uso exclusivo de la paleta oficial (`#002244`, `#FF0066`, `#0D1634`, `#273275`, `#752E7D`).
- [ ] Iconos 3D Glassy reservados para pilares principales y portadas.
- [ ] Gráficos con la serie destacada en `#FF0066` y notas al pie con fuentes en `Roboto Medium 10pt`.
- [ ] Código HTML 100% compatible con el canvas `1920x1080` de `dom-to-pptx`.
