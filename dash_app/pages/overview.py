# import libraries
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# app instantiation





# app layout
layout = html.Div([
    html.H1("Overview"),
    html.Br(),
    html.H2("Tweets"),
    html.Br(),
    html.P("Let see some tweets"),
        dbc.Carousel(
            items=[
                {"key":"1","src":"assets/tweets/tweet_depmed.png","img_style":{"height":"500px","width":"20px"}},
                {"key":"2","src":"assets/tweets/tweet_largo.png","img_style":{"height":"500px", "width":"20px"}},
                ],
        controls=True,
        indicators=True,
        variant="dark",
        class_name="carousel-fade",
        style={"height":"200px","width":"600px"},
        ),
    html.Br(),
    html.H2("MDP"),
    ])

