# Statistical Climate Downscaling Tool

This package provides implementation of several statistical climate downscaling techniques, as well as evaluation tools for downscaling outputs.
Preprint version of this research: https://egusphere.copernicus.org/preprints/2022/egusphere-2022-282/egusphere-2022-282.pdf

## Methods
This library runs through several downscaling methods, including SOM, random forest, and quantile mapping. All these methods are then compared on PDF skill score, KS test, RMSE, bias, and autocorrelation, along with the undownscaled values from the NCEP reanalysis.

## Examples for Climate Change Application Education

Start JupyterHub environment using Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DavidChoi76/CCdownscaling.git/HEAD)

### 1. Uganda
   
   a. The <a href="https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6?tab=form" target="_blank"> first notebook </a> to download Climate Change Scenario Data from <a href="https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6?tab=form" target="_blank"> CMIP6 Climate Projections Data Store </a> using API
   
   b. The <a href="https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6?tab=form" target="_blank"> second notebook </a> to downscale climate scenario data using CCdownscaling tool
   
### 2. Pakistan

   a. The <a href="https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6?tab=form" target="_blank"> first notebook </a> to download Climate Change Scenario Data from <a href="https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6?tab=form" target="_blank"> CMIP6 Climate Projections Data Store </a> using API
   
   b. The <a href="https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6?tab=form" target="_blank"> second notebook </a> to downscale climate scenario data using CCdownscaling tool
   
### 3. Mozambique

   a. The <a href="https://github.com/DavidChoi76/CCdownscaling/blob/main/example/mozambique/1_Downloading_Climate_Data_from_Clmate_Data_Store.ipynb" target="_blank"> first notebook </a> to download Climate Change Scenario Data from <a href="https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6?tab=form" target="_blank"> CMIP6 Climate Projections Data Store </a> using API
   
   b. The <a href="https://github.com/DavidChoi76/CCdownscaling/blob/main/example/mozambique/2_application_of%20_downscaling_methods_using_climate_data.ipynb" target="_blank"> second notebook </a> to downscale climate scenario data using CCdownscaling tool

