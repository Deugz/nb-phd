# Step 1 

***
<p class="emphase">Sanity Check Merging</p>
***




## Overview

Same for all samples, 2 notebooks
- DR1
- DR1.1 (merge all the individual sample together for ease of opening later).

## DR1

First, I create a `file_path` that is the folder location of the Raw (smoothed) scans. 

Then, I created a <strong>for loop</strong>:
    
```python
for file in glob.glob(file_path):    
```

That do (for each scans) the following actions:    

- Read the data file (csv) and create a `data-frame`
```python
df = pd.read_csv(file, names=["Wavenumber", str(spl)+"_"+str(date)+"_"+str(file_number)])
```
- Append the df into a previously created empty list, <strong>All_data_frame</strong> 
```python
All_data_frame.append(df)
```
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

