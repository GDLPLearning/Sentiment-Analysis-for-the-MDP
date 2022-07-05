# import libraries
from app import app
import plotly
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
#from dash_table import DataTable
import pandas as pd
pd.options.display.max_columns = None

#df=pd.read_csv('https://media.githubusercontent.com/media/GDLPLearning/Sentiment-Analysis-for-the-MDP/master/notebooks/Exploratory/data/2019.csv')
df = pd.read_csv('pages/data/2019.csv')
df['num_chars'] = df['full_text'].str.len()
df['num_words'] = df['full_text'].str.split().str.len()

#df2=pd.read_csv('https://media.githubusercontent.com/media/GDLPLearning/Sentiment-Analysis-for-the-MDP/master/notebooks/Exploratory/data/tweets.csv')
df2 = pd.read_csv('pages/data/tweets.csv')
df2['weekday'] = pd.to_datetime(df2['date']).dt.weekday
df2['year'] = pd.to_datetime(df2['date']).dt.year
df2['month'] = pd.to_datetime(df2['date']).dt.month
df2['num_chars'] = df2['full_text'].str.len()
df2['num_words'] = df2['full_text'].str.split().str.len()

months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May',
          6:'June', 7:'July', 8:'August', 9:'September', 10:'October',
          11:'November', 12:'December'}

lineas_estrategicas = {'Medellin Development Plan': 0,
                       'Línea estratégica 1: Reactivación Económica y Valle del Software': 1,
                       'Línea estratégica 2: Transformación Educativa y Cultura': 2,
                       'Línea estratégica 3: Medellin Me Cuida': 3,
                       'Línea estratégica 4: Ecociudad': 4,
                       'Línea estratégica 5: Gobernanza y Gobernabilidad': 5,
                       }


df3 = df2['year'].value_counts().sort_index().to_frame().reset_index()
fig = px.pie(df3,values='year',names='index', 
    title=f'Pie chart - Tweets distribution by year.')

df_words = pd.read_csv('pages/data/word_fre_2019.csv')

def rep_words():
    fig = px.bar(df_words.head(35).sort_values(by='frequency'), 
                 x='frequency', 
                 y='word',
                 orientation='h',
                 height=600,
                 color_discrete_sequence=['#5BC0BE']
                 )
    fig.update_layout(title_font_size=15)
    fig.layout.paper_bgcolor = '#FFFFFF'
    fig.layout.plot_bgcolor = '#FFFFFF'

    return fig



p1 = """
Welcome to the EDA, in this section you can interact with the data sets used to 
develop the model, through interactive content you can learn first hand some of 
the most important findings of each of the sections, as well as brief explanations 
of how those responsible for the project manipulated, cleaned, enriched and visualized 
the information to draw conclusions for the construction of the model and its future 
interpretation, always guiding the analysis to find answers to the two hypotheses 
proposed in the definition of the problem.

"""

p2 = """

Explicación de la sección del data understanding I

"""


p3 = """

Conclusiones de los histogramas

"""

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])


def make_empty_fig():
    fig = go.Figure()
    fig.layout.paper_bgcolor = '#FFFFFF'
    fig.layout.plot_bgcolor = '#FFFFFF'
    return fig

