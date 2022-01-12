#!/usr/bin/env python
# coding: utf-8

# # JupyterDash
# The `jupyter-dash` package makes it easy to develop Plotly Dash apps from the Jupyter Notebook and JupyterLab.
# 
# Just replace the standard `dash.Dash` class with the `jupyter_dash.JupyterDash` subclass.

# In[21]:


port = 8050


# In[22]:


# in case we use Colab
#!pip install jupyter-dash

from jupyter_dash import JupyterDash


# In[23]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


# In[24]:


import plotly.graph_objs as go
from dash.dependencies import Input, Output


# In[25]:


import dash_bootstrap_components as dbc


# When running in JupyterHub or Binder, call the `infer_jupyter_config` function to detect the proxy configuration.

# In[26]:


#JupyterDash.infer_jupyter_proxy_config()


# Construct the app

# In[27]:


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets=[dbc.themes.BOOTSTRAP]
app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

# Create server variable with Flask server object for use with gunicorn
server = app.server


# In[28]:


colors = {
    'background': 'grey',
    'text': 'blue'
}


# Load and preprocess data

# In[29]:


df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
#df
available_indicators = df[['Indicator Name']].copy()
available_indicators = available_indicators.drop_duplicates()
available_indicators


# In[30]:


ii = [{'label': i, 'value': i} for i in available_indicators]
ii


# In[31]:


available_indicators = df[['Indicator Name']].copy()
available_indicators = available_indicators.drop_duplicates()
available_indicators['label'] = available_indicators['Indicator Name']
available_indicators['value'] = available_indicators['Indicator Name']
#value_default = 'Fertility rate, total (births per woman)'
#menu_id_var = 'crossfilter-xaxis-column'
#available_indicators = available_indicators.drop(['Indicator Name'], axis=1)
available_indicators_dict = available_indicators[['label','value']].to_dict('records')
available_indicators_dict


# In[32]:


linearorlog_dict = [{'label': i, 'value': i} for i in ['Linear', 'Log']]
linearorlog_dict


# Set up layout

# from layout.my_layout import app_layout

# In[33]:


slider_row = dbc.Row(dbc.Col(html.Div(dcc.Slider(
        id='crossfilter-year--slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'].max(),
        marks={str(year): str(year) for year in df['Year'].unique()},
        step=None
)),style={'backgroundColor': colors['background']},width=6))
#app.layout = slider_row
#app.run_server(mode="inline")


# In[34]:


top_menu_row = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div(
            dcc.Dropdown(
                id='crossfilter-xaxis-column',
                options=available_indicators_dict,
                value='Fertility rate, total (births per woman)'
            )),width=6),
        dbc.Col(html.Div(
            dcc.Dropdown(
                id='crossfilter-yaxis-column',
                options=available_indicators_dict,
                value='Life expectancy at birth, total (years)'
            )),width=6)]),
            
    dbc.Row([
        dbc.Col(html.Div(dcc.RadioItems(
                id='crossfilter-xaxis-type',
                options=linearorlog_dict,
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )),width=6),
        dbc.Col(html.Div(dcc.RadioItems(
                    id='crossfilter-yaxis-type',
                    options=linearorlog_dict,
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )),width=6)])
        ],style={'backgroundColor': colors['background']}, fluid=True)
#app.layout = top_menu_row
#app.run_server(mode="inline")


# In[35]:


graph_layout = dbc.Container([dbc.Row([
    dbc.Col([
        dcc.Graph(
            id='crossfilter-indicator-scatter',
            hoverData={'points': [{'customdata': 'Japan'}]}
        )
    ]),
    dbc.Col([
        dcc.Graph(id='x-time-series'),
        dcc.Graph(id='y-time-series'),
    ])])],style={'backgroundColor': colors['background']}, fluid=True)

#app.layout = graph_layout
#app.run_server(mode="inline")


# In[36]:


app_layout = dbc.Container([
        top_menu_row,
        graph_layout,
        slider_row
],style={'backgroundColor': colors['background']},fluid=True)


# In[37]:


app.layout = app_layout


# In[38]:


def create_time_series(dff, axis_type, title):
    return {
        'data': [dict(
            x=dff['Year'],
            y=dff['Value'],
            mode='lines+markers'
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': title
            }],
            'yaxis': {'type': 'linear' if axis_type == 'Linear' else 'log'},
            'xaxis': {'showgrid': False}
        }
    }


# In[39]:


@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df[df['Year'] == year_value]

    return {
        'data': [dict(
            x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
            y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
            text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            customdata=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            mode='markers',
            marker={
                'size': 25,
                'opacity': 0.7,
                'color': 'orange',
                'line': {'width': 2, 'color': 'purple'}
            }
        )],
        'layout': dict(
            xaxis={
                'title': xaxis_column_name,
                'color' : 'red',
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                'color' : 'pink',
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
            height=450,
            hovermode='closest',
            paper_bgcolor='blue',
            plot_bgcolor='green'
        )
    }





@app.callback(
    dash.dependencies.Output('x-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
     dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value')])
def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
    country_name = hoverData['points'][0]['customdata']
    dff = df[df['Country Name'] == country_name]
    dff = dff[dff['Indicator Name'] == xaxis_column_name]
    title = '<b>{}</b><br>{}'.format(country_name, xaxis_column_name)
    return create_time_series(dff, axis_type, title)


@app.callback(
    dash.dependencies.Output('y-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type', 'value')])
def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
    dff = df[df['Country Name'] == hoverData['points'][0]['customdata']]
    dff = dff[dff['Indicator Name'] == yaxis_column_name]
    return create_time_series(dff, axis_type, yaxis_column_name)


# Serve the app using `run_server`.  Unlike the standard `Dash.run_server` method, the `JupyterDash.run_server` method doesn't block execution of the notebook. It serves the app in a background thread, making it possible to run other notebook calculations while the app is running.
# 
# This makes it possible to iterativly update the app without rerunning the potentially expensive data processing steps.

# In[40]:


app.run_server(debug=True,port=port,mode='external')


# By default, `run_server` displays a URL that you can click on to open the app in a browser tab. The `mode` argument to `run_server` can be used to change this behavior.  Setting `mode="inline"` will display the app directly in the notebook output cell.

# In[41]:


#app.run_server(mode="inline")


# When running in JupyterLab, with the `jupyterlab-dash` extension, setting `mode="jupyterlab"` will open the app in a tab in JupyterLab.
# 
# ```python
# app.run_server(mode="jupyterlab")
# ```

# In[ ]:




