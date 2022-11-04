# Style Guide

This section is a place where I keep track of the style of the Notebook (very important to be consistent through the whole notebook). 

a custom_css file is used to modify the titles.

### Legend

#### Notes

```{note}
:class: dropdown
The note body will be hidden!
```

```{warning}
- Here is a warning
```

:::{tip}
This text is **standard** _Markdown_
:::


#### Comments

Comments are made for me to directly communicate with the reader. 

***

Comment formatting 

***

<div class="alert alert-block alert-success">
<b>Questions:</b> aimed at my supervisors or potential referees.
</div>

<div class="alert alert-block alert-warning">
<b>Basic notes: </b> This is for me to highligt my thoughts during the writing process.
</div>

<div class="alert alert-block alert-danger">
<b>Important notes:</b> Same as above but with an high importance level
</div>

<div class="alert alert-block alert-info">
<b>Teaching notes:</b> This is for me to "speak" to a potential tierce audience.
</div>

### HTML Symbol

 [Symbol list](https://www.w3schools.com/charsets/ref_utf_arrows.asp)

#### Used

- &#9989; - ticked box
- &#x274C; - red cross

- &#x2192; - right arrow
- &#x0394; - delta
- &rho; - rho
- &#8826; - inferior

- &#127773; - happy emoji


#### Other intersting feature of JupyterBook

##### Margin content

The content on the right will be located in the margin

```
:figclass: margin
```

```{figure} Docs/M-X1178.png
:figclass: margin
---
name: Mould X1178
---
Mould X1178 
```

##### Panels

````{panels}

title 1
^^^^^^^^^^^^^^

panel 1

---

title 2
^^^^^^^^^^^^^^

panel 2

````

There is ways to modify the formatting of the panel:
- include link

#### Tables

Best method to produce table is to use html. Here is a website to produce such html table:

-  [Web-site](https://www.tablesgenerator.com/html_tables)
    - Copy/Paste html and css directly into the notebook.
    - Produce a .TGN file that can be loaded and modified.

#### Cards

need the instalation of sphinx-design extension

````{card} Card 1 title

Card header 1
^^^
Card body 1
+++
Card footer 1
````


::::{grid}
:gutter: 3

:::{grid-item-card} One!
Here's the first card.
:::

:::{grid-item-card} Two!
Here's the second card.
:::

:::{grid-item-card} Three!
Here's the third card.
:::
::::

##### Card caroussel

::::{card-carousel} 2

:::{card} card 1
content
:::
:::{card} card 2
Longer

content
:::
:::{card} card 3
:::
:::{card} card 4
:::
:::{card} card 5
:::
:::{card} card 6
:::
::::