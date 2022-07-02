# import libraries
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from pyrsistent import s

layout =html.Div([
    html.Div([
        html.H1(children='Home',style={'textAlign': 'center','color':'black'}),
        html.P(children='This is the home page of the app.',style={'textAlign': 'center','color':'black'}),
    ])
],style={'background-image': 'url(/assets/images/colombia-2722716_1920.jpg)', 'background-repeat': 'no-repeat', 'background-size': 'cover', 'background-position': 'center','opacity': '0.3'})