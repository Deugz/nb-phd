# Overview

## Experiments

:::::{div} full-width
::::{grid} 3
:::{grid-item-card}
:link: XP-1_1/XP-1_1.html
:text-align: center
:columns: 4

<h4><strong>XP 1-1</strong> ASW</h4>

<br>
<br>

![flag alt >>](../../Docs/Svg_icons/Chemistry/Chem_water.png) 

![flag alt >](../../Docs/Svg_icons/Chemistry/ice2-svgrepo-com.svg) **Deposition  temperature**
- 20 - 130K

![flag alt >](../../Docs/Svg_icons/Chemistry/thermometer.png) **Ramp temperature**
- 30 - 160 K

![flag alt >](../../Docs/Svg_icons/Chemistry/wait-hourglass-svgrepo-com.svg) **Isotherms**
- 30K


:::



:::{grid-item-card}
:link: XP-1_2/XP-1_2.html
:text-align: center
:columns: 4

<h4><strong>XP 1-2</strong> Ethane</h4>

<br>
<br>


<span style="float:center;width:100px"> ![flag alt >>](../../Docs/Svg_icons/Chemistry/Chem_ethane.png) </span>

![flag alt >](../../Docs/Svg_icons/Chemistry/ice2-svgrepo-com.svg) **Deposition  temperature**
- 20 - 130K

![flag alt >](../../Docs/Svg_icons/Chemistry/thermometer.png) **Ramp temperature**
- 30 - 70 K

![flag alt >](../../Docs/Svg_icons/Chemistry/wait-hourglass-svgrepo-com.svg) **Isotherms**
- 30K

:::

:::{grid-item-card}
:link: XP-1_2/XP-1_2.html
:text-align: center
:columns: 4

<h4><strong>XP 1-2</strong> Ethane + ASW</h4>

<br>
<br>

<span style="float:center;width:100px"> ![flag alt >>](../../Docs/Svg_icons/Chemistry/Chem_mix.png) </span>

![flag alt >](../../Docs/Svg_icons/Chemistry/ice2-svgrepo-com.svg) **Deposition  temperature**
- 20 - 130K

![flag alt >](../../Docs/Svg_icons/Chemistry/thermometer.png) **Ramp temperature**
- 30 - 70 K

![flag alt >](../../Docs/Svg_icons/Chemistry/wait-hourglass-svgrepo-com.svg) **Isotherms**
- 30K

:::
::::
:::::

### Samples

:::::{div} full-width
<iframe class="preview-iframe" id="preview-iframe" src="../../_static/assets/Sample_list/Sample_list.html" width="100%" height="600"></iframe>
:::::


## Data

### RAW

Data from ice films deposited at various conditions is obtained from **IR spectroscopy** (absorbance). We obtain a multitude of scans (Absorbance vs wavenumber) that are saved and stored in a `csv` format under a *dated folder*. Before we can compare the different samples, the data has to undergo various reduction and processing steps that I referred as data **pipeline** 


### Pipeline

```{margin}
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
<lottie-player src="https://assets6.lottiefiles.com/packages/lf20_KXdLRdwnM5.json"  background="transparent"  speed="1"  style="width: 100%; height: 100%;"  loop  autoplay></lottie-player>
```

::::{grid} 2
:::{grid-item-card}
:link: XP-1_1/XP-1_1.html
:text-align: center
:columns: 4
Interactive Notebook
^^^

Data Binder Notebook

:::



:::{grid-item}
:link: XP-1_2/XP-1_2.html
:text-align: center
:columns: 8

One of the aim of my PhD is to deliver a software for scientist to "play" with the data and plot it within their browser (cf link left). But between the RAW data and the data tht would appear on your screen there is a long and tedious pathway (which you can take as well, may you wish)  

:::
::::

#### Reduction

The Reduction pipeline is made of 4 steps.

:::::{div} full-width

::::{grid} 1 1 2 4
:class-container: text-center
:gutter: 4

:::{grid-item-card}
:class-header: bg-light
:link: DR/Sample_thickness.html
**Sample Thickness** 
^^^

:::

:::{grid-item-card}
:class-header: bg-light
:link: DR/DR1.html
**DR1** 
^^^


:::
:::{grid-item-card}
:class-header: bg-light
:link: DR/DR2.html
**DR2** 
^^^

:::

:::{grid-item-card}
:class-header: bg-light
:link: DR/DR1.html
**DR3** 
^^^

:::

::::
:::::

#### Processing

Once all the samples have been reduced and are comparable, we have two more steps to increase the information we extract about our samples

::::{grid} 1 1 2 4
:class-container: text-center
:gutter: 2

:::{grid-item-card}
:class-header: bg-light
:link: Processing/Step1.html
**Substraction** 
^^^

:::

:::{grid-item-card}
:class-header: bg-light
:link: Processing/Step2.html
**Gaussian fitting** 
^^^


:::
::::


#### Analysis 

<img src="https://imgs.xkcd.com/comics/change_in_slope.png" />


The Analysis of the data is performed in a rather creative fashion. Indeed, I intend to perform the anysis by chunck of samples that relate to one another and write stories about them. I have created one page per stories those samples told me.

## Progress

```{note}

Make note of progress and **deadlines**

```

::::{grid} 2
:::{grid-item-card}
**Data** 
^^^

**Raw Data**

![flag alt >](../../Documents/SVG_icons/folder-svgrepo-com.svg) Folder Structure

**Processed Data**

![flag alt >](../../Documents/SVG_icons/folder-svgrepo-com.svg) Folder Structure


**DR1_full.csv**

- Description:
- Location:


**DR2_full.csv**

- Description:
- Location:

**DR3_full.csv**

- Description:
- Location:


**Ice_thickness.csv**
**Ice_thickness2.csv**

- Why 2 ?

**Sample_list.xlsx**

- Nicely formatted .xlsx file with sample information, ramp (isotherms ..) -> Not used during the reduction routine

**XP_list_test.csv**
  
- All the samples. **Link scan number with temperature**
- Generated manually using T_ramp

+  Samples
:::
:::{grid-item-card}
**Processing Workflow** 
^^^

**DR0 Notebook**

- Update the Temperature Ramp into Xp_list_test csv using **DR1**
- All done: &#9989;

**DR1 Notebook**

- Sanity check / merging of indivv sample scan into 1 df per sample.
- Export
    - DR1_(date)_All-scans.csv
    - DR1_(date)_data_annex.csv (intermediate data_annex)
- All done: ?

**DR1.1 Notebook**

- Create DR1_Full.csv
- to run once once DR1 performed for all samples
- Done: ?
- Data put on Figshare: ?

**DR2 Notebook** - 3 sub-notebooks

- Baseline Correction

**DR2_ASW**

**DR2_C2H6**

**DR2_ASW_C2H6**

:::
::::
