# JEC_tool
Tool to debug the splitting of JEC uncertainties.

The code reads in the input text file, and first parses it to bin the JEC uncertainties according to eta and pt bins. This is done for all JEC sources. Then it plots the uncertainties for each JEC source as a function of pt for each eta bin, and as a function of eta for each pt bin.

## Usage

```
python JEC.py <options>
```

### Options

The scripts supports command line options as follow :
- --ymax float : Maximum of y axis. Default = 20
- --ymin float : Minimum of y axis. Default = 0.
- --logx : Set x axis to log. Disabled by default. Only possible for the pt distribution.
- --logy : Set y axis to log. Disabled by default.
- --legdim x1 y1 x2 y2: Customize the legend position and size. Default is [0.5, 0.5, 0.9, 0.88]
- --year str : Selects the year file UL2016preVFP/UL2016/UL2017/UL2018. Default = UL2018.

## Config section

The config section in the beginning of the script affords the following functionality.

- config["eta"] and config["pt"] : One can produce plots for specific values of pt and eta. If these lines are commented out, the script by default produces plots for all values of pt and eta.
- config["sources"] : One can choose the individual sources of JEC uncertainty using the config["sources"]. Simply uncomment the sources needed.
- config["quad"] : One can choose the sources to be added in quadrature. The script supports multiple sets of uncertainties to be added in quadrature. Three sets of sources are included in the script as an example, these may be extended or reduced as needed.

Have fun!
