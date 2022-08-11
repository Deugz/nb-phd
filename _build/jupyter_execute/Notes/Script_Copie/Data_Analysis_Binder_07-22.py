#!/usr/bin/env python
# coding: utf-8

# # DATA Analysis - Binder version

# Explain
# 
# 
# #### Further implementation:
# 
# - Data to be put in ordo (or Zenodo)

# #### Libraries

# In[1]:


import numpy 
import math
import matplotlib
import matplotlib.pyplot as plt
import ipympl 
from matplotlib import cm
import matplotlib.colors as mcolors
import pandas as pd
from glob import glob
from functools import reduce
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual, Layout, HBox
import re
from itertools import cycle
import zipfile  
#import wx
import gdown


# In[2]:


get_ipython().run_line_magic('matplotlib', 'widget')


# In[3]:


spl = 'ASW'


# # Data import

# 5 csv that include all the reduced data so far (31-03-2022) are imported as df :
# 
# - XP_list_test (XP_Ramp_df)
# - Data_Annex_full (Data_Annex_full_df)
# - DR1_full (DR1_full_df)
# - DR2_full (DR2_full_df)
# - DR3_full (DR3_full_df)

# ### Download  

# DR2 and DR1 are big files, hence they are stored on google drive and needs to be uploaded within the notebook.

# In[4]:


# DR2

url = "https://drive.google.com/file/d/1deWpgNp7kvvIsh056PGX9fBzADer0eYX/view?usp=sharing"
gdown.download(url=url, quiet=False, fuzzy=True)

#DR1

url = "https://drive.google.com/file/d/1zmtG61wYExabbecMznA8P5JIA7BXy49n/view?usp=sharing"
gdown.download(url=url, quiet=False, fuzzy=True)


# ### Data-frame construction

# In[5]:


# XP-Ramp

XP_Ramp_df = pd.read_csv('XP_list_test.csv')
XP_Ramp_df_I = XP_Ramp_df.set_index('Date')

#Data_Annex

Data_Annex_full_df1 = pd.read_csv('Data_Annex_full.csv')
Data_Annex_full_df = Data_Annex_full_df1.set_index('Name')
del Data_Annex_full_df['Unnamed: 0']

#DR1

DR1_full_df = pd.read_csv('DR1_full.csv')

#DR2

DR2_full_df = pd.read_csv('DR2_full.csv')

#DR3

DR3_full_df = pd.read_csv('DR3_full.csv')


# ### Sanity Check

# In[ ]:


#Data_Annex_full_df


# # Scan selection

# ## Parameter list

# In[7]:


Temp = XP_Ramp_df_I.columns[1:].values.tolist()
Date = XP_Ramp_df_I.index.values.tolist()
Sample = XP_Ramp_df_I['Sample'].values.tolist()
Reduc = ['DR2','DR3']
#Scans = ['Single','Multi']
Param = list(Data_Annex_full_df.columns.values)


# ## Widget selection

# Some stuffs

# In[8]:


#Create Dropdown Box Widget

#wR = widgets.SelectMultiple(
#    options= Reduc,
#    description='Reduction',
#    disabled=False,
#)

wT = widgets.SelectMultiple(
    options= Temp,
    description='Temperature:',
    disabled=False,
)

wD = widgets.SelectMultiple(
    options= Date,
    description='Date',
    disabled=False,
)

#wS = widgets.SelectMultiple(
#    options= Sample,
#    description='Sample',
#    disabled=False,
#)

wSc = widgets.Checkbox(
    value=False,
    description='Iso',
    disabled=False,
    indent=False
)


#widgets.HBox([wD,wT])

h1 = widgets.HBox(children=[wD,wT,wSc])


#display(wT,wD)
display(h1)


# ### Confirm 

# Click on the cell below to confirm the selected scans

# In[82]:


wT_L = list(wT.value)
wD_L = list(wD.value)
wSc_B = bool(wSc.value)


# In[83]:


wSc_B


# ## Sample name construction

# Can I create an intermediate step to select only one number from the many per temperature when I don`t want to plot the isotherms
# - create input button (boolean that allow to choose between 1 scan or isotherm)

# In[84]:


#date = ['2020_09_16','2020_09_17']
#temp = ['60K','80K']
#spl = 'ASW'

z = []
value_1 = []
value_2 = []



       



