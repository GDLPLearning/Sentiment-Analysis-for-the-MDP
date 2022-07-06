# import libraries
from click import style
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
                html.Br(),
                html.Br(),
                dbc.Row([
                    dbc.Col([]),
                    dbc.Col([
                        html.Div([
                            html.A([
                                html.Img(src='assets/profile/repo.png', style={'width': '100%', 'height': '100%'}),
                            ],href='https://github.com/GDLPLearning/Sentiment-Analysis-for-the-MDP',target='_blank'),
                        ], style={'textAlign': 'center'}),
                    ],lg=10),
                    dbc.Col([]),
                ]),
            ],style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','height':'330px','text-align':'center'})   
        ],lg=4),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Presentation', style={'textAlign': 'center'})),
                html.Br(),
                html.Br(),
                dbc.Row([
                    dbc.Col([]),
                    dbc.Col([
                        html.Div([
                            html.A([
                                html.Img(src='https://api.iconify.design/entypo-social/youtube.svg', style={'width': '150px','height': '150px'}),
                            ]),
                        ],style={'text-align': 'center'}),
                    ],lg=10),
                    dbc.Col([]),
                ]),
            ], style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','height':'330px','text-align':'center'}),
        ],lg=4),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Datafolio', style={'textAlign': 'center'})),
                html.Br(),
                dbc.Row([
                    dbc.Col([]),
                    dbc.Col([
                        html.Div([
                            html.A([
                                html.Img(src='assets/images/datafolio.png', style={'width':'100%','height':'100%'}),
                            ]),
                        ],style={'text-align':'center'}),
                    ],lg=10),
                    dbc.Col([]),
                ]),
            ], style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','height':'330px','text-align':'center'}),
        ],lg=4),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Report', style={'textAlign': 'center'})),
                html.Br(),
                dbc.Row([
                    dbc.Col([]),
                    dbc.Col([
                        html.Div([
                            html.A([
                                html.Img(src='assets/images/logo_reporte.jpg', style={'width': '60%','height': '60%'}),
                            ]),
                        ],style={'text-align':'center'}),
                    ],lg=10),
                    dbc.Col([]),
                ]),
                html.Br(),
            ], style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','height':'330px','text-align':'center'}),
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Documentation', style={'textAlign': 'center'})),
                html.Br(),
                html.Br(),
                dbc.Row([
                    dbc.Col([]),
                    dbc.Col([
                        html.Div([
                            html.A([
                                html.Img(src='assets/images/mkdocs.png', style={'width': '60%','height': '60%'}),
                            ]),
                        ],style={'text-align':'center'}),
                    ],lg=10),
                    dbc.Col([]),
                ]),
                html.Br(),
                html.Br(),
            ], style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','height':'330px','text-align':'center'}),
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Notebooks', style={'textAlign': 'center'})),
                html.Br(),
                html.Br(),
                dbc.Row([
                    dbc.Col([]),
                    dbc.Col([
                        html.Div([
                            html.A([
                                html.Img(src='assets/images/jupyterlogo.png', style={'width': '50%','height': '50%'}),
                            ]),
                        ],style={'text-align':'center'}),
                    ],lg=10),
                    dbc.Col([]),
                ]),
                html.Br(),
                html.Br(),
            ], style={'border':'#5BC0BE 0.03rem solid ','border-radius':'1rem','height':'330px','text-align':'center'}),
        ]),
    ]),
])