layout = html.Div([
################ Section Title ############################

    dbc.Col([
        html.Br(),
        html.H1('Exploratory Data Analisis - EDA'),
        ], style={'textAlign': 'center'}),
    html.Br(), html.Br(),
        html.P(p1),

############### Tabs #############################

    dbc.Tabs([

############### EDA: Tweets 2019 (Tab 1) #################

############### Data understanding I #################
        
        dbc.Tab([
            dbc.Col([
                html.Br(),
                html.H2('Data understanding I'),
        ], style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),
            html.P(p2),
            html.Br(),

############### Distribution of tweet text length #################

            dbc.CardHeader(html.H3('Distribution of tweet text length')),
            html.Br(),
            html.P('Explicacion de esta sección'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        dcc.Graph(id='chars_freq_hist')
                        ]),
                ], lg=6),
                dbc.Col([
                    dcc.Loading([
                        dcc.Graph(id='words_freq_hist')
                        ]),                 
                ], lg=6),
        ]),
            html.Br(),
            html.Div([
                dbc.Alert(f"Please select the number of bins before generating the graphs, otherwise the default will be used.",
                         color='info',
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],

                id='feedback_1'),
            dbc.Row([
                dbc.Col(lg=1),
                dbc.Col([
                    dbc.Label('Modify number of bins:'),
                    dcc.Slider(id='hist_bins_slider', 
                       dots=True, min=0, max=100, step=5, included=False,
                       marks={x: str(x) for x in range(0, 105, 5)}),
                ], lg=10),
                dbc.Col(lg=1),
            ]),
            html.Br(),
            html.Div([
                dbc.Button("Generate Graphs", outline=True, color="primary", className="me-1", size="sm", id="button1"),
                ],  className="d-grid gap-2 col-6 mx-auto"),      
            html.Br(),
            html.P('Conclusiones de los gráficos anteriores'),

############### Explore the text content of the tweet #################
            html.Br(),html.Br(),
            dbc.CardHeader(html.H3('Explore the text content of the tweets')),
            html.Br(),
            html.P('Explicacion de esta sección'),
            html.Br(),
            dcc.Loading([
                dcc.Markdown(id='display_tweet_md',
                             style={'backgroundColor': '#FFFFFF', 'border': '2px solid powderblue', 'padding': '30px'}),
            ]),
            html.Br(),
            html.Div(id='feedback_2'), 
            html.Div([
                dbc.Button("Generate a random tweet", outline=True, color="primary", className="me-1", size="sm", id="button2"),
                ], className="d-grid gap-2 col-6 mx-auto"),
            html.Br(), html.Br(),
            html.P('Conclusiones de los gráficos anteriores'),



############### Words frequency #################
            html.Br(),html.Br(),
            dbc.CardHeader(html.H3('Words frequency')),
            html.Br(),
            html.P('Explicacion de esta sección'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        dcc.Graph(id='freq_words', figure=rep_words())
                        ]),
                    ]),
                dbc.Col([
                    dcc.Loading([
                        html.Div([
                            html.Img(src='assets/images/wc_text.jpg')
                        ]),
                    ]),

                ]),

            ]),
            html.Br(), html.Br(),
            html.P('Explicacion de esta seccion'),



        ],label='EDA: Tweets 2019'),

############### Medellin Development Plan (Tab 2) #################

        dbc.Tab([
            dbc.Col([
                    html.Br(),
                    html.H2('Text Analysis'),
            ], style={'textAlign': 'center'}),
                html.Br(),
                html.Br(),

            dbc.CardHeader(html.H3('Wordclouds by "Linea Estrategica"')),
            html.P('Explicacion de esta sección'),
            html.Br(),
            dcc.Dropdown(id='lineas_estrategicas',
                         placeholder='Select one "Linea Estrategica"',
                         options=[{'label':linea, 'value':i}
                                  for linea,i in lineas_estrategicas.items()]),
            html.Br(),
            html.Div([
                dbc.Button("Generate Wordclouds", outline=True, color="primary", className="me-1", size="sm", id="button_lestr"),
                ],  className="d-grid gap-2 col-6 mx-auto"),
            html.Br(),html.Br(),
            dbc.Row([
                dbc.Col(),
                dbc.Col([
                    dcc.Loading([
                    html.Div([
                    html.Img(id='word_cloud_linea')]),
                ]),
                    ]),
                dbc.Col(),
                ]),
            

        ], label='Medellin Development Plan'),



############### EDA: Tweets keywords 2019 - 2022 (Tab 3) #################