for x in wD_L:
    for y in wT_L:

        value = str(XP_Ramp_df_I.loc[XP_Ramp_df_I.index == x, y].values[0])
        print(value)
        print(type(value))
        value_1 = re.findall(r"[-+]?\d*\.\d+|\d+", value)
        print(value_1)
        
        #Isotherm (all values but first one - Warm-up scan)
        value_2 = value_1[1:]   #here we selct all but first value (warm-up)
        
        #Multiple scans (T range) - (Only the last value)
        #value_2 = value_1[-1:]  #here we selct only the last value of the list
        
        print(value_2)
        for items in value_2:
        
            to_plot = str('{}_{}_{}'.format(spl, x, items))
            z.append({
                
               'Name' : str(to_plot),
               'Temp' : y,
               'Date' : x, 
                
          
         
         })

dat= pd.DataFrame(z)
data_df = dat.set_index('Name')
            


# ## Plot pre-formating

# ### Temperature

# In[85]:


def Temp_color(row):
    if row['Temp'] == '20':
        return int(1)
    elif row['Temp'] == '30':
        return int(2) 
    elif row['Temp'] == '40':
        return int(3)
    elif row['Temp'] == '50':
        return int(4)
    elif row['Temp'] == '60':
        return int(5)
    elif row['Temp'] == '70':
        return int(6)
    elif row['Temp'] == '80':
        return int(7)
    elif row['Temp'] == '90':
        return int(8)
    elif row['Temp'] == '100':
        return int(9)
    elif row['Temp'] == '110':
        return int(10)
    elif row['Temp'] == '120':
        return int(11)
    elif row['Temp'] == '125':
        return int(12)
    elif row['Temp'] == '130':
        return int(13)
    elif row['Temp'] == '132':
        return int(14)
    elif row['Temp'] == '134':
        return int(15)
    elif row['Temp'] == '135':
        return int(16)
    elif row['Temp'] == '136':
        return int(17)
    elif row['Temp'] == '137':
        return int(18)
    elif row['Temp'] == '138':
        return int(19)
    elif row['Temp'] == '140':
        return int(20)
    elif row['Temp'] == '145':
        return int(21)
    elif row['Temp'] == '150':
        return int(21)
    elif row['Temp'] == '155':
        return int(22)
    elif row['Temp'] == '160':
        return int(23)
    elif row['Temp'] == '180':
        return int(24)
    elif row['Temp'] == '200':
        return int(25)


# In[86]:


data_df['Colour'] = data_df.apply (lambda row: Temp_color(row), axis=1)


# ### Linestyle (date)

# In[87]:


linestyle = ['-',':','--','-.']


# In[88]:


LD = dict(zip(wD_L, linestyle))

data_df['linestyle'] = data_df['Date'].map(LD)


# In[89]:


LD


# ### Sanity Check

# In[90]:


data_df


# # Plotting

# ## Scans

# ### DR3

# In[91]:


nscan = len(list(data_df['Date'].values.tolist()))

print(nscan)

fig, ax= plt.subplots(figsize=(12,10))

normalize = mcolors.Normalize(vmin=20, vmax=200)
colormap = cm.jet

for i in dat['Name']:
    
#`DR3

    x = DR3_full_df.Wavenumber
    y = DR3_full_df['{}'.format(i)]
    
    plt.plot(x,y, label="{}_{}".format(str(data_df.loc[i]['Date']), str(data_df.loc[i]['Temp'])), color=colormap(normalize(int(data_df.loc[i]['Temp']))), linestyle=(data_df.loc[i]['linestyle'])) 


plt.title('DR3 ')
plt.axis([3800,2800,0,0.45])
plt.xlabel('Wavenumber (cm-1)').set_fontsize(13)
plt.ylabel('Absorbance').set_fontsize(13)
#ax = fig.gca()
plt.grid()
plt.legend()

scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nscan)
plt.colorbar(scalarmappaple)


#plt.savefig('D:\PhD-WS\Projects\PAC\XP_1-1\DATA\{0}\Plots\DR1\DR1_{0}_All_scans.png'.format(date))

plt.show()


# ### DR2

# In[67]:


nscan = len(list(data_df['Date'].values.tolist()))

print(nscan)

fig, ax= plt.subplots(figsize=(10,10))

normalize = mcolors.Normalize(vmin=20, vmax=200)
colormap = cm.jet

