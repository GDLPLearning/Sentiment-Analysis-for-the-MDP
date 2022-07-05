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
        html.Br(),
        html.H1('Sentiment Analysis in Twitter for the Medellin Development Plan'),
    ], style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Repository')),
                html.Br(),
                html.A([
                    html.Img(src='assets/profile/repo.png', style={'width':'100%','height':'100%'}),
                ],href='https://github.com/GDLPLearning/Sentiment-Analysis-for-the-MDP',target='_blank'),
            ],style=style_div)    
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Presentation')),
                html.Br(),
                html.A([
                    html.Img(src='https://api.iconify.design/entypo-social/youtube.svg', style={'width':'42%','height':'42%','margin-left':'25%'}),
                ]),
            ], style=style_div),
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Datafolio')),
            ], style=style_div),
        ]),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Report')),
                html.Br(),
                html.Img(src='assets/images/logo_reporte.jpg', style={'width':'50%','height':'50%','margin-left':'25%'}),
            ], style=style_div),
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Documentation')),
            ], style=style_div),
        ]),
        dbc.Col([]),
    ]),
])
