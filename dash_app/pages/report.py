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
            dbc.Label('Year:'),
            dcc.Dropdown(id='random_tweet_year_dropdown',
                         #multi=True,
                         placeholder='Select one or more years',
                         options=[{'label': year, 'value': year} for year in df['year'].drop_duplicates().sort_values()]),
                    ]),
        dbc.Col([
            dbc.Label('Month:'),
            dcc.Dropdown(id='random_tweet_month_dropdown',
                         #multi=True,
                         placeholder='Select one or more years',
                         options=[{'label':month.title(), 'value':i} for i, month in months.items()]),
            ]),
        dbc.Col([
            dbc.Label('Day:'),
            dcc.Dropdown(id='random_tweet_day_dropdown',
                         #multi=True,
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
        dcc.Markdown(id='display_random_tweet_by_key_md',
                     style={'backgroundColor': '#FFFFFF', 'border': '2px solid powderblue', 'padding': '30px'}),]),
    html.Br(),
    html.Div(id='feedback_2'), 
    html.Div([
        dbc.Button("Generate a random tweet", outline=True, color="primary", className="me-1", size="sm", id="button1"),
            ], className="d-grid gap-2 col-6 mx-auto"),
    html.Br(),
    html.P('Conclusiones de los gráficos anteriores'),

############### Historical evolution of sentiment by keyword #################

    html.Br(),
    dbc.CardHeader(html.H3('Historical evolution of sentiment by keyword')),
    html.P('Explore tweet text sentiment by keyword.'),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Year:"),
            dcc.Slider(id='hist_slider', dots=True, min=2019, max=2022, step=1, included=False,
                       marks={x: str(x) for x in range(2019, 2023, 1)})
            ]),
        dbc.Col([
            dbc.Label("Keyword:"),
            dcc.Dropdown(id='hist_keyword',
                         placeholder='Select one keyword',
                         multi=True,
                         options=[{'label':keyword.title(), 'value':i}
                                  for i, keyword in keywords.items()]),

            ]),

        ]),
    html.Br(),
    html.Div([
        dbc.Button("Generate Graph", outline=True, color="primary", className="me-1", size="sm", id="button4"),
            ], className="d-grid gap-2 col-6 mx-auto"),
    html.Br(),html.Br(),
    dcc.Loading([
        dcc.Graph(id='hist_ev'),
        ]),
        

############### Word cloud by keyword and sentiment #################

    html.Br(),html.Br(),
    dbc.CardHeader(html.H3('Word cloud by keyword and sentiment')),
    html.P('Explore tweet text sentiment by keyword.'),
    html.Br(),   
    dbc.Col([
        dbc.Label('Keyword:'),
        dcc.Dropdown(id='word_cloud_sentiment_keyword_dropdown',
                     placeholder='Select one keyword',
                     options=[{'label':keyword.title(), 'value':i}
                     for i, keyword in keywords.items()]),
            ]),
    html.Br(),
    html.Div([
        dbc.Button("Generate Wordclouds", outline=True, color="primary", className="me-1", size="sm", id="button3"),
            ], className="d-grid gap-2 col-6 mx-auto"),
    html.Br(),html.Br(),
    dcc.Loading([
        html.Div([
            html.Img(id='word_cloud_keyword')
            ]),
        
        # dcc.Markdown(id='word_cloud_keyword',
        #              style={'backgroundColor': '#FFFFFF', 'border': '2px solid powderblue'}),
            ]),

############### Ratio of sentiment per keyword #################

    html.Br(),html.Br(),
    dbc.CardHeader(html.H3('Ratio of sentiment per keyword')),
    html.P('Explore tweet text sentiment by keyword.'),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Year:"),
            dcc.Slider(id='ratio_slider', dots=True, min=2019, max=2022, step=1, included=True,
                       marks={x: str(x) for x in range(2019, 2023, 1)})
            ]),
        dbc.Col([
            dbc.Label("Keyword:"),
            dcc.Dropdown(id='ratio_keyword',
                         placeholder='Select one keyword',
                         multi=True,
                         options=[{'label':keyword.title(), 'value':i}
                                  for i, keyword in keywords.items()]),

            ]),

        ]),
    html.Br(),
    html.Div([
        dbc.Button("Generate Graph", outline=True, color="primary", className="me-1", size="sm", id="button5"),
            ], className="d-grid gap-2 col-6 mx-auto"),
    html.Br(),html.Br(),
    dcc.Loading([
        dcc.Graph(id='ratio_graph'),
        ]),


])

