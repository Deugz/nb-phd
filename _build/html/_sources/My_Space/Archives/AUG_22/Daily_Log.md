# Daily Log

## 18/08/2022

Run DR1.1 Notebook to produce **DR1_full.csv**

```{warning}

Problem with the 2021_10_28 sample (ethane+ASW - electron irradiation) --> (not included in DR1_full, named change to DR1_2021_10_28_All-scansX.csv (so not picked up by glob function))

```

## 18/08/2022

- Corrected the file 141 (2021_10_18) and run DR1
- Check the file name for remaining ethane sample when spl mistake
Rerunned:
- 2021_01_29
- 2021_02_24
- 2021_03_08
- 2021_03_24
- 2021_07_16
- 2021_08_16
- 2021_09_20
- 2021_09_23
- 2021_09_27
- 2021_10_04
- 2021_10_07
- 2021_10_11

OK, DR1 routine has now been performed for all samples.



## 17/08/2022

```{note}

- Downloaded H2O ice spectra from [Leiden Ice Database](https://icedb.strw.leidenuniv.nl/)


- Finish splitting DR1 (Sanity Check_Merging)

**XP-1_2**

- &#9989; 2020_12_03
- &#9989; 2021_01_29
- &#9989; 2021_02_24
- &#9989; 2021_03_08 - CO2 contamination at some point - supress some scans ?
- &#9989; 2021_03_24
- &#9989; 2021_07_16 - CO2 contamination
- &#9989; 2021_08_16
- &#9989; 2021_09_15
- &#9989; 2021_09_18 - good ethane only sample
- &#9989; 2021_09_19
- &#9989; 2021_09_20
- &#9989; 2021_09_23
- &#9989; 2021_09_27
- &#9989; 2021_10_04
- &#9989; 2021_10_07
- &#9989; 2021_10_11
- &#x274C; 2021_10_18 - Problem in reduction routine at scan 141 - **Redo OMNIC smooth**
- &#9989; 2021_10_22 - no ethane
- &#9989; 2021_10_24 - Good for ethane band shifting in progress !!
- &#9989; 2021_10_28


- generate DR1_full and put on figshare ?

- Start splitting DR2
    - Create 3 subnotbooks: ASW, C2H6, ASW_c2h6

- Find Dartois ethane article and check for BC procedure

```

```{warning}

Forgot to swith between C2H6 and C2H6_ASW 
- Some samples name may be wrong
```

problem w/ scan 141 for sample 2021_10_18 


### Ethane Reduction

```{note}
Was wondering if it worth taking notes of ethane range within data_annex at the DR1 stage

```

Sample comparison to check consistency of ethane peak



````{panels}

2020_12_03
^^^^^^^^^^^^^^

```{figure} Data_Notes/XP-1_2/2020_12_03/Plots/DR/DR1_2020_12_03_Ethane-range.png
:width: 800px
2020/12/03 DR1 Ethane range
```

---

2021_01_29
^^^^^^^^^^^^^^

```{figure} Data_Notes/XP-1_2/2021_01_29/Plots/DR/DR1_2021_01_29_Ethane-range.png
:width: 800px
2021_01_29 DR1 Ethane range
```

````


Lines are located at:

- 3025 (3000 may be better option)
- 2963
- 2950
- 2893
- 2870

Looks like water + ethane shifts ethane peaks

**No need to modify DR1 at this point**

- Same reduction for all samples! we will check in DR2 to check for max peak absorbance etc.

## 16/08/2022

