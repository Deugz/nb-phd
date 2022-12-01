#!/usr/bin/env python
# coding: utf-8

# <span style="font-size:42px;"><strong>DATA Reduction </strong></span>
# 
# <hr>
# 

# # Intro

# The purpose of this Notebook is to perform the Reduction pipeline for each samples (ie classified by dates) divided in 3 steps:
# - DR1: Sanity Check Merging
# - DR2: Baseline Correction
# - DR3: Integration Normalisation
# 
# I learned Python during my PhD, starting from scratch and I have to confess, it was a mixed feeling experience all along. It looked very scary at first, was painfull most of the time but sometimes very satisfying and rewarding as well. All together, it is a great tool for analysing data and I will try to show you why, and teach you how to use it using a "real life example" by breaking down all the steps I took to perform the analysis of my own data set. 
# 
# ***
# 
# For more information about the research itself (which I strongly recommend) have a look there: [Personal Web-site](www.include_later.com)  
# 
# ***
# 
# <b> Notes formatting: </b>
# 
# <div class="alert alert-block alert-info">
# <b>Teaching notes:</b> I produced this notebook while learning, hence I think it may be uselfull for teaching python
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Other users notes:</b> It is also one of the aim of my work to produce reliable and interoperable tools to reduce, process and analyse IR data
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Notes for me: </b> This is for me to highligt improvment needed.
# </div>
# 
# 
# <div class="alert alert-block alert-danger">
# <b>Important notes for all:</b> Just in case ;)
# </div>

# ## Workflow

# <div class="alert alert-block alert-info">
# <b>First thing first:</b> Download your python environment: Jupyter, Donload Anaconda ...
# </div>

# ![DR_workflow_02_08_21.png](attachment:DR_workflow_02_08_21.png)

# **Figure 1:** Workflow

# Explain ...

# ## Libraries

# <div class="alert alert-block alert-info">
# One of the greatest strength of Python reside in it`s collaborative nature ... libraries developped by the community ... (Open source ...)
# </div>

# In[1]:


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

get_ipython().run_line_magic('matplotlib', 'inline')


# ## The RAW Data

# From Omnic I obtain individual .spa scans named: 
# <br><br>$\color{red}{\text{ASW}}$_$\color{blue}{\text{2020_09_15}}$_$\color{green}{\text{0001}}$.spa<br>
# 
# - $\color{red}{\text{Sample type}}$ : can take value : ASW, C2H6, C2H6_ASW
# - $\color{blue}{\text{Sample date}}$ : format yyyy_mm_dd (is the id of every sample).
# - $\color{green}{\text{Scan number}}$ : is allocate incrementaly and represent each scan.
# 
# 
# This scan is saved as a csv and I performe a smoothing (15) using Omnic. 
# Overall, for each experimental scans I obtain 3 output: <br>
# 
# 
# <div class="alert alert-block alert-success">
# <b>The RAW Data:</b>
# <br><br>
# - ASW_2020_09_15_0001.spa (Raw Data)<br>
# - ASW_2020_09_15_0001.csv (Raw Data - python ready)<br>
# - ASW_2020_09_15_0001_smooth.csv (pre-reduced Data) 
# <br>    
# </div>
# 
# In the remaining reduction steps, I will used the smoothed Data.
# 
# [List of experiments](Data_test/Sample_list.xlsx): click on the link to download a table summarising the different experiments.
# 
# 
# 
# To continue ...

# ## Input parameters

# The Data Reduction routine is performed "per sample". Hence we need to define some input parameters to select what sample we want to reduce (and how).
# 

# ### Date (today)

# somehow allow for version control (really?)
# 
# Check for calendar input

# In[2]:


date_jour = "2021_09_15"


# ### Experiment

# <div class="alert alert-block alert-success">
# <b>X:</b>
# blabla
# </div>
# 
# <div class="alert alert-block alert-warning">
# Should I use input to make sure those fields are filled ? --> later
# </div>
#  
#  
# $\color{red}{\text{Update manually !}}$

# In[3]:


# 0.1 Date

date = "2020_09_15"

# 0.2 XP
    # Can take value XP_1-1, XP_1-2 

XP = "XP_1-1"

# 0.3 Sample type
    # Can take value ASW, C2H6, C2H6_ASW

spl = "ASW"

# 0.4 Deposition Temperature

Tdep = "20"


# ### Temperature Ramp

#  Needs to be $\color{red}{\text{Implemented manually !}}$
# 
# <div class="alert alert-block alert-info">
# Dictionary: {key: value }
# </div>

# In[4]:


T_ramp = []

T_ramp.append(
        
        {
            'Sample' : str(spl),
            'Date' : str(date),
            '20' :  "",
            '30' : "",
            '40' : numpy.arange(1, 3, 1).tolist(),
            '50' : "",
            '60' : numpy.arange(3, 13, 1).tolist(),
            '70' : "",
            '80' : numpy.arange(13, 23, 1).tolist(),
            '90' : "",
            '100' : numpy.arange(23, 35, 1).tolist(),
            '110' :"",
            '120' : numpy.arange(35, 45, 1).tolist(),
            '125' : "",
            '130' : numpy.arange(45, 55, 1).tolist(),
            '132' : "",
            '134' : "",
            '135' : numpy.arange(55, 65, 1).tolist(),
            '136' : "",
            '137' : "",
            '138' : "",
            '140' : numpy.arange(65, 76, 1).tolist(),
            '142' : "",
            '145' : numpy.arange(76, 166, 1).tolist(),
            '150' :"",
            '155' : "",
            '160' : "",
            '180' : "",
            '200' : "",

            })

#T_ramp


# <div class="alert alert-block alert-info">
# Pandas library
# </div>

# In[5]:


T_ramp_df = pd.DataFrame(T_ramp)

#T_ramp_df 


# ####  Append df to csv

# We want to append T_ramp_df to XP_file.cvs, only if the date is not already present
# 
# Open XP_Ramp csv and create a df
# 
# <div class="alert alert-block alert-info">
# Read csv
# </div>

# In[16]:


XP_Ramp_df = pd.read_csv('..\DATA\DATA-Processing\PAC\XP_list_test.csv')

#XP_Ramp_df


# <div class="alert alert-block alert-info">
# Extract information from df
# </div>
# 
# What date are already present

# In[17]:


XP_Date = []

XP_Date = str(XP_Ramp_df['Date'])

#print(XP_Date)


# <div class="alert alert-block alert-info">
# if statement
# </div>
# 
# Conditions that state if date already exist, don`t append, otherwise append T_ramp_df to XP_ramp_df

# In[18]:


if date in XP_Date:
    print("Not appended")
else:
    T_ramp_df.to_csv('..\DATA\DATA-Processing\PAC\XP_list_test.csv', mode='a', header=False, index=False)


# #### Sanity Check 

# In[20]:


#XP_file_df = pd.read_csv('D:\PhD-WS\Projects\PAC\XP_1-1\DATA\XP_list_test.csv')

#XP_file_df


# ### T ramp for Reduction

# #### Ramp

# Purpose here is to produce a dictionnary where one scan is allocated to a Temperature for a rough processing within this Reduction Notebook.
# 
# $\color{red}{\text{Implement manually !}}$

# In[12]:


i = [0,1,2,3]
j = ["20","130","140","160"]


Tdictionary = dict(zip(j, i))


# ___Previous Dictionnaries___

# Creating those dictionnary is a tedious process that, hence to prevent having to rewrite them each times we store them here as comments. However there is probaly a better method preventing a surcharge here (to implement) 

# In[13]:


#15-09 Sample 

#i = [0,1,2,3]
#j = ["20","130","140","160"]

#16-09 Sample 

#i = [0,1,4,7,10,13,16,19,22,25,28,30]
#j = ["Dep","20","40","60","80","100","120","130","140","160","180","200"]

#28-09

#i = [0,1,4,8,12,16,20,24,28,32,36,40,48,52,56,60,64,68,76,79]
#j = ["Dep","20","30","40","50","60","70","80","90","100","110","120","125","130","135","140","145","150","155","160",]

#17-09 and 21-09

#i = [0,1,4,7,10,13,16,19,22,25,27]
#j = ["Dep","20","40","60","80","100","120","130","140","160","180"]

#22-10

#i = [0,1,4,8,34,37,40,43,46,49,52,55,57,66]
#j = ["Dep","20","120","130", "130*", "132","134","136","138","140","142","145","150","150*"]

#16-11

#i = [0,1,4,6,17,18,41,45,49,51,63,66,68,88]
#j = ["Dep","20","60","70","70*","130","130*","136","137","138","138*","140","145","145*"]

#11-19

#i = [0,1,4,9,12,52,55,66,69,88,91,94,159]
#j = ["Dep","20","60","60*","70","70*","130","130*","135","135*","140","145","145*"]

