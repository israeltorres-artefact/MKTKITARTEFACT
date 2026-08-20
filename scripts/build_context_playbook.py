import os, json, shutil

BASE_DIR = "/Users/israeltorres/Documents/antigravity/calm-babbage"
DESKTOP_DIR = "/Users/israeltorres/Desktop/SKILL PPT"
KIT_DIR = os.path.join(BASE_DIR, "company-kits", "artefact")

playbook_content = """# 📖 PLAYBOOK MAESTRO: USO DE ELEMENTOS, COMPONENTES & CONTEXTOS VISUALES
## Guía Práctica de Aplicación para Presentaciones Ejecutivas Artefact (Noviembre 2024)

Este manual responde con precisión milimétrica a la pregunta: **"¿Qué elemento visual, color, tipografía, icono o componente debo usar para este contexto específico de negocio?"**

---

## 🧭 1. ÁRBOL DE DECISIÓN: ¿QUÉ FONDO DE SLIDE ELEGIR?

Artefact utiliza tres universos visuales para evitar la fatiga visual y modular el ritmo de la presentación:

```
¿Cuál es el objetivo de esta diapositiva?
 ├── Apertura / Portada de Alto Impacto ────────► FONDO CON DEGRADADO (Signature Gradient)
 ├── Separador de Sección Principal ───────────► FONDO AZUL OSCURO (#0D1634 o #002244)
 ├── Mensaje Estratégico / Manifiesto C-Level ──► FONDO AZUL OSCURO (#0D1634)
 ├── Contenido Analítico / Datos / Tablas ─────► FONDO BLANCO PURO (#FFFFFF)
 ├── Ficha de Caso de Éxito / Client Case ─────► FONDO BLANCO con Tarjeta de KPI Azul Marino
 ├── Roadmap / Plan de Implementación ─────────► FONDO BLANCO con Fases Destacadas
 └── Agradecimiento & Cierre (Thank You) ──────► FONDO CON DEGRADADO (Signature Gradient)
```

| Universo Visual | Fondo CSS | Texto Principal | Tono Emocional | Cuándo Usarlo |
| :--- | :--- | :--- | :--- | :--- |
| **1. White Background** | `#FFFFFF` | `#002244` / `#212121` | Riguroso, analítico, estructurado | El **70% del deck**. Slides de trabajo, análisis de datos, grillas, matrices y propuestas técnicas. |
| **2. Blue Background** | `#0D1634` o `#002244` | `#FFFFFF` | Solemne, ejecutivo, estratégico | El **20% del deck**. Aperturas de capítulo, visión estratégica, pilares clave de capacidades y decks C-Level. |
| **3. Gradient Background** | `linear-gradient(135deg, #002244 0%, #273275 33%, #752E7D 66%, #FF0066 100%)` | `#FFFFFF` | Inspirador, dinámico, memorable | El **10% del deck**. Portadas principales, diapositiva de cierre y citas de gran impacto. |

---

## 🏷️ 2. MATRIZ DE SELECCIÓN DE LOGOTIPOS

| Contexto / Fondo | Archivo de Logo Recomendado | Ruta en el Kit | Regla de Oro |
| :--- | :--- | :--- | :--- |
| **Slide Blanca / Fondo Claro** | `artefact_logo_primary_dark.png` | `assets/logos/` | Logotipo completo azul oscuro `#002244`. Altura recomendada: 40px - 48px. |
| **Slide Azul / Fondo Oscuro** | `artefact_logo_primary_white.png` | `assets/logos/` | Logotipo completo blanco `#FFFFFF`. |
| **Slide con Degradado** | `artefact_logo_primary_white.png` | `assets/logos/` | Siempre blanco para máximo contraste con el degradado. |
| **Portadas Minimalistas** | `artefact_monogram_a_white.png` / `dark.png` | `assets/logos/` | Isotipo "A" gigante de 2048x2048 como elemento hero o marca de agua. |
| **Encabezados Compactos** | `artefact_logo_horizontal_dark.png` / `white.png`| `assets/logos/` | Wordmark estilizado para barras superiores o navegación. |

---

## ✍️ 3. REGLAS DE REDACCIÓN TIPOGRÁFICA & "ACTION TITLES"

### La Fórmula del Action Title de Artefact
Todo título de diapositiva **debe afirmar una conclusión de negocio**, nunca titular un tema pasivo.

$$\text{Action Title} = \text{[Verbo de Acción]} + \text{[Hallazgo / Palanca Estratégica]} + \text{[Impacto Cuantificado]}$$

| ❌ Título Pasivo (Prohibido) | ✅ Action Title Oficial de Artefact |
| :--- | :--- |
| *"Arquitectura de Datos"* | *"La modernización hacia un Lakehouse unificado reduce los costos de cómputo en un 40%"* |
| *"Resultados de la Campaña"* | *"La personalización con IA generativa incrementó las conversiones omnicanal en un +22%"* |
| *"Roadmap de Proyecto"* | *"El plan de aceleración en 3 fases garantiza el primer MVP en producción al Mes 3"* |
| *"Pilares de la Propuesta"* | *"Tres palancas integradas aseguran la adopción operativa y el gobierno ético de la IA"* |

### Jerarquía Tipográfica y Formato de Texto
1. **Título**: `Roboto Normal 20pt - 24pt` (`font-weight: 400`). **No usar negrita en el título**, para mantener la elegancia editorial de la consultora.
2. **Subtítulo**: `Roboto Bold 14pt - 15pt` (`font-weight: 700`). Siempre en negrita para anclar el contexto.
3. **Bullets / Puntos de Lista**:
   - **Regla del Lead-in en Negrita**: Resaltar siempre en `Roboto Bold` las primeras 2-3 palabras del bullet.
   - *Ejemplo*: `<li><strong>Gobernanza activa:</strong> Implementación de catálogo automatizado con linaje extremo a extremo.</li>`
4. **Cifras KPI**: `Roboto Black 44pt - 64pt` exclusivamente en color `#FF0066` (Rosa Artefact).
5. **Fuentes / Atribución**: `Roboto Medium 10pt` (`#595959`) en la esquina inferior izquierda.

---

## 🔮 4. DICCIONARIO DE ICONOS 3D GLASSY: ¿CUÁNDO USAR CADA UNO?

Los iconos 3D Glassy representan las verticales y soluciones maestras de Artefact:

| Icono 3D | Archivo de Imagen | Conceptos & Temas Asociados | Cuándo Usarlo en una Slide |
| :---: | :--- | :--- | :--- |
| ![AI](assets/icons/glassy_3d/icon_glassy_ai_acceleration.png) | `icon_glassy_ai_acceleration.png` | Inteligencia Artificial, Agentes Cognitivos, LLMs, GenAI, Machine Learning, Automatización Predictiva. | En diapositivas sobre modelos de IA, asistentes virtuales, aceleración analítica o PoCs de IA. |
| ![BI](assets/icons/glassy_3d/icon_glassy_data_foundations_bi.png) | `icon_glassy_data_foundations_bi.png` | Data Lakehouse, Gobierno de Datos, Calidad de Datos, Business Intelligence, Dashboards, Data Mesh. | En diapositivas de cimientos de datos, modernización de bodegas analíticas y reporting ejecutivo. |
| ![Strategy](assets/icons/glassy_3d/icon_glassy_strategy_transformation.png) | `icon_glassy_strategy_transformation.png` | Estrategia de Negocio, Data Operating Model, Transformación Digital, ROI, Priorización de Casos de Uso. | En diapositivas de resumen ejecutivo, diagnóstico estratégico, visión C-Level y modelos de valor. |
| ![IT](assets/icons/glassy_3d/icon_glassy_it_data_platform.png) | `icon_glassy_it_data_platform.png` | Infraestructura Cloud (GCP, AWS, Azure, Databricks, Snowflake), MLOps, CI/CD, Arquitectura Técnica. | En diapositivas de arquitectura tecnológica, seguridad, pipelines de datos y escalabilidad cloud. |
| ![CX](assets/icons/glassy_3d/icon_glassy_cx_digital_marketing.png) | `icon_glassy_cx_digital_marketing.png` | Customer Experience, Customer 360, CDP, Personalización, Omnicanalidad, Fidelización y CRM. | En propuestas de marketing digital, hiper-personalización y segmentación de clientes. |
| ![Marketing](assets/icons/glassy_3d/icon_glassy_marketing_datadriven.png) | `icon_glassy_marketing_datadriven.png` | Media Mix Modeling (MMM), Atribución Multitáctil, Performance Marketing, AdTech, Optimización de Inversión. | En slides de medición de efectividad publicitaria, optimización de gasto en medios y marketing de precisión. |
| ![People](assets/icons/glassy_3d/icon_glassy_people.png) | `icon_glassy_people.png` | Talento, Cambio Organizacional, Alfabetización en IA (AI Literacy), Cultura Data-Driven, Equipos. | En slides de gestión del cambio, adopción de usuarios, capacitación y fichas de equipo. |
| ![Clients](assets/icons/glassy_3d/icon_glassy_clients.png) | `icon_glassy_clients.png` | Clientes, Ecosistema de Alianzas, Partners Tecnológicos, Benchmarks de Mercado. | En slides de credenciales, portafolio de clientes, ecosistema tecnológico o casos de éxito. |
| ![Iconic A](assets/icons/glassy_3d/icon_glassy_iconic_a.png) | `icon_glassy_iconic_a.png` | La Marca Artefact, Metodología Propietaria, Excelencia en Consultoría, Cierre Institucional. | En portadas, diapositiva de manifiesto o slide final de contacto (*Thank You*). |

---

## 🗂️ 5. SELECCIÓN DE COMPONENTES & TARJETAS POR TIPO DE INFORMACIÓN

| Si quieres comunicar... | Usa este Componente / Grilla | Código de Estilo Recomendado |
| :--- | :--- | :--- |
| **3 Pilares Estratégicos** | Grilla de 3 Columnas (`grid-3`) con tarjetas grises | `artefact-card` con Icono 3D arriba + Título Bold + 3 bullets. |
| **Diagnóstico en 4 Pasos** (Desafío → Oportunidad → Palanca → Impacto) | Grilla de 4 Columnas (`grid-4`) con pastillas de fase | Tarjetas con `badge-pink` y `badge-blue` alternadas. |
| **Caso de Éxito de Cliente** | Grilla Dividida 50/50 (`grid-2`) | Izquierda: 2 cards de Contexto/Solución. Derecha: Card Azul Marino con KPI gigante en Rosa `#FF0066`. |
| **Comparativa de Opciones (A vs B)** | 2 Tarjetas lado a lado | Opción estándar: Card gris normal. Opción Recomendada: Card con borde `2px solid #FF0066` y badge "Recomendado". |
| **Roadmap Temporal (Fases 1, 2, 3)** | 3 Tarjetas con barra de progreso | Fase activa destacada con borde `#FF0066`. Tareas con checkmarks. |
| **Cifras de Gran Impacto** | Bloque KPI Hero | Número a 52-64pt en `#FF0066`, etiqueta superior en `Roboto Bold 14pt` y delta inferior (`+35%`). |
| **Ficha de Perfil de Consultor** | Tarjeta de Perfil Modular | Foto cuadrada con radio de 12px + Nombre Bold + Cargo en Rosa `#FF0066` + Bio + Logos de experiencia. |

---

## 🏭 6. SELECCIÓN DE FOTOGRAFÍA POR VERTICAL DE CLIENTE

Al construir propuestas comerciales para sectores específicos, utiliza las imágenes de `assets/photography/` según esta guía:

```text
┌──────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Vertical de Negocio                  │ Recomendación Fotográfica                              │
├──────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Retail, Supermercados & E-commerce   │ Carritos, cajas de autoservicio, apps de delivery.     │
│ FMCG, Alimentos & Bebidas            │ Plantas embotelladoras, cintas de producción, almacén. │
│ Lujo, Moda & Alta Cosmética          │ Productos minimalistas, frascos con luz dramática.    │
│ Banca, Seguros & Fintech             │ Tarjetas contactless, terminales POS, banca móvil.     │
│ Salud, Farmacéutica & Clínicas       │ Laboratorios de investigación, científicos con tablets.│
│ Energía, Utilities & Minería         │ Parques eólicos marinos, granjas solares, carga EV.   │
│ Telecomunicaciones & Tech Media      │ Racks de servidores, cables de fibra óptica, 5G.       │
│ Sostenibilidad & Huella Verde (ESG)  │ Paneles verdes, bosques, gráficos de descarbonización. │
└──────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 🚀 7. CHECKLIST DEFINITIVO PARA VALIDAR UN DECK ARTEFACT

Antes de entregar o compilar una presentación, verifica estos 7 puntos:

1. **¿Cada slide tiene un Action Title activo?** (Verbo + Insight, nunca título de tema).
2. **¿El título está en Roboto Regular y el subtítulo en Roboto Bold?**
3. **¿Se respeta el contraste de colores?** (`#002244` en fondo blanco, `#FFFFFF` en azul/degradado, `#FF0066` para KPIs).
4. **¿Los iconos 3D Glassy corresponden a la temática exacta?** (AI para modelos, BI para Lakehouse, Strategy para ROI).
5. **¿Los primeros 3 términos de cada viñeta están en negrita?**
6. **¿Existe una línea de fuente/metadatos en el footer?** (`data-pptx-role="source"`).
7. **¿El HTML respeta el canvas de 1920x1080 sin scrollbars?**
"""

