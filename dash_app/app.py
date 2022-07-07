import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


# app instantiation
dash_app = dash.Dash(external_stylesheets=[dbc.themes.CERULEAN],suppress_callback_exceptions=True)

app = dash_app.server

#CERULEAN
#COSMO
#LITERA
#LUMEN
#MATERIA
#SOLAR
#YETI