#11-23


# #### Isotherm

# For specific samples, it is necessary to have the same approach as before but using Isotherm data. ie for one temperature specific scans are selected and included in a dictionnary where key is time (hour)
# 
# <div class="alert alert-block alert-info">
# if statement
# <br>   
#     
# <a href="https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#Boolean-widgets">Widget list</a>    
#     
# </div>
# 
# 
# 
# 
# 
# $\color{red}{\text{Modify accordingly !}}$

# In[28]:


Iso = widgets.Checkbox(
      value=False,
      description='Isotherm',
      disabled=False,
      indent=False
)

display(Iso)


# In[ ]:


$\color{red}{\text{Implement the Tiso !}}$


# In[22]:


#Tiso1 = "130"


# In[23]:


#k = [8,24,41,58,75,90,106,123,140,157,174,191,208,225,242,259,276,293,310,327,344,361,378,395,412,429,446,463,480,497,514,531,548,565,582,599,616,633,650,667,684,701,718,735,752,769,786]
#l = ["0","4","8","12","16","20","24","28","32","36","40","44","48","52","56","60","64","68","72","76","80","84","88","92","96","100","104","108","112","116","120","124","128","132","136","140","144","148","152","156","160","164","168","172","176","180"]

#k = [8,12,16,20,24,28,31,35,39,43,47,51,55,59,63,67,71,75,79,83,87,90,94,98,102,106,110,114,118,122,125,129,133,137,141,145,149,153,157,161,165,169,173,177,181,185,189,193]
#l = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48"]

#k = [10,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800] 
#l = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]

Isodic1 = dict(zip(l, k))


# ___Previous Dictionnaries___

# In[24]:


#10-22 130K

#k = [6,10,14,18,22,26,29,33]
#l = ["0","1","2","3","4","5","15","16"]

#11-16 130K

#k = [20,24,28,32,36,40]
#l = ["0","1","2","3","4","16"]

#11-19 145K

#k = [94,98,102,106,110,114,118,122,126,130,134,138,142,146,150,154,158]
#l = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]

#11-19 135K

#k = [68,72,76,80,84,89]
#l = ["0","1","2","3","4","22"]


# # <span style='background :yellow' > $\color{green}{\text{DR1 : Sanity Check and Merging}}$ </span>

# I have one individual csv for each experimental scan (smoothed by omnic) called: ASW_2020_09_15_0001_smooth and located in the folder "D:\DATA-RAW\PAC\XP_1-1/2020_09_15/"   
# 
# Purpose :
# 
# - Import all the data 
# - Create one data frame for each spectrum and add header (wavenumber, spectrum title)  
# - merge all the data frame and create one big with (wavenumber, 0001, 0002, 0003, ...)
# - Also during this phase a new csv will be created with various data that we aquired from the sample processing and named data_anex.csv
# 
# All the outputs generated will be located in the following folder: D:\DATA-Processing\PAC\XP_1-1\Samples\2020_09_15 and we expect two types of outputs:
# - Data
# - Plots
# 

# ## <u>Import and read the data</u>

# In[6]:


file_path = "..\DATA\DATA-RAW\PAC\{}/{}/*_smooth.csv".format(XP,date)


# ___Empty lists___

# In[7]:


# List within which all the individual scans will be added prior to merging
All_data_frame = []

# List where all the "data annex" (ie max absorbance ...), will be stored 
data_anex = []

#Temperature Ramp that the sample experienced (need to be entered manually later)
T_ramp = []

# Data annex values
data_max = []
minimum_1 = []
minimum_1_index = []
minimum_2 = []
minimum_2_index = []
minimum_3 = []
minimum_3_index = []
minimum_4 = []
minimum_4_index = []
minimum_5 = []
minimum_5_index = []
minimum_6 = []
minimum_6_index = []

maximum = []
maximum_index = []


# ___For loop___ 

# Open all the individual files (df) and append to a list (All_data_frame) that will subsequently be transformed into a df.
# 
# Extract some informations for each sample: 
# - min between 3 ranges
# - max
# that will subsequently be used for the remaining of the Data reduction pipeline and store it in data annex 
# 
# 

# In[8]:


# iterator

file_number = 1

#for loop

for file in glob.glob(file_path):

    df = pd.read_csv(file, names=["Wavenumber", str(spl)+"_"+str(date)+"_"+str(file_number)])
    
    All_data_frame.append(df) 

    #Min 4000 - 3800 wavenumber
    
    min1 = df.iloc[6223:6639,1].astype(float).min()
    min1_index= df.iloc[6223:6639,1].astype(float).idxmin()
    
    #Min 3000 - 2800 wavenumber
    
    min2 = df.iloc[4149:4564,1].astype(float).min()
    min2_index = df.iloc[4149:4564,1].astype(float).idxmin()
    
    #Min 2800 - 2700 wavenumber
    
    min3 = df.iloc[3941:4149,1].astype(float).min()
    min3_index= df.iloc[3941:4149,1].astype(float).idxmin()
    
    #Min 2000 - 1900 wavenumber
    
    min4 = df.iloc[2282:2490,1].astype(float).min()
    min4_index = df.iloc[2282:2490,1].astype(float).idxmin()
    
    #Min 2800 - 2700 wavenumber
    
    min3 = df.iloc[3941:4149,1].astype(float).min()
    min3_index= df.iloc[3941:4149,1].astype(float).idxmin()
    
    #Min 2000 - 1900 wavenumber
    
    min4 = df.iloc[2282:2490,1].astype(float).min()
    min4_index = df.iloc[2282:2490,1].astype(float).idxmin()
    
    #Min 1900 - 1800 wavenumber
    
    min5 = df.iloc[2075:2282,1].astype(float).min()
    min5_index= df.iloc[2075:2282,1].astype(float).idxmin()
    
    #Min 1300 - 800 wavenumber
    
    min6 = df.iloc[0:1038,1].astype(float).min()
    min6_index = df.iloc[0:1038,1].astype(float).idxmin()
    
    maxi = df.iloc[4149:6639,1].astype(float).max()
    maxi_index= df.iloc[4149:6639,1].astype(float).idxmax()
    

    #Wavenumber.append(Wav)    
    #RAW_data.append(RAW)
    
    minimum_1.append(min1)
    minimum_1_index.append(min1_index)
    
    minimum_2.append(min2)
    minimum_2_index.append(min2_index)
    
    minimum_3.append(min3)
    minimum_3_index.append(min3_index)
    
    minimum_4.append(min3)
    minimum_4_index.append(min3_index)
    
    minimum_5.append(min5)
    minimum_5_index.append(min5_index)
    
    minimum_6.append(min6)
    minimum_6_index.append(min6_index)
    
    maximum.append(maxi)
    maximum_index.append(maxi_index)
        
    data_anex.append(
        
        {

            'Name' : str(spl)+"_"+str(date)+"_" + str(file_number),
            'min1' : min1,
            'index1' :  min1_index,
            'min2' : min2,
            'index2' :  min2_index,
            'min3' : min3,
            'index3' :  min3_index,
            'min4' : min4,
            'index4' :  min4_index,
            'min5' : min5,
            'index5' :  min5_index,
            'min6' : min6,
            'index6' :  min6_index,
            'max' : maxi,
            'max_index' :  maxi_index,
        })
    


    
    file_number +=1


# Should I had a new min range for ethane data ?

# ## <u>Sanity Check </u>

# ___All Data___

# Check that the list has the same number of scans, and that every scan has 6639 rows

# In[9]:


All_data_frame


# In[10]:


data_anex


# ___Data Annex___

# In[12]:


data_anex_df = pd.DataFrame(data_anex)


# In[13]:


data_anex_df.head(5)


# ##  <u>Concatenation </u>

# Purpose here is to concatenate all the individual scans into 1 big df that will subsequently be converted into csv

# In[14]:


All_RAW_df = reduce(lambda left,right: pd.merge(left,right, on=['Wavenumber'],how='outer'), All_data_frame)


# In[15]:


All_RAW_df 


# In[16]:


pd.DataFrame(All_RAW_df)


# ___CSV Export___

# In[26]:


All_RAW_df.to_csv("..\DATA\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR1_{}_All-scans.csv".format(XP,date,date))


# ## <u> Plotting </u>

# In[27]:


nscan = len(list(All_RAW_df.columns.values.tolist()))

print(nscan)


fig= plt.figure(figsize=(12,6))


normalize = mcolors.Normalize(vmin=0, vmax=nscan)
colormap = cm.jet
i=1

for i in range(1,nscan):
    
    plt.plot(All_RAW_df.Wavenumber, All_RAW_df['{}_{}_{}'.format(spl, date, i)], color=colormap(normalize(i)))
    
    i=+1
    