############### Data understanding II #################

        dbc.Tab([
            dbc.Col([
                html.Br(),
                html.H2('Data understanding II'),
        ], style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),

############### Distribution of tweet text length #################

            dbc.CardHeader(html.H3('Distribution of tweet text length')),
            html.P('Explicacion de esta sección'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Label('Years:'),
                    dcc.Dropdown(id='hist_year_dropdown_2022',
                                 multi=True,
                                 placeholder='Select one or more years',
                                 options=[{'label': year, 'value': year} for year in df2['year'].drop_duplicates().sort_values()]),
                    ]),
                dbc.Col([
                    dbc.Label('Keyword:'),
                    dcc.Dropdown(id='keyword_selector_20221',
                                 placeholder='Select one keyword',
                                 options=[{'label':keyword.title(), 'value':keyword}
                                          for keyword in df2['key_word'].drop_duplicates().sort_values()]),
                ]),
                ]),
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        dcc.Graph(id='chars_freq_hist_2022')
                        ]),
                ], lg=6),
                dbc.Col([
                    dcc.Loading([
                        dcc.Graph(id='words_freq_hist_2022')
                        ]),                 
                ], lg=6),
        ]),
            html.Br(),
            html.Div(id='feedback_1_2022'),
            dbc.Row([
                dbc.Col(lg=1),
                dbc.Col([
                    dbc.Label('Modify number of bins:'),
                    dcc.Slider(id='hist_bins_slider_2022',
                       dots=True, min=0, max=100, step=5, included=False,
                       marks={x: str(x) for x in range(0, 105, 5)}),
                ], lg=10),
                dbc.Col(lg=1),
            ]),
            html.Br(),
            html.Div([
                dbc.Button("Generate Graphs", outline=True, color="primary", className="me-1", size="sm", id="button1_2022"),
                ],  className="d-grid gap-2 col-6 mx-auto"),      
            html.Br(),
            html.P('Conclusiones de los gráficos anteriores'),

############### Explore the text content of the tweet #################

            html.Br(),html.Br(),
            dbc.CardHeader(html.H3('Explore the text content of the tweets')),
            html.P('Explicacion de esta sección'),
            html.Br(),
            html.Div(id='feedback_3_2022'), 
            dbc.Label('Keyword:'),
            dcc.Dropdown(id='keyword_selector_20222',
                         placeholder='Select one keyword',
                         options=[{'label':keyword.title(), 'value':keyword}
                                   for keyword in df2['key_word'].drop_duplicates().sort_values()]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Label('Year:'),
                    dcc.Slider(id='years_random_tweet_slider_2022',
                       dots=True, min=2019, max=2022, step=1, included=False,
                       marks={x: str(x) for x in range(2019, 2023, 1)}),
                    ]),
                dbc.Col([
                    dbc.Label('Month:'),
                    dcc.Dropdown(id='month_selector_2022',
                         placeholder='Select one month',
                         options=[{'label':month, 'value':i}
                                   for i, month in months.items()]),
                    ]),


                ]),
            html.Br(),
            dcc.Loading([
                dcc.Markdown(id='display_tweet_text_2022_md',
                             style={'backgroundColor': '#FFFFFF', 'border': '2px solid powderblue', 'padding': '30px'}),
            ]),
            html.Br(),
            html.Div(id='feedback_2_2022'), 
            html.Div([
                dbc.Button("Generate a random tweet", outline=True, color="primary", className="me-1", size="sm", id="button2_2022"),
                ], className="d-grid gap-2 col-6 mx-auto"),
            html.Br(),
            html.P('Conclusiones de los gráficos anteriores'),           


        ],label='EDA: Tweets keywords 2019 - 2022'),
        
        ]),
    ])



############### Callbacks #################

############### EDA: Tweets 2019 (Tab 1) #################

############### Data understanding I #################

############### Distribution of tweet text length #################


@app.callback(Output('chars_freq_hist', 'figure'),
              Output('words_freq_hist', 'figure'),
              Output('feedback_1', 'children'),
              Input('button1', 'n_clicks'),
              State('hist_bins_slider', 'value'),
              )

def plot_freq_hist(nclicks, nbins):
    if (not nclicks):
        raise PreventUpdate

    fig1 = px.histogram(df,
                        x='num_chars',
                        nbins=nbins,
                        color_discrete_sequence=['#5BC0BE'],
                        title='Histogram - Character tweets distribution by length.',
                        marginal="box",
                        height=500,
                        width=500,
                        labels={'num_chars':'Length of text in characters'})
    fig1.layout.paper_bgcolor = '#FFFFFF'
    fig1.layout.plot_bgcolor = '#FFFFFF'
    fig1.update_layout(title_font_size=15)
    
    fig2 = px.histogram(df,
                        x='num_words',
                        nbins=nbins,
                        color_discrete_sequence=['#5BC0BE'],
                        title='Histogram - Words tweets distribution by length.',
                        marginal="box",
                        height=500,
                        width=500,
                        labels={'num_words':'Length of text in words'})
    fig2.layout.paper_bgcolor = '#FFFFFF'
    fig2.layout.plot_bgcolor = '#FFFFFF'
    fig2.update_layout(title_font_size=15)



    message = dbc.Alert(f"The number of bins has been modified to: {nbins} bins.",
                        color='success',
                         fade=True,
                         is_open=True,
                         duration=4000,
                         dismissable=True,)
                        

    return fig1, fig2, message


