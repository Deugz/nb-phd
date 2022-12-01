#!/usr/bin/env python
# coding: utf-8

# # DATA Analysis

# The purpose of this Notebook is to perform the data Analysis, that is comparing the outputs generated from the previous notebooks for all the different samples. 
# 
# 

# ### Packages installation (since Aug 2021)

# In[2]:


#pip install -U wxPython


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
from ipywidgets import interact, interactive, fixed, interact_manual
import re
from itertools import cycle
import wx



#%matplotlib notebook


# # 1. Data import and merging 

# In[ ]:





# ## 1.1 XP-Ramp

# In[2]:


spl = 'ASW'


# In[ ]:





# In[4]:


XP_Ramp_df = pd.read_csv('..\DATA\DATA-Processing\PAC\XP_list_test.csv')
XP_Ramp_df_I = XP_Ramp_df.set_index('Date')


# In[5]:


XP_Ramp_df_I.head(5)


# ## 1.2 DR1 - DR2 - DR3 all dates

#  DR1 - DR2 - DR3 are merged together

# ### 1.2.1 Import

# In[6]:


#DR1

DR1_Allscans = glob('..\DATA\DATA-Processing\PAC\XP_1-1/Samples/*/Data/DR/DR1_*_All-scans.csv')

# DR2

DR2_Allscans = glob('..\DATA\DATA-Processing\PAC\XP_1-1/Samples/*/Data/DR/DR2_*_All-scans.csv')

# DR3

DR3_Allscans = glob("..\DATA\DATA-Processing\PAC\XP_1-1/Samples/*\Data\DR\DR3_*_A.csv")


# #### Sanity Check

# In[8]:


DR1_Allscans


# In[9]:


#DR2_Allscans


# In[10]:


#DR3_Allscans


# ### 1.2.2 Merging

# #### DR1

# In[11]:


All_data_frame = []

for items in DR1_Allscans:

    df = pd.read_csv(items)
    df_1 = df.T.iloc[1:].T
    
    All_data_frame.append(df_1) 
    
    del df
    del df_1
    
    DR1_Allscans_full = reduce(lambda left,right: pd.merge(left,right, on=['Wavenumber'],how='outer'), All_data_frame)
    
    


# In[12]:


DR1_Allscans_full


# In[13]:


#DR1_Allscans_full.to_csv('..\DATA\DATA-Processing\PAC\DR1_full.csv')


# #### DR2

# In[16]:


All_data_frame = []

for items in DR2_Allscans:

    df = pd.read_csv(items)
    df_1 = df.T.iloc[1:].T
    
    All_data_frame.append(df_1) 
    
    del df
    del df_1
    
    DR2_Allscans_full = reduce(lambda left,right: pd.merge(left,right, on=['Wavenumber'],how='outer'), All_data_frame)
    
    


# In[17]:


#DR2_Allscans_full.to_csv('D:\DATA-Processing\PAC\DR2_full.csv')


# In[18]:


DR2_Allscans_full


#DR2_Allscans = glob("D:\PhD-WS\Projects\PAC\XP_1-1\DATA\*\Data\DR\DR2*All-scans.csv")


# In[19]:


DR2_Allscans_full


# In[20]:


print(DR2_Allscans_full['Wavenumber'])


# $\color{red}{\text{Problem with Row number (should be 6639)!}}$
# 

# #### DR3

# In[21]:


All_data_frame = []

#Wavenumber = 

for items in DR3_Allscans:

    df = pd.read_csv(items)
    df_1 = df.T.iloc[1:].T

    
    All_data_frame.append(df_1) 
    
    DR3_Allscans_full = reduce(lambda left,right: pd.merge(left,right, on=['Wavenumber'],how='outer'), All_data_frame)


# In[22]:


DR3_Allscans_full


# Row number --> OK :) (2490)

# In[23]:


#DR3_Allscans_full.to_csv('D:\DATA-Processing\PAC\DR3_full.csv')


# ## 1.3 Data_annex

# In[16]:


data_anex = glob("..\DATA\DATA-Processing\PAC\XP_1-1\Samples\*\Data\DR\**_data_annex.csv")


# In[17]:


data_anex


# ### 1.2.2 Merging