############### Callbacks #####################


############### Explore tweet text sentiment by keyword #####################

@app.callback(Output('display_random_tweet_by_key_md', 'children'),
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

    random_tweet = df_filtered[['full_text', 'predicted_probability']].sample()


    tweet = random_tweet.iloc[0,0]
    predict_prob = random_tweet.iloc[0,1]

    if sentiment == 1:
        p_value = 100 * (2 * predict_prob - 1)
        name = 'Positive Probability'
    elif sentiment == 0:
        p_value = -100 * (2 * predict_prob - 1)
        name = 'Negative Probability'

    markdown = f""" 
    **Tweet:** {tweet}

    **Predicted Probability:** {predict_prob:.4f}

    **{name}**: {p_value:.2f}% 
    """

    return markdown


############### Historical evolution of sentiment by keyword #################

@app.callback(Output('hist_ev', 'figure'),
              Input('button4', 'n_clicks'),
              State('hist_slider', 'value'),
              State('hist_keyword', 'value'))

def plotly_month_keyword(nclicks, year ,keyword):

    if (not nclicks):
        raise PreventUpdate

    df_sent_freq=pd.DataFrame()
    df_plot=df[(df['year']==year)]
    for months in df_plot['month'].unique():
        df_cross=pd.crosstab(df_plot[df_plot['month']==months]['key_word'],df_plot[df_plot['month']==months]['sentiment']).reset_index()
        df_cross['total']=df_cross.sum(axis=1)
        df_cross['month']=months
        df_cross['porc_pos']=df_cross[1]/df_cross['total']
        df_cross=df_cross[['month','key_word','porc_pos']]
        df_sent_freq=pd.concat([df_sent_freq,df_cross])

    df_sent_freq.reset_index(drop=True,inplace=True)
    df_sent_freq=df_sent_freq.sort_values(by=['month','key_word'],ascending=True)
    fig=px.line(df_sent_freq[df_sent_freq['key_word'].isin(keyword)], 
        x='month', 
        y='porc_pos',
        color='key_word',
        markers=True,
        title='Frequency of Keywords in the Tweets',
        width=1000,
        height=600,
        color_discrete_sequence=px.colors.sequential.Turbo,
        labels={'porc_pos': '% Rate Positive Tweets', 'month': 'Months'},)

    newnames = {'1': 'Cultura', '2': 'Empresa', '3': 'Jovenes', '4': 'Metro', 
                '5': 'Movilidad', '6': 'Seguridad', '7': 'Tecnologia', 
                '8': 'Trabajo', '9': 'Vida'}
    fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )   
    
    fig.layout.paper_bgcolor = '#FFFFFF'
    fig.layout.plot_bgcolor = '#FFFFFF'
    fig.update_layout(title_font_size=15)

    return fig 





############### Word cloud by keyword and sentiment #################
@app.callback(Output('word_cloud_keyword', 'src'),
              Input('button3', 'n_clicks'),
              State('word_cloud_sentiment_keyword_dropdown', 'value'))


def gen_wordcloud(nclicks, keyword):

    if (not nclicks):
        raise PreventUpdate

    if keyword == 1:
        return 'assets/images/key_word_1.jpg'
    elif keyword == 2:
        return 'assets/images/key_word_2.jpg'
    elif keyword == 3:
        return 'assets/images/key_word_3.jpg'
    elif keyword == 4:
        return 'assets/images/key_word_4.jpg'
    elif keyword == 5:
        return 'assets/images/key_word_5.jpg'
    elif keyword == 6:
        return 'assets/images/key_word_6.jpg'
    elif keyword == 7:
        return 'assets/images/key_word_7.jpg'
    elif keyword == 8:
        return 'assets/images/key_word_8.jpg'
    elif keyword == 9:
        return 'assets/images/key_word_9.jpg'



############### Ratio of sentiment per keyword #################

# @app.callback(Output('ratio_graph', 'figure'),
#               Input('button5', 'n_clicks'),
#               State('ratio_slider', 'value'),
#               State('ratio_keyword', 'value'))









