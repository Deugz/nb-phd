#!/usr/bin/env python
# coding: utf-8

# # DATA Processing

# The purpose of this Notebook is to perform the data processing steps for each sample:
# 
# - DP1 : Substraction
# - DP2 : Gaussian fitting
# 
# One aim is to make this Notebook working within an html page and interactive using ipython widget

# ## Workflow

# In[1]:


#


# To create (drag and drop image when produced)

# ### Libraries

# In[1]:


import numpy 
import math
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
from glob import glob
from functools import reduce
import ipywidgets as widgets
import matplotlib.gridspec as gridspec
from ipywidgets import interact
import re
from cycler import cycler
import seaborn as sns
import matplotlib.gridspec as gridspec
import pylab

from lmfit.models import ExponentialModel, GaussianModel


# In[2]:


get_ipython().run_line_magic('matplotlib', '')


# # 0 Input parameters

# Not use (but here just in case)
# 
# Take time to describe method used with respect to previous Notebook (Improvement - Emphase on python teaching)

# ## Sample  type

# In[3]:


# 0.1 Date

date = "2020_09_16"

# 0.2 XP
    # Can take value XP_1-1, XP_1-2 

XP = "XP_1-1"

# 0.3 Sample type
    # Can take value ASW, C2H6, C2H6_ASW

spl = "ASW"


# ## Sample annex 

# For quick sample comparison (max 3 sample named 2-3-4)

# In[4]:


date2 = "2020_09_28"
date3 = "2020_09_17"
date4 = "2020_09_21"


# # <span style='background :yellow' > $\color{green}{\text{DP1 : Sample Checking}}$ </span>

# # 1.1 DATA Import

# The Data processing routine is performed per sample. 
# 
# A date is set as input
# 
# from the previous data analysis, summarized in the following document below, we have identified 4 temeperature ranges where the sample undergo different physical processes.
# 
# [XP1_Plan](D:\PhD-WS\Projects\PAC\Document\Reports\XP1_Plan.docx)
# 
# So the purpose here is to chop the data with respect to those ranges before to perform the Substraction
# 
# Experimental ranges (in T):
# 
# - Range 1: 20 - 100K
# - Range 2: 100 to 130K
# - Range 3: 130K - 140K
# - Range 4: Beyond 140K
# 
# 
# I want to extract the temperature ramp info from XP Ramp:
# 

# ## 1.1.1 XP-Ramp

# In[5]:


XP_Ramp_df = pd.read_csv('D:\DATA-Processing\PAC\XP_list_test.csv')
XP_Ramp_df_I = XP_Ramp_df.set_index('Date')


# In[6]:


#XP_Ramp_df_I.head(5)


# ## 1.1.2 DR1, DR2, DR3

# ###  DR1 (Date)

# In[7]:


DR1_Allscan_df = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR1_{}_All-scans.csv".format(XP,date,date))
DR1_Allscan_df = DR1_Allscan_df.T.iloc[1:].T


# In[8]:


#DR1_Allscan_df


# ###  DR1 (Date Annex)

# In[9]:


DR1_Allscan_df_2 = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR1_{}_All-scans.csv".format(XP,date2,date2))
DR1_Allscan_df_3 = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR1_{}_All-scans.csv".format(XP,date3,date3))
DR1_Allscan_df_4 = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR1_{}_All-scans.csv".format(XP,date4,date4))


DR1_Allscan_df_2 = DR1_Allscan_df_2.T.iloc[1:].T
DR1_Allscan_df_3 = DR1_Allscan_df_3.T.iloc[1:].T
DR1_Allscan_df_4 = DR1_Allscan_df_4.T.iloc[1:].T


# In[10]:


#DR1_Allscan_df_2


# ###  DR2 (Date)

# In[11]:


DR2_Allscan_df = pd.read_csv('D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR2_{}_All-scans.csv'.format(XP, date, date))
DR2_Allscan_df = DR2_Allscan_df.T.iloc[1:].T


# In[12]:


#DR2_Allscan_df


