# Sample thickness

:::::{div} full-width
::::{grid} 3

:::{grid-item}
:columns: 6

> The ices are deposited for 20 minutes and during deposition, the pressure in the PAC is regulated between 1 – 1.2 × 10<sup>−7</sup> mbar. In situ laser measurements are aquired using a monocromatic laser (HeNe) directed toward the center of the sample holder and reflected to a photodiode. Interference patterns arising from the constructive and destructive interference of the growing sample are recorded manually during deposition. The purpose of this reduction step is to fit the resulting data and get an average value of the sample thickness.

:::

:::{grid-item-card}
:class-header: bg-light
:columns: 3
:link: ../../../Method/sub_Interferometry.html
<span style="float: right">🔧</span>**PAC**
^^^

The PAC Chamber


:::

:::{grid-item-card}
:class-header: bg-light
:columns: 3
:link: ../../../Method/sub_Interferometry.html
<span style="float: right">📓</span>**Interferometry** 
^^^

Theory page related to laser interferometry


:::
::::
:::::

```{note}

There is better method to do that
- Double beam
- RAIRS


```


## Workflow 

:::::{div} full-width
::::{grid} 4

:::{grid-item-card}
:class-header: bg-light
**Notebook**

^^^

- ![flag alt >](../../../Docs/Svg_icons/excel-svgrepo-com.svg) laser-diode_{}.csv 
    - <a href="D:\DATA-RAW\PAC\{}/{}/laser-diode_{}.csv">example</a>


:::

:::{grid-item-card}
:class-header: bg-light
**Input**

^^^

- ![flag alt >](../../../Docs/Svg_icons/excel-svgrepo-com.svg) laser-diode_{}.csv 
    - <a href="D:\DATA-RAW\PAC\{}/{}/laser-diode_{}.csv">example</a>


:::

:::{grid-item-card}
:class-header: bg-light
**Output Data**

^^^

- ![flag alt >](../../../Docs/Svg_icons/excel-svgrepo-com.svg) Ice_thickness.csv  
 

:::

:::{grid-item-card}
:class-header: bg-light
**Output Plots**

^^^

- ![flag alt >](../../../Docs/Svg_icons/chart-svgrepo-com.svg) Thickness-calc_{}_1  

- ![flag alt >](../../../Docs/Svg_icons/chart-svgrepo-com.svg) Thickness-calc_{}_2  


:::
::::
:::::

## Data Import and Cleaning

The Raw data is of the shape

:::::{div} full-width

::::{grid} 2

:::{grid-item}
:columns: 6

> We aquire one data point every 30s

:::

:::{grid-item}
:columns: 6

<iframe class="preview-iframe" id="preview-iframe" src="../../_static/assets/GC/GC6-08-2022.htm" width="100%" height="400"></iframe>


```{note}

Insert here the data
- Export some example datasets to show the format

```

:::


::::

:::::

## Fitting

The purpose of the notebook is to fit the data of `laser-diode_{}.csv`

:::::{div} full-width

::::{grid} 2

:::{grid-item}
:columns: 6

$$

y = y_0 + A sin(\frac{2\pi}{w}(x-x_c))

$$ (laser diode fit)

:::

:::{grid-item}
:columns: 6

- $y_0$ is the vertical offset, 
- $A$ is the amplitude, 
- $x_c$ is the horizontal offset,
- $w$ is the period (i.e. $2\pi/w$ is the frequency)


:::

::::

:::::


We define the sine function `sinfit(x, *p)` for the fit with some initial guesses, which can be edited accordingly.

### <strong> &#x2023; <u>Example</u> 2020_09_16  </strong>

#### <strong> &#x2023; &#x2023;  Thickness Calculation 1 </strong>

> For this step we use the full range and it gives:

```{figure} ../../../Data/DATA_PROCESSING/2020_09_16/Plots/Thickness-calculation_2020_09_16_1.png

Thickness calculation 1 for 2020_09_16 sample
```

#### <strong> &#x2023; &#x2023; Thickness Calculation 2 </strong>

> For this second step, we reduce the range so that it only contains the beginning (more reliable) part of the interference spectrum. In this case I have selected a range of:
- 0 < time (s) < 540 

```{figure} ../../../Data/DATA_PROCESSING/2020_09_16/Plots/Thickness-calculation_2020_09_16_2.png

Thickness calculation 2 for 2020_09_16 sample
```


## Extra calculations

```{note}

May be should go in DR3

```

### Optical Depth

- &tau;<sub>&upsilon;</sub> is the optical depth and is equal to ln(10) times the integrated absorbance


### Column Density

N (mollecule cm<sup>-2</sup>)


$$

N = \frac{\left ( \int \left ( \tau _{\upsilon } \right ) d \upsilon  \right )}{A}
  
$$ (column_density)


- A is the band strength in cm molecule<sup>−1</sup>
