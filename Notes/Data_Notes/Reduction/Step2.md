# Step 2 

***
<p class="emphase">Baseline Correction</p>

***

## Overview

The purpose of this Reduction step is to substract the baseline contribution. There will be 3 sub-notebooks with respect to the different types of sample, respectively
- DR2_ASW
- DR2_C2H6
- DR2_C2H6_ASW

***
**Plan**:
- Load data
    - 1
    - 2
- T Ramp for reduction
- Chop the Data
    - A: 4000 - 2800
    - B: 2800 - 1900
    - C: 1900 - 800
- Background function definition
- Baseline correction
- Max Absorbance
- Plotting

***

### Plots

```{note}

- Plot all different samples together and find suitable range that work with all the data 

```

```{image} Documents/3Dsuccess.png
:alt: 3D cool plot
:width: 650px
:align: center
```

## DR2_ASW

```{warning}

- All the export.csv not working (wrong folder tree ?)

- Explain what every step does 

- When finished, copy and paste into reduction page

```

#### Imports
#### Input Parameters
#### Load Data

- All_RAW_df
- data_annex (what is the data loaded witin data annex)

#### T ramp for reduction

XP_Ramp_df from XP_list_test.csv

- Sanity Check

#### Chop the data

#### Background function definition

- Sanity Check

#### Baseline Correction

- data- background substraction

- Cleaning and Sanity Check

- Concatenation

- Export as csv

#### Max Absorbance

- Preliminary work

- Extract Max A

- Clean 

- Append to data Annex

#### Plotting

- Full Range

- OH Stretch
    - Baseline Correction
    - All scans
    - Max A
    - ... (to clean a bit)
    
- Comb Bands
    - Baseline Correction
    - ALL Scans
    - Max A
    - ...
    
- Bending
    - Baseline Correction
    - All scans
    - Max A
    
```{warning}

- Some plots not working (problem with new dictionnary of temperatures)
    - Plots related to plot of max A

```

#### Data Annex format


```{note}
Insert table in Reduction step 2
```

**Data Annex**

|Name              |   ASW_2020_09_16_1|
| :-------------   |    :------------- |
|min1              |         -0.0188444|
|index1            |               6636|
|min2              |        -0.00846373|
|index2            |               4235|
|min3              |        -0.00836861|
|index3            |               4139|
|min4              |        -0.00141767|
|index4            |               2403|
|min5              |       -0.000785604|
|index5            |               2269|
|min6              |         0.00514518|
|index6            |                530|
|max               |           0.278402|
|max_index         |               5120|
|maxAi_x           |               5120|
|maxA_x            |           0.290691|
|maxAw_x           |            3268.32|
|scan_number_x     |                  1|
|maxA0i_x          |               5120|
|maxA0_x           |           0.278402|
|maxA0w_x          |            3268.32|
|maxBi_x           |               2945|
|maxB_x            |         0.00928422|
|maxBw_x           |             2219.7|
|maxCi_x           |               1773|
|maxC_x            |          0.0235572|
|maxCw_x           |            1654.65|
|Int_A             |            95.9131|
|Int_C             |            6.95224|
|Int_N_A           |                100|
|maxAi_y           |               5120|
|maxA_y            |           0.290691|
|maxAw_y           |            3268.32|
|scan_number_y     |                  1|
|maxA0i_y          |               5120|
|maxA0_y           |           0.278402|
|maxA0w_y          |            3268.32|
|maxBi_y           |               2945|
|maxB_y            |         0.00928422|
|maxBw_y           |             2219.7|
|maxCi_y           |               1773|
|maxC_y            |          0.0235572|
|maxCw_y           |            1654.65|

```{note}
Even if columns doesn't match between ethane and water, doesn't really matter because we can have an if/else statement for comparison
```

    

## DR2_C2H6




## DR2_C2H6_ASW

