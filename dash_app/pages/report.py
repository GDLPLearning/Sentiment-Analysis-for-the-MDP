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

################## Redacción ##################

p1 = f"""
Welcome to the report, this last section summarizes all the significant findings 
during the development of the project, exposes its limitations, the requirements 
to improve it, in which other fields of action something similar can be executed 
and most importantly, answers the second hypothesis of the problem: What is the 
perception of the citizens in relation to the programs and projects during
the government's term? Enjoy the end of this journey!

"""

p2 = f"""
Thanks to the model it is now possible to tag each of our tweets with a sentiment 
and an associated prediction probability. At this point, it is time to put our approach 
under a critical eye and define lines of improvement or recognize its strengths.
To do this, the first thing we will do is to know the content of the tweets this 
time using more filters (time stamp, keyword and sentiment), with this it is easier 
to locate a positive or a negative tweet and see if it responds to a trend thanks to 
the variables of time or how much if they differ in the way of writing them, before 
moving to the conclusions of this section we invite you to generate a couple of random 
tweets and generate ideas and see how much they match the ideas proposed by those 
responsible for the project. 

"""

p3_1 = f"""

After several minutes of exploration (it is very catching), we can affirm that 
the context of the word and its wide semantic spectrum deviates the ability to 
conclude with total certainty the reflection of a need. An example of this, 
could be the keyword 'Trabajo', our goal at the time it was chosen was to be used 
as a proxy for the macroeconomic variable of employment, however, many job offer 
tweets seem to surface and according to the model algorithm they will be classified 
in some sentiment, but is then a job offer something positive? We could state what 
yes, new jobs are generated and employment is expected to be reduced, but what about 
'Trabajo' when it refers to someone's job? Here the interpretation is more subjective.
"""
p3_2 = f"""

With this, for the future development of the project we have proposed to add the 
sentiment 'neutral' to the classification categories so that texts that are not 
very clear to define do not bias our interpretation (cell phone plan spam, we 
refer to you). The other recommendation is to generate subcategories when querying 
the API or when exploring the chosen category, using NLP and extending the previous 
example, we could use a subcategory that refers to job offers and interpret it as an 
indicator for the generation of new positions, while giving a wider range to the 
user if they wants to know more specific dynamics.
"""
p3_3 = f"""

One approach proposed for the development of this project was to use the programs and 
projects of each of the strategic lines, however, this made it impossible for us to compare 
them before and after because we would have no way to explore them before the plan, since 
they had not been executed until the current mayor took office. This is a reminder that the 
initial problem must always be kept in mind and that the approach must be coherent. Remember to share your findings with us.

"""

p4 = f"""
To answer the second question proposed in the problem we needed information that would 
allow us to visualize a change in the number of positive and negative tweets over 
time and how was the behavior on twitter for these same keywords before the development 
plan of the city of Medellin came into force. Therefore, we decided to visualize the 
proportion of positive tweets compared to negative ones, and thus have the change month 
by month in the years of our analysis. We invite the user to explore the graph before 
jumping to the conclusions, and to complement the information in this with the previous 
section, if you see a very pronounced change in any of the months, use the random tweet 
generator for that date and know the nature of them.

"""

p5 = f"""
The first finding to highlight is the appearance of two clusters in all years, one set 
of words has a higher proportion of negative tweets while others stand out for the positive, 
to go deeper into this we will have to look at the proportion in detail. The second, 
best seen in the report document associated with this project, where more clearly this 
will be detailed (spoiler alert), trends or seasonality reflect volatility. 

"""

p6 = f"""
When we were discussing the conclusions of the project, one of our members wondered 
what made a keyword to be recognized as negative or positive, going into detail about 
this could give us an approximation to the content they express and their social load. 
What usually accompanies this keyword? With how much recurrence? Is this easy to interpret? 
Is there a very marked difference between positive and negative sentiment according to the 
filtered word? For this we generated word clouds where we grouped the frequency of words 
from tweets categorized by positive, negative and general (or words in common), remember 
to draw your conclusions before moving on to ours.
"""

p7 = f"""
This analysis was more profitable than expected, it could even serve as an input to 
generate new public policies in order to change the citizen's perception of sensitive 
issues, the power of social networks cannot be underestimated. The most evident example 
of this section was with the keyword "culture", in common terms culture is centered on being 
"paisa", on its people, on the city, they seem to be very proud of them, also of their "metro", 
however, the more they love it, the more they seem to criticize it. For the positive, we find 
the expected, words like art, theater, music, artists, festivals take importance, but when we 
focus on the opposite side, another reality appears. The negative culture of Medellin is associated 
with violence, Pablo Escobar, mafias, a "traqueta" culture and cartels, this exploration by opposite 
poles allows us to evidence the good performances of some subcategories of the key word, while 
sounding the alarm for those associated with negative feelings. 


"""

p8 = f"""
To close we wanted to list those keywords that after our analysis represented a high unfavorable 
image, and highlight those with better performance in terms of interaction on Twitter. Therefore, 
we focused on sentiment proportionality in each of our categories. Do you have any idea which 
keywords might be the ones with the highest negative interaction?

"""