# concat, not append

# In[22]:


All_data_frame = []

for items in data_anex:

    df = pd.read_csv(items)
    #print(df)
    #df_1 = df.T.iloc[1:].T
    
    All_data_frame.append(df) 
    
print(All_data_frame)
    
    #del df
    #del df_1
    
data_anex_full = pd.concat(All_data_frame)
    
    


# In[23]:


data_anex_full


# In[24]:


data_anex_full.to_csv('..\DATA\DATA-Processing\PAC\Data_Annex_full.csv')


# # 2 Scans selection (Temperature - isotherms)

# Using I python widget
# 
# [I python widget list](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html)
# 
# [Widgets layout](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Styling.html)

# ## 2.1 Parameter list

# In[18]:


Temp = XP_Ramp_df_I.columns[1:].values.tolist()
Date = XP_Ramp_df_I.index.values.tolist()
Sample = XP_Ramp_df_I['Sample'].values.tolist()  


# ## 2.2 Widget selection

# the purpose of the widget is to select the data we want to plot using widget
# - create list
# 
# Document:
# 
# [I python widget list](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html)

# In[19]:


#Create Dropdown Box Widget
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

wS = widgets.SelectMultiple(
    options= Sample,
    description='Sample',
    disabled=False,
)

widgets.HBox([wS,wD, wT])



display(wT,wD,wS)


# In[ ]:


wT_L = list(wT.value)
wD_L = list(wD.value)


# ## Sanity Check

# In[ ]:


wT_L


# In[22]:


wD_L


# ## sample neme construction

# use list value to extract scan number and produce file name

# insert condition to supress first scan (ramp)

# In[23]:


#date = ['2020_09_16','2020_09_17']
#temp = ['60K','80K']
#spl = 'ASW'

z = []
value_1 = []

for x in wD_L:
    for y in wT_L:

        value = XP_Ramp_df_I.loc[XP_Ramp_df_I.index == x, y].values[0]
        value_1 = re.findall(r"[-+]?\d*\.\d+|\d+", value)
    
        for items in value_1:
        
            to_plot = str('{}_{}_{}'.format(spl, x, items))
            z.append({
                
               'Name' : str(to_plot),
               'Temp' : y,
               'Date' : x, 
                
          
         
         })
             


# In[24]:


z


# In[25]:


dat= pd.DataFrame(z)
data_df = dat.set_index('Name')


# In[26]:


data_df


# ## 1.1.4 Plot pre-formating

# ### Temperature

# Find a way to have a specific c=cmjet when we want to plot long isotherm data.

# In[27]:


def Temp_color(row):
    if row['Temp'] == '20K ':
        return int(1)
    if row['Temp'] == '30K ':
        return int(2) 
    elif row['Temp'] == '40K':
        return int(3)
    elif row['Temp'] == '50K':
        return int(4)
    elif row['Temp'] == '60K':
        return int(5)
    elif row['Temp'] == '70K':
        return int(6)
    elif row['Temp'] == '80K':
        return int(7)
    elif row['Temp'] == '90K':
        return int(8)
    elif row['Temp'] == '100K':
        return int(9)
    elif row['Temp'] == '110K':
        return int(10)
    elif row['Temp'] == '120K':
        return int(11)
    elif row['Temp'] == '125K':
        return int(12)
    elif row['Temp'] == '130K':
        return int(13)
    elif row['Temp'] == '132K':
        return int(14)
    elif row['Temp'] == '134K':
        return int(15)
    elif row['Temp'] == '135K':
        return int(16)
    elif row['Temp'] == '136K':
        return int(17)
    elif row['Temp'] == '137K':
        return int(18)
    elif row['Temp'] == '138K':
        return int(19)
    elif row['Temp'] == '140K':
        return int(20)
    elif row['Temp'] == '145K':
        return int(21)
    elif row['Temp'] == '150K':
        return int(21)
    elif row['Temp'] == '155K':
        return int(22)
    elif row['Temp'] == '160K':
        return int(23)
    elif row['Temp'] == '180K':
        return int(24)
    elif row['Temp'] == '200K':
        return int(25)


# In[28]:


data_df['Colour'] = data_df.apply (lambda row: Temp_color(row), axis=1)


