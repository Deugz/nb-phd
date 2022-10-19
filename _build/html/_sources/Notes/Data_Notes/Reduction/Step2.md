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
    

## DR2_C2H6




## DR2_C2H6_ASW

