# import libraries

from turtle import width
from click import style
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


# app instantiation
list_color=['#0C1821','#0B132B','#1C2541','#1B2A41','#324A5F','#3A506B','#5BC0BE','#CCC9DC','#6FFFE9']

style_div={
    'border':'#5BC0BE 0.03rem solid ',
    'border-radius':'1rem',
    'padding':'10px',
}



# app layout
layout =html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Overview'),
        html.H2('Business context'),
        ], style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.P("The objective will be to answer the following questions"),
    html.Br(),
    html.Ol([
        html.Li("Is the Medellin Development Plan 2020 - 2023 (MDP) aligned with the expressed by the population?"),
        html.Li("What is the perception of citizens in relation to MDP programs and projects during the government's term?"),
    ]),
    html.Br(),
    html.P('First of all, you can explore on the bottom left an explanation of the development plan for the city of Medellín and on the bottom right some tweets from citizens.'),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('MDP')),
                html.Br(),
                html.P("The Medellin Development Plan (MDP) 2020 - 2023 is the local government proposal that seeks to guarantee comprehensive attention to the needs of Medellin's citizens. It is divided into five strategic lines:"),
                html.Br(),
                dbc.Accordion([
                    dbc.AccordionItem([
                        html.P("This strategic line is focused on economic development. It aims to ensure entrepreneurship, opportunities and the promotion of new jobs in areas associated with the economy and the fourth industrial revolution."),
                        html.Br(),
                        html.P("Some programs are:"),
                        html.Ul([            
                            html.Li("Centros del Valle del Software."),
                            html.Li("Gobierno digital."),
                            html.Li("Semilla bilingüe para Valle del Software."),
                            html.Li("Economía creativa."),
                        ]),
                        ],title="Linea estrategica 1: Reactivación Económica y Valle del Software"),
                    dbc.AccordionItem([
                        html.P("Guarantee quality education and promote culture and safeguard heritage and memories to turn Medellín into a peaceful and supportive city."),
                        html.Br(),
                        html.P("Some programs are:"),
                        html.Ul([
                            html.Li("Pertinencia, calidad y habilidades para la educación del futuro."),
                            html.Li("Aula segura y amigable."),
                            html.Li("Medellín ciudad de la ciencia y el conocimiento."),
                            html.Li("Medellín vive las artes y la cultura."),
                        ]),
                        ],title="Linea estrategica 2: Transformación Educativa y Cultural"),
                    dbc.AccordionItem([
                        html.P("To guarantee the basic, social and cultural conditions that allow the citizens of Medellín to develop their human potential to the maximum."),
                        html.Br(),
                        html.P("Some programs are:"),
                        html.Ul([
                            html.Li("Tecnologías en salud, gestión de información y del conocimiento."),
                            html.Li("Seguridad, vida libre de violencias y protección integral para las mujeres."),
                            html.Li("Canasta básica de derechos."),
                            html.Li("Acciones de fortalecimiento social para el cuidado y la protección."),
                        ]),
                        ],title="Linea estrategica 3: Medellín Me Cuida"),
                    dbc.AccordionItem([
                        html.P("to lead Medellín to a future of sustainability and guarantee the integration of the city and the rural space."),
                        html.Br(),
                        html.P("Some programs are:"),
                        html.Ul([
                            html.Li("Protección y gestión de la biodiversidad."),
                            html.Li("Gestión del riesgo de desastres, del medio ambiente y adaptación al cambio climático."),
                            html.Li("Vivienda, hábitat sostenible y mejoramiento integral de barrios."),
                            html.Li("Desarrollo rural sostenible."),
                        ]),
                        ],title="Linea estrategica 4: Ecociudad"),
                    dbc.AccordionItem([
                        html.P("Generate institutional, political and citizen conditions and capacities to strengthen the public sector, generating synergy between government and citizens. Dialogue with different sectors for a collective construction of citizen processes."),
                        html.Br(),
                        html.P("Some programs are:"),
                        html.Ul([
                            html.Li("Talento humano para el buen gobierno."),
                            html.Li("Direccionamiento estratégico del Conglomerado Público de Medellín."),
                            html.Li("Memoria histórica, construcción de paz y superación del conflicto."),
                            html.Li("Inteligencia, tecnología e infraestructura para la seguridad y la convivencia."),
                            html.Li("Planeación territorial para el desarrollo."),
                        ]),
                        ],title="Linea estrategica 5: Gobernanza y Gobernabilidad"),
                ],start_collapsed=True),
                html.Br(),
                html.P('Descriptive analysis of this plan will allow us to answer the first question.')
            ],style=style_div),
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H3('Tweets')),
                html.Br(),
                html.P('The tweets show the main topics people are talking about. Therefore, they are an approximation of the needs of the citizens of the city of Medellín.'),
                html.Br(),
                dbc.Carousel(
                    items=[
                        {"key":"1","src":"assets/tweets/tweet1.png",'caption':'Tweet 1: about security and opportunities','img_style':{'height':'400px','padding':'80px',"padding-top":"5px"}},
                        {"key":"2","src":"assets/tweets/tweet2.png",'caption':'Tweeet 2: about "Metro de Medellín" ','img_style':{'height':'400px','padding':'80px',"padding-top":"5px"}},
                    ],
                    controls=True,
                    indicators=True,
                    class_name="carousel-fade",
                    variant='dark',
                    style={'height': '400px', 'width': '500px'}
                ),
                html.P('How would you classify, in terms of sentiment the above tweets? positive, negative or neutral? Sentiment analysis could help you with that and also answer the second question mentioned at the beginning of this page.'),
            ],style=style_div),
        ]),
    ]),
])