p9 = f"""
The words with the highest number of negative tweets are: 'Metro', 'Movilidad' and 'Seguridad', 
while the words with the highest number of positive tweets are: 'Vida', 'Trabajo' and 'Cultura'. We can 
also highlight the word that generates the least interaction: 'Tecnologia' and the two with the 
most interaction: 'Metro' and 'Vida'. We hope this tour has been to your liking, remember to 
consult all the complementary resources to this project to go into technical details and 
complement the sections. 

"""
layout = html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Report'),
        html.H2(''),
    ], style={'textAlign': 'center'}),
    html.Br(),html.Br(),
    html.P(p1),



############### Explore tweet text sentiment by keyword #################
    html.Br(),html.Br(),
    dbc.CardHeader(html.H3('Explore tweet text sentiment by keyword')),
    html.Br(),
    html.P(p2),
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
    html.Div([

        dbc.Alert(f"Select a value for year, month, day, keyword and sentiment, otherwise the default value will be selected, then press the button to generate a random tweet, every time you press it a new random tweet will be generated.",
                         color="info",
                         fade=True,
                         is_open=True,
                         dismissable=True,)

        ], id='explore_feedback'),
    html.Div([
                dbc.Alert(f"At the time of viewing this message, the model has an accuracy of 77.7%, so the user may find unexpected results. Please send us your report.",
                         color="warning",
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],

                id='class_warn1'), 
    html.Div([
        dbc.Button("Generate a random tweet", outline=True, color="primary", className="me-1", size="sm", id="button1"),
            ], className="d-grid gap-2 col-6 mx-auto"),
    html.Br(),html.Br(),
    html.P(p3_1), html.P(p3_2), html.P(p3_3),

############### Historical evolution of sentiment by keyword #################

    html.Br(),
    dbc.CardHeader(html.H3('Historical evolution of sentiment by keyword')),
    html.Br(),
    html.P(p4),
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
                dbc.Alert(f"Select a year and one or more keywords to observe the evolution month by month during that year of the rate of positive tweets per keyword.",
                         color="info",
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],

                id='historical_alert'),
    html.Br(),
    html.Div([
        dbc.Button("Generate Graph", outline=True, color="primary", className="me-1", size="sm", id="button4"),
            ], className="d-grid gap-2 col-6 mx-auto"),
    html.Br(),html.Br(),
    dcc.Loading([
        dcc.Graph(id='hist_ev'),
        ]),
    html.Br(),html.Br(),
    html.P(p5),
        

############### Word cloud by keyword and sentiment #################

    html.Br(),html.Br(),
    dbc.CardHeader(html.H3('Word cloud by keyword and sentiment')),
    html.Br(),
    html.P(p6),
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
            dbc.Alert(f"Select a keyword to generate three word clouds: positive sentiment, neutral words and negative sentiment.",
                         color="info",
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],

                id='wc_alert'),
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
    html.Br(),html.Br(),
    html.P(p7),

############### Ratio of sentiment per keyword #################

    html.Br(),html.Br(),
    dbc.CardHeader(html.H3('Ratio of sentiment per keyword')),
    html.Br(),
    html.P(p8),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Years:"),
            dcc.Dropdown(id='ratio_year',
                         multi=True,
                         placeholder='Select one or more years',
                         options=[{'label': year, 'value': year} for year in df['year'].drop_duplicates().sort_values()]),
            ]),
        dbc.Col([
            dbc.Label("Keywords:"),
            dcc.Dropdown(id='ratio_keyword',
                         placeholder='Select one keyword',
                         multi=True,
                         options=[{'label':keyword.title(), 'value':i}
                                  for i, keyword in keywords.items()]),

            ]),

        ]),
    html.Br(),
    html.Div([

        dbc.Alert(f"Select one or more years and one or more keywords to generate a graph with the number of positive tweets vs. the number of negative tweets for the selected years. .",
                         color="info",
                         fade=True,
                         is_open=True,
                         dismissable=True,)

        ], id='ratio_feedback'),
    html.Br(),
    html.Div([
        dbc.Button("Generate Graph", outline=True, color="primary", className="me-1", size="sm", id="button5"),
            ], className="d-grid gap-2 col-6 mx-auto"),
    html.Br(),html.Br(),
    dcc.Loading([
        dcc.Graph(id='ratio_graph'),
        ]),
    html.Br(),html.Br(),
    html.P(p9),


])

############### Callbacks #####################


############### Explore tweet text sentiment by keyword #####################

@app.callback(Output('explore_feedback', 'children'),
              Output('display_random_tweet_by_key_md', 'children'),
              Input('button1', 'n_clicks'),
              State('random_tweet_year_dropdown', 'value'),
              State('random_tweet_month_dropdown', 'value'),
              State('random_tweet_day_dropdown', 'value'),
              State('random_tweet_keyword_dropdown', 'value'),
              State('random_tweet_sentiment_dropdown', 'value'),)

