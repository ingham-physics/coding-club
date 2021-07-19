
# Coding Club - Dash

19/07/2021 - Daniel Al Mouiee

## Introduction to Dash

- [Dash Overview](https://dash.plotly.com/introduction)
#### Web dev
- [**Dash Core Components (DCC)**](https://dash.plotly.com/dash-core-components)
- [**Dash HTML Components (DHC)**](https://dash.plotly.com/dash-html-components)
- [**Dash Boostrap Components (DBC)**](https://dash-bootstrap-components.opensource.faculty.ai/)
- [**Plotly Express (PX)**](https://plotly.com/python/plotly-express/)
- [**Dash Datatable**](https://dash.plotly.com/datatable)
- [Dash DAQ](https://dash.plotly.com/daq)
- [Dash Canvas](https://dash.plotly.com/canvas)
- [Dash Slider](https://dash.plotly.com/slider)
#### Bioinformatics
- [Dash Bio](https://dash.plotly.com/datatable)
#### VTK
- [Dash VTK](https://dash.plotly.com/vtk)
#### Networks/Connective Graphs
- [Dash Cytoscape](https://dash.plotly.com/cytoscape)

## Installation
```
pip install dash
```
For Jupyter notebook development:
```
pip install jupyter-dash
```

## Dash building blocks
- Layout: 
    - [DCC](https://dash.plotly.com/dash-core-components), [DHC](https://dash.plotly.com/dash-html-components), [DBC](https://dash-bootstrap-components.opensource.faculty.ai/)
    - Application visual skeleton
    - Made up of HTML + CSS components
    - Good idea to give these components IDs to easily identify them in case of callback use cases 
- Graphs:
    - [PX](https://plotly.com/python/plotly-express/)

- Callback:
    - [Dash functions](https://dash.plotly.com/basic-callbacks) that are called when a trigger occurs (ie. clicking a button, scheduled intervals, dependent chaining, etc...)
    - Normal python function additional Output and Input (with optionally State) components defined with a ```@app.callback()``` decorator.


## VSC Extensions
- [Plotly Dash Snippets](https://marketplace.visualstudio.com/items?itemName=PlotlyDashSnippets.plotly-dash-snippets): suggests macro popups for predefined segments of Dash components, boilerplate and functional code 