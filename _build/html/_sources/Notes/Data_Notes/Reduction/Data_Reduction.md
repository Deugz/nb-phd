# Reduction

## Reduction pipeline

***
**3 steps**:
- DR1
- DR2
- DR3
***

<h3><strong>&#187;  <u>STEP 1: Sanity Check, Merging</u></strong></h3>

<h4><strong>DR1 </strong></h4>

````{margin} 
**Outputs**

- DR1_Date
- Date_data Annex

````

<article id="P1">

<div id="subdiv1-3">    
    
:::{grid-item-card}
:link: Step1.html
**DR1 Notebook**
^^^
**Sanity Check Merging**

2 Notebooks
- DR1
- DR1.1
:::


</div>
    
<div id="subdiv2-3"> 

This reduction step is done **per sample** 
    
</div>
    
</article>

<h4><strong>DR1.1  </strong></h4>

<article id="P1">

<div id="subdiv1-3">    
    
:::{grid-item-card}
:link: Step1.html
**DR1.1 Notebook**
^^^
**Sanity Check Merging**

2 Notebooks
- DR1
- DR1.1
:::


</div>
    
<div id="subdiv2-3"> 
    
- **Explanation**
    
Merge all the sample together into one big dataframe
    
</div>
    
</article>


<h3><strong>&#187;  <u>STEP 2: Baseline Correction</u></strong></h3>

<h4><strong>DR2  </strong></h4>

:::::{div} full-width

::::{grid} 3
:::{grid-item-card}
:link: Step1.html
**DR2_ASW**
^^^

range:
- 1
- 2
- 3

:::

:::{grid-item-card}
:link: Step2.html
**DR2_C2H6**
^^^

different range for ethane ?

:::

:::{grid-item-card}
:link: Step3.html
**DR2_C2H6_ASW**
^^^

- first baseline correct ASW 
- then substract for ethane ?
:::
::::
:::::

```{warning}

During the baseline correction reduction step, we extract the max absorbance and the associated wavenumber position. those would be different for the different sample (more max A peaks to extract for ethane) leading to different **data_annex** files. 

- Would that create problems

```

<h4><strong>DR2.1  </strong></h4>

Similar to DR_1.1, once all the samples have been reduced, they all be grabbed and put into a single dataframe and then exported as a csv

<h3><strong>&#187;  <u>STEP 3: Integration / Normalisation</u></strong></h3>

<h4><strong>DR3 </strong></h4>

````{margin} 
**Outputs**

- DR1_Date
- Date_data Annex

````

<article id="P1">

<div id="subdiv1-3">    
    
:::{grid-item-card}
:link: Step1.html
**DR3 Notebook**
^^^
**Integration Normalisation**

:::


</div>
    
<div id="subdiv2-3"> 

This reduction step is done **per sample** 

```{note}
    
- Compare the sample thickness w/ Integration value for all samples
    - Does they match ?
    
```
    
</div>
    
</article>

# Reduction Table

## XP 1_1

|    Samples        |   Page                                    |    Tdep        |    Isotherm  |   DR1          |   DR2          |  DR3          |
| :---------------- | :---------------------------------------  | :------------  | :------------  | -------------: | -------------: |-------------: |
| **2020_09_15**    | [Page](../XP-1_1/2020_09_15/2020_09_15)   | 20           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_09_16**    | [Page](../XP-1_1/2020_09_16/2020_09_16)   | 20           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_09_17**    | [Page](../XP-1_1/2020_09_17/2020_09_17)   | 20           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_09_21**    | [Page](../XP-1_1/2020_09_21/2020_09_21)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_09_24**    | [Page](../XP-1_1/2020_09_24/2020_09_24)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_09_28**    | [Page](../XP-1_1/2020_09_28/2020_09_28)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_10_14**    | [Page](../XP-1_1/2020_10_14/2020_10_14)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_10_15**    | [Page](../XP-1_1/2020_10_15/2020_10_15)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_10_22**    | [Page](../XP-1_1/2020_10_22/2020_10_22)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_10_30**    | [Page](../XP-1_1/2020_10_30/2020_10_30)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_11_16**    | [Page](../XP-1_1/2020_11_16/2020_11_16)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_11_19**    | [Page](../XP-1_1/2020_11_19/2020_11_19)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_11_23**    | [Page](../XP-1_1/2020_11_23/2020_11_23)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_11_26**    | [Page](../XP-1_1/2020_11_26/2020_11_26)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_11_30**    | [Page](../XP-1_1/2020_11_30/2020_11_30)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_01_21**    | [Page](../XP-1_1/2021_01_21/2021_01_21)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_01_25**    | [Page](../XP-1_1/2021_01_25/2021_01_25)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_02_09**    | [Page](../XP-1_1/2021_02_09/2021_02_09)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_04_26**    | [Page](../XP-1_1/2021_04_26/2021_04_26)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_05_13**    | [Page](../XP-1_1/2021_05_13/2021_05_13)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_05_24**    | [Page](../XP-1_1/2021_05_24/2021_05_24)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |
| **2020_07_13**    | [Page](../XP-1_1/2021_07_13/2021_07_13)   | Info           | Info           |  &#9989;       |   &#x274C;     |   &#x274C;    |



## XP 1_2