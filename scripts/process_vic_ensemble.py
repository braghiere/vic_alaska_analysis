import os
import numpy as np
import xarray as xr
from tqdm import tqdm  # For progress tracking

# Define paths
INPUT_DIR = "/glade/campaign/ral/hap/mizukami/archive/oconus_hydro/uncompressed/alaska/vic/monthly/BCSD"
OUTPUT_DIR = "/glade/derecho/scratch/renatob/vic_alaska"
SCENARIOS = ["rcp45", "rcp85"]
FILE_TYPES = ["ws", "wf", "eb"]
YEARS = range(1950, 2100)  # 1950-2099

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Iterate over scenarios and file types
for SCENARIO in SCENARIOS:
    for FILE_TYPE in FILE_TYPES:
        print(f"🚀 Processing {SCENARIO} - {FILE_TYPE} ...")

        # List all models
        models = [d for d in os.listdir(INPUT_DIR) if os.path.isdir(os.path.join(INPUT_DIR, d))]

        # Collect yearly datasets
        yearly_datasets = []
        
        # Progress bar for years
        for YEAR in tqdm(YEARS, desc=f"⏳ {SCENARIO} {FILE_TYPE}"):
            file_paths = []
            for model in models:
                file_path = os.path.join(INPUT_DIR, model, SCENARIO, f"{model}_{SCENARIO}_BCSD_{FILE_TYPE}_{YEAR}.nc")
                if os.path.exists(file_path):
                    file_paths.append(file_path)

            if len(file_paths) == 0:
                print(f"❌ No files found for {SCENARIO}, {FILE_TYPE}, {YEAR}")
                continue

            # Load datasets
            datasets = [xr.open_dataset(f) for f in file_paths]

            # Stack along ensemble dimension
            ensemble_ds = xr.concat(datasets, dim="ensemble")

            # Compute mean and standard deviation (uncertainty)
            ensemble_mean = ensemble_ds.mean(dim="ensemble")
            ensemble_std = ensemble_ds.std(dim="ensemble")  # Standard deviation among models

            # Append to list for concatenation later
            yearly_datasets.append((ensemble_mean, ensemble_std))

            # Close datasets
            for ds in datasets:
                ds.close()

        if not yearly_datasets:
            print(f"⚠️ No valid data for {SCENARIO} - {FILE_TYPE}, skipping...")
            continue

        # Concatenate over time
        all_mean = xr.concat([ds[0] for ds in yearly_datasets], dim="time")
        all_std = xr.concat([ds[1] for ds in yearly_datasets], dim="time")

        # Save outputs
        mean_file = os.path.join(OUTPUT_DIR, f"cmip5_ensemble_{FILE_TYPE}_{SCENARIO}.nc")
        std_file = os.path.join(OUTPUT_DIR, f"cmip5_ensemble_{FILE_TYPE}_{SCENARIO}_uncertainty.nc")

        all_mean.to_netcdf(mean_file)
        all_std.to_netcdf(std_file)

        print(f"✅ Saved: {mean_file}")
        print(f"✅ Saved: {std_file}")

print("🎉 All processing complete!")

