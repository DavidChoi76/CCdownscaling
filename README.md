# CCdownscaling

This package provides implementation of several statistical climate downscaling techniques, as well as evaluation tools for downscaling outputs.
Preprint version of this research: https://egusphere.copernicus.org/preprints/2022/egusphere-2022-282/egusphere-2022-282.pdf
## Requirements

See [`environment.yml`](./environment.yml). Tensorflow is pinned in this conda environment in the interest of reproducibility.

## Usage

An example use case for downscaling precipitation at Chicago O'Hare airport can be found in the example folder.
This example requires some example data, which can be downloaded from: https://zenodo.org/record/6506677

Once that data is in place, the example can be run with: 
```bash
cd example
python ohare_example.py
```
And runs through several downscaling methods, including SOM, random forest, and quantile mapping. All these methods are then compared on PDF skill score, KS test, RMSE, bias, and autocorrelation, along with the undownscaled values from the NCEP reanalysis.

## Additional Examples: Uganda and Pakistan international education

Add two Jupyter Notebooks 
1. The first notebook to download Climate Change Scenario Data from https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cmip6?tab=form using API
2. The second notebook to downscale climate scenario data using CCdownscaling tool

Start downscaling using Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DavidChoi76/CCdownscaling.git/HEAD)

