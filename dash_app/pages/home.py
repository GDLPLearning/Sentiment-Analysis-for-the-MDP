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
}

layout =html.Div([
    dbc.Col([
        html.Div([
            html.H1('Sentiment analysis in Twitter for the Medellin Development Plan'),
            html.Img(src='https://api.iconify.design/logos/twitter.svg', style={'width': '5%', 'height': '5%'}),
        ], style={'text-align': 'center'}),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Repository', style={'textAlign': 'center'})),
                html.Br(),
                html.A([
                    html.Img(src='assets/profile/repo.png',style={'width': '100%','margin-top': '40px'}),
                ],href='https://github.com/GDLPLearning/Sentiment-Analysis-for-the-MDP',target='_blank'),
                html.Br(),
                html.Br(),
            ],style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','padding':'10px','height':'355px'})   
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Presentation', style={'textAlign': 'center'})),
                html.Br(),
                html.A([
                    html.Img(src='https://api.iconify.design/entypo-social/youtube.svg', style={'width': '150px','height': '150px','margin-top': '40px','margin-left': '25%'}),
                ]),
                html.Br(),
                html.Br(),
            ], style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','padding':'10px','height':'355px'}),
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Datafolio', style={'textAlign': 'center'})),
                html.Br(),
                html.A([
                    html.Img(src='assets/images/datafolio.png', style={'width':'100%','height':'100%'}),
                ]),
                html.Br(),
                html.Br(),
            ], style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','padding':'10px'}),
        ]),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Report', style={'textAlign': 'center'})),
                html.Br(),
                html.Img(src='assets/images/logo_reporte.jpg', style={'width': '50%','height': '50%','margin-left': '25%'}),
                html.Br(),
                html.Br(),
            ], style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','padding':'10px'}),
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Documentation', style={'textAlign': 'center'})),
                html.Br(),
                html.A([
                    html.Img(src='assets/images/documentation.jpg', style={'width': '100%','height': '70%','margin-top': '5px','padding': '10px'}),
                ]),
                html.Br(),
                html.Br(),
            ], style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','padding':'10px','height':'358px'}),
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Notebooks', style={'textAlign': 'center'})),
                html.Br(),
                html.A([
                    html.Img(src='assets/images/notebooks.png', style={'width': '100%','height': '70%','margin-top': '5px','padding': '10px'}),
                ]),
                html.Br(),
                html.Br(),
            ], style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','padding':'10px','height':'358px'}),
        ]),
    ]),
])
