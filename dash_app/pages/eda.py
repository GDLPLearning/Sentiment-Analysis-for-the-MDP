# import libraries
# from app import app
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


df = pd.read_csv('data/2019.csv')
df['num_chars'] = df['full_text'].str.len()
df['num_words'] = df['full_text'].str.split().str.len()


df2 = pd.read_csv('data/tweets.csv')
df2['weekday'] = pd.to_datetime(df2['date']).dt.weekday
df2['year'] = pd.to_datetime(df2['date']).dt.year
df2['month'] = pd.to_datetime(df2['date']).dt.month


df3 = df2['year'].value_counts().sort_index().to_frame().reset_index()
fig = px.pie(df3,values='year',names='index')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])


def make_empty_fig():
    fig = go.Figure()
    fig.layout.paper_bgcolor = '#FFFFFF'
    fig.layout.plot_bgcolor = '#FFFFFF'
    return fig

app.layout = html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Exploratory Data Analisis - EDA'),
        html.H2('Data understanding I'),
        ], style={'textAlign': 'center'}),

    html.Br(),
    html.Br(),
    html.H4('EDA: Tweets 2019'),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='chars_freq_hist')
        ], lg=6),
        dbc.Col([
            dcc.Graph(id='words_freq_hist')
        ], lg=6),
    ]),

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

    dbc.Col([
        html.Br(),
        html.H2('Data understanding II'),
        ], style={'textAlign': 'center'}),

    html.Br(),
    dbc.Label('Bar chart - Tweets frequency by weekday.'),
    dcc.Dropdown(id='year_weekday_dropdown',
                 multi=True,
                 placeholder='Select one or more years',
                 options=[{'label': year, 'value': year} for year in df2['year'].drop_duplicates().sort_values()]),
    dcc.Graph(id='bar_freq_weekday', figure=make_empty_fig()),
    
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label('Pie chart - Tweets distribution by year.'),
            dcc.Graph(figure=fig)], lg=4),
        dbc.Col([
            dcc.Graph(figure=make_empty_fig())
            ], lg=8),

        ]),
     
    ])  

@app.callback(Output('chars_freq_hist', 'figure'),
              Output('words_freq_hist', 'figure'),
              Input('hist_bins_slider', 'value'))

def plot_freq_hist(nbins):
    fig1 = px.histogram(df,
                        x='num_chars',
                        nbins=nbins,
                        color_discrete_sequence=['#5BC0BE'],
                        title='Histogram - Character tweets distribution by length.',
                        marginal="box",
                        height=550,
                        labels={'num_chars':'Length of text in characters'})
    fig1.layout.paper_bgcolor = '#FFFFFF'
    fig1.layout.plot_bgcolor = '#FFFFFF'
    
    fig2 = px.histogram(df,
                        x='num_words',
                        nbins=nbins,
                        color_discrete_sequence=['#5BC0BE'],
                        title='Histogram - Words tweets distribution by length.',
                        marginal="box",
                        height=550,
                        labels={'num_words':'Length of text in words'})
    fig2.layout.paper_bgcolor = '#FFFFFF'
    fig2.layout.plot_bgcolor = '#FFFFFF'

    return fig1, fig2

@app.callback(Output('bar_freq_weekday', 'figure'),
              Input('year_weekday_dropdown', 'value'))
def plot_tweets_freq_weekday(year):
    if (not year):
        raise PreventUpdate

    df = df2[df2['year'].eq(year)]
    df = df['weekday'].value_counts().sort_index().to_frame().reset_index()
    
    fig = px.bar(df,
                 x='index',
                 y='weekday',
                 title='Bar chart - Tweets frequency by weekday.')
    return fig

layout = 0

if __name__ == '__main__':
    app.run_server(debug=True, port=8041)