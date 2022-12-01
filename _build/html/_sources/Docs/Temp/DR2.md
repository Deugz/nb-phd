# DR2

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

At first glance, it seems that a linear background over the whole range is sufficient (Method 1). However I attempted to use a similar reduction routine than for ASW (ie splitting the data in 3 ranges) and appliying a linear background for each range.


#### Method comparison

:::::{div} full-width
::::{grid} 2
:::{grid-item-card}
:class-header: bg-light
:columns: 6
**Method 1** 
^^^

Different ranges (like ASW) + rolling(5)

:::

:::{grid-item-card}
:class-header: bg-light
:columns: 6
**Method 2** 
^^^

Single baseline over whole range

:::
::::
:::::





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