# In[29]:


data_df


# In[ ]:





# ### Dates

# In[46]:


linestyle = ['-',':','--']


# 6 sample max

# In[47]:


LD = dict(zip(wD_L, linestyle))


# In[48]:


LD 


# In[49]:


data_df['linestyle'] = data_df['Date'].map(LD)


# In[50]:


data_df


# [Cycler methodology](https://matplotlib.org/stable/tutorials/intermediate/color_cycle.html#sphx-glr-tutorials-intermediate-color-cycle-py)
# 
# For plotting
# 
# [Seaborn library](https://seaborn.pydata.org/)
# 

# ### Could try Class attribute

# What do we want to do:
# 
# 
# Vocabulary:
# - Method = function associated with a class
# - Attributes = 
# 
# Class XP_Param is a blueprint to construct a list of sample that we want to plot based on the parameters enters with the widget.
# 
# One function should find within XP_Ramp_df_I the scan numbers associated with a peculiar date and temperature.
# A second function should build a string with the format spl_date_scan number and append it into a list
# 
# differences between instance variables and class variables ?

# # Plotting

# Purpose here is to plot from DR2_all scan the scan present in dat using Temp and date in the legend and use the groupping for formatting
# 
# Find way to implement label with respect to dataframe value (input for color ?)

# ## 3 different DR

# In[51]:


print(dat['Name'])


# In[52]:


nscan = len(list(data_df['Date'].values.tolist()))

print(nscan)

fig, ax= plt.subplots(figsize=(10,10))

#colors = sns.color_palette("coolwarm", data_df.Temp.nunique())
#ax.set_prop_cycle('color', colors)

#ax.set_prop_cycle(color =['b', 'g'])
#cc = (cycler(linestyle=['-', '--', '-.', ]))

for i in dat['Name']:
    
#DR2
    
    #x = DR2_Allscans_full.Wavenumber
    #y = DR2_Allscans_full['{}'.format(i)]

#`DR3

    x = DR3_Allscans_full.Wavenumber
    y = DR3_Allscans_full['{}'.format(i)]
    
    plt.plot(x,y, label="{}_{}".format(str(data_df.loc[i]['Date']), str(data_df.loc[i]['Temp'])), c=cm.jet(int(data_df.loc[i]['Colour'])/25), linestyle=(data_df.loc[i]['linestyle'])) 


#plt.title('{0} DR1 '.format(date))
plt.axis([3800,2800,0,0.45])
plt.xlabel('Wavenumber (cm-1)').set_fontsize(13)
plt.ylabel('Absorbance').set_fontsize(13)
#ax = fig.gca()
plt.grid()
plt.legend()


#plt.savefig('D:\PhD-WS\Projects\PAC\XP_1-1\DATA\{0}\Plots\DR1\DR1_{0}_All_scans.png'.format(date))

plt.show()


# ### Max Absorbance

# Import code from DR

# In[ ]:





# ### Other plotting

# In[53]:


# imports
get_ipython().run_line_magic('matplotlib', 'inline')

from ipywidgets import interactive
import pandas as pd
import numpy as np
# from jupyterthemes import jtplot

# Sample data
np.random.seed(123)
rows = 50
dfx = pd.DataFrame(np.random.randint(90,110,size=(rows, 1)), columns=['Variable X'])
dfy = pd.DataFrame(np.random.randint(25,68,size=(rows, 1)), columns=['Variable Y'])
dfz = pd.DataFrame(np.random.randint(60,70,size=(rows, 1)), columns=['Variable Z'])

df = pd.concat([dfx,dfy,dfz], axis = 1)
#jtplot.style()

import ipywidgets as widgets
from IPython.display import display

def multiplot(a):
    opts = df.columns.values
    df.loc[:, a].plot()

interactive_plot = interactive(multiplot, a=['Variable X', 'Variable Y', 'Variable Z'])
output = interactive_plot.children[-1]
output.layout.height = '350px'
interactive_plot


# In[ ]:





# ## Create class with widget input as variable 

# Embed Naming function
# 
# [Youtube tutorial on classes](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)

# In[54]:


class XP_Param:
    
    def found(self):
        print("input is" + self.column + self.row )
        return XP_Ramp_df_I.loc[self.row,self.column]
    

    


