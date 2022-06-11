# import libraries
import dash
from dash import dcc as dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# app instantiation
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


theme_colors = {
    'titulo': '#000000', 
    'primario': '#0C1821', 
    'secundario': '#1B2A41',
    'terciario': '#324A5F', 
    'fondo': '#CCC9DC', 
}

# app layout
app.layout = html.Div([
    html.Div([
        html.H2(children='Overview'),
        html.H3(children='BUSINESS PROBLEM', style={'background-color': theme_colors['fondo']}),
        html.P(children= "The Medellín Development Plan (MDP) 2020 - 2023 is the local government proposal that seeks to guarantee comprehensive attention to the needs of Medellín's citizens, care for vulnerable populations, economic reactivation, the construction of a sustainable city and the generation of opportunities based on a major educational transformation."),
        html.P(children="In other words, it is a promise of public policies by the mayor's office in order to improve the welfare of the people they represent by trying to meet the needs that afflict them. But are these in tune with the proposals presented in the city's development plan? This is what this project will try to answer, for which it will divide the analysis into two components:"),
        html.Ol([html.Li(children="Is the MDP aligned with the needs expressed by the population?"),
            html.Ul([
                html.Li(children="In this first component, the main problems expressed by the inhabitants of Medellin prior to the entry into force of the MDP will be identified and it will check if these are part of the development plan."), 
                html.Li(children="To solve this question a text analysis of information extracted will be performed from Twitter (needs) and MDP (proposals) to check if there is any relationship between them.")
                ]),
                html.Li(children="What is the perception of citizens in relation to MDP programs and projects during the government's term?"),
            html.Ul([
                html.Li(children="The response of the citizens of Medellin in relation to this topic will be analyzed through a sentiment analysis based on the perception exposed by the inhabitants on Twitter in relation to these projects and programs of the MDP.")
                ])
           ]),
     ]),

    html.Div([
    html.H3(children="BUSINESS IMPACT   ", style={'background-color': theme_colors['fondo'], 'text-align':'right'}),
    html.P(children="Through the citizen's perception of the MDP programs, as well as the needs felt by the population on Twitter, it is possible to establish an alternative measurement of the assertiveness of the current local government plan and likewise to open up the possibility of configuring a more appropriate action horizon for future development plans for Medellin aligned with the above.")
    ])
])

# running the app
if __name__ == '__main__':
    app.run_server(debug=True, port=1045)