plt.title('DR1 Unprocessed {0}'.format(date))
plt.axis([4000,800,-0.05,0.50])
plt.xlabel('Wavenumber (cm-1)').set_fontsize(13)
plt.ylabel('Absorbance').set_fontsize(13)
#ax = fig.gca()
plt.grid()
#plt.legend()

scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nscan)
plt.colorbar(scalarmappaple)

plt.savefig('..\DATA\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR1_{}_Full-range.png'.format(XP, date, date))

plt.show()


# ## <u> Chop the data </u>

# Data is choped in 3 range:
# - A: OH stretch : (4000 - 2800 cm-1)
# - B: Combination bands : (2800 - 1900 cm-1)
# - C: Bending modes : (1900 - 800 cm-1)
# 
# If spl = C2H6 implement sub range for each peak:
# 
# $\color{blue}{\text{do we need to do that ?}}$
# 
# Yes because each baseline correction function will use the data within those ranges (there is probably a better solution there but for the moment that work quite well)

# ### 1.5.1 OH Stretch

# In[28]:


DR1_A_df = All_RAW_df[4150:6639]

#DR1_A_df


# ___Export as csv___

# In[29]:


#DR1_A_df.to_csv('..\DATA\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR1_{}_A.csv'.format(XP, date, date))


# ### 1.5.2 Combination bands

# In[30]:


DR1_B_df = All_RAW_df[2282:4150]

#DR1_B_df


# ___Export as csv___

# In[31]:


#DR1_B_df.to_csv('..\DATA\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR1_{}_B.csv'.format(XP, date, date))


# ### 1.5.3 bending modes

# In[32]:


DR1_C_df = All_RAW_df[0:2282]

#DR1_C_df


# ___Export as csv___

# In[33]:


#DR1_C_df.to_csv('..\DATA\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR1_{}_C.csv'.format(XP, date, date))


# # <span style='background :yellow' > $\color{green}{\text{DR2 : Baseline Correction}}$ </span>

# One of the reason to perform all the reduction steps within the same notebook is that we can keep the previously created df all along. Also, the various outputs that are generated at the various reduction steps will be implemented into the same df (data_annex that will be converted to a csv at the end of the reduction). Here is a list of the df created so far:
# 
# Dataframe | Purpose
# - | - 
# All_RAW_df | - 
# T_ramp_df | - 
# data_annex_df | - 
# DR1_A_df | - 
# DR1_B_df | - 
# DR1_C_df | - 
# 
# The purpose of this section is to perform a Baseline correction for each of the previously chopped data before to concatenate them in a fully baseline corrected df
# 
# Different samples (ASW - C2H6 - ASW_C2H6) needs different baseline correction. Hence, based on the variable "Spl" we will run different sub-notebooks that will aply the baseline correction:
# 
# 
# Sample | Notebook | Function | Dataframe (name) | Output (csv)
#  :-: | :-: | :-: 
# ASW 1 | ASW_DR2_1.ipynb | select minimum value within a range 
# ASW 2 | ASW_DR2_2.ipynb | Select mean value within +- 5 wavenumber around a centered value
# C2H6 | - | -
# C2H6_ASW | - | -
# 

# 

# ___Empty List___

# In[34]:


maxA = []
maxAi = []


# ___Data check___

# In[83]:


#DR1_A_df
#DR1_B_df
#DR1_C_df


# In[38]:


#All_RAW_df


# ## <u>Background function definition </u>

# ### Minimum (single point) within a range

# Here we select a minimum within a predefined range (stored in data_annex). 
# 
# 
# Idea for latter: Try to not select an individual point as minimum but a local minimum with a rolling average
# 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html

# In[39]:


#DR1_A_df


# In[40]:


# We supress the first column (Wavenumber)

DR1_A_df = DR1_A_df.T.iloc[1:].T
DR1_B_df = DR1_B_df.T.iloc[1:].T
DR1_C_df = DR1_C_df.T.iloc[1:].T

# Now compute a new DataFrame indexed by the file names with rows that contain the
# minimum value and the index of that minimum value within specific row ranges
# of the column in data corresponding to the filename.
dataStats = pd.DataFrame.from_dict(
  dict(min1=All_RAW_df.T.iloc[1:].T.iloc[6223:6639].min(axis=0), # min within rows 6000 - end
       mini1=All_RAW_df.T.iloc[1:].T.iloc[6223:6639].idxmin(axis=0), # index of that min
       min2=All_RAW_df.T.iloc[1:].T.iloc[4149:4564].min(axis=0), # min within rows 4000 - 5000
       mini2=All_RAW_df.T.iloc[1:].T.iloc[4149:4564].idxmin(axis=0), # index of that min
       min3=All_RAW_df.T.iloc[1:].T.iloc[3941:4149].min(axis=0), # min within rows 2282 - 2697
       mini3=All_RAW_df.T.iloc[1:].T.iloc[3941:4149].idxmin(axis=0), # index of that min
       min4=All_RAW_df.T.iloc[1:].T.iloc[2282:2490].min(axis=0), # min within rows 415 - 830
       mini4=All_RAW_df.T.iloc[1:].T.iloc[2282:2490].idxmin(axis=0), # index of that min   
       min5=All_RAW_df.T.iloc[1:].T.iloc[2075:2282].min(axis=0), # min within rows 2282 - 2697
       mini5=All_RAW_df.T.iloc[1:].T.iloc[2075:2282].idxmin(axis=0), # index of that min
       min6=All_RAW_df.T.iloc[1:].T.iloc[0:1038].min(axis=0), # min within rows 415 - 830
       mini6=All_RAW_df.T.iloc[1:].T.iloc[0:1038].idxmin(axis=0), # index of that min   
        )
    
)

print(dataStats)

# select average around minimum value 

#.rolling(4).mean()



# Breaking down what's happening in:
# `data.T.iloc[1:].T.iloc[6000:6800].min(axis=0)`
# 1) `data.T.iloc[1:].T` - This is a cheeky way of stripping away the first column, "Wavenumber",
# 1a) `data.T`, transposes the frame i.e. switches rows and columns
# 1b) `.iloc[1:]` selects all but the first row (previously all but the first column).
# 1c) The final `.T` switches rows and columns back again.
# 2) `.iloc[6000:6800]` selects rows at *positions* between 6000 and 6800. We now have a 
# 2D block of data.
# 3) `.min(axis=0)` computes the column-wise minima of the 2D block we just selected, to 
# give us a 1D Series of numbers.
# 3.1) On the next line, `.idxmin(axis=0)` computes the column-wise index of the minimum for 
# the 2D block we just selected, to give us a 1D Series of index locations.

# We want to subtract a linear function from each column in data, that will
# connect the minimum values in the two ranges. 
# We'll use the `apply` method of pd.DataFrame to do that.
# Apply operates on rows (or columns if the argument axis is set to 0) of a Dataframe to 
# compute a function on the elements of that whole row or column.
#
# We'll define the function that we want to compute.
# The first argument is the column or row data themselves and we are free to 
# provide other data that we need to compute out function.
def computeLinearBackground1(values,     # The column values (e.g. Y)
                            waveNumber, # The corresponding wavenumbers (e.g. X)
                            valueStats  # The dataframe containing the minima and their 
                                        # indices for each file
                 ):
    # extract the correct set of minima using the `name` attribute of the `values` series
    # to index the `valueStats` frame.
    stats = valueStats.loc[values.name, :]
    # compute a linear background function
    gradient = ((stats.min1 - stats.min2)/(stats.mini1 - stats.mini2))
    intercept = stats.min1 - stats.mini1*gradient
    linearBackground1 = (gradient * waveNumber.index) + intercept
    # subtract that function from the column values
    return linearBackground1

def computeLinearBackground2(values,    
                            waveNumber, 
                            valueStats  
                                        
                 ):

    stats = valueStats.loc[values.name, :]
    gradient = ((stats.min3 - stats.min4)/(stats.mini3 - stats.mini4))
    intercept = stats.min3 - stats.mini3*gradient
    linearBackground2 = (gradient * waveNumber.index) + intercept
    return linearBackground2



def computeLinearBackground3(values,   
                            waveNumber, 
                            valueStats  
                 ):
    
    stats = valueStats.loc[values.name, :]
    gradient = ((stats.min5 - stats.min6)/(stats.mini5 - stats.mini6))
    intercept = stats.min5 - stats.mini5*gradient
    linearBackground3 = (gradient * waveNumber.index) + intercept
    return linearBackground3

# Finally apply our function to the columns of the dataframe (except the wavenumber column)
# We specify axis=0 to operate on the columns (confusingly this is referred to as *along*
# the index direction in the docs), and pass the first (wavenumber) column and the summary 
# statistics dataframe, wrapped in a tuple, as the `args` argument.
backgroundsA = DR1_A_df.T.iloc[0:].T.apply(computeLinearBackground1, axis=0, args=(DR1_A_df.T.iloc[0], dataStats))
backgroundsB = DR1_B_df.T.iloc[0:].T.apply(computeLinearBackground2, axis=0, args=(DR1_B_df.T.iloc[0], dataStats))
backgroundsC = DR1_C_df.T.iloc[0:].T.apply(computeLinearBackground3, axis=0, args=(DR1_C_df.T.iloc[0], dataStats))


# In[41]:


DR1_A_df


# In[42]:


#min1


# ###  Minimum within a range + Smoothing

# $\color{red}{\text{In the making - not ready}}$ 
# 
# https://scipy-cookbook.readthedocs.io/items/SignalSmooth.html

# In[43]:


def smooth(x,window_len=5,window='flat'):
    s=numpy.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
    w=numpy.ones(window_len,'d')
    y=numpy.convolve(w/w.sum(),s,mode='valid')
    return y


# In[44]:


min1B = All_RAW_df.T.iloc[1].T.iloc[6223:6639]


# In[45]:


#min1B


# In[46]:


#for x in min1B:
#    print(x)
#    z = smooth(x,window_len=5,window='flat')


# In[47]:


#print(z)


#  $\color{red}{\text{To perform with a single value and not a range}}$ 

# ### Minimum Using single value (same for all scans)

# 

# Check the difference between those different baseline correction method

# In[48]:


All_RAW_df


# 

# 

# In[70]:





# In[51]:





# In[71]:





# ## <u>Baseline correction</u>

# ### data - background subtraction 

# ####  ASW

# Previous step produced a background for each data range (A,B,C). We will now substract this background to the data and create new BC Data frame. 

# In[72]:


dataA_BC = pd.DataFrame(DR1_A_df - backgroundsA)
dataB_BC = pd.DataFrame(DR1_B_df - backgroundsB)
dataC_BC = pd.DataFrame(DR1_C_df - backgroundsC)


# In[73]:





# In[74]:


dataA_BC


# In[80]:


dataA_BC_U


# In[78]:


dataB_BC_U


# In[79]:


dataC_BC_U


# #### Ethane samples

#  $\color{red}{\text{If Ethane Different baseline nedd to be fitted - polynomial}}$ <br>
#  
#  https://docs.scipy.org/doc/scipy/tutorial/interpolate.html#using-radial-basis-functions-for-smoothing-interpolation
#  
#  New range nedd to be created
#  
#  $\color{red}{\text{If Ethane implement sub range to extract max A for each peak}}$
# 
# if statement for sample = C2H6

# ___Run specific notebook___

# In[ ]:


#if spl == "C2H6":

    get_ipython().run_line_magic('run', '-i "test1.py"')

#elif spl == "C2H6_ASW":
    
#    %run -i "test1.py"
    
#elif spl == "ASW":
    
#    print('its OK bro, carry on')
    
#    %run -i "test1.py"
 


# ### Cleaning and Sanity Check

# We reinsert the Wavenumber that was removed prior to the baseline function aplied

# In[81]:


dataA_BC.insert(0, 'Wavenumber', All_RAW_df['Wavenumber'])
dataB_BC.insert(0, 'Wavenumber', All_RAW_df['Wavenumber'])
dataC_BC.insert(0, 'Wavenumber', All_RAW_df['Wavenumber'])

backgroundsA.insert(0, 'Wavenumber', All_RAW_df['Wavenumber'])
backgroundsB.insert(0, 'Wavenumber', All_RAW_df['Wavenumber'])
backgroundsC.insert(0, 'Wavenumber', All_RAW_df['Wavenumber'])


# In[ ]:


#dataA_BC


# In[ ]:


#backgroundsA


# #### Concatenation

# In[ ]:


All_data_A = dataC_BC.append(dataB_BC).drop_duplicates().reset_index(drop=True)


# In[ ]:


All_data_BC = All_data_A.append(dataA_BC).drop_duplicates().reset_index(drop=True)


# In[ ]:


All_data_BC


# #### Export as csv

# In[ ]:


All_data_BC.to_csv('D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR2_{}_All-scans.csv'.format(XP, date, date))


# ## <u>Max Absorbance</u>

# A first step in our analysis is to extract and use the maximum absorbance in order to make a first comparison of the frequency shifts with respect to temperature for each sample.

# ### Preliminary steps

# ####  Range B

# For range B (combination modes), we need to supress the CO2 signature (that would otherwise contribute to the max A value for this range). As a first guess we aim to supress data from 2390 to 2290 wavenumber

# ___Find index based on column value___

# In[ ]:


#dataB_BC[(dataB_BC['Wavenumber'] > 2388) & (dataB_BC['Wavenumber'] < 2392)].index.tolist()


# In[ ]:


#dataB_BC.loc[3299, 'Wavenumber']


# ___Supress data within a specified range___

# Create a new dataframe where the datapoints corresponding to the absorbtion of CO2 is suppressed. (value are different than the one above because the index was reinitialised (simple substraction do the trick))

# In[ ]:


dataB_BC_U = dataB_BC.drop(dataB_BC.index[808:1016])


# In[ ]:


#dataB_BC_U


# ####  Range C

# Concerning range C, we are only aiming for the maximum absorbance of the bending modes but the libration modes have a contribution more important. However the peak is incomplete and we need to supress it. <br>
# Same approach as previously will be used and we aim to cut the data at wavenumber = 1040 cm-1

# In[ ]:


#dataC_BC[(dataC_BC['Wavenumber'] > 1038) & (dataC_BC['Wavenumber'] < 1042)].index.tolist()


# In[ ]:


dataC_BC_U = dataC_BC.drop(dataC_BC.index[0:498])


# In[ ]:


#dataC_BC_U


# ###  Extract max A

# Here we look for 4 maximum:
# - two for the range A (1 with the baseline corrected scan and one from the unreduced data, to check that they concord and that the reduction routine does not affect the spectral signature)
# - one for range B (using dataB_BC_U that excude the CO2 signature)
# - one for range C (using dataC_BC_U that excude the libration modes)

# In[ ]:


#Data max from unreduced data in range A 

dataA_Max = pd.DataFrame.from_dict(
  dict(maxA0=DR1_A_df.T.iloc[0:].T.iloc[0:].max(axis=0), # min within rows 6000 - end
       maxA0i=DR1_A_df.T.iloc[0:].T.iloc[0:].idxmax(axis=0),  

        )
)

#Data max from Baseline Corrected Data in range A 

dataA_BC_Max = pd.DataFrame.from_dict(
  dict(maxA=dataA_BC.T.iloc[1:].T.iloc[1:].max(axis=0), # min within rows 6000 - end
       maxAi=dataA_BC.T.iloc[1:].T.iloc[1:].idxmax(axis=0),  

        )
)

#Data max from Baseline Corrected Data in range B

dataB_BC_Max = pd.DataFrame.from_dict(
  dict(maxB=dataB_BC_U.T.iloc[1:].T.iloc[1:].max(axis=0), # min within rows 6000 - end
       maxBi=dataB_BC_U.T.iloc[1:].T.iloc[1:].idxmax(axis=0),  

        )
)

#Data max from Baseline Corrected Data in range C

dataC_BC_Max = pd.DataFrame.from_dict(
  dict(maxC=dataC_BC_U.T.iloc[1:].T.iloc[1:].max(axis=0), # min within rows 6000 - end
       maxCi=dataC_BC_U.T.iloc[1:].T.iloc[1:].idxmax(axis=0),  

        )
)



# In[ ]:


dataA_BC_Max


# In[ ]:


#dataA_Max


# ### Clean 

# Describe

# In[ ]:


wavelength = All_RAW_df.T.iloc[0]

# A DR2

dataA_BC_Max = dataA_BC_Max.reset_index()
dataA_BC_Max['Name'] = dataA_BC_Max['index']
dataA_BC_Max = dataA_BC_Max.T.iloc[1:].T

dataA_BC_Max1 = dataA_BC_Max.set_index('maxAi',drop=True)
dataA_BC_Max2 = dataA_BC_Max1.join(wavelength, on='maxAi')
dataA_BC_Max2 = dataA_BC_Max2.reset_index()
dataA_BC_Max_F = dataA_BC_Max2.set_index(dataA_BC_Max.index)
dataA_BC_Max_F.rename(columns={'Wavenumber': 'maxAw'}, inplace=True)

# A DR1

dataA_Max = dataA_Max.reset_index()
dataA_Max['Name'] = dataA_Max['index']
dataA_Max = dataA_Max.T.iloc[1:].T

dataA_Max1 = dataA_Max.set_index('maxA0i',drop=True)
dataA_Max2 = dataA_Max1.join(wavelength, on='maxA0i')
dataA_Max2 = dataA_Max2.reset_index()
dataA_Max_F = dataA_Max2.set_index(dataA_Max.index)
dataA_Max_F.rename(columns={'Wavenumber': 'maxA0w'}, inplace=True)

# B DR2



dataB_BC_Max = dataB_BC_Max.reset_index()
dataB_BC_Max['Name'] = dataB_BC_Max['index']
dataB_BC_Max = dataB_BC_Max.T.iloc[1:].T

dataB_BC_Max1 = dataB_BC_Max.set_index('maxBi',drop=True)
dataB_BC_Max2 = dataB_BC_Max1.join(wavelength, on='maxBi')
dataB_BC_Max2 = dataB_BC_Max2.reset_index()
dataB_BC_Max_F = dataB_BC_Max2.set_index(dataB_BC_Max.index)
dataB_BC_Max_F.rename(columns={'Wavenumber': 'maxBw'}, inplace=True)

# C DR2

dataC_BC_Max = dataC_BC_Max.reset_index()
dataC_BC_Max['Name'] = dataC_BC_Max['index']
dataC_BC_Max = dataC_BC_Max.T.iloc[1:].T

dataC_BC_Max1 = dataC_BC_Max.set_index('maxCi',drop=True)
dataC_BC_Max2 = dataC_BC_Max1.join(wavelength, on='maxCi')
dataC_BC_Max2 = dataC_BC_Max2.reset_index()
dataC_BC_Max_F = dataC_BC_Max2.set_index(dataC_BC_Max.index)
dataC_BC_Max_F.rename(columns={'Wavenumber': 'maxCw'}, inplace=True)


# In[ ]:


#dataA_Max_F


# ___Insert column scan number___ 

# to be able to link data_annex with XP_Ramp_df

# In[ ]:


nscan = len(list(dataA_BC_Max_F.index.values.tolist()))
scan_number = pd.Series(range(1,nscan+1))
scan_number.astype(int)


# In[ ]:


dataA_BC_Max_F['scan_number'] = scan_number


# In[ ]:


#dataA_BC_Max_F


# In[ ]:


#dataB_BC_Max_F


# In[ ]:


#dataC_BC_Max_F


# ___Insert column Time stamp ?___

# add time stamp for scan where interuption of T ramp 
# 
# 2 time stamp:
# - real time
# - relative time
# 
# Check the possibility for input type implementation
# 
# [Slack Overflow time stamp insertion](https://stackoverflow.com/questions/36932759/pandas-adding-new-column-to-dataframe-which-is-a-copy-of-the-index-column)

# create two empty column type datetime
# 
# May be best to implement in excell when need be

# In[ ]:


#data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")


# In[ ]:


#data_anex_df


# Find a way to display entirely and scroll within 
# 
# 
# 
#  $\color{red}{\text{Implement Observation on lab-book}}$
#  
#   - Max A 

# In[ ]:


#data_anex_df['Real_T'] = scan_number


# In[ ]:


#dt_string = "{}_"+str(input('Enter date(hh-mm): ')).format(date)


# In[ ]:


#dt_string


# In[ ]:


#dt_object1 = datetime.strptime(dt_string, "%Y_%m_%d_%H%M")
#print("dt_object1 =", dt_object1)


# ###  Append to data Annex

# In[ ]:


#data_anex_df


# In[ ]:


data_anex_df = pd.merge(data_anex_df, dataA_BC_Max_F, on="Name")


# In[ ]:


data_anex_df = pd.merge(data_anex_df, dataA_Max_F, on="Name")


# In[ ]:


data_anex_df = pd.merge(data_anex_df, dataB_BC_Max_F, on="Name")


# In[ ]:


data_anex_df = pd.merge(data_anex_df, dataC_BC_Max_F, on="Name")


# In[ ]:


#data_anex_df 


# ## <u>Plotting</u> 

# ### Full range 

# In[ ]:


nscan = len(list(dataA_BC.columns.values.tolist()))

ymax =   data_anex_df.iloc[1:,16].astype(float).max()
ymin =   data_anex_df.iloc[1:,16].astype(float).min()
ymax2 = ymax + 0.01
ymin2 = ymin - 0.01 


# In[ ]:


nscan = len(list(All_RAW_df.columns.values.tolist()))

print(nscan)


fig= plt.figure(figsize=(12,6))


normalize = mcolors.Normalize(vmin=0, vmax=nscan)
colormap = cm.jet
i=1

for i in range(1,nscan):
    
    plt.plot(All_data_BC.Wavenumber, All_data_BC['{}_{}_{}'.format(spl, date, i)], color=colormap(normalize(i)))
    
    i=+1
    

plt.title('DR2 Baseline Corrected {0}'.format(date))
plt.axis([4000,800,-0.05,0.45])
plt.xlabel('Wavenumber (cm-1)').set_fontsize(13)
plt.ylabel('Absorbance').set_fontsize(13)
#ax = fig.gca()
plt.grid()
#plt.legend()

scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nscan)
plt.colorbar(scalarmappaple)

#plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_Full-range.png'.format(XP, date, date))

plt.show()


# ###  Oh stretch

# #### Baseline correction

# Insert in legend parameters of BC from data_annex

# In[ ]:


nscan = len(list(dataA_BC.columns.values.tolist()))

nscan2 = nscan//int(2)
nscan1 = nscan2*int(5)

figure, panels = plt.subplots(figsize=(12, nscan1), ncols=2, nrows=nscan2)

for panel, column in zip(panels.flatten(), dataA_BC.columns[1:]):
    panel.plot(dataA_BC.Wavenumber, dataA_BC[column], label="data")
    panel.plot(dataA_BC.Wavenumber, backgroundsA[column], ls="dashed",  label="bg")

    panel.plot(dataA_BC.Wavenumber, dataA_BC[column]+ backgroundsA[column], ls="dotted",  label="data+bg (RAW)")

    
    
    #panel.legend()
    panel.set_xlabel("wavenumber")
    panel.invert_xaxis()
    panel.set_title(column)
    panel.legend()
    
    plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_BCA.png'.format(XP, date, date))

    
plt.show()
    
    
#plt.tight_layout()
    


# ####  All scans 

# (using scan number - All data)
# <br>
# Idea for later : plot OH and maxA together
# 
# [Marker modification](https://matplotlib.org/stable/api/markers_api.html)

# In[ ]:


nscan = len(list(All_RAW_df.columns.values.tolist()))

print(nscan)


fig= plt.figure(figsize=(10,8))


normalize = mcolors.Normalize(vmin=0, vmax=nscan)
colormap = cm.jet
i=1

for i in range(1,nscan):
    
    plt.plot(dataA_BC.Wavenumber, dataA_BC['{}_{}_{}'.format(spl, date, i)], color=colormap(normalize(i)))
    
    i=+1
    

plt.title('DR2-A Baseline Corrected {0}'.format(date))
plt.axis([3800,2800,0,ymax2])
plt.xlabel('Wavenumber (cm-1)').set_fontsize(13)
plt.ylabel('Absorbance').set_fontsize(13)
#ax = fig.gca()
#plt.grid()
plt.legend()

scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nscan)
plt.colorbar(scalarmappaple)

plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_A.png'.format(XP, date, date))

plt.show()


# #### 2.4.A.4b All scans (using dictionnary vale - discrete T)

# later

# #### 2.4.A.4 Max Absorbance (peak frequency shift) - Clean

# In[ ]:


fig= plt.figure(figsize=(10,8))

for keys, values in Tdictionary.items():

    plt.plot(keys, data_anex_df.iloc[values,17], '+', mew=3, ms=12, c=cm.jet(values/nscan),label= str(keys)+" - "+str(values+1)+" - "+str(int(data_anex_df.iloc[values,17])))
    plt.plot(keys, data_anex_df.iloc[values,21], '.', mew=3, ms=12, c=cm.jet(values/nscan),label= str(keys)+" - "+str(values+1)+" - "+str(int(data_anex_df.iloc[values,21])))

plt.title('{0} DR2 OH stretch Peak frequency (DR1-DR2 comparison)'.format(date))
#plt.axis([3210,3270])
plt.xlabel('Temperature (K)').set_fontsize(13)
plt.ylabel('Peak frequency (cm-1)').set_fontsize(13)
#ax = fig.gca()
#plt.grid()
plt.legend()


plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_PeakA-frequency_wA0.png'.format(XP, date, date))

plt.show()


# #### 2.4.A.5 Max Absorbance (peak frequency shift) - Isotherm 1

# In[30]:


if Iso == True:

    fig = plt.figure(figsize=(8,6))

    for keys, values in Isodic1.items():

        plt.plot(keys, data_anex_df.iloc[values,17], '+', mew=3, ms=12, c=cm.jet(values/nscan),label= str(keys)+" - "+str(values+1)+" - "+str(int(data_anex_df.iloc[values,17])))
        
    plt.title('{0} DR2 OH stretch Peak frequency Isotherm at {1} K'.format(date,Tiso1))
    #plt.axis([3210,3270])
    plt.xlabel('Time (h)').set_fontsize(13)
    plt.ylabel('Peak frequency (cm-1)').set_fontsize(13)
    ax = fig.gca()
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))    
    #plt.grid()
    #plt.legend()


    #plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_PeakA-frequency_Iso_{}.png'.format(XP, date, date, Tiso1))

    plt.show()


# In[ ]:


if Iso == True:

    fig = plt.figure(figsize=(8,6))

    for keys, values in Isodic1.items():

        plt.plot(keys, data_anex_df.iloc[values,16], '+', mew=3, ms=12, c=cm.jet(values/nscan),label= str(keys)+" - "+str(values+1)+" - "+str(int(data_anex_df.iloc[values,17])))
        
    plt.title('{0} DR2 Max A Isotherm at {1} K'.format(date,Tiso1))
    #plt.axis([3210,3270])
    plt.xlabel('Time (h)').set_fontsize(13)
    plt.ylabel('Peak frequency (cm-1)').set_fontsize(13)
    ax = fig.gca()
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))    
    #plt.grid()
    #plt.legend()


    plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_max_A_Iso_{}.png'.format(XP, date, date, Tiso1))

    plt.show()


# ###  2.4.B Comb Bands

# #### 2.4.B.1 Baseline correction

# In[ ]:


nscan = len(list(dataB_BC.columns.values.tolist()))

nscan2 = nscan//int(2)
nscan1 = nscan2*int(5)

figure, panels = plt.subplots(figsize=(10, nscan1), ncols=2, nrows=nscan2)

for panel, column in zip(panels.flatten(), dataB_BC.columns[1:]):
    panel.plot(dataB_BC.Wavenumber, dataB_BC[column], label="data")
    panel.plot(dataB_BC.Wavenumber, backgroundsB[column], ls="dashed",  label="bg")

    panel.plot(dataB_BC.Wavenumber, dataB_BC[column] + backgroundsB[column], ls="dotted",  label="data+bg (RAW)")

    
    
    #panel.legend()
    panel.set_xlabel("wavenumber")
    panel.set_title(column)
    panel.invert_xaxis()
    panel.legend()
    
    plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_BCB.png'.format(XP, date, date))

    
plt.show()
    
    
#plt.tight_layout()
    


# #### 2.4.B.2 Backgrounds

# In[ ]:





# #### 2.4.B.3 All scans

# In[ ]:


nscan = len(list(All_RAW_df.columns.values.tolist()))

print(nscan)


f,(ax,ax2) = plt.subplots(1,2,sharey=True)



normalize = mcolors.Normalize(vmin=0, vmax=nscan)
colormap = cm.jet

i=1

for i in range(1,nscan):
    
    ax.plot(dataB_BC_U.Wavenumber, dataB_BC_U['{}_{}_{}'.format(spl, date, i)], color=colormap(normalize(i)))
    ax2.plot(dataB_BC_U.Wavenumber, dataB_BC_U['{}_{}_{}'.format(spl, date, i)], color=colormap(normalize(i)))
    
    i=+1
    

ax.set_xlim(2800,2390)
ax2.set_xlim(2290,1900)

ax.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)

ax.yaxis.tick_left()
ax2.yaxis.set_visible(False)

d = .022 # how big to make the diagonal lines in axes coordinates
# arguments to pass plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((1-d,1+d), (-d,+d), **kwargs)
ax.plot((1-d,1+d),(1-d,1+d), **kwargs)

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d,+d), (1-d,1+d), **kwargs)
ax2.plot((-d,+d), (-d,+d), **kwargs)

f.subplots_adjust(wspace=.070)

plt.title('DR2-B Baseline Corrected {0}'.format(date))
#plt.axis([2800,1900,0,0.015])
#plt.xlabel('Wavenumber (cm-1)').set_fontsize(13)
#plt.ylabel('Absorbance').set_fontsize(13)
#ax = fig.gca()
#plt.grid()
#plt.legend()

scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nscan)
plt.colorbar(scalarmappaple)

plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_B.png'.format(XP, date, date))

plt.show()


# #### 2.4.B.4 Max A + Redshift

# In[ ]:


fig= plt.figure(figsize=(10,8))

for keys, values in Tdictionary.items():

    plt.plot(keys, data_anex_df.iloc[values,24], '+', mew=3, ms=12, c=cm.jet(values/nscan),label= str(keys)+" - "+str(values+1)+" - "+str(int(data_anex_df.iloc[values,24])))
    #plt.plot(keys, data_anex_df.iloc[values,21], '.', mew=3, ms=12, c=cm.jet(values/nscan),label= str(keys)+" - "+str(values+1)+" - "+str(int(data_anex_df.iloc[values,21])))

plt.title('{0} DR2_B Peak frequency'.format(date))
#plt.axis([3210,3270])
plt.xlabel('Temperature (K)').set_fontsize(13)
plt.ylabel('Peak frequency (cm-1)').set_fontsize(13)
#ax = fig.gca()
#plt.grid()
plt.legend()


plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_PeakB-frequency.png'.format(XP, date, date))

plt.show()


# ###  2.4.C Bending

# #### 2.4.B.1 Baseline correction

# In[ ]:


nscan = len(list(dataC_BC.columns.values.tolist()))

nscan2 = nscan//int(2)
nscan1 = nscan2*int(5)

figure, panels = plt.subplots(figsize=(12, nscan1), ncols=2, nrows=nscan2)

for panel, column in zip(panels.flatten(), dataC_BC.columns[1:]):
    panel.plot(dataC_BC.Wavenumber, dataC_BC[column], label="data")
    panel.plot(dataC_BC.Wavenumber, backgroundsC[column], ls="dashed",  label="bg")

    panel.plot(dataC_BC.Wavenumber, dataC_BC[column]+ backgroundsC[column], ls="dotted",  label="data+bg")

    
    
    #panel.legend()
    panel.set_xlabel("wavenumber")
    panel.invert_xaxis()
    panel.set_title(column)
    panel.legend()
    
    plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_BCC.png'.format(XP, date, date))

    
plt.show()
    
    
#plt.tight_layout()
    


# #### 2.4.B.2 Backgrounds

# In[ ]:





# #### 2.4.B.3 All scans

# In[ ]:


nscan = len(list(dataC_BC.columns.values.tolist()))

ymax =   data_anex_df.iloc[1:,23].astype(float).max()
ymin =   data_anex_df.iloc[1:,23].astype(float).min()
ymax2 = ymax + 0.005
ymin2 = ymin - 0.01 


# In[ ]:


nscan = len(list(All_RAW_df.columns.values.tolist()))

print(nscan)


fig= plt.figure(figsize=(10,8))


normalize = mcolors.Normalize(vmin=0, vmax=nscan)
colormap = cm.jet
i=1

for i in range(1,nscan):
    
    plt.plot(dataC_BC.Wavenumber, dataC_BC['{}_{}_{}'.format(spl, date, i)], color=colormap(normalize(i)))
    
    i=+1
    

plt.title('DR2-C Baseline Corrected {0}'.format(date))
plt.axis([1900,800,0,0.06])
plt.xlabel('Wavenumber (cm-1)').set_fontsize(13)
plt.ylabel('Absorbance').set_fontsize(13)
#ax = fig.gca()
#plt.grid()
plt.legend()

scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nscan)
plt.colorbar(scalarmappaple)

plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_C.png'.format(XP, date, date))

plt.show()


# Plot the unreduced (BC) scans to see if a polynomial would be better

# In[ ]:


nscan = len(list(All_RAW_df.columns.values.tolist()))

print(nscan)


fig= plt.figure(figsize=(10,8))


normalize = mcolors.Normalize(vmin=0, vmax=nscan)
colormap = cm.jet
i=1

for i in range(1,nscan):
    
    plt.plot(dataC_BC_U.Wavenumber, dataC_BC_U['{}_{}_{}'.format(spl, date, i)], color=colormap(normalize(i)))
    
    i=+1
    

plt.title('DR2-A Baseline Corrected {0}'.format(date))
plt.axis([1900,1030,0,0.06])
plt.xlabel('Wavenumber (cm-1)').set_fontsize(13)
plt.ylabel('Absorbance').set_fontsize(13)
#ax = fig.gca()
#plt.grid()
plt.legend()

scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(nscan)
plt.colorbar(scalarmappaple)

plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_C_U.png'.format(XP, date, date))

plt.show()


# #### 2.4.B.4 Max A + Redshift

# In[ ]:





# #### 2.4.B.4 Max A, per temperature

# In[ ]:





