import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


#import parts of the app
<<<<<<< HEAD
from pages import home, overview , eda ,dataset, model, report, contact

=======
from pages import home, overview  ,dataset, model, report, contact
from pages import eda
>>>>>>> 0561d3990526710287be73cde2f108190e29813e
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
    "background-color": "#1B2A41",
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
        html.H2(children="Team 247", className="display-4", style={"text-align":"center"}),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Overview", href="/page-1", active="exact"),
                dbc.NavLink("Dataset", href="/page-2", active="exact"),
                dbc.NavLink("EDA", href="/page-3", active="exact"),
                dbc.NavLink("Model", href="/page-4", active="exact"),
                dbc.NavLink("Report", href="/page-5", active="exact"),
                dbc.NavLink("Contact us", href="/page-6", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/page-1":
        return overview.layout
    elif pathname == "/page-2":
        return dataset.layout
    elif pathname == "/page-3":
        return eda.layout
    elif pathname == "/page-4":
        return model.layout
    elif pathname == "/page-5":
        return report.layout
    elif pathname == "/page-6":
        return contact.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )



