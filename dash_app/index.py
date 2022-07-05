from turtle import width
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from matplotlib import image
from sklearn.feature_extraction import img_to_graph


#import parts of the app
from pages import home, overview , eda ,dataset, model, report, contact

# app instantiation
from app import app

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#0C1821",
    "color": "white",
    "overflow": "scroll",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.Img(src="assets/images/logo.jpg", height="200px",width="200px"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Overview", href="/overview", active="exact"),
                dbc.NavLink("Dataset", href="/dataset", active="exact"),
                dbc.NavLink("EDA", href="/EDA", active="exact"),
                dbc.NavLink("Model", href="/model", active="exact"),
                dbc.NavLink("Report", href="/report", active="exact"),
                dbc.NavLink("Contact us", href="/contact-us", active="exact"),   
            ],
            vertical=True,
            pills=True,
        ),
        html.Br(),
        html.Div([
            html.A([
                html.Img(src="assets/images/DS4A - C1.jpg", height="60px",width="200px"),
            ], href="https://www.correlation-one.com/data-science-for-all-colombia",target="_blank"),
        ]),
        html.Br(),
        html.Div([
            html.A([
                html.Img(src="assets/images//MinTic.jpg", height="50px",width="200px"),
            ], href="https://www.mintic.gov.co/micrositios/cienciadedatos/747/w3-channel.html",target="_blank"),
        ]),
               
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/overview":
        return overview.layout
    elif pathname == "/dataset":
        return dataset.layout
    elif pathname == "/EDA":
        return eda.layout
    elif pathname == "/model":
        return model.layout
    elif pathname == "/report":
        return report.layout
    elif pathname == "/contact-us":
        return contact.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )



