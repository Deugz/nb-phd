# DR2 First Analysis

***

- **Anita meeting**: 14/03/2023 

This week I have performed the **DR2** [Notebook]() for:
- Water Samples
- Ethane
- Ethane + ASW

I have also fixed the **Data_Analysis_Binder** [Notebook](), that is now working on my local machine (not on the binder cloud system)

Below is a first (rough analysis of what I observed)

***

## Water

### Reference Sample

:::{div} full-width

<p class="emphase2">2020_09_28</p>

:::

:::::{div} full-width
::::{grid} 2
:::{grid-item}
:columns: 4

- Deposition Temperature: 20 K
- Deposition time: 20 min 
- Deposition pressure: 1 * 10<sup>-7</sup> mbar
- Thickness: ? 

- Ramp: 4 scans per temperature step (1 annealing and 3 isotherm)

```{note}

How can I convert µm thickness into monolayer (ML)

```

:::

:::{grid-item}
:columns: 8

```{figure} ../../../Data/DATA_PROCESSING/2020_09_28/Plots/DR2_2020_09_28_A.png
:width: 1000px
:name: DR2_2020_09_28_A
Caption
```

:::
::::
:::::

#### OH Stretch peak evolution

:::::{div} full-width
::::{grid} 2
:::{grid-item}
:columns: 6

**Frequency**

```{figure} ../../../Data/DATA_PROCESSING/2020_09_28/Plots/DR2_2020_09_28_PeakA-frequency_shift_no_legend.png
:width: 1000px
:name: DR2_2020_09_28_PeakA-frequency_shift
Caption
```

````{dropdown} Legend

```{figure} ../../../Data/DATA_PROCESSING/2020_09_28/Plots/DR2_2020_09_28_PeakA-frequency_shift_legend.png
:width: 200px
:name: DR2_2020_09_28_PeakA-frequency_shift_legend
Caption
```

````

:::

:::{grid-item}
:columns: 6

**Intesity**

```{figure} ../../../Data/DATA_PROCESSING/2020_09_28/Plots/DR2_2020_09_28_PeakA-Intensity_shift_no_legend.png
:width: 1000px
:name: DR2_2020_09_28_PeakA-Intensity_shift
Caption
```

````{dropdown} Legend

```{figure} ../../../Data/DATA_PROCESSING/2020_09_28/Plots/DR2_2020_09_28_PeakA-Intensity_shift_legend.png
:width: 200px
:name: DR2_2020_09_28_PeakA-Intensity_shift_legend
Caption
```

````

:::
::::
:::::

##### Observations

- The peak intensity fluctuate a lot (+- 5 cm<sup>-1</sup>) 



#### Comparison

##### Litterature

##### This work




- Changes happening at 135 K (bellow glass transition)
    - insert right plot
    
    
### 2020_10_15

-  Big change at 140 K (nothing seen at 135)





## C2H6

Ethane Ice phases

- Crystaline
- Amorphous 
- Clathrate


## C2H6/ASW

### 2021/03/08 

- Dodgy sample (CO2 contamination + unsmoothed sample)
- We can observe that some ethane remain embeded within the ice during all the annealing step (**Embeded into the pores**)

- Big peak growing at (?)

:::::{div} full-width
::::{grid} 2 
:::{grid-item}


```{figure} ../../../Data/DATA_PROCESSING/2021_03_08/Plots/DR2_2021_03_08_A.png
:width: 800px
:name: DR2_2021_03_08_A.png
Caption
```

:::

:::{grid-item}


```{figure} ../../../Data/DATA_PROCESSING/2021_03_08/Plots/DR2_2021_03_08_PeakA-frequency_shift_no_legend.png
:width: 800px
:name: DR2_2021_03_08_PeakA-frequency_shift_no_legend
Caption
```

:::
::::
:::::

```{note}

A more friendly view of the sample (splitted by the different ranges) will be generated during the data-processing phase

```

### 2021/03/24


- (C2H6:ASW 1:1 Mixture)
- **Step to 130K**

Again, dodgy sample with some unsmoothed scans 

```{note}

Will need to put something in place to take care of those

ie (in the processing phase)


```

### 2021/07/16

Nice sample but lots of CO2 contamination

```{note}

would that influence the sample signal
- No because it is only the detector box that is contaminated and not the chamber itself


How can I supress that contribution

```

### 2021/09/20

- Layered sample.

```{note}

Is there still some ethane present at high temperature ? 

We dont see a modification of the OH stretch as is happening for the codeposition samples above.

```

OK sample (some CO2 contamination but contained)

Not too much ethane though

### 2021/10/04

***

Very Intersting sample


***

```{warning}

Is the peak growing when  we go down in temperature the same as the one that grow when we have codeposition of ASW + ethane

- What would that mean ?

```

**Insert plots**

### 2021/10/07


Scan 3,4,5 very interesting dangling bond feature, is it due to CO2 contamination






