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
    #'background-color':'#CCC9DC'
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
                html.H4('MDP'),
                html.Br(),
                html.P("The Medellin Development Plan (MDP) 2020 - 2023 is the local government proposal that seeks to guarantee comprehensive attention to the needs of Medellin's citizens. It is divided into five strategic lines:"),
                html.Br(),
                dbc.Accordion([
                    dbc.AccordionItem([html.P("Economic Reactivation and the Software Valley are part of an economic development strategy. Its objective is to manage new opportunities, based on education, innovation and entrepreneurship, taking advantage of our needs and strengths to enhance, sophisticate and diversify our needs and strengths to enhance, sophisticate and diversify the city's economy by opening new scenarios and generating thousands of jobs, in areas associated with the digital economy and the Fourth Industrial Revolution.")],title="Linea estrategica 1: Reactivación Económica y Valle del Software"),
                    dbc.AccordionItem([html.P("To guarantee quality education as a right that mobilizes the human, economic, political, environmental and social transformation of Medellín Futuro; that is linked to a cultural project for the city, based on cultural rights; that strengthens the creative potential of its citizens, safeguards their heritage and memories, and contributes to making Medellín a more supportive, participatory and peaceful city.")],title="Linea estrategica 2: Transformación Educativa y Cultural"),
                    dbc.AccordionItem([html.P("To promote, create, renew and guarantee the basic social and cultural conditions that allow the citizens of Medellín, in their different life courses, to have the capabilities to develop their human and individual potential and contribute, from their possibilities, to generate healthy, safe, creative and sustainable social and community environments.")],title="Linea estrategica 3: Medellín Me Cuida"),
                    dbc.AccordionItem([html.P("Establish the foundations of the ecological transition to direct Medellín to a future of sustainability, in which the full enjoyment of the right to the city, the dignified habitability for its inhabitants and the functional and harmonious integration of rurality are guaranteed through the recognition of the rights of rural dwellers and their access to them.")],title="Linea estrategica 4: Ecociudad"),
                    dbc.AccordionItem([html.P("Generate institutional, political and citizen conditions and capacities to strengthen the public sector, generating synergy between government and citizens. We seek open dialogue based on different knowledge, consensus-building among the different actors and the collective construction of citizen processes of territorial peace, based on knowledge of the territory, the installation of local and institutional capacities for the management and protection of the public, the use of data and information as a value-giving asset, and intra- and inter-institutional and territorial articulation.")],title="Linea estrategica 5: Gobernanza y Gobernabilidad"),
                ],start_collapsed=True),
                html.Br(),
                html.P('Descriptive analysis of this plan will allow us to answer the first question.')
            ],style=style_div),
        ]),
        dbc.Col([
            html.Div([
                html.H4('Tweets'),
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



