# import libraries
import dash
from dash import dcc as dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

layout =html.Div([
    html.Div([
        html.H1(children='OVERVIEW'),
        html.Img(src='/assets/images/colombia-2722716_1920.jpg', style={'height': '700px', 'width': '700px'}),
    ])
])