# Step 2 

***
<p class="emphase">Baseline Correction</p>

The purpose of this Reduction step is to substract the baseline contribution. There will be 3 sub-notebooks with respect to the different types of sample, respectively:

***

**Notebooks**:

::::{grid} 3

:::{grid-item-card}
:class-header: bg-light
:link: Step1.html
<span style="float: right">![flag alt >](../../../Docs/Svg_icons/jupyter-svgrepo-com.svg)</span>**DR2_ASW**
^^^

```{image} ../../../Docs/Svg_icons/Chemistry/Chem_water.png
:alt: Water_moleucule
:width: 60px
:align: center
```

:::

:::{grid-item-card}
:class-header: bg-light
:link: Step1.html
<span style="float: right">![flag alt >](../../../Docs/Svg_icons/jupyter-svgrepo-com.svg)</span>**DR2_C2H6**
^^^

```{image} ../../../Docs/Svg_icons/Chemistry/Chem_ethane.png
:alt: Water_moleucule
:width: 60px
:align: center
```

:::

:::{grid-item-card}
:class-header: bg-light
:link: Step1.html
<span style="float: right">![flag alt >](../../../Docs/Svg_icons/jupyter-svgrepo-com.svg)</span>**DR2_C2H6_ASW**
^^^

```{image} ../../../Docs/Svg_icons/Chemistry/Chem_mix.png
:alt: Water_moleucule
:width: 60px
:align: center
```

:::


::::

## Overview



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

```{note}
Implement here the general strcture of the notebook
```

[/----------------------------------------------------------------------------------------------------------------------------------------------------------------------- Is it a comment ?/]: # 

## DR2_ASW

### <strong>&#187;  <u>Baseline strategy</u></strong>

:::::{div} full-width
::::{grid} 3
:::{grid-item}
:columns: 4

- 3 different Ranges
- Presence of CO<sub>2</sub> to take into account

:::

:::{grid-item}
:columns: 8

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-1/Samples/2020_09_16/Plots/DR/DR1_2020_09_16_Full-range.png
---
name: ET1
width: 600px
---
ASW DR1 2020_09_16 (pre Baseline correction), whole range
```

:::
::::
:::::

### <strong>&#187;  <u>Band assignment and evolution with T</u></strong>

#### <strong>Range 1</strong>  

:::::{div} full-width
::::{grid} 3
:::{grid-item}
:columns: 6

- OH Stretch 


:::

:::{grid-item}
:columns: 6

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_sub-range_1.png
---
name: ET1
width: 600px
---
description 
```

:::
::::
:::::

##### &#9824; Peaks






## DR2_C2H6

### <strong>&#187;  <u>Baseline strategy</u></strong>

:::::{div} full-width
::::{grid} 3
:::{grid-item}
:columns: 4

I compute a linear background over the whole range of the data. The data will subsequently be splitted in 3 ranges:
- Range 1 (3050 - 2850 cm<sup>-1</sup>)
    - CH stretch ?
- Range 2
- Range 3
:::

:::{grid-item}
:columns: 8

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR1_2020_12_03_Full-range_U.png
---
name: ET1
width: 600px
---
Ethane 2020_12_03 DR1 (pre Baseline correction), whole range 
```

:::
::::
:::::



### <strong>&#187;  <u>Band assignment and evolution with T</u></strong>

#### <strong>Range 1</strong>  

:::::{div} full-width
::::{grid} 3
:::{grid-item}
:columns: 6

3 main peaks (labelled as E1, E2, E3 with decreasing wavenumber).

```{warning}

There seems to be also a very small feature between E2 and E3 that has not been reported in the following litterature:
- {cite:p}`Dartois2021` no report
- {cite:p}`Hudson2014` to check
- {cite:p}`Hudson2009` to check
- {cite:p}`Hepp1999` to check

could be ethane:oxirane (7:3) mixed clathrate spectrum

- {cite:p}`Richardson1985` to check

```



:::

:::{grid-item}
:columns: 6

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_sub-range_1.png
---
name: ET1
width: 600px
---
description 
```

:::
::::
:::::

```{note}

Should I try to plot them with an **offset**

```

##### &#9824; Peaks


:::::{div} full-width
::::{grid} 3
:::{grid-item-card}
:columns: 4

**E1**

^^^

- **assignment**: 2972 cm<sup>-1</sup>
- **vibrational mode**: &nu;<sub>7</sub>

***

**Frequency**

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE1-freq.png
---
name: ET1
width: 600px
---
description 
```

***

**Absorbance**

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE1-Abs.png
---
name: ET1
width: 600px
---
description 
```

:::

:::{grid-item-card}
:columns: 4

**E2** 

^^^

- **assignment**: 2942 cm<sup>-1</sup>
- **vibrational mode**: &nu;<sub>1</sub>, &nu;<sub>8</sub> + &nu;<sub>11</sub>

