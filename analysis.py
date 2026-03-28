import rasterio
import numpy as np

with rasterio.open("data/delta_ndvi.tif") as src:
    ndvi = src.read(1)
    meta = src.meta
    nodata = src.nodata

print("Raster cargado correctamente")
print("Shape:", ndvi.shape)
print("NoData:", nodata)