# # <span style='background :yellow' > $\color{green}{\text{DR3 : Normalisation}}$ </span>

# ## 3.1 <u>Integration</u> 

# In the following we are going to integrate the spectra between two borns with the trapezoidal integration technique

# ### Function definition

# In[ ]:


# this function computes the inegral of the scan of index index, between borns 1 and 2 (in cm-1)

def integration(index, data, wavelength, born_1, born_2):

    nwl = len(wavelength) #number of wavelenght - spectra resolution

    list_names =  list(data.columns.values.tolist())
    
    scan_place = 0
    
    for i in range(len(list_names)):
        
        name_corr = list_names[i].split('_')
        
        if int(name_corr[-1]) == index:
    
            scan_place = i
    
    scan = data.T.iloc[scan_place]
        
    index_born_1 = 0
    index_born_2 = 0
    
    for iwl in range(nwl):
        
        if abs(wavelength[iwl] - born_1) < 0.5:
            
            index_born_1 = iwl
    
        elif abs(wavelength[iwl] - born_2) < 0.5:
            
            index_born_2 = iwl
    
    area = 0
    
    for iint in range(index_born_1, index_born_2):
        
        d_area = 0.5*(scan[iint]+scan[iint+1])*(wavelength[iint+1]-wavelength[iint])
    
        area = area + d_area
        
    return area


# ### 3.1.A Oh stretch

# In[ ]:


#range A
wavelengthA = dataA_BC.T.iloc[0]
wavelengthA = wavelengthA.reset_index(drop=True)


# In[ ]:


#wavelengthA


# In[ ]:


#range A
dataA_BC_I = dataA_BC.T.iloc[1:].T
dataA_BC_I = dataA_BC_I.reset_index(drop=True)


# In[ ]:


dataA_BC_I


# In[ ]:


nscan = len(list(dataA_BC_I.columns.values.tolist()))

areas = numpy.zeros(nscan)
areasBCA = numpy.zeros(nscan)

times = numpy.zeros(nscan)

for iint in range(0, nscan):
    
    #areas[iint] = integration(iint+1, data, wavelength, 2900, 3900)
    areasBCA[iint] = integration(iint+1, dataA_BC_I, wavelengthA, 2800, 4000)
    #times[iint] = 15*iint
    


# In[ ]:


areasBCA


# ### 3.1.B Bending Modes

# In[ ]:


#range C (think to supress libration mode contribution!)
wavelengthC = dataC_BC_U.T.iloc[0]
wavelengthC = wavelengthC.reset_index(drop=True)


# In[ ]:


wavelengthC


# In[ ]:


#range C
dataC_BC_I = dataC_BC_U.T.iloc[1:].T
dataC_BC_I = dataC_BC_I.reset_index(drop=True)


# In[ ]:


dataC_BC_I


# In[ ]:


nscan = len(list(dataC_BC_I.columns.values.tolist()))

areas = numpy.zeros(nscan)
areasBCC = numpy.zeros(nscan)

times = numpy.zeros(nscan)

for iint in range(0, nscan):
    
    #areas[iint] = integration(iint+1, data, wavelength, 2900, 3900)
    areasBCC[iint] = integration(iint+1, dataC_BC_I, wavelengthC, 1040, 1900)
    #times[iint] = 15*iint
    


# In[ ]:


areasBCC


# ### 3.1.4 Clean 

# In[ ]:


#range A

areasBCA_df = pd.DataFrame({ 'File number': dataA_BC_I.iloc[0,:], 'Int_A': areasBCA[:]})
areasBCA_df = areasBCA_df.T.iloc[1:].T

areasBCA_df = areasBCA_df.reset_index()
areasBCA_df['Name'] = areasBCA_df['index']
areasBCA_df= areasBCA_df.T.iloc[1:].T

#range C

areasBCC_df = pd.DataFrame({ 'File number': dataC_BC_I.iloc[0,:], 'Int_C': areasBCC[:]})
areasBCC_df = areasBCC_df.T.iloc[1:].T

areasBCC_df = areasBCC_df.reset_index()
areasBCC_df['Name'] = areasBCC_df['index']
areasBCC_df= areasBCC_df.T.iloc[1:].T


# In[ ]:


#areasBCA_df


# In[ ]:


#areasBCC_df


# ### 3.1.A.2 Ethane peaks integration

# Integration of ethane peaks:
# 
# create if statement spl = C2H6, C2H6_ASW ...
# 
# Integrate over specified range (?)
# 
# Do I need another baseline correction to make the ethane peak region flat ? To check

# In[ ]:





# ### 3.1.5 Append to data Annex

# In[ ]:


data_anex_df = pd.merge(data_anex_df, areasBCA_df, on="Name")


# In[ ]:


data_anex_df = pd.merge(data_anex_df, areasBCC_df, on="Name")


# In[ ]:


data_anex_df


# ### 3.1.6 Plotting

# #### Dict values

# In[ ]:


fig= plt.figure(figsize=(8,6))

for keys, values in Tdictionary.items():

    plt.plot(keys, data_anex_df.iloc[values,28], '+', mew=3, ms=12, c=cm.jet(values/nscan),label= str(keys)+" - "+str(values+1)+" - "+str(int(data_anex_df.iloc[values,28])))    

plt.title('{0} DR3 Integration '.format(date))
#plt.axis([3210,3270])
plt.xlabel('Temperature (K)').set_fontsize(13)
plt.ylabel('OH stretch Integration (AU)').set_fontsize(13)
#ax = fig.gca()
#plt.grid()
plt.legend()


plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_PeakA-Integration.png'.format(XP, date, date))

plt.show()


# #### Dict values

# In[ ]:


if Iso == True:   
    
    fig= plt.figure(figsize=(8,6))

    for keys, values in Isodic1.items():

        plt.plot(keys, data_anex_df.iloc[values,28], '+', mew=3, ms=12, c=cm.jet(values/nscan),label= str(keys)+" - "+str(values+1)+" - "+str(int(data_anex_df.iloc[values,28])))    

    plt.title('{0} DR3 Integration Iso {1}  '.format(date, Tiso1))
    #plt.axis([3210,3270])
    plt.xlabel('Time (h)').set_fontsize(13)
    plt.ylabel('OH stretch Integration (AU)').set_fontsize(13)
    ax = fig.gca()
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))  
    #plt.grid()
    #plt.legend()


    plt.savefig('D:\DATA-Processing\PAC\{}/Samples/{}/Plots/DR/DR2_{}_PeakA-Integration_Iso_{}.png'.format(XP, date, date, Tiso1))

    plt.show()


# ## 3.2 <u>Column Density Calculation </u>

# ### 3.2.1 Theory

# To do

# ![Thick-calc-form-3.svg'](Thick-calc-form-3.svg)

# Blabla

# ![Thick-calc-form-4.svg'](Thick-calc-form-4.svg)

# ### 3.2.2 Normalisation factor 

# Dep_val_A correspond to the first value found in the column Int_A or C. This corrspond to the integration for from the deposition for all the samples

# In[ ]:


Dep_val_A = data_anex_df['Int_A'].values[0]

Dep_val_C = data_anex_df['Int_C'].values[0]


# In[ ]:


Dep_val_A 


# In[ ]:


Dep_val_C 


# ### 3.3 Optical depth Calcul

# ### 3.3.A Oh stretch

# Aa taken from ref ... Hagen 1981
# 
# Find more recent value

# In[ ]:


Aa = 2 * 10**(-16)


# In[ ]:


NA = Dep_val_A / Aa


# In[ ]:


NA


# ### 3.3.B Oh bend

# In[ ]:


Ac = 1.2 * 10**(-17)


# In[ ]:


NC = Dep_val_C / Ac


# In[ ]:


NC


# ### 3.3.C Comparison and analysis

# In[ ]:


comp = NA/NC * 100


# In[ ]:


comp


# ### 3.3.E Append to Ice_thickness_df

# Prior to the Reduction analysis, the laser-diode thickness notebook should have been performed and a csv being producing with he inputs. We will append the previously obtained data into this csv

# In[ ]:


Ice_thickness_df = pd.read_csv('D:\DATA-Processing\PAC\Ice_thickness.csv')


# In[ ]:


Ice_thickness_df


# In[ ]:


Ice_thickness_df.loc[Ice_thickness_df["Date"] == date, 'Na'] = NA 
Ice_thickness_df.loc[Ice_thickness_df["Date"] == date, 'Nc'] = NC 


# In[ ]:


#Ice_thickness_df


# In[ ]:


Ice_thickness_df.to_csv('D:\DATA-Processing\PAC\Ice_thickness.csv', index=False)


# ## 3.3 <u> Normalisation </u>

# 2 different normalisations
# - The 20K sample can be normalised with the first scan (ie the deposition)
# - The sample deposited at the higher T needs to be with normalised with respect to the Integration from the normalized scan (3.3?)  

