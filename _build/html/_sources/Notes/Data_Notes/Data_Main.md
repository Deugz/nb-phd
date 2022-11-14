# Management plan


## Samples Overview


:::::{div} full-width
<iframe class="preview-iframe" id="preview-iframe" src="../../_static/assets/Sample_list/Sample_list.html" width="100%" height="600"></iframe>
:::::


## Data

### Experimental

Data from IR spectroscopy (Absorbance - wavenumber) 
- csv files


### Pipeline

:::::{div} full-width

::::{grid} 1 1 2 4
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:class-header: bg-light
:link: Reduction/Data_Reduction.html
**Reduction** 
^^^

- DR1 Sanity chenck / Merging
- DR2 Baseline correction
- DR3 Normalisation

:::

:::{grid-item-card}
:class-header: bg-light
:link: Processing/Data_Processing_Main.html
**Processing** 
^^^
- DP1
- DP2

:::
:::{grid-item-card}
:class-header: bg-light
:link: Analysis/Data_Analysis.html
**Analysis** 
^^^

- Binder
- PCA

:::
::::
:::::






## Workflow

### Reduction

#### Steps

::::{grid} 3
:::{grid-item-card}
:class-header: bg-light
:link: Reduction/Step1.html
**DR1** 
^^^



:::
:::{grid-item-card}
:class-header: bg-light
:link: Reduction/Step2.html
**DR2** 
^^^

For each sample - All outputs generated

:::

:::{grid-item-card}
:class-header: bg-light
:link: Reduction/Step3.html
**DR3**
^^^


:::
::::

#### Overview 

```{figure} Docs/DR_workflow_02_08_21.png
---
name: MC_X
width: 1000px
---
Reduction Workflow
```

Each sample is reduced individually going through each reduction steps. Once a reduction step is achieved for all the samples, the samples are merged together to produce a **single data file, uploaded on Zenodo**.


#### Data Accessibility 

- Include figshare link

### Processing


### Analysis

#### Steps


#### Stories

I intend to perform the anysis by chunck of samples that relate to one another. I have created one page per stories those samples told me.




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
