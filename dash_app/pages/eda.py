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


df = pd.read_csv('pages/data/2019.csv')
df['num_chars'] = df['full_text'].str.len()
df['num_words'] = df['full_text'].str.split().str.len()


df2 = pd.read_csv('pages/data/tweets.csv')
df2['weekday'] = pd.to_datetime(df2['date']).dt.weekday
df2['year'] = pd.to_datetime(df2['date']).dt.year
df2['month'] = pd.to_datetime(df2['date']).dt.month


df3 = df2['year'].value_counts().sort_index().to_frame().reset_index()
fig = px.pie(df3,values='year',names='index', 
    title=f'Pie chart - Tweets distribution by year.')


# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])


def make_empty_fig():
    fig = go.Figure()
    fig.layout.paper_bgcolor = '#FFFFFF'
    fig.layout.plot_bgcolor = '#FFFFFF'
    return fig

layout = html.Div([
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
    html.Br(),
    html.P('Conclusiones de los gráficos anteriores'),
    dbc.Col([
        html.Br(),
        html.H2('Data understanding II'),
        ], style={'textAlign': 'center'}),

    html.Br(),
    html.Br(),
    html.H4('EDA: Tweets keywords 2019 - 2022'),
    html.Br(),
    html.Br(),
    dcc.Dropdown(id='year_weekday_dropdown',
                 placeholder='Select one year',
                 #multi=True,
                 #placeholder='Select one or more years',
                 options=[{'label': year, 'value': year} for year in df2['year'].drop_duplicates().sort_values()]),
    dcc.Graph(id='bar_freq_weekday', figure=make_empty_fig()),
    dcc.Markdown(id='indicator_map_details_md',
                 style={'backgroundColor': '#E5ECF6'}),
    
    html.Br(),
    dbc.Row([
        dbc.Col(lg=9),
        dbc.Col([
        dcc.Dropdown(id='year_keyword_dropdown',
                     placeholder='Select one year',
                     options=[{'label': year, 'value': year} for year in df2['year'].drop_duplicates().sort_values()])  
            ], lg=3),
        ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig)], lg=4),
        dbc.Col([
            dcc.Markdown(id='year_keyword_md',
                        style={'backgroundColor': '#E5ECF6'}),
            ], lg=3), 
        dbc.Col([dcc.Graph(id='year_keyword_piechart', figure=make_empty_fig())], lg=5)
        

        ]),

    html.Br(),
    html.Br(),
    dcc.Dropdown(id='year_month_dropdown',
                 placeholder='Select one year',
                 #multi=True,
                 #placeholder='Select one or more years',
                 options=[{'label': year, 'value': year} for year in df2['year'].drop_duplicates().sort_values()]),
    dcc.Graph(id='bar_freq_month', figure=make_empty_fig()),
    dcc.Markdown(id='year_month_freq_md',
                 style={'backgroundColor': '#E5ECF6'}),
     
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
                        width=600,
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
                        width=600,
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
                 title=f'Bar chart - Tweets frequency by weekday ({year}).',
                 labels={'index': 'weekdays', 'weekday': 'number of tweets'},
                 text_auto='.2s')
    fig.update_traces(marker_color='rgb(91,192,190)', marker_line_color='rgb(54,115,114)',
                  marker_line_width=1.5, opacity=0.7)
    fig.layout.paper_bgcolor = '#FFFFFF'
    fig.layout.plot_bgcolor = '#FFFFFF'
    return fig

@app.callback(Output('year_keyword_piechart', 'figure'),
              Output('year_keyword_md', 'children'),
              Input('year_keyword_dropdown', 'value'))

def plot_year_keyword_piechart(year):
    if (not year):
        raise PreventUpdate
    df = df2[df2['year'].eq(year)]
    df = df['key_word'].value_counts().sort_index().to_frame().reset_index()
    fig = px.pie(df,values='key_word',names='index',
                 title=f'Pie chart - Tweets distribution by keyword ({year}).')

    if year == 2019:
        markdown = f'Texto descriptivo para el año 2019'
    elif year == 2020:
        markdown = f'Texto descriptivo para el año 2020'
    elif year == 2021:
        markdown = f'Texto descriptivo para el año 2021'
    elif year == 2022:
        markdown = f'Texto descriptivo para el año 2022'
    
    return fig, markdown

@app.callback(Output('bar_freq_month', 'figure'),
              Output('year_month_freq_md', 'children'),
              Input('year_month_dropdown', 'value'))
def plot_tweets_freq_weekday(year):
    if (not year):
        raise PreventUpdate

    df = df2[df2['year'].eq(year)]
    df = df['month'].value_counts().sort_index().to_frame().reset_index()
    
    fig = px.bar(df,
                 x='index',
                 y='month',
                 title=f'Bar chart - Tweets frequency by month ({year}).',
                 labels={'index': 'months', 'month': 'number of tweets'},
                 text_auto='.2s')
    fig.update_traces(marker_color='rgb(91,192,190)', marker_line_color='rgb(54,115,114)',
                  marker_line_width=1.5, opacity=0.7)
    fig.layout.paper_bgcolor = '#FFFFFF'
    fig.layout.plot_bgcolor = '#FFFFFF'

    if year == 2019:
        markdown = f'Texto descriptivo para el año 2019'
    elif year == 2020:
        markdown = f'Texto descriptivo para el año 2020'
    elif year == 2021:
        markdown = f'Texto descriptivo para el año 2021'
    elif year == 2022:
        markdown = f'Texto descriptivo para el año 2022'

    return fig, markdown