# ###  DR2 (Date Annex)

# In[13]:


DR2_Allscan_df_2 = pd.read_csv('D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR2_{}_All-scans.csv'.format(XP, date2, date2))
DR2_Allscan_df_3 = pd.read_csv('D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR2_{}_All-scans.csv'.format(XP, date3, date3))
DR2_Allscan_df_4 = pd.read_csv('D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR2_{}_All-scans.csv'.format(XP, date4, date4))

DR2_Allscan_df_2 = DR2_Allscan_df_2.T.iloc[1:].T
DR2_Allscan_df_3 = DR2_Allscan_df_3.T.iloc[1:].T
DR2_Allscan_df_4 = DR2_Allscan_df_4.T.iloc[1:].T


# In[14]:


#DR2_Allscan_df_2


# ###  DR3 (Date)

# In[15]:


DR3_Allscan_df = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR3_{}_A.csv".format(XP,date,date))
DR3_Allscan_df = DR3_Allscan_df.T.iloc[1:].T


# In[16]:


#DR3_Allscan_df


# ###  DR3 (Date Annex)

# In[17]:


DR3_Allscan_df_2 = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR3_{}_A.csv".format(XP,date2,date2))
DR3_Allscan_df_3 = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR3_{}_A.csv".format(XP,date3,date3))
DR3_Allscan_df_4 = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR3_{}_A.csv".format(XP,date4,date4))

DR3_Allscan_df_2 = DR3_Allscan_df_2.T.iloc[1:].T
DR3_Allscan_df_3 = DR3_Allscan_df_3.T.iloc[1:].T
DR3_Allscan_df_4 = DR3_Allscan_df_4.T.iloc[1:].T


# ## 1.3 Data_annex

# ### 1.2.1 Import

# In[23]:


#Date

data_anex_df = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/{}_data_annex.csv".format(XP,date,date))

#Date Annex

data_anex_df_2 = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/{}_data_annex.csv".format(XP,date2,date2))
data_anex_df_3 = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/{}_data_annex.csv".format(XP,date3,date3))
data_anex_df_4 = pd.read_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/{}_data_annex.csv".format(XP,date4,date4))


# In[24]:


data_anex_df


# In[25]:


#data_anex_df = data_anex_df.T.iloc[1:].T
#data_anex_df_2 = data_anex_df_2.T.iloc[1:].T
#data_anex_df_3 = data_anex_df_3.T.iloc[1:].T
#data_anex_df_4 = data_anex_df_4.T.iloc[1:].T


# In[26]:


data_anex_df_2


# Purpose of this section is to perform a deep analysis of the sample with respect to the temperature ramp as for example,
# - plots various scans at different temperature, identify various range of interest.
# - perform linear regression of desorption data
# - average scans when isotherm ?

# # 1.2 DATA Cleaning

# ## 1.2.1 Annealing scan supression and averaging of the isotherms ?

# In[ ]:





# ## 1.2.2 Error Analysis

# After having avaeraged the scan previously, the purpose of this section is to identify the potential sources of errors and to generate error bars for the data accordingly

# In[ ]:





# # 1.2 DATA Compare

# ## 1.2.1 MaxA

# ### Prepare two dictionnaries

# #### Dict 1

# 16-09

# In[29]:



i = [0,1,4,7,10,13,16,19,22,25]
j = ["Dep","20","40","60","80","100","120","130","140","160"]

Td = dict(zip(j, i))

nscanTd = len(list(data_anex_df.index.values.tolist()))

print(nscanTd)
print(Td)


# #### Dict 2

# 28-09

# In[30]:


i = [0,1,8,16,24,32,40,52,60,79]
j = ["Dep","20","40","60","80","100","120","130","140","160"]

T2d = dict(zip(j, i))

nscanT2d = len(list(data_anex_df_2.index.values.tolist()))

print(nscanT2d)
print(T2d)


# ### Plot

# #### Peak frequency shift

# In[33]:


fig= plt.figure(figsize=(10,8))

