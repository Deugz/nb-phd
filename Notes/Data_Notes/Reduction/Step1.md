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
