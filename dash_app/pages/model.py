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
import pandas as pd
pd.options.display.max_columns = None
from pages import tools
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv('pages/data/sentiment_1_0.csv')

def log_reg(text):
    df_rating = df
    #df_rating=pd.read_csv('dash_app/pages/data/sentiment_1_0.csv')
    # clean the tweet and save it on a new column

    def clean_tweet(tweet):
        new_tweet=' '
        words = tweet.split()
        for w in words:
            wl = w.lower() # word in lower case
    
            # replace numbers
            for number, new_value in tools.replace_numbers_dict.items():
                wl = str(wl).replace(number,new_value)

            # replace some punctuations mark to keep only words
            for punctuation, new_value in tools.replace_punctuation_dict.items():
                wl = wl.replace(punctuation,new_value)
    
            # replace accent mark 
            for accent, new_value in tools.replace_accent_dict.items():
                wl = wl.replace(accent,new_value)

            if wl not in tools.model_stop_wprds:
                new_tweet += f'{wl} '
        return new_tweet[:-1]
    # clean data
    df_rating['clean_tweet'] = df_rating['full_text'].apply(clean_tweet)
    # split data into train and test
    tweets_train, tweets_test = train_test_split(df_rating, test_size=0.2, random_state=0)    # vectorize data
    vectorizer = CountVectorizer()
    x_train_bow = vectorizer.fit_transform(tweets_train['clean_tweet'])
    y_train_bow = tweets_train['sentiment']
    # train model
    lr_model_all = LogisticRegression()
    lr_model_all.fit(x_train_bow, y_train_bow)
    # predict
    text=clean_tweet(text)
    return lr_model_all.predict(vectorizer.transform([text]))[0]

def clean_tweet(tweet):

    new_tweet = ''
    words = tweet.split()
    for w in words:
        wl = w.lower() # word in lower case

        # replace numbers
        for number, new_value in tools.replace_numbers_dict.items():
            wl = str(wl).replace(number,new_value)

        # replace some punctuations mark to keep only words
        for punctuation, new_value in tools.replace_punctuation_dict.items():
            wl = wl.replace(punctuation,new_value)
        # replace accent
        for accent, new_value in tools.replace_accent_dict.items():
            wl = wl.replace(accent,new_value)

        # remove stop words
        if wl not in tools.model_stop_wprds:
            new_tweet += f'{wl} '

    return new_tweet[:-1]

def text_to_lower(tweet):
    new_tweet = ''
    words = tweet.split()
    for w in words:
        wl = w.lower() # word in lower case
        new_tweet += f'{wl} '
    return new_tweet[:-1]

def remove_numbers(tweet):
    new_tweet = ''
    words = tweet.split()
    for w in words:
        for number, new_value in tools.replace_numbers_dict.items():
            w = str(w).replace(number,new_value)
        new_tweet += f'{w} '
    return new_tweet[:-1]

def remove_punct(tweet):
    new_tweet = ''
    words = tweet.split()
    for w in words:
        for punctuation, new_value in tools.replace_punctuation_dict.items():
            w = w.replace(punctuation,new_value)
        new_tweet += f'{w} '
    return new_tweet[:-1]

def remove_accent(tweet):
    new_tweet = ''
    words = tweet.split()
    for w in words:
        for accent, new_value in tools.replace_accent_dict.items():
            w = w.replace(accent,new_value)
        new_tweet += f'{w} '
    return new_tweet[:-1]

def remove_stopword(tweet):
    new_tweet = ''
    words = tweet.split()
    for w in words:
        if w not in tools.model_stop_wprds:
            new_tweet += f'{w} '
    return new_tweet[:-1]


layout = html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Model'),
        html.H2(''),
        ], style={'textAlign': 'center'}),

############### Tweet text preprocessing #################

    dbc.CardHeader(html.H3('Tweet text preprocessing')),
    html.P('Explicacion de esta sección'),
    html.Br(),
    dbc.Label('Tweet text:'),
    dcc.Textarea(
        id='textarea_preprocess',
        placeholder='Enter the text of the tweet',
        style={'width': '100%', 'height': 100}),
    html.Div([
        dbc.Button("Preprocess Text", outline=True, color="primary", className="me-1", size="sm", id="button1"),
        ],  className="d-grid gap-2 col-6 mx-auto"), 
    html.Br(),
        dcc.Loading([
            dcc.Markdown(id='display_preprocess_tweet_text_md',
                        style={'backgroundColor': '#FFFFFF', 'border': '2px solid powderblue', 'padding': '30px'}),
        ]),

############### Tweet classification #################
    html.Br(),
    dbc.CardHeader(html.H3('Tweet classification')),
    html.P('Explicacion de esta sección'),
    html.Br(), 
     html.Div([
        dbc.Button("Sentiment classification", outline=True, color="primary", className="me-1", size="sm", id="button2"),
        ],  className="d-grid gap-2 col-6 mx-auto"), 
    html.Br(),
        dcc.Loading([
            dcc.Markdown(id='display_tweet_sentiment_md',
                        style={'backgroundColor': '#FFFFFF', 'border': '2px solid powderblue', 'padding': '30px'}),
        ]),
    ])


############### Callbacks #################

############### Tweet text preprocessing #################

@app.callback(Output('display_preprocess_tweet_text_md', 'children'),
              Input('button1', 'n_clicks'),
              State('textarea_preprocess', 'value'))

def display_preprocees_text(nclicks, text):

    if (not nclicks):
        raise PreventUpdate

    clean_text = clean_tweet(text)

    text1 = text_to_lower(text)
    text2 = remove_numbers(text1)
    text3 = remove_punct(text2)
    text4 = remove_accent(text3)
    text5 = remove_stopword(text4)


    markdown = f"""

    ###### Raw Text

    {text}

    ----

    ###### Unify the case of the text: convert it to lowercase.

    {text1}

    ----


    ###### Remove numbers.

    {text2}

    ----


    ###### Remove punctuation marks and special characters

    {text3}

    ----


    ###### Remove accents

    {text4}

    ----

    ###### Remove stopwords

    {text5}

    ----

    ###### All funct together

    {clean_text}

    """

    return markdown

@app.callback(Output('display_tweet_sentiment_md', 'children'),
              Input('button2', 'n_clicks'),
              State('textarea_preprocess', 'value'))

def gen_sentiment(nclicks, tweet):
    if (not nclicks):
        raise PreventUpdate

    sentiment = log_reg(tweet)

    if sentiment:
        markdown = f"Positive 😃✅"
    else:
        markdown = f"Negative 😡❌"



    return markdown

