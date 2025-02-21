# **VIC Alaska Analysis**

This repository contains scripts and Jupyter notebooks for analyzing Variable Infiltration Capacity (VIC) model hydrologic projections in Alaska. The project compares historical (1980-2010) and future (2070-2100) climate scenarios (RCP4.5 and RCP8.5), focusing on key hydrological variables such as **runoff, baseflow, snow water equivalent, and soil moisture**.

## **Installation**
To set up the environment, clone this repository and install the necessary dependencies using Conda:

```sh
git clone https://github.com/braghiere/vic_alaska_analysis.git
cd vic_alaska_analysis
conda env create -f environment.yml
conda activate vic_env
```

To update the Conda environment (if necessary):

```sh
conda env update --file environment.yml
```

## **Data Availability**
The VIC model outputs, downscaled GCM meteorological data, and hydrological variables are archived and publicly available at **NCAR Research Data Archive (RDA)** (Mizukami et al., 2022). The dataset includes:

- **Downscaled GCM meteorology**: Daily minimum and maximum temperatures and precipitation.
- **VIC hydrological model outputs**:
  - **Water fluxes**: Surface runoff, baseflow, total evapotranspiration, snowmelt, and ice melt.
  - **State variables**: Soil moisture, snow water equivalent, and ice water equivalent.
  - **Energy fluxes**: Shortwave and longwave radiation, latent and sensible heat fluxes, ground heat, and soil temperature.

Due to storage limitations, the dataset is not included in this repository but can be downloaded from the following sources:

- **VIC Model Outputs**: [NCAR RDA Dataset](https://rda.ucar.edu/)
- **Downscaled GCM Meteorology**: [Dataset Link](https://rda.ucar.edu/)
- **Hydrological Variables**: [Dataset Link](https://rda.ucar.edu/)

## **Code Availability**
The VIC and downscaling codes used to generate the data are open-source:

- **VIC hydrology model**: [VIC 4.2 Glacier Version](https://github.com/UW-Hydro/VIC)
- **Bias-Corrected Spatially Disaggregated (BCSD) downscaling**: [scikit-downscale](https://github.com/pangeo-data/scikit-downscale)

## **Usage**
### **Jupyter Notebooks**
Run the following notebooks to generate key hydrological visualizations:

```sh
notebooks/Fig1.ipynb
notebooks/Fig2.ipynb
notebooks/Fig3.ipynb
notebooks/Fig4.ipynb
notebooks/Fig5.ipynb
```

### **Python Scripts**
```sh
scripts/process_vic_ensemble.py  # Processes VIC model ensemble outputs.
scripts/plot_wf.py               # Generates seasonal and spatial plots for water fluxes.
```

## **Figures**
Generated figures are stored in the `figures/` directory:

```sh
figures/Fig1.png   # Spatial changes in runoff, baseflow, snow water equivalent, and soil moisture across Alaska.
figures/Fig2.pdf   # Seasonal cycles of these variables for two study sites (Tok and Canol Trail), comparing historical and future climate scenarios.
figures/Fig3.pdf   # Projected permafrost extent changes under RCP4.5 and RCP8.5.
figures/Fig4.pdf   # Soil temperature changes and active layer deepening.
figures/Fig5.pdf   # Soil moisture variability and its impact on contaminant transport.
```

## **Reproducibility**
To ensure full reproducibility, make sure to:

```sh
# Download the VIC model data from NCAR RDA
# Use the provided Conda environment (environment.yml)
# Follow the script execution order:
1. Run `scripts/process_vic_ensemble.py` to process VIC model ensemble outputs.
2. Run the Jupyter notebooks for visualization.
```
