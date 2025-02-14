import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from netCDF4 import Dataset

# File path for wf data
file_path = "/glade/campaign/ral/hap/mizukami/archive/oconus_hydro/uncompressed/alaska/vic/monthly/BCSD/ACCESS1-3/rcp85/ACCESS1-3_rcp85_BCSD_wf_2099.nc"

# Load dataset
nc = Dataset(file_path, 'r')
longitude = nc.variables['longitude'][:]
latitude = nc.variables['latitude'][:]
runoff = nc.variables['RUNOFF'][0, :, :]  # Extract first time slice

# Mask fill values
runoff = np.ma.masked_where(runoff == -999, runoff)

# Plot
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(10, 6))
ax.set_extent([-180, -130, 50, 75])  # Alaska bounds

# Add map features
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=":")

# Plot data
c = ax.pcolormesh(longitude, latitude, runoff, transform=ccrs.PlateCarree(), cmap='viridis')
plt.colorbar(c, ax=ax, orientation='vertical', label="Runoff (mm/month)")

plt.title("Surface Runoff - 2099")
plt.savefig("wf_2099.png", dpi=300)
plt.show()

