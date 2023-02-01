# Daily Log

## 28/11/2022

***
**Focus**

- Implement web-documentation relative to the different reduction steps

**Objectif**:

    
**Good day?**
   
***


## 21/11/2022

***
**Focus**

- Modify DR2_C2H6 to have 3 different baseline (like ASW actually)
    - Include Rolling average,

- Continue and finish DR2_C2H6_ASW Notebook

**Objectif**:

    
**Good day?**
   
***

## 16/11/2022

***
**Focus**

- DR2_C2H6_ASW: Continue
    - reference sample - 2021_01_29
- Perform notebook for the remaining Ethane (only samples) 
    - 2021_09_15
    - 2021_09_18
    - 2021_09_19
        - Analyse the sample in a dedicated page -> [link](link)

**Objectif**:

    
**Good day?**
   
***

## 12/11/2022

***
**Focus**

- DR2_C2H6_ASW: Continue
    - reference sample - 2021_01_29
- Check for mistakes in DR2_C2H6 and if none found perform notebook for the remaining Ethane (only samples) 
    - 2021_09_15
    - 2021_09_18
    - 2021_09_19
        - Analyse the sample in a dedicated page -> **To create**

**Objectif**:

    
**Good day?**
   
***


## 11/11/2022

***
**Focus**

- DR2_C2H6: Finish
- DR2_C2H6_ASW: Start 

**Objectif**:

- Finish DR2_C2H6_ASW by the week end
    - process for all ethane sample
        - 2021_09_15
        - 2021_09_18
        - 2021_09_19
```{warning}

- Implement Hudson Integration range 
    - In daily log,
    - Find index value
    - Implement on graphs (general)

```

- Monday put **DR2_Full** in Figshare
    - Implement in Data_Binder
        - modif - Ethane different data annex, sample naming etc ...

- Tuesday Anita meeting
    - Good, neet *Daily log*
    - Implement Data Reduction section
    - Implement question page

- Prepare team meeting - Thursday 10 AM
    - Show introduction page -> *Implement*


    
**Good day?** &#128513; 

- Things Done
    - Finish DR2_C2H6
   
***



## 10/11/2022

***
**Focus**

- DR2_C2H6: Make the Notebook work
    - Sample test = "2020_12_03"  
    
**Good day?** &#128513; 

- **Things Done**

    - Complete DR2_ASW
    - Start DR2_C2H6
   
***


```{warning}

- A previous attempt of baseline has already been performed in the specific range of the CH stretch 

    - Make sure to don't overwrite those plots and compare -> Implement specific reduction page for ethane


```

- Post MaxA append, data annex is 37 column 


```{note}

- Don't create 1 single data_annex_full but 3:
    - data_annex_A_full
    - data_annex_E_full
    - data_annex_AE_full

```

### Difference with ASW

#### No data chopping

A single baseline correction will be sufficient 



```{figure} ../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR1_2020_12_03_Full-range.png
---
name: MC_X
width: 500px
---
description
```

```{note}

- DR2_2020_12_03_All-scans.csv already present in Data folder so saved the new csv with U at the end ie DR2_2020_12_03_All-scans_U.csv (just to check in case there is difference)

```

#### Max Absorbance peaks

What peaks do we want to investigate in order to follow the evolution of the ethane phase transformations

- first, identify the different ranges within which we can look for the max value

- use the python magic (notebook) and zoom in and out to check for specific ranges -> Doesn't work on jupyter lab, need to try with notebook instead ...

    - peak 1 - centered 2972 / range 3000 - 2955
    - peak 2 - centered 2940 / range 2955 - 2900
    - peak 3 - centered 2879 / range 2900 - 2860
    
**Index values**:

In order to determine the index min, I use the following command:

```python
All_RAW_df_BC[(All_RAW_df_BC['Wavenumber'] > 2998) & (All_RAW_df_BC['Wavenumber'] < 3002)].index.tolist()

# Followed by 

All_RAW_df_BC.loc[4564, 'Wavenumber']

```


- **Wavenumber / df index**

- 3000  - *4564*
- 2955 - *4470* 
- 2900 - *4356*
- 2860 - *4273*


```{note}

- Compare the centered peak position with dartois / Hudson

- Are other peaks of any interests ?
    - Find and perform band assignment Marta style

``` 

## 07/11/2022

***
**Focus**

- DR2_ASW: Make the Notebook work
    - solve *scan number to Temperature* link issue.
    
```{warning}

**Done**  &#128513;

```
    
***

- Insert Plot generated


:::::{div} full-width
::::{grid} 2
:::{grid-item}
:columns: 6

```{figure} ../DATA/DATA-Processing/PAC/XP_1-1/Samples/2020_09_16/Plots/DR/DR2_2020_09_16_A.png
---
name: MC_X
width: 500px
---
description
```

:::

:::{grid-item}
:columns: 6

**Formatting parameters**

- 

:::
::::

::::{grid} 2
:::{grid-item}
:columns: 6

```{figure} ../DATA/DATA-Processing/PAC/XP_1-1/Samples/2020_09_16/Plots/DR/DR2_2020_09_16_PeakA-frequency_shift.png
---
name: MC_X
width: 600px
---
description 
```

:::

:::{grid-item}
:columns: 6

```{figure} ../DATA/DATA-Processing/PAC/XP_1-1/Samples/2020_09_16/Plots/DR/DR2_2020_09_16_PeakA-Intensity_shift.png
---
name: MC_X
width: 600px
---
description
```

:::
::::

:::::