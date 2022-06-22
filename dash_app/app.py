import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


# app instantiation
app = dash.Dash(external_stylesheets=[dbc.themes.YETI],suppress_callback_exceptions=True)