***

**Frequency**

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE2-freq.png
---
name: ET1
width: 600px
---
description 
```

***

**Absorbance**


```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE2-Abs.png
---
name: ET2
width: 600px
---
description
```

:::

:::{grid-item-card}
:columns: 4

**E3** 

^^^

- **assignment**: 2880 cm<sup>-1</sup>
- **vibrational mode**: &nu;<sub>5</sub>

***

**Frequency**

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE3-freq.png
---
name: ET1
width: 600px
---
description 
```

***

**Absorbance**

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE3-Abs.png
---
name: ET3
width: 600px
---
description
```

:::

::::
:::::

```{admonition} Comments

- No band **frequency shift** is observed within the **margin of error**


- **Intensity shift**: E1 and E3 see some changes in their maximum absorbance peak and hence are good tracers for the **crystalisation processes**


- May be a slight peak sharpening is present ?


- Evaluation of the peaks at lower wavenumber are necessary to reveal the full picture of phase change


```


***

#### <strong>Range 2</strong>  

:::::{div} full-width
::::{grid} 3
:::{grid-item}
:columns: 6

```{warning}

Baseline correction is not great within this range
- Have I performed a previous 
```


:::

:::{grid-item}
:columns: 6

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_sub-range_2.png
---
name: ET1
width: 600px
---
description 
```

:::
::::
:::::

````{margin}
```{note}

Need to create two new ranges for those range
- E4 - centered 1460 / range 1500 - 1425
- E5 - centered 1370 / range 1400 - 1350

**Wavenumber / df index**

- 1500  - *1452*
- 1425 - *1297* 
- 1400 - *1245*
- 1350 - *1141*

```
````

##### &#9824; Peaks

::::{grid} 2
:::{grid-item-card}
:columns: 6

**E4**

^^^

- **assignment**: 1460 cm<sup>-1</sup>
- **vibrational mode**: &nu;<sub>8</sub>

***

**Frequency**

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE4-freq.png
---
name: ET1
width: 600px
---
description 
```

***

**Absorbance**

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE4-Abs.png
---
name: ET1
width: 600px
---
description 
```

:::

:::{grid-item-card}
:columns: 6
    
 **E5**
 
^^^

- **assignment**: 1370 cm<sup>-1</sup>
- **vibrational mode**: &nu;<sub>6</sub>

***

**Frequency**

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE5-freq.png
---
name: ET1
width: 600px
---
description 
```

***

**Absorbance**


```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE5-Abs.png
---
name: ET2
width: 600px
---
description
```

:::

::::


***

#### <strong>Range 3</strong> 

:::::{div} full-width
::::{grid} 3
:::{grid-item}
:columns: 6


```{note}
Intersting because band splitt
- How do I take that into account in reduction process
    - peak 6 remain the same
    - peak 7 is the appearing one
- Check litterature review on what have been said there
```


:::

:::{grid-item}
:columns: 6

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_sub-range_3.png
---
name: ET1
width: 600px
---
description 
```

:::
::::
:::::

##### &#9824; Peaks

````{margin}

```{note}

**Low T**

(work for both low and high T) - different for reduction though

- peak 6 - centered 815 / range 820 - 810

- **Wavenumber / df index**

- 820  - *42*
- 810 - *21* 


**High T**


- peak 7 - centered 825 / range 820 - 830

- **Wavenumber / df index**

- 820 - *42*
- 830 - *63* 

```
````



::::{grid} 2
:::{grid-item-card}
:columns: 6

**E6**

^^^


- **assignment**: cm<sup>-1</sup>
- **vibrational mode**: ? (not reported in Dartois)


***

**Frequency**

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE6-freq.png
---
name: ET1
width: 600px
---
description 
```

***

**Absorbance**

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE6-Abs.png
---
name: ET1
width: 600px
---
description 
```

:::

:::{grid-item-card}
:columns: 6
    
**E7**

^^^

- **assignment**: cm<sup>-1</sup>
- **vibrational mode**: &nu;<sub>6</sub>

***

**Frequency**

```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE7-freq.png
---
name: ET1
width: 600px
---
description 
```

***

**Absorbance**


```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2020_12_03/Plots/DR/DR2_2020_12_03_PeakE7-Abs.png
---
name: ET2
width: 600px
---
description
```

:::

::::


```{admonition} Comments

- Those peaks are not reported in - {cite:p}`Dartois2021`
- 2

```



````{margin}
```{figure} ../../../DATA/DATA-Processing/PAC/XP_1-2/Samples/2021_09_15/Plots/DR/DR2_2021_09_15_BC_total.png
---
name: ET2
width: 200px
height: 200px
---
BC 2021_09_15 (click for bigger plot)
```
````

### <strong>&#187;  <u>Adjustments</u></strong>

