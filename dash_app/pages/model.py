# import libraries
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

layout = html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Model'),
        html.H2(''),
        ], style={'textAlign': 'center'}),

############### Tweet text preprocessing #################

    dbc.CardHeader(html.H3('Tweet text preprocessing')),
    html.P('Explicacion de esta sección'),
    html.Br(),
    dbc.Label('Tweet text:'),
    dcc.Textarea(
        id='textarea-example',
        placeholder='Enter the text of the tweet',
        style={'width': '100%', 'height': 100}),
    html.Div([
        dbc.Button("Generate Graphs", outline=True, color="primary", className="me-1", size="sm", id="button"),
        ],  className="d-grid gap-2 col-6 mx-auto"),  
    ])