# Write to workspace kit
playbook_ws = os.path.join(KIT_DIR, "guidelines", "ELEMENTS_AND_CONTEXT_PLAYBOOK.md")
with open(playbook_ws, "w") as f:
    f.write(playbook_content)

# Write to desktop kit
playbook_dt = os.path.join(DESKTOP_DIR, "company-kits", "artefact", "guidelines", "ELEMENTS_AND_CONTEXT_PLAYBOOK.md")
with open(playbook_dt, "w") as f:
    f.write(playbook_content)

# Also write to docs/ in workspace root for direct preview
docs_playbook = os.path.join(BASE_DIR, "docs", "ELEMENTS_AND_CONTEXT_PLAYBOOK.md")
with open(docs_playbook, "w") as f:
    f.write(playbook_content)

# Update manifest.json in both places
manifest_path = os.path.join(KIT_DIR, "manifest.json")
with open(manifest_path, "r") as f:
    mf = json.load(f)

mf["files"]["elementsAndContextPlaybook"] = "guidelines/ELEMENTS_AND_CONTEXT_PLAYBOOK.md"

with open(manifest_path, "w") as f:
    json.dump(mf, f, indent=2)

shutil.copyfile(manifest_path, os.path.join(DESKTOP_DIR, "company-kits", "artefact", "manifest.json"))

print("Elements and Context Playbook successfully generated in all locations!")