for (k,v), (k2,v2) in zip(Td.items(), T2d.items()):

    spl1, = plt.plot(k, data_anex_df.iloc[v,17], '+', mew=3, ms=12, c=cm.jet(v/nscanTd), label= "16_09")
    spl2, = plt.plot(k2, data_anex_df_2.iloc[v2,17], 'o', mew=3, ms=10, c=cm.jet(v2/nscanT2d), label= "28_09")
    spl3, = plt.plot(k, data_anex_df_3.iloc[v,17], '.', mew=3, ms=12, c=cm.jet(v/nscanTd), label= "17_09")
    spl4, = plt.plot(k, data_anex_df_4.iloc[v,17], '*', mew=3, ms=12, c=cm.jet(v/nscanTd), label= "21_09")
    
plt.title('DR2 OH stretch Peak frequency (sample comparison)')
#plt.axis([3210,3270])
plt.xlabel('Temperature (K)').set_fontsize(13)
plt.ylabel('Peak frequency (cm-1)').set_fontsize(13)
#ax = fig.gca()
#plt.grid()
#plt.legend()
plt.legend([spl1, spl2, spl3, spl4], ["16_09", "28_09", "17_09", "21_09"],bbox_to_anchor =(1.25, 1),)

#plt.savefig('D:\DATA-Processing\PAC\{}/Compare/DR2_{}_{}_PeakA-frequency.png'.format(XP, date, date2))

plt.show()


# #### Integration from normalized data

# In[38]:


fig= plt.figure(figsize=(10,8))

for (k,v), (k2,v2) in zip(Td.items(), T2d.items()):

    spl1, = plt.plot(k, data_anex_df.iloc[v,30], '+', mew=3, ms=12, c=cm.jet(v/nscanTd), label= "16_09")
    spl2, = plt.plot(k2, data_anex_df_2.iloc[v2,30], 'o', mew=3, ms=10, c=cm.jet(v2/nscanT2d), label= "28_09")
    spl3, = plt.plot(k, data_anex_df_3.iloc[v,30], '.', mew=3, ms=12, c=cm.jet(v/nscanTd), label= "17_09")
    spl4, = plt.plot(k, data_anex_df_4.iloc[v,30], '*', mew=3, ms=12, c=cm.jet(v/nscanTd), label= "21_09")
    
plt.title('DR2 OH stretch Integration value (sample comparison)')
#plt.axis([3210,3270])
plt.xlabel('Temperature (K)').set_fontsize(13)
plt.ylabel('Integration (AU)').set_fontsize(13)
#ax = fig.gca()
#plt.grid()
#plt.legend()
plt.legend([spl1, spl2, spl3, spl4], ["16_09", "28_09", "17_09", "21_09"])

#plt.savefig('D:\DATA-Processing\PAC\{}/Compare/DR2_{}_{}_PeakA-frequency.png'.format(XP, date, date2))

plt.show()


# # 1.3 Data chopping

# ## 1.3.1 Temperature list splitting

# In[14]:


Temp = XP_Ramp_df_I.columns[1:].values.tolist()


# In[15]:


Temp


# iterate through temp and recover scan number value for T in range 1,2,3,4

# In[16]:


T1 = Temp[0:9]
T2 = Temp[8:13]
T3 = Temp[12:20]
T4 = Temp[19:26]


# ### Sanity Check

# In[17]:


T2


# ## 1.1.3 List of sample names per range

# ### Range 1

# In[18]:


z = []
value_1 = []
file_number1 = []

for y in T1:

    value = XP_Ramp_df_I.loc[XP_Ramp_df_I.index == date, y].values[0]
    if pd.notnull(value):
        
        value_1 = re.findall(r"[-+]?\d*\.\d+|\d+", value)
    
        for items in value_1:
        
            to_plot = str('{}_{}_{}'.format(spl, date, items))
            z.append({
                
            'Name' : str(to_plot),
            'Temp' : y,
            'Date': date,
         
            })
            
            file_number1.append(int(items))

dat1= pd.DataFrame(z)
R1_df = dat1.set_index('Name')