#### <strong> BC lower range </strong>

After processing the 2021_09_15, I decided to reduce the range of the Baseline correction in order to exclude the lower part of the spectrum that create some errors (cf Plots in the margin)

- range modified from index 0 to index 40 (new baseline coorected scan have _U at the end of it's name)

## DR2_C2H6_ASW



## Appendix


### <strong>&#187;  <u>Data Annex</u></strong>

````{sidebar} Important parameters

- Max A
- MaxAw


````


As the data is processed using the different notebooks, some usefull (or not) data is extracted within the reduction flow and appended into an evolving dataframe called data_annex.
because of the variability of parameters extracted for each samples data_annex has a different shape for the different types of sample and because the index is used to retrieve the appropriate data, find below the various format of data_annex post DR2 reduction.

```{note}
Even if columns doesn't match between ethane and water, doesn't really matter because we can have an if/else statement for comparison
```



:::::{div} full-width

::::{grid} 3

:::{grid-item}

**DR2_ASW**

|Index    |Name              |   ASW_2020_09_16_1|
| :------ | :-------------   |    :------------- |
|1        |min1              |         -0.0188444|
|2        |index1            |               6636|
|3        |min2              |        -0.00846373|
|4        |index2            |               4235|
|5        |min3              |        -0.00836861|
|6        |index3            |               4139|
|7        |min4              |        -0.00141767|
|8        |index4            |               2403|
|9        |min5              |       -0.000785604|
|10       |index5            |               2269|
|11       |min6              |         0.00514518|
|12       |index6            |                530|
|13       |max               |           0.278402|
|14       |max_index         |               5120|
|15       |maxAi_x           |               5120|
|16       |maxA_x            |           0.290691|
|17       |maxAw_x           |            3268.32|
|18       |scan_number_x     |                  1|
|19       |maxA0i_x          |               5120|
|20       |maxA0_x           |           0.278402|
|21       |maxA0w_x          |            3268.32|
|22       |maxBi_x           |               2945|
|23       |maxB_x            |         0.00928422|
|24       |maxBw_x           |             2219.7|
|25       |maxCi_x           |               1773|
|26       |maxC_x            |          0.0235572|
|27       |maxCw_x           |            1654.65|
|28       |Int_A             |            95.9131|
|29       |Int_C             |            6.95224|
|30       |Int_N_A           |                100|
|31       |maxAi_y           |               5120|
|32       |maxA_y            |           0.290691|
|33       |maxAw_y           |            3268.32|
|34       |scan_number_y     |                  1|
|35       |maxA0i_y          |               5120|
|36       |maxA0_y           |           0.278402|
|37       |maxA0w_y          |            3268.32|
|38       |maxBi_y           |               2945|
|39       |maxB_y            |         0.00928422|
|40       |maxBw_y           |             2219.7|
|41       |maxCi_y           |               1773|
|42       |maxC_y            |          0.0235572|
|43       |maxCw_y           |            1654.65|

:::

:::{grid-item}

**DR2_C2H6**

|Index    |Name              |  C2H6_2020_12_03_1  |
| :------ | :-------------   |  :-------------     |
|1        |min1              |     0.0255654       |
|2        |index1            |          6638       |
|3        |min2              |     0.0362991       |
|4        |index2            |          4290       |
|5        |min3              |     0.0385687       |
|6        |index3            |          4146       |
|7        |min4              |     0.0508658       |
|8        |index4            |   2481              | 
|9        |min5              |     0.0520633       |
|10       |index5            |          2278       |
|11       |min6              |     0.0570417       |
|12       |index6            |          1036       |
|13       |max               |      0.335483       |
|14       |max_index         |          4505       |
|15       |maxE1i            |          4505       |
|16       |maxE1             |      0.297932       |
|17       |maxE1w            |       2971.81       |
|18       |scan_number       |             1       |
|19       |maxE2i            |          4443       |
|20       |maxE2             |     0.0545266       |
|21       |maxE2w            |       2941.92       |
|22       |maxE3i            |          4314       |
|23       |maxE3             |      0.107159       |
|24       |maxE3w            |       2879.73       |
|25       |maxE4i            |          1377       |
|26       |maxE4             |      0.036049       |
|27       |maxE4w            |       1463.73       |
|28       |maxE5i            |          1183       |
|29       |maxE5             |      0.0207815      |
|30       |maxE5w            |        1370.2       |
|31       |maxE6i            |             36      |
|32       |maxE6             |     0.0382103       |
|33       |maxE6w            |       817.201       |
|34       |maxE7i            |            43       |
|35       |maxE7             |     0.0237016       |
|36       |maxE7w            |       820.576       |

:::

:::{grid-item}

**DR2_C2H6_ASW**

:::


::::

:::::

### <strong>&#187;  <u>Reduction Plots</u></strong>
