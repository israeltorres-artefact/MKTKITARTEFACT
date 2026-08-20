# CÓMO COMPILAR PRESENTATION HTML A POWERPOINT (.PPTX) CON DOM-TO-PPTX

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