# In[55]:


T1 = XP_Param()
T1.column = "60K"
T1.row = "2020_09_21"


# In[56]:


T1.found()


# ## Name the desired sample

# Purpose here is to create a function that create sample name based on previously selected parameters (date / Temperature)

# ### Documentation

# [Interact function](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html#interactive)

# In[57]:


output_Date = wD.value


# In[58]:


# Define any function
def file_name(output_Date):
    return print(output_Date) 
    


# ### Plotting strategy

# 

# # Plotting

# ## Data from Data_Annex 

# ## Data from DR2

# ## Interactive Plotting

# In[ ]:





# [I python widget list](https://kapernikov.com/ipywidgets-with-matplotlib/)
# 
# 

# In[ ]:





# In[59]:


x = numpy.linspace(0, 2 * numpy.pi, 100)
 
fig, ax = plt.subplots()
line, = ax.plot(x, numpy.sin(x))
ax.grid(True)
 
def update(change):
    line.set_ydata(numpy.sin(change.new * x))
    fig.canvas.draw()
     

int_slider = widgets.IntSlider(
    value=1, 
    min=0, max=10, step=1,
    description='$\omega$',
    continuous_update=False
)
int_slider.observe(update, 'value')
int_slider


# ## wx GUI creation

# In[ ]:


import wx


# In[60]:


# Création d'un nouveau cadre, dérivé du wxPython 'Frame'.
class TestFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, -1, title, pos=(0, 0), size=(500, 200))

        # À l'intérieur du cadre, créer un panneau..
        panel = wx.Panel(self, -1)

        # Créer un texte dans le panneau
        texte = wx.StaticText(panel, -1, "Bonjour tout le monde!", wx.Point(10, 5), wx.Size(-1, -1))
                
        # Créer un bouton dans le panneau
        bouton = wx.Button(panel, -1, "Cliquez-moi!",  wx.Point(10, 35), wx.Size(-1, -1))
        # lier le bouton à une fonction:
        self.Bind(wx.EVT_BUTTON, self.creerDiag, bouton)
        
    # fonction qui affiche une boîte de dialogue
    def creerDiag(self, event):
        dlg = wx.MessageDialog(self, "Merci de m'avoir cliqué, ça fait du bien.",
          "Merci!", wx.ICON_EXCLAMATION | wx.YES_NO | wx.CANCEL)
        dlg.ShowModal()
        dlg.Destroy()
        

# Chaque application wxWidgets doit avoir une classe dérivée de wx.App
class TestApp(wx.App):
    def OnInit(self):
        frame = TestFrame(None, -1, "Test")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = TestApp(0) # créer une nouvelle instance de l'application
    app.MainLoop()   # lancer l'application


# In[61]:


app = wx.App()

frame = wx.Frame(None, title='Simple application')
frame.Show()

app.MainLoop()


# In[62]:


#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example, we create a submenu and a menu
separator.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')

        fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((900, 600))
        self.SetTitle('Data Analysis Plotting GUI')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()


# In[ ]:


#!/usr/bin/env python


"""
ZetCode wxPython tutorial

In this example we create a Go To class
layout with wx.BoxSizer.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Class Name')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Matching Classes')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=10)

        vbox.Add((-1, 25))

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        cb1 = wx.CheckBox(panel, label='Case Sensitive')
        cb1.SetFont(font)
        hbox4.Add(cb1)
        cb2 = wx.CheckBox(panel, label='Nested Classes')
        cb2.SetFont(font)
        hbox4.Add(cb2, flag=wx.LEFT, border=10)
        cb3 = wx.CheckBox(panel, label='Non-Project classes')
        cb3.SetFont(font)
        hbox4.Add(cb3, flag=wx.LEFT, border=10)
        vbox.Add(hbox4, flag=wx.LEFT, border=10)

        vbox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)


def main():

    app = wx.App()
    ex = Example(None, title='Go To Class')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()


# In[63]:


get_ipython().run_line_magic('load_ext', 'watermark')


# ## Package version for binder

# In[6]:


get_ipython().run_line_magic('watermark', '--iversions')


# In[2]:





# In[ ]:




