# Análisis de pérdida de vegetación con NDVI

## Descripción
Este proyecto evalúa la pérdida de vegetación posterior a un incendio utilizando imágenes satelitales Sentinel-2 y el índice NDVI.

Se implementa un flujo reproducible en Python para procesar datos raster, reclasificar el ΔNDVI y cuantificar el área afectada.

---

## Metodología

1. Cálculo de NDVI a partir de bandas espectrales
2. Cálculo de ΔNDVI (pre vs post incendio)
3. Eliminación de áreas no relevantes (mar)
4. Reclasificación en 4 categorías:

| Clase | Interpretación |
|------|--------------|
| 1 | Recuperación / aumento de vegetación |
| 2 | Baja afectación |
| 3 | Afectación moderada |
| 4 | Alta afectación |

5. Cálculo de superficie por clase (hectáreas)

---

## Tecnologías

- Python
- Rasterio
- NumPy
- QGIS (preprocesamiento)

---

## Uso

```bash
pip install -r requirements.txt
python src/analysis.py

##Estructura

data/       # raster de entrada (no incluido)
src/        # código Python
results/    # resultados generados