# In[19]:


z


# In[20]:


R1_df


# ### Range 2

# In[21]:


z = []
value_1 = []
file_number2 = []

for y in T2:

    value = XP_Ramp_df_I.loc[XP_Ramp_df_I.index == date, y].values[0]
    if pd.notnull(value):
        
        value_1 = re.findall(r"[-+]?\d*\.\d+|\d+", value)
    
        for items in value_1:
        
            to_plot = str('{}_{}_{}'.format(spl, date, items))
            z.append({
                
            'Name' : str(to_plot),
            'Temp' : y,
            'Date': date,
         
            })
            
            file_number2.append(int(items))

dat2= pd.DataFrame(z)
R2_df = dat2.set_index('Name')


# In[ ]:


R2_df


# ### Range 3

# In[22]:


z = []
value_1 = []
file_number3 = []

for y in T3:

    value = XP_Ramp_df_I.loc[XP_Ramp_df_I.index == date, y].values[0]
    if pd.notnull(value):
        
        value_1 = re.findall(r"[-+]?\d*\.\d+|\d+", value)
    
        for items in value_1:
        
            to_plot = str('{}_{}_{}'.format(spl, date, items))
            z.append({
                
            'Name' : str(to_plot),
            'Temp' : y,
            'Date': date,
         
            })
            
            file_number3.append(int(items))

dat3= pd.DataFrame(z)
R3_df = dat3.set_index('Name')


# In[23]:


R3_df


# ### Range 4

# In[24]:


z = []
value_1 = []
file_number4 = []

for y in T4:

    value = XP_Ramp_df_I.loc[XP_Ramp_df_I.index == date, y].values[0]
    if pd.notnull(value):
        
        value_1 = re.findall(r"[-+]?\d*\.\d+|\d+", value)
    
        for items in value_1:
        
            to_plot = str('{}_{}_{}'.format(spl, date, items))
            z.append({
                
            'Name' : str(to_plot),
            'Temp' : y,
            'Date': date,
         
            })
            
            file_number4.append(int(items))

dat4= pd.DataFrame(z)
R4_df = dat4.set_index('Name')


# In[25]:


R4_df


# # 1.4 Plotting

# Plot 4 subplot in square formating for all 4 T range

# ## 1.4.1 T ranges

# ## Gridspec

# In[26]:


gs = gridspec.GridSpec(16, 16,hspace=0.8,wspace=0.5)

fig = plt.figure(figsize=(16,16))

fig.suptitle('20K 10-7 All samples')

ax1 = fig.add_subplot(gs[0:8, 0:8]) # row 0, col 0

nscan = len(list(R1_df['Date'].values.tolist()))


j = 1
for i, j in zip(dat1['Name'], range(1,nscan)):   
#    for iscan in range(1,nscan):
#DR2

    #x = DR2_Allscans_full.Wavenumber
    #y = DR2_Allscans_full['{}'.format(i)]

    x = DR3_Allscan_df.Wavenumber
    y = DR3_Allscan_df['{}'.format(i)]
    
    plt.plot(x,y, label="{}_{}".format(str(R1_df.loc[i]['Date']), str(R1_df.loc[i]['Temp'])), c=cm.jet(j/nscan)) 
    
    j=+1
ax1.set_title('Full range')
ax1.axis([4000, 2800, 0, 0.5])

plt.legend()

ax2 = fig.add_subplot(gs[0:8, 8:16]) # row 0, col 0
nscan = len(list(R2_df['Date'].values.tolist()))


j = 1
for i, j in zip(dat2['Name'], range(1,nscan)):   
#    for iscan in range(1,nscan):
#DR2

    #x = DR2_Allscans_full.Wavenumber
    #y = DR2_Allscans_full['{}'.format(i)]

    x = DR3_Allscan_df.Wavenumber
    y = DR3_Allscan_df['{}'.format(i)]
    
    plt.plot(x,y, label="{}_{}".format(str(R2_df.loc[i]['Date']), str(R2_df.loc[i]['Temp'])), c=cm.jet(j/nscan)) 
    
    j=+1