# ### 20K depositions

# For 20K deposition no problem, we take the Integration value of the deposition and normalised through it
# 
# Insert if statement: if TRamp[:3] not Nan continue otherwise don`t perform normalisation

# In[ ]:


#Dep_val_A


#  $\color{red}{\text{Here we need to have a if statement that say that if the sample is deposited at 20K - norm factor = 100 / Dep_val_A, else, another notebook is run to get the Norm factor at the temperature of interest!}}$

# In[ ]:


if Tdep == "20":

    
    NormFactor = 100 / Dep_val_A
    print(NormFactor)
    
else:

    get_ipython().run_line_magic('run', '-i "HighTreduction.py"')
    print(mean_X)
    NormFactor = mean_X / Dep_val_A


# In[ ]:


NormFactor


#  $\color{red}{\text{Append Norm factor into sample thick csv}}$

# In[ ]:


dataA_N = dataA_BC_I * NormFactor


# Saanity Check:
#     
# - Insert wavenumber (before export)

# In[ ]:


dataA_N.insert(loc = 0,
          column = 'Wavenumber',
          value =  wavelengthA)

dataA_N


# ## Export as csv

# In[ ]:


dataA_N.to_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/DR3_{}_A.csv".format(XP,date,date))


# ## 3.4 <u>Integration II</u> 

# Purpose here is to integrate the normalised scan so we can have integration value for scans at higher temperature to use as normalisation value for scans deposited at higherrt temperature

# Supress wavenumber

# In[ ]:


dataA_N


# In[ ]:


dataA_N = dataA_N.T.iloc[1:].T


# In[ ]:


dataA_N


# In[ ]:


nscan = len(list(dataA_N.columns.values.tolist()))

areas = numpy.zeros(nscan)
areasBCA2 = numpy.zeros(nscan)

times = numpy.zeros(nscan)

for iint in range(0, nscan):
    
    #areas[iint] = integration(iint+1, data, wavelength, 2900, 3900)
    areasBCA2[iint] = integration(iint+1, dataA_N, wavelengthA, 2800, 4000)
    #times[iint] = 15*iint
    


# In[ ]:


areasBCA2


# In[ ]:


areasBCA2_df = pd.DataFrame({ 'File number': dataA_BC_I.iloc[0,:], 'Int_N_A': areasBCA2[:]})
areasBCA2_df = areasBCA2_df.T.iloc[1:].T
areasBCA2_df = areasBCA2_df.reset_index()
areasBCA2_df['Name'] = areasBCA2_df['index']
areasBCA2_df= areasBCA2_df.T.iloc[1:].T


# In[ ]:


#areasBCA2_df


# In[ ]:


data_anex_df = pd.merge(data_anex_df, areasBCA2_df, on="Name")


# ### High Temperature deposition

# For the higher temperature deposited, normalising through the deposition would not allowed a good comparison with the sample deposited at 20K. Hence, we will make an average of the normalised value (from Integration II) at the temperature of interest and use this value as a normalisation factor.<br>
# 
# We will use a separate notebook to to that that will run separately if need be

# # <span style='background :yellow' > $\color{green}{\text{DR4 : Cleaning and error analysis}}$ </span>

# ## 4.1 Export data_Anex as csv

# ## Insert time column

# <table><tr>
# <td>
#     
#  Id | Input | Why 
#  - | - | - 
#  0 | id | N/A 
#  1 | Name | N/A 
#  2 | min1 | N/A 
#  3 | index1 | N/A 
#  4 | min2 | N/A 
#  5 | index2 | N/A 
#  6 | min3 | N/A 
#  7 | index3 | N/A 
#  6 | min4 | N/A 
#  7 | index4 | N/A 
#     
# </td>
#     
# <td>
#     
# <p align="center" style="padding: 10px">
# Even if all sample don`t require a time stamp, for future concatenation it is import that all the data has same shape
# For loop iterate through scan number if scan number = input manually time in column, else = ''
# Insert manually for now   
# </p> 
#     
# </td>
#     
#   
# </tr></table>
# 
# 
# 
# 

# In[ ]:


#data_anex_df


# In[ ]:


data_anex_df.to_csv("D:\DATA-Processing\PAC\{}/Samples/{}/Data/DR/{}_data_annex.csv".format(XP,date,date), index=False)


# # 5. Sample specific reduction

# Link toward peculiar cases
# 
# - 02_09

# ## 02_09

# In[ ]:





# ## 4.2 Export result in web-page

# All the output are inserted onto a blank ? web page

# ### Common feature

# In[ ]:


f = open("D:\DATA-Processing\PAC\{}/Samples/{}/{}_DP.html".format(XP,date,date),'a')



message = """<html>
<head></head>
<body>

<h1>Data Reduction results</h1>

<p>Reduction performed:"""+str(date_jour) + """</p>

<h2>Full scan unreduced</h2>

<figure>
<a href="Plots\DR\DR1_"""+str(date) + """_Full-range.png" target="_blank"><image src="Plots\DR\DR1_"""+str(date) + """_Full-range.png" width=""  Id=""  alt=""/></a>      
<figcaption></figcaption>
</figure>

<p>Output</p>

<h2>Baseline corrected scan A</h2>

<figure>
<a href="Plots\DR\DR2_"""+str(date) + """_A.png" target="_blank"><image src="Plots\DR\DR2_"""+str(date) + """_A.png" width=""  Id=""  alt=""/></a>      
<figcaption></figcaption>
</figure>

<p>Output</p>

<h2>Baseline corrected scan B</h2>

<figure>
<a href="Plots\DR\DR2_"""+str(date) + """_B.png" target="_blank"><image src="Plots\DR\DR2_"""+str(date) + """_B.png" width=""  Id=""  alt=""/></a>      
<figcaption></figcaption>
</figure>

<p>Output</p>


<h2>Baseline corrected scan C</h2>

<figure>
<a href="Plots\DR\DR2_"""+str(date) + """_C.png" target="_blank"><image src="Plots\DR\DR2_"""+str(date) + """_C.png" width=""  Id=""  alt=""/></a>      
<figcaption></figcaption>
</figure>

<p>Output</p>


<h2>Range A frequency shift</h2>

<figure>
<a href="Plots\DR\DR2_"""+str(date) + """_PeakA-frequency_wA0.png" target="_blank"><image src="Plots\DR\DR2_"""+str(date) + """_PeakA-frequency_wA0.png" width=""  Id=""  alt=""/></a>      
<figcaption></figcaption>
</figure>

<p>Output</p>

<h2>Range A Integration</h2>

<figure>
<a href="Plots\DR\DR2_"""+str(date) + """_PeakA-Integration.png" target="_blank"><image src="Plots\DR\DR2_"""+str(date) + """_PeakA-Integration.png" width=""  Id=""  alt=""/></a>      
<figcaption></figcaption>
</figure>

<p>Output</p>

<h2>Range B frequency shift</h2>

<figure>
<a href="Plots\DR\DR2_"""+str(date) + """_PeakB-frequency.png" target="_blank"><image src="Plots\DR\DR2_"""+str(date) + """_PeakB-frequency.png" width=""  Id=""  alt=""/></a>      
<figcaption></figcaption>
</figure>

<p>Output</p>



</body>
</html>"""




f.write(message)
f.close()


# ### Specific feature

# #### Isotherms

# In[ ]:


if Iso == True:   
    
    f = open("D:\DATA-Processing\PAC\{}/Samples/{}/{}_DP.html".format(XP,date,date),'a')



    message = """<html>
    <head></head>
    <body>

    <h1>Isotherms</h1>

    <h2> """+str(Tiso1) + """ </h2>
    
    <article id="P1">
    
    <div>
    
    <h3>Peak frequency shift </h3>

    <figure>
    <a href="Plots/DR/DR2_"""+str(date) + """_PeakA-frequency_Iso_"""+str(Tiso1) + """.png" target="_blank"><image src="Plots/DR/DR2_"""+str(date) + """_PeakA-frequency_Iso_"""+str(Tiso1) + """.png" width=""  Id=""  alt=""/></a>      
    <figcaption></figcaption>
    </figure>

    <p>Output</p>

    </div>
    
    <div>
    
    <h3>Integration </h3>

    <figure>
    <a href="Plots/DR/DR2_"""+str(date) + """_PeakA-Integration_Iso_"""+str(Tiso1) + """.png" target="_blank"><image src="Plots/DR/DR2_"""+str(date) + """_PeakA-Integration_Iso_"""+str(Tiso1) + """.png" width=""  Id=""  alt=""/></a>      
    <figcaption></figcaption>
    </figure>

    <p>Output</p>

    </div>



    </article>




    </body>
    </html>"""




    f.write(message)
    f.close()


# In[ ]:




