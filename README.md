# **VIC Alaska Analysis**
This repository contains scripts and Jupyter notebooks for analyzing Variable Infiltration Capacity (VIC) model hydrologic projections in Alaska. The project compares historical (1980-2010) and future (2070-2100) climate scenarios (RCP4.5 and RCP8.5), focusing on key hydrological variables such as **runoff, baseflow, snow water equivalent, and soil moisture**.

## **Installation**
To set up the environment, clone this repository and install the necessary dependencies using Conda:

```sh
git clone https://github.com/yourusername/vic_alaska_analysis.git
cd vic_alaska_analysis
conda env create -f environment.yml
conda activate vic_env
To update the Conda environment (if necessary):

sh
Copy
Edit
conda env update --file environment.yml
Data Availability
The VIC model outputs, downscaled GCM meteorological data, and hydrological variables are archived and publicly available at NCAR Research Data Archive (RDA) (Mizukami et al., 2022). The dataset includes:

Downscaled GCM meteorology: Daily minimum and maximum temperatures and precipitation.
VIC hydrological model outputs:
Water fluxes: Surface runoff, baseflow, total evapotranspiration, snowmelt, and ice melt.
State variables: Soil moisture, snow water equivalent, and ice water equivalent.
Energy fluxes: Shortwave and longwave radiation, latent and sensible heat fluxes, ground heat, and soil temperature.
Due to storage limitations, the dataset is not included in this repository but can be downloaded from the DOI above.

Code Availability
The VIC and downscaling codes used to generate the data are open-source:

VIC hydrology model: VIC 4.2 Glacier Version
Bias-Corrected Spatially Disaggregated (BCSD) downscaling: scikit-downscale
Usage
Jupyter Notebooks: Run notebooks/Fig1.ipynb and notebooks/Fig2.ipynb to generate key hydrological visualizations.
Python Scripts:
scripts/process_vic_ensemble.py → Processes VIC model ensemble outputs.
scripts/plot_wf.py → Generates seasonal and spatial plots for water fluxes.
Figures
Generated figures are stored in the figures/ directory:

Fig1: Spatial changes in runoff, baseflow, snow water equivalent, and soil moisture across Alaska.
Fig2: Seasonal cycles of these variables for two study sites (Tok and Canol Trail), comparing historical and future climate scenarios.
Reproducibility
To ensure full reproducibility, make sure to:

Download the VIC model data from NCAR RDA.
Use the provided Conda environment (environment.yml).
Follow the script execution order (process the data first, then run the notebooks for visualization).