ax2.set_title('Normalized zoom')
ax2.margins(2, 2)     
ax2.axis([4000, 2800, 0, 0.5])

plt.legend()

ax3 = fig.add_subplot(gs[8:16, 0:8]) # row 0, col 0  

nscan = len(list(R3_df['Date'].values.tolist()))


j = 1
for i, j in zip(dat3['Name'], range(1,nscan)):   
#    for iscan in range(1,nscan):
#DR2

    #x = DR2_Allscans_full.Wavenumber
    #y = DR2_Allscans_full['{}'.format(i)]

    x = DR3_Allscan_df.Wavenumber
    y = DR3_Allscan_df['{}'.format(i)]
    
    plt.plot(x,y, label="{}_{}".format(str(R3_df.loc[i]['Date']), str(R3_df.loc[i]['Temp'])), c=cm.jet(j/nscan)) 
    
    j=+1

ax3.set_title('BC zoomed')
ax3.axis([4000, 2800, 0, 0.5])

plt.legend()

ax4 = fig.add_subplot(gs[8:16, 8:16]) # row 0, col 0  

nscan = len(list(R4_df['Date'].values.tolist()))


j = 1
for i, j in zip(dat4['Name'], range(1,nscan)):   
#    for iscan in range(1,nscan):
#DR2

    #x = DR2_Allscans_full.Wavenumber
    #y = DR2_Allscans_full['{}'.format(i)]

    x = DR3_Allscan_df.Wavenumber
    y = DR3_Allscan_df['{}'.format(i)]
    
    plt.plot(x,y, label="{}_{}".format(str(R4_df.loc[i]['Date']), str(R4_df.loc[i]['Temp'])), c=cm.jet(j/nscan)) 
    
    j=+1

ax4.set_title('BC zoomed')
ax4.axis([4000, 2800, 0, 0.5])

plt.legend()

plt.show()


# insert condition to supress first scan (ramp)
# Implement maxA 
# Increase spacing between plots

# ## Other plot

# ### Different DR Outputs

# # 1.6 Scan Averaging and error analysis ?

# Supress the first scan and average the remaining scan 
# 
# Have a though about error bars

# In[ ]:





# # 1.7 Data processing

# ## 1.7.1 Linear regression of desorption

# This is where some fitting options needs to be implemented ie:
# 
# - linear regression for desorption data
# - Polynomial for isotherms at 130, 135K ?
# 

# ## 1.7.2 polynomial fitting of isotherm at 130K

# Goal,

# # <span style='background :yellow' > $\color{green}{\text{DP2 : Substraction scan}}$ </span>

# use DR2 data
# 
# Purpose here is to obtain 4 different substraction spectra for each of the presestablished range (use hot-warm color to plot)

# ## 2.1 Data Sanity Check

# In[27]:


DR2_Allscan_df


# In[28]:


wavelength = DR2_Allscan_df.T.iloc[0]


# In[29]:


wavelength


# ## 2.2  Function definition

# In[30]:


def substraction(index1, date, index2):
    
#    exp_date1 = input('date of experiment 1 (format YYYY_MM_DD) = ')
#    index1 = int(input('index 1 = '))
#    exp_date2 = input('date of experiment 2 (format YYYY_MM_DD) = ')
#    index2 = int(input('index 2 = '))
    
    data1 = DR2_Allscan_df
    #data2 = pd.read_csv('D:\PhD-WS\Projects\PAC\{}}\DATA\{0}\Data\DR2_{}_All_data.csv'.format(XP,date))

    data1 = data1.T.iloc[1:].T
    #data2 = data2.T.iloc[1:].T
    
    
#Scan 1    
    
    list_name1 =  list(data1.columns.values.tolist())
    
    scan_place1 = 0
    
    for i in range(len(list_name1)):
                
        name_corr = list_name1[i].split('_')
        
        if int(name_corr[-1]) == int(index1):
    
            scan_place1 = i
    
    scan1 = data1.T.iloc[scan_place1]
    
