# statistik_citra.py
"""
Script untuk menghitung statistik dasar dari citra raster hasil pemodelan.
"""

import numpy as np
import rasterio
import matplotlib.pyplot as plt

# Path ke file raster
raster_path = "hasil_model.tif"

# Membaca raster
with rasterio.open(raster_path) as src:
    raster_data = src.read(1)  # Membaca band pertama
    nodata = src.nodata

# Masking nilai NoData
if nodata is not None:
    raster_data = np.ma.masked_equal(raster_data, nodata)

# Hitung statistik dasar
min_val = raster_data.min()
max_val = raster_data.max()
mean_val = raster_data.mean()
std_val = raster_data.std()

print(f"Statistik Raster:")
print(f"Minimum: {min_val}")
print(f"Maksimum: {max_val}")
print(f"Rata-rata: {mean_val}")
print(f"Standar deviasi: {std_val}")

# Plot histogram
plt.figure(figsize=(8, 6))
plt.hist(raster_data.compressed(), bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram Nilai Piksel")
plt.xlabel("Nilai Piksel")
plt.ylabel("Frekuensi")
plt.grid(True)
plt.tight_layout()
plt.show()
