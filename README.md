# Análisis de pérdida de vegetación con NDVI

## Objetivo
Evaluar la pérdida de vegetación post-incendio utilizando imágenes satelitales Sentinel-2 y el índice NDVI.

## Metodología
1. Cálculo de NDVI
2. Diferencia de NDVI (ΔNDVI)
3. Reclasificación en 4 categorías:
   - 1: Recuperación / aumento
   - 2: Baja afectación
   - 3: Afectación moderada
   - 4: Alta afectación

## Resultados
Se calcularon las superficies (hectáreas) para cada clase a partir del raster clasificado.

## Uso

```bash
pip install rasterio numpy
python src/analysis.py

##Estructura

data/       # raster de entrada
src/        # código Python
results/    # resultados generados