#Scan 2    
    
    list_name2 =  list(data1.columns.values.tolist())
    
    scan_place2 = 0
    
    for i in range(len(list_name2)):
        
        name_corr = list_name2[i].split('_')
        
        if int(name_corr[-1]) == int(index2):
    
            scan_place2 = i
    
    scan2 = data1.T.iloc[scan_place2]
    
    sub_scan = numpy.zeros(len(scan1))
    
    for iscan in range(len(sub_scan)):
        
        sub_scan[iscan] = scan2[iscan] - scan1[iscan]
    
    return sub_scan


# ## 2.3 Plotting

# ### All Range

# In[31]:


#date = "2020_09_15"

data1 = DR2_Allscan_df


data1 = data1.T.iloc[1:].T
    
#data = data.T.iloc[1:].T
#data = data1


nscan = len(list(data1.columns.values.tolist()))

print(nscan)
#print(data1)


fig = plt.figure(figsize=(16,16))
ax = fig.add_subplot()


ax.set_xlabel('Wavenumber (cm-1)')
ax.set_ylabel('Absorbance')
#ax.set_zlabel('Absorbance')

data_sub = []
data_sub_2 =[]

for iscan in range(nscan-1):
    
    iscan = iscan+1
     
    sub_scan = substraction(iscan, date, iscan+1)
    
    df = pd.DataFrame({'Wavenumber': wavelength, "ASW_"+str(date)+"_" + str(iscan) +"-" + str(iscan+1): sub_scan})
    
    #df.to_csv('D:\PhD-WS\Projects\PAC\XP_1-1\DATA\{}\Data\DP1\DP1_{}_sub-scan_{}.csv'.format(date,date, iscan))
    
    #data_int.append(df)
    
    
    data_sub.append(
        
        {
            

            'Name' : "ASW_"+str(date)+"_" + str(iscan) +"-" + str(iscan+1),
            'Wavenumber' : wavelength,
            'sub_scan' : sub_scan,

        }) 
    
    data_sub_2.append(df)
    


    plt.plot(wavelength, sub_scan, c=cm.jet(iscan/nscan), label = "scan{0}".format(str(iscan)))
       

plt.title('{}_Substraction scans'.format(date), pad=20).set_fontsize(18)
ax.hlines(0,3900,2900)
plt.xlim([3800,2900])
plt.legend()
plt.show()


# ### Range 1

# Insert condition to use only items present in range 1 

# In[32]:


#date = "2020_09_15"

data1 = DR2_Allscan_df


data1 = data1.T.iloc[1:].T
    
#data = data.T.iloc[1:].T
#data = data1


nscan = len(list(data1.columns.values.tolist()))

print(nscan)
#print(data1)


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()


ax.set_xlabel('Wavenumber (cm-1)')
ax.set_ylabel('Absorbance')
#ax.set_zlabel('Absorbance')

data_sub = []
data_sub_2 =[]

for iscan in file_number1:
    
    iscan = iscan+1
     
    sub_scan = substraction(iscan, date, iscan+1)
    
    df = pd.DataFrame({'Wavenumber': wavelength, "ASW_"+str(date)+"_" + str(iscan) +"-" + str(iscan+1): sub_scan})
    
    #df.to_csv('D:\PhD-WS\Projects\PAC\XP_1-1\DATA\{}\Data\DP1\DP1_{}_sub-scan_{}.csv'.format(date,date, iscan))
    
    #data_int.append(df)
    
    
    data_sub.append(
        
        {
            

            'Name' : "ASW_"+str(date)+"_" + str(iscan) +"-" + str(iscan+1),
            'Wavenumber' : wavelength,
            'sub_scan' : sub_scan,

        }) 
    
    data_sub_2.append(df)
    


    plt.plot(wavelength, sub_scan, c=cm.jet(iscan/nscan), label = "scan{0}".format(str(iscan)))
       

plt.title('{}_Substraction scans'.format(date), pad=20).set_fontsize(18)
ax.hlines(0,3900,2900)
plt.xlim([3800,2900])
plt.legend()
plt.show()