def gen_random_tweet(nclicks, year, month, day, keyword, sentiment):

    if (not nclicks):
        raise PreventUpdate

    if (not year) and (not month) and (not day) and (not keyword) and (not sentiment):
        year = 2019
        month = 12
        day = 24
        keyword = 9 
        sentiment = 1 

    df_filtered = df[(df['year'].eq(year)) & (df['month'].eq(month)) & (df['day'].eq(day)) & (df['key_word'] == (keyword)) & (df['sentiment'].eq(sentiment))]

    try:
        random_tweet = df_filtered[['full_text', 'predicted_probability']].sample()
    except ValueError:
        raise PreventUpdate
    else:

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

        sentiments = {1: 'Positive', 0:'Negative'}


    message = dbc.Alert(f"Random tweet generated successfully, you have chosen: {year} (year), {month} (month), {day} (day), {keywords.get(keyword)} (keyword) and {sentiments.get(sentiment)} (sentiment).",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True,)

    return message, markdown


############### Historical evolution of sentiment by keyword #################

@app.callback(Output('historical_alert', 'children'),
              Output('hist_ev', 'figure'),
              Input('button4', 'n_clicks'),
              State('hist_slider', 'value'),
              State('hist_keyword', 'value'))

def plotly_month_keyword(nclicks, year ,keyword):

    if (not nclicks):
        raise PreventUpdate

    if (not year) or (not keyword):
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
        title=f'Month-to-month evolution of the rate of positive tweets by keyword [<b>{year}</b>].',
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

    names = ''
    for word in keyword:
        names += keywords.get(word) + ', '


    message = dbc.Alert(f"The graph has been successfully generated, , you have chosen: {names} (keyword), {year} (year).",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True,)

    return message, fig 





############### Word cloud by keyword and sentiment #################
@app.callback(Output('wc_alert', 'children'),
              Output('word_cloud_keyword', 'src'),
              Input('button3', 'n_clicks'),
              State('word_cloud_sentiment_keyword_dropdown', 'value'))


def gen_wordcloud(nclicks, keyword):

    if (not nclicks):
        raise PreventUpdate

    if (not keyword):
        raise PreventUpdate



    message = dbc.Alert(f"The word clouds have been generated successfully, you have selected the keyword: {keywords.get(keyword)}.",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True,)

    if keyword == 1:
        return message,'assets/images/key_word_1.jpg'
    elif keyword == 2:
        return message,'assets/images/key_word_2.jpg'
    elif keyword == 3:
        return message,'assets/images/key_word_3.jpg'
    elif keyword == 4:
        return message,'assets/images/key_word_4.jpg'
    elif keyword == 5:
        return message,'assets/images/key_word_5.jpg'
    elif keyword == 6:
        return message,'assets/images/key_word_6.jpg'
    elif keyword == 7:
        return message,'assets/images/key_word_7.jpg'
    elif keyword == 8:
        return 'assets/images/key_word_8.jpg'
    elif keyword == 9:
        return message,'assets/images/key_word_9.jpg'



############### Ratio of sentiment per keyword #################

@app.callback(Output('ratio_feedback', 'children'),
              Output('ratio_graph', 'figure'),
              Input('button5', 'n_clicks'),
              State('ratio_year', 'value'),
              State('ratio_keyword', 'value'))

def freq_year(nclicks, year, keyword):

    if (not nclicks):
        raise PreventUpdate

    if (not year) or (not keyword):
        raise PreventUpdate


    df_year=df[(df['year'].isin(year))]
    df_count=df_year.groupby(['key_word','sentiment']).size().reset_index().rename(columns={0: 'frequency'})
    df_count.replace({'sentiment': {0: 'Negative', 1: 'Positive'}}, inplace=True)
    df_count=df_count[df_count['key_word'].isin(keyword)]
    df_count.replace({'key_word':{1:'Cultura',2:'Empresa',3:'Jovenes',4:'Metro',5:'Movilidad',6:'Seguridad',7:'Tecnologia',8:'Trabajo',9:'Vida'}},inplace=True)
    fig=px.bar(df_count,
               x='key_word',
               y='frequency',
               color='sentiment',
               title=f'Frequency of tweets by sentiment <b>{year}</b>',
               barmode='group',
               text_auto='.2s',
               color_discrete_map={'Positive':'#5BC0BE', 'Negative':'#1C2541'},
               width=1000,
               height=600,
               labels={'key_word':'Keywords'})
    fig.update_traces(marker_line_width=1.5, opacity=0.7)
    fig.update_layout(title_font_size=15)
    fig.layout.paper_bgcolor = '#FFFFFF'
    fig.layout.plot_bgcolor = '#FFFFFF'

    names = ''
    for word in keyword:
        names += keywords.get(word) + ', '

    message = dbc.Alert(f"The graph has been generated successfully, you have selected: {names} (keywords) and {year} (years).",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True,)
    
    return message, fig