for i in dat['Name']:
    

    x = DR2_full_df.Wavenumber
    y = DR2_full_df['{}'.format(i)]
    
    plt.plot(x,y, label="{}_{}".format(str(data_df.loc[i]['Date']), str(data_df.loc[i]['Temp'])), color=colormap(normalize(int(data_df.loc[i]['Temp']))), linestyle=(data_df.loc[i]['linestyle'])) 


plt.title('DR2')
plt.axis([3800,2800,0,0.60])
plt.xlabel('Wavenumber (cm-1)').set_fontsize(13)
plt.ylabel('Absorbance').set_fontsize(13)
#ax = fig.gca()
plt.grid()
plt.legend()

scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nscan)
plt.colorbar(scalarmappaple)


#plt.savefig('D:\PhD-WS\Projects\PAC\XP_1-1\DATA\{0}\Plots\DR1\DR1_{0}_All_scans.png'.format(date))

plt.show()


# ### DR1

# Why:
# - Compare the DR2 and DR1 to see if the difference observed arise from the reduction process.

# In[56]:


nscan = len(list(data_df['Date'].values.tolist()))

print(nscan)

fig, ax= plt.subplots(figsize=(10,10))

normalize = mcolors.Normalize(vmin=20, vmax=200)
colormap = cm.jet

for i in dat['Name']:
    

    x = DR1_full_df.Wavenumber
    y = DR1_full_df['{}'.format(i)]
    
    plt.plot(x,y, label="{}_{}".format(str(data_df.loc[i]['Date']), str(data_df.loc[i]['Temp'])), color=colormap(normalize(int(data_df.loc[i]['Temp']))), linestyle=(data_df.loc[i]['linestyle'])) 


plt.title('DR1')
plt.axis([3800,2800,-0.2,0.6])
plt.xlabel('Wavenumber (cm-1)').set_fontsize(13)
plt.ylabel('Absorbance').set_fontsize(13)
#ax = fig.gca()
plt.grid()
plt.legend()

scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nscan)
plt.colorbar(scalarmappaple)


#plt.savefig('D:\PhD-WS\Projects\PAC\XP_1-1\DATA\{0}\Plots\DR1\DR1_{0}_All_scans.png'.format(date))

plt.show()


# ## Data Annex

# ## Plotting

# Use interact to play with the data I plot

# In[43]:


wP = widgets.SelectMultiple(
    options= Param,
    description='Parameters',
    disabled=False,
)

display(wP)


# In[97]:


wP_L = list(wP.value)


# In[98]:


# Widget selection



#interact(wP = widgets.SelectMultiple(
#    options= Param,
#    description='Parameters',
#    disabled=False,
#));




# Figure

fig, ax= plt.subplots(figsize=(10,10))

normalize = mcolors.Normalize(vmin=20, vmax=200)
colormap = cm.jet

for i in dat['Name']:
    for j in wP_L:

    #print(i)
    #print(j)
        
        x = Data_Annex_full_df[('{}'.format(j))].loc[('{}'.format(i))]
        #y = Data_Annex_full_df['{}'.format(j)]
        #y = Data_Annex_full_df['{}'.format(j)].loc[Data_Annex_full_df.index == ('{}'.format(i))]
        #y = Data_Annex_full_df.loc[(Data_Annex_full_df['{}'.format(j)])] & [(Data_Annex_full_df['column_name'] == x)]
        #print(x,y)
        #print(i)    
        #print(x)
    
        

        plt.plot(i,x, '+', mew=2, ms=8, color=colormap(normalize(int(data_df.loc[i]['Temp']))) )

plt.title('Data Annex')
#plt.axis([3800,2800,0,0.45])
# Set number of ticks for x-axis

# Set ticks labels for x-axis

#plt.xlabel('Wavenumber (cm-1)').set_fontsize(13)

#plt.ylabel('Absorbance').set_fontsize(13)
plt.xticks(rotation=90)
#plt.tight_layout()
ax = fig.gca()
#plt.grid()
#plt.legend()

scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nscan)
plt.colorbar(scalarmappaple)


#plt.savefig('D:\PhD-WS\Projects\PAC\XP_1-1\DATA\{0}\Plots\DR1\DR1_{0}_All_scans.png'.format(date))

plt.show()


# ## More

#  - fit linear model to desorption great