# In[33]:


df


# In[34]:


data_sub


# In[35]:


data_sub_2


# ### Range 2

# In[35]:


#date = "2020_09_15"

data1 = DR2_Allscan_df


data1 = data1.T.iloc[1:].T
    
#data = data.T.iloc[1:].T
#data = data1


nscan = len(list(data1.columns.values.tolist()))

print(nscan)
#print(data1)


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()


ax.set_xlabel('Wavenumber (cm-1)')
ax.set_ylabel('Absorbance')
#ax.set_zlabel('Absorbance')

data_sub = []
data_sub_2 =[]

for iscan in file_number2:
    
    iscan = iscan+1
     
    sub_scan = substraction(iscan, date, iscan+1)
    
    df = pd.DataFrame({'Wavenumber': wavelength, "ASW_"+str(date)+"_" + str(iscan) +"-" + str(iscan+1): sub_scan})
    
    #df.to_csv('D:\PhD-WS\Projects\PAC\XP_1-1\DATA\{}\Data\DP1\DP1_{}_sub-scan_{}.csv'.format(date,date, iscan))
    
    #data_int.append(df)
    
    
    data_sub.append(
        
        {
            

            'Name' : "ASW_"+str(date)+"_" + str(iscan) +"-" + str(iscan+1),
            'Wavenumber' : wavelength,
            'sub_scan' : sub_scan,

        }) 
    
    data_sub_2.append(df)
    


    plt.plot(wavelength, sub_scan, c=cm.jet(iscan/nscan), label = "scan{0}".format(str(iscan)))
       

plt.title('{}_Substraction scans'.format(date), pad=20).set_fontsize(18)
ax.hlines(0,3900,2900)
plt.xlim([3800,2900])
plt.legend()
plt.show()


# ### Range 3

# In[41]:


#date = "2020_09_15"

data1 = DR2_Allscan_df


data1 = data1.T.iloc[1:].T
    
#data = data.T.iloc[1:].T
#data = data1


nscan = len(list(data1.columns.values.tolist()))

print(nscan)
#print(data1)


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()


ax.set_xlabel('Wavenumber (cm-1)')
ax.set_ylabel('Absorbance')
#ax.set_zlabel('Absorbance')

data_sub = []
data_sub_2 =[]

for iscan in file_number3:
    
    iscan = iscan+1
     
    sub_scan = substraction(iscan, date, iscan+1)
    
    df = pd.DataFrame({'Wavenumber': wavelength, "ASW_"+str(date)+"_" + str(iscan) +"-" + str(iscan+1): sub_scan})
    
    #df.to_csv('D:\PhD-WS\Projects\PAC\XP_1-1\DATA\{}\Data\DP1\DP1_{}_sub-scan_{}.csv'.format(date,date, iscan))
    
    #data_int.append(df)
    
    
    data_sub.append(
        
        {
            

            'Name' : "ASW_"+str(date)+"_" + str(iscan) +"-" + str(iscan+1),
            'Wavenumber' : wavelength,
            'sub_scan' : sub_scan,

        }) 
    
    data_sub_2.append(df)
    


    plt.plot(wavelength, sub_scan, c=cm.jet(iscan/nscan), label = "scan{0}".format(str(iscan)))
       

plt.title('{}_Substraction scans'.format(date), pad=20).set_fontsize(18)
ax.hlines(0,3900,2900)
plt.xlim([3800,2900])
plt.ylim([-0.0075,0.0075])
#plt.legend()
plt.show()


# ### Range 4

# In[37]:


#date = "2020_09_15"

data1 = DR2_Allscan_df


data1 = data1.T.iloc[1:].T
    
#data = data.T.iloc[1:].T
#data = data1


nscan = len(list(data1.columns.values.tolist()))

print(nscan)
#print(data1)


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()


ax.set_xlabel('Wavenumber (cm-1)')
ax.set_ylabel('Absorbance')
#ax.set_zlabel('Absorbance')

