# 🏢 COMPANY PRESENTATION KITS — MULTI-BRAND ARCHITECTURE

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
