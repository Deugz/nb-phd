# Management plan



````{margin} 

**litterature Data**

- XP 1.1


    - [Leiden Database](https://icedb.strw.leidenuniv.nl/)
2 water spectra with different thickness (4 temperatures each)


to cite: {cite}`Oberg2007`

- XP 1.2

    - Dartois

    - Nasa, hudson



````

## Data Overview


### Naming convention

#### Samples

From Omnic I obtain individual .spa scans named: 
<br><br>$\color{red}{\text{ASW_}}$_$\color{blue}{\text{2020_09_15_}}$_$\color{green}{\text{0001}}$.spa<br>

- $\color{red}{\text{Sample type}}$ : can take value : ASW, C2H6, C2H6_ASW
- $\color{blue}{\text{Sample date}}$ : format yyyy_mm_dd (is the id of every sample).
- $\color{green}{\text{Scan number}}$ : is allocate incrementaly and represent each scan.

The Data is quickly processsed using Omnic (Smoothing with a window of (15)) and finally a collection of .CSV files of shape (ASW_2020_09_15_0001_smooth.CSV, ASW_2020_09_15_0002_smooth.CSV, ...) is exported within a **dated** folder of shape
- 2020_09_15
- 2020_09_16
- ...

#### Storage

The exported data is considered Raw and the dated folder containing the data is located in a hardrive uner the location


![flag alt >](../../Documents/SVG_icons/folder-svgrepo-com.svg) 


### Data-Management Plan

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


Implement web_version of Sample_list

<iframe class="preview-iframe" id="preview-iframe" src="../../_static/assets/Sample_list/Sample_list.html" width="100%" height="400"></iframe>



### Reduction routine


## Data Handling


::::{grid} 3
:::{grid-item-card}
:link: Reduction/Data_Reduction.html
**Reduction** 
^^^

Check what samples are still to be reduced

:::
:::{grid-item-card}
:link: Processing/Data_Processing_Main.html
**Processing** 
^^^

For each sample - All outputs generated

:::

:::{grid-item-card}
:link: Analysis/Data_Analysis.html
**Analysis**
^^^

Comparison between samples

:::
::::

## Workflow

What Data, how is it processed Workflow ...

## Sample list

Create card like template of all samples, their information classified by categories.