data_sub = []
data_sub_2 =[]

for iscan in file_number4:
    
    iscan = iscan+1
     
    sub_scan = substraction(iscan, date, iscan+1)
    
    df = pd.DataFrame({'Wavenumber': wavelength, "ASW_"+str(date)+"_" + str(iscan) +"-" + str(iscan+1): sub_scan})
    
    #df.to_csv('D:\PhD-WS\Projects\PAC\XP_1-1\DATA\{}\Data\DP1\DP1_{}_sub-scan_{}.csv'.format(date,date, iscan))
    
    #data_int.append(df)
    
    
    data_sub.append(
        
        {
            

            'Name' : "ASW_"+str(date)+"_" + str(iscan) +"-" + str(iscan+1),
            'Wavenumber' : wavelength,
            'sub_scan' : sub_scan,

        }) 
    
    data_sub_2.append(df)
    


    plt.plot(wavelength, sub_scan, c=cm.jet(iscan/nscan), label = "scan{0}".format(str(iscan)))
       

plt.title('{}_Substraction scans'.format(date), pad=20).set_fontsize(18)
ax.hlines(0,3900,2900)
plt.xlim([3800,2900])
plt.legend()
plt.show()


# 

# ## Preliminary analysis 

# Purpose here would be (for the different physical processes that the ice undergo upon annealing) to investigate the different contributions lost and gain from the substraction spectra
# 
# This will subsequently be used as initial guesses for the gaussian fit of the whole samples
# 
# An intermediate gaussian fitting routine could be implemented here with the substraction spectra

# In[ ]:





# ## Export Data Sub as csv

# ### Concatenation

# In[ ]:


data_sub


# In[ ]:


data_sub_2_df  = reduce(lambda left,right: pd.merge(left,right, on=['Wavenumber'],how='outer'), data_sub_2)


# ## Export as csv

# In[ ]:





# # <span style='background :yellow' > $\color{green}{\text{DP3 : Gaussian Fitting}}$ </span>

# [Lmfit web-site - Example](https://lmfit.github.io/lmfit-py/builtin_models.html#example-3-fitting-multiple-peaks-and-using-prefixes)

# ## What Data ?

# ### Substraction scan

# Later

# In[ ]:





# In[ ]:





# In[ ]:





# ### OH Stretch

# In[ ]:


DR2_A_df = DR2_df[4149:6639]


# In[ ]:


DR2_A_df


# ## Gaussian fit 1

# In[42]:



x = DR2_A_df["Wavenumber"]
y = DR2_A_df["ASW_2020_09_16_1"]

pars = exp_mod.guess(y, x=x)

gauss1 = GaussianModel(prefix='g1_')
pars.update(gauss1.make_params())

pars['g1_center'].set(value=3400, min=3300, max=3500)
pars['g1_sigma'].set(value=15, min=3)
pars['g1_amplitude'].set(value=10, min=1)

gauss2 = GaussianModel(prefix='g2_')
pars.update(gauss2.make_params())

pars['g2_center'].set(value=3260, min=3200, max=3300)
pars['g2_sigma'].set(value=15, min=3)
pars['g2_amplitude'].set(value=10, min=1)

mod = gauss1 + gauss2 

init = mod.eval(pars, x=x)
out = mod.fit(y, pars, x=x)

print(out.fit_report(min_correl=0.5))

fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.8))
axes[0].plot(x, y, 'b')
axes[0].plot(x, init, 'k--', label='initial fit')
axes[0].plot(x, out.best_fit, 'r-', label='best fit')
axes[0].invert_xaxis()
axes[0].legend(loc='best')

comps = out.eval_components(x=x)
axes[1].plot(x, y, 'b')
axes[1].plot(x, comps['g1_'], 'g--', label='Gaussian component 1')
axes[1].plot(x, comps['g2_'], 'm--', label='Gaussian component 2')
axes[1].invert_xaxis()
axes[1].legend(loc='best')

plt.show()
# <end examples/doc_builtinmodels_nistgauss.py>


# In[ ]:




