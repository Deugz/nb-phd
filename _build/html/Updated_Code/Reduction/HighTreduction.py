# -*- coding: utf-8 -*-
# # High Temperature DR3

# This sub-notebook purpose is to extract the Normalisation value at a certain Temperature (Tint) from all the samples deposited at 20K and subsequently normalise the samples deposited at this higher Temperature with that value. 

# ## Open Data annex for all 20K samples

# +
import numpy 
import math
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as mcolors
import pandas as pd
import glob
from functools import reduce
import ipywidgets as widgets
import matplotlib.gridspec as gridspec
from datetime import datetime
from IPython.core.display import SVG

import statistics

# -

# ## Sample



# ### 20K sample list

# +
XP = "XP_1-1"
spl = "ASW"

spl20K1 = ['2020_09_16','2020_09_17','2020_09_21']
spl20K2 = ['2020_09_28']
# -

# ### Data Annex

# +
for i in spl20K1:
    
    locals()['data_annex_%s' % i] = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/{}_data_annex.csv".format(XP,i,i)) 
    
for j in spl20K2:
    
    locals()['data_annex_%s' % j] = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/{}_data_annex.csv".format(XP,j,j))
# -

#data_annex_2020_09_16


# +
#data_anex_df
# -

# ## Open XP_ramp_df

# May be I don't have to do that!

XP_Ramp_df = pd.read_csv('D:\DATA-Processing\PAC\XP_list_test.csv')

# ### T dictionnary (for now)

# +
# 16-17-21 09

i = [0,1,4,7,10,13,16,19,22,25]
j = ["Dep","20","40","60","80","100","120","130","140","160"]

Td = dict(zip(j, i))

print(Td)

# +
#28 09

i = [0,1,8,16,24,32,40,52,60,79]
j = ["Dep","20","40","60","80","100","120","130","140","160"]

T2d = dict(zip(j, i))

print(T2d)
# -

# # For loop

# Here we want to extract the value for all the 20K samples ...

#  $\color{red}{\text{Need to have a function to perform median of the value in Int_value df}}$

# +
df_list = []

for i in spl20K1:
    for (k,v) in Td.items():    
        if k == Tdep:            
            sample1 = "{}_{}_{}".format(spl,i,v)
            #Extract the value in data annex column 30
            dftoplot = "data_annex_" + str(i)
            df = locals()[dftoplot]
            Int_val = df.iloc[(v-1),30]
            df_list.append(Int_val)

for j in spl20K2:
    for (k2,v2) in T2d.items():              
        if k2 == Tdep:        
            sample2 = "{}_{}_{}".format(spl,j,v2)
            dftoplot = "data_annex_" + str(j)
            df = locals()[dftoplot]
            Int_val = df.iloc[(v2-1),30]
            df_list.append(Int_val)
            dfx = df.head(10)

print(df_list)



# -

mean_X = statistics.mean(df_list)
print(mean_X)