```{note}


- Finish splitting DR1 (Sanity Check_Merging)

     - What are the samples in DR1_full ?
        - 2021_07_13
        - 2021_05_24
        - 2021_05_13
        - 2020_11_23 (40K dep)
        - 2020_11_19
        - 2020_11_16
        - 2020_10_22
        - 2020_10_14
        - 2020_09_28
        - 2020_09_21
        - 2020_09_17
        - 2020_09_16
        - 2020_09_15
    - All 20K Samples ? (missing 2021_05_08, 2021_02_09)

    - perform for remaining samples (including ethane)
    
They will have a different reduction routine (ie, one data_annex file will be generated after each DR steps)

**XP-1_1**

- &#9989; 2020_09_24
- &#9989; 2020_10_15
- &#9989; 2020_10_30 - lots of different baseline !
- &#9989; 2020_11_26 - Leak valve open (really) - Interesting sample :)
- &#9989; 2021_01_21 - 2 scans only
- &#9989; 2021_01_25
- &#9989; 2021_02_09 - Super interesting sample (lots of things to do in processing phase - create specific Notebook and be creative)
- &#9989; 2021_04_26 
- &#9989; 2021_05_08 - DODGY BASELINE - could be good to test different DR2 routines

**XP-1_2**


- generate DR1_full and put on figshare ?

- Start splitting DR2
    - Create 3 subnotbooks: ASW, C2H6, ASW_c2h6

- Find Dartois ethane article and check for BC procedure

```

### DR1_full.csv ?

Created DR1.1 subnotebook to produce it once all the samples have been reduced

- Figshare implementation (is it the best ?)


## 15/08/2022

```{note}

- &#9989; Create one specific Notebook for T_Ramp -> XP_list_test implementation - **DR0**
    - What are the samples missing in XP_list_test ?
    - &#9989; XP_1-1
        - &#9989; 2020_09_24
        - &#9989; 2020_10_15
        - &#9989; 2020_10_30
        - &#9989; 2020_11_23 - first scan 30K - WRONG deposition is 40K - CORRECT !!!
        - &#9989; 2020_11_26
        - 2021_01_21 - null-sample
        - &#9989; 2021_01_25
        - &#9989; 2021_02_09
        - &#9989; 2021_04_26
        - &#9989; 2020_05_08
    - &#9989; XP_1-2
        - &#9989; 2021_07_16
        - &#9989; 2021_08_16
        - &#9989; 2021_10_18


```



## 08/08/2022

```{note}
- &#9989; Finish Book Skeleton
    - Delete Thesis book structure and implement chapters section
- Finish Implementing sample list in **Data Processing** (split into ASW - Ethane - Mixture)
- Split Data_Reduction Notebook into 3 Notebooks (DR1, DR2, DR3)
    - Easier to work with

```


## Week 1

**Plan**

```{warning}

**Book**

- Finish Book Skeleton
- Implement nb extensions:
    - Ortograph corrector
    - Rise presentation
- Finish implementing all samples into XP-1_1 and XP-1_2
- Put first version online

**Data Reduction**

- Split Data_Reduction_full Notebook into 3 smaller ones
    - DR1
    - DR2
    - DR3
- Create sub-notebooks for specific samples
    - Higher T samples
    - Ethane samples
    
**Litterature Review**

- Put in place the right structure for the .bib files
- Read and implement *Ice structures, patterns, and processes: A view across the ice fields*
    

```




## 04/08/2022

```{note}
- &#9989; Finish Book Skeleton
    - Delete Thesis book structure and implement chapters section
- Finish Implementing sample list in **Data Processing** (split into ASW - Ethane - Mixture)
- Split Data_Reduction Notebook into 3 Notebooks (DR1, DR2, DR3)
    - Easier to work with

```


## 03/08/2022

### Meeting w/ Anita

- Review together Gant chart (make upward Link)

    - Submission 

    - Drafts ?

**Realistic Aims**

- Data Analysis full time until mid October.

- Correct Chapter 5 and 6 until end November - hand for Supervision comments

- December January Draft Chapter 1 + Method section - hand for supervision comments

- Febraury - April : Write chapter 2,3,4 - hand for supervision comments

- Submission - End of May

- Monthly plan

    - Use Data_Binder Notebook () to compare, classify and ** clean ? ** the different samples
    
    - Data_Processing Notebook (improve along the way) to Compare the samples 
        - Could host cleaning (declutter) routine

    - Generate some Results to present at Astra conference

- Holliday (mid September)
- Keep working on Jim project for rest of the week 
    - (Example?)


## Preliminary work


- Read the different Notebooks and critisize
- Implement notes by modifying the Copied version


- 
