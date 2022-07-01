# import libraries
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


style_div={
    'border':'#5BC0BE 0.03rem solid ',
    'border-radius':'1rem',
    'padding':'10px',
    #'background-color':'#CCC9DC'
}


layout=html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Contact us'),
    ], style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H4('Gustavo Vergara', style={'textAlign': 'center'}),
                html.Img(src='assets/profile/gv.jpg', style={'width': '45%', 'height': '45%', 'border-radius': '50%', 'margin-left': '25%'}),
                html.Ul([
                    html.Li('Matematician, Universidad Del Norte'),
                    html.Li('Professor of Mathematics, Universidad Del Norte'),
                    html.Li("Experience with Python, Matlab, and R"),
                    html.Li('gustavovergara238@gmail.com'),
                    html.Li('Lnkedin: https://www.linkedin.com/in/gustavovergara238/'),
                    html.Li('Github: https://github.com/gustavovergara238/'),
                ]),
            ],style=style_div)    
        ]),
        dbc.Col([
            html.Div([

            ], style=style_div),
        ]),
        dbc.Col([
            html.Div([

            ], style=style_div),
        ]),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([]),
    ]),
])