# import libraries

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


# app instantiation





# app layout
layout = html.Div([
    html.Div([html.H1("Overview",style={"text-align":"center"})]),
    html.Br(),
    html.Div([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2("Tweets",style={"text-align":"center"}),
                    dbc.Carousel(
                        items=[
                            {"key":"1","src":"assets/tweets/tweet_depmed.png","img_style":{"height":"500px","padding":"50px"}},
                            {"key":"2","src":"assets/tweets/tweet_largo.png","img_style":{"height":"500px", "padding":"50px"}},
                        ],
                    controls=True,
                    indicators=True,
                    class_name="carousel-fade",
                    variant='dark',
                    ),
                ])
            ]),
            dbc.Col(
                html.Div([html.H2("MDP",style={"text-align":"center"})]),
            ),
        ]),
    ]),
])