############### Explore the text content of the tweet #################
@app.callback(Output('display_tweet_md', 'children'),
              Output('feedback_2', 'children'),
              Input('button2', 'n_clicks'),)

def gen_random_tweet(nclicks):
    if (not nclicks):
        raise PreventUpdate

    random_tweet = df['full_text'].sample().values[0]

    markdown = f"{random_tweet}"

    message = dbc.Alert(f"Random tweet successfully generated.",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=5000,
                        dismissable=True,)

    return markdown, message

############### Medellin Development Plan (Tab 2) #################

@app.callback(Output('word_cloud_linea','src'),
              Input('button_lestr', 'n_clicks'),
              State('lineas_estrategicas', 'value'))

def word_cloud_lin(nclicks, linea):

    if (not nclicks):
        raise PreventUpdate

    if linea == 0:
        return 'assets/images/wc_pdm.jpg'
    elif linea == 1:
        return 'assets/images/wcl1.jpg'
    elif linea == 2:
        return 'assets/images/wcl2.jpg'
    elif linea == 3:
        return 'assets/images/wcl3.jpg'
    elif linea == 4:
        return 'assets/images/wcl4.jpg'
    elif linea == 5:
        return 'assets/images/wcl5.jpg'



############### Data understanding II #################

############### Distribution of tweet text length #################

@app.callback(Output('chars_freq_hist_2022', 'figure'),
              Output('words_freq_hist_2022', 'figure'),
              Output('feedback_1_2022', 'children'),
              Input('button1_2022', 'n_clicks'),
              State('hist_bins_slider_2022', 'value'),
              State('hist_year_dropdown_2022', 'value'),
              State('keyword_selector_20221', 'value'),
              )
def plot_freq_hist(nclicks, nbins, years, keyword):
    if (not nclicks):
        raise PreventUpdate

    df = df2[(df2['year'].isin(years)) & (df2['key_word'] == keyword)]


    fig1 = px.histogram(df,
                        x='num_chars',
                        nbins=nbins,
                        color_discrete_sequence=['#5BC0BE'],
                        title='Histogram - Character tweets distribution by length.',
                        marginal="box",
                        height=500,
                        width=500,
                        labels={'num_chars': 'Length of text in characters'})
    fig1.layout.paper_bgcolor = '#FFFFFF'
    fig1.layout.plot_bgcolor = '#FFFFFF'
    fig1.update_layout(title_font_size=15)

    fig2 = px.histogram(df,
                        x='num_words',
                        nbins=nbins,
                        color_discrete_sequence=['#5BC0BE'],
                        title='Histogram - Words tweets distribution by length.',
                        marginal="box",
                        height=500,
                        width=500,
                        labels={'num_words': 'Length of text in words'})
    fig2.layout.paper_bgcolor = '#FFFFFF'
    fig2.layout.plot_bgcolor = '#FFFFFF'
    fig2.update_layout(title_font_size=15)

    message = dbc.Alert(f"The number of bins has been modified to: {nbins} bins.",
                        color='success',
                        dismissable=True,)

    return fig1, fig2, message

############### Explore the text content of the tweet #################
@app.callback(Output('display_tweet_text_2022_md', 'children'),
              Output('feedback_2_2022', 'children'),
              Output('feedback_3_2022', 'children'),
              Input('button2_2022', 'n_clicks'),
              State('keyword_selector_20222', 'value'),
              State('years_random_tweet_slider_2022', 'value'),
              State('month_selector_2022', 'value'))

def gen_random_tweet_2022(nclicks, keyword, year, month):
    if (not nclicks):
        raise PreventUpdate

    df = df2[(df2['key_word'] == keyword) & (df2['year'].eq(year)) & (df2['month'].eq(month))]

    random_tweet = df['full_text'].sample().values[0]

    markdown = f"{random_tweet}"

    message = dbc.Alert(f"Successfully generated random tweet.",
                         color='success',
                         dismissable=True)

    message2 = dbc.Alert(f"You have selected - keyword: {keyword.title()} | year: {year} | month: {month}",
                         color='info',
                         dismissable=True)

    return markdown, message, message2

