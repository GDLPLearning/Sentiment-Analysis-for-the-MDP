# import libraries
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
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
import pandas as pd
pd.options.display.max_columns = None
from pages import tools
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv('pages/data/historic_prediction_sentiment.csv')

df['day'] = pd.to_datetime(df['date']).dt.day
df['year'] = pd.to_datetime(df['date']).dt.year
df['month'] = pd.to_datetime(df['date']).dt.month


keywords = {1:'cultura', 2:'empresa', 3:'jovenes',
                 4:'metro', 5:'movilidad', 6:'seguridad',
                 7:'tecnologia', 8:'trabajo', 9:'vida'}

months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May',
          6:'June', 7:'July', 8:'August', 9:'September', 10:'October',
          11:'November', 12:'December'}

layout = html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Report'),
        html.H2(''),
    ], style={'textAlign': 'center'}),
    html.Br(),html.Br(),
    html.P('Explicacion de la seccion.'),

############### Explore tweet text sentiment by keyword #################
    html.Br(),
    dbc.CardHeader(html.H3('Explore tweet text sentiment by keyword')),
    html.P('Explore tweet text sentiment by keyword.'),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label('Years:'),
            dcc.Dropdown(id='random_tweet_year_dropdown',
                         multi=True,
                         placeholder='Select one or more years',
                         options=[{'label': year, 'value': year} for year in df['year'].drop_duplicates().sort_values()]),
                    ]),
        dbc.Col([
            dbc.Label('Months:'),
            dcc.Dropdown(id='random_tweet_month_dropdown',
                         multi=True,
                         placeholder='Select one or more years',
                         options=[{'label':month.title(), 'value':i} for i, month in months.items()]),
            ]),
        dbc.Col([
            dbc.Label('Days:'),
            dcc.Dropdown(id='random_tweet_day_dropdown',
                         multi=True,
                         placeholder='Select one or more years',
                         options=[{'label': days, 'value': days} for days in df['day'].drop_duplicates().sort_values()])
            ])
        ]),

    dbc.Row([
        dbc.Col([
            dbc.Label('Keyword:'),
            dcc.Dropdown(id='random_tweet_keyword_dropdown',
                         placeholder='Select one keyword',
                         options=[{'label':keyword.title(), 'value':i}
                         for i, keyword in keywords.items()]),
        ]),
        dbc.Col([
        dbc.Label('Sentiment:'),
            dcc.Dropdown(id='random_tweet_sentiment_dropdown',
                         placeholder='Select a sentiment',
                         options=[{'label':'Positive', 'value':1}, {'label':'Negative', 'value':0},
            ]),
    ]),
]),

    html.Br(),
    dcc.Loading([
        dcc.Markdown(id='display_random_tweet_by_keyword_and_sentiment_md',
                     style={'backgroundColor': '#FFFFFF', 'border': '2px solid powderblue', 'padding': '30px'}),]),
    html.Br(),
    html.Div(id='feedback_2'), 
    html.Div([
        dbc.Button("Generate a random tweet", outline=True, color="primary", className="me-1", size="sm", id="button1"),
            ], className="d-grid gap-2 col-6 mx-auto"),
    html.Br(),
    html.P('Conclusiones de los gráficos anteriores'),


])


@app.callback(Output('display_random_tweet_by_keyword_and_sentiment_md', 'children'),
              Input('button1', 'n_clicks'),
              State('random_tweet_year_dropdown', 'value'),
              State('random_tweet_month_dropdown', 'value'),
              State('random_tweet_day_dropdown', 'value'),
              State('random_tweet_keyword_dropdown', 'value'),
              State('random_tweet_sentiment_dropdown', 'value'),)

def gen_random_tweet(nclicks, year, month, day, keyword, sentiment):

    if (not nclicks):
        raise PreventUpdate

    df_filtered = df[(df['year'].eq(year)) & (df['month'].eq(month)) & (df['day'].eq(day)) & (df['key_word'] == (keyword)) & (df['sentiment'].eq(sentiment))]

    random_tweet = df_filtered['full_text'].sample().values[0]

    markdown = f"{random_tweet}"

    return markdown