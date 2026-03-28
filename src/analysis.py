import rasterio
import numpy as np

with rasterio.open("data/delta_ndvi.tif") as src:
    ndvi = src.read(1)
    meta = src.meta
    nodata = src.nodata

print("Raster cargado correctamente")
print("Shape:", ndvi.shape)
print("NoData:", nodata)

# --- reclasificación ---
clas = np.zeros_like(ndvi)

clas[(ndvi >= -1.1) & (ndvi < 0)] = 1
clas[(ndvi >= 0) & (ndvi < 0.2)] = 2
clas[(ndvi >= 0.2) & (ndvi < 0.4)] = 3
clas[(ndvi >= 0.4)] = 4

print("Reclasificación lista")

# --- guardar raster ---
meta.update(dtype=rasterio.int16)

with rasterio.open("results/clas_ndvi_python.tif", "w", **meta) as dst:
    dst.write(clas.astype(rasterio.int16), 1)

print("Raster clasificado guardado")

# --- cálculo de áreas ---
valid = clas[clas > 0]

unique, counts = np.unique(valid, return_counts=True)

print("Área por clase (hectáreas):")
for val, count in zip(unique, counts):
    area = count * 0.01
    print(f"Clase {int(val)}: {area:.2f} ha")
