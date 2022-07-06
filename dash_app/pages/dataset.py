# import libraries
from app import app
import dash
from dash.dash_table import DataTable
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import pandas as pd

#Create data description
data_description={
    'column_name':['full_text','user','location','date','tweet_id','number_rt','number_likes','id_key_word'],
    #'data_type':['string','string','string','datetime','int','int','int','int'],
    'description':['full text of the tweet','username who posted the tweet','location where the tweet was post','time when the tweet was post','primary key, number id of the tweet','number of retweets of the tweet','number of likes of the tweet','foreign key with the id that represent the key word']
    }
df_description=pd.DataFrame(data_description)


p = f"Descripcion de esta seccion"

layout = html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Dataset'),
        html.Br(),html.Br(),
        ], style={'textAlign': 'center'}),
    html.P(p),
    html.Br(), html.Br(),
    dbc.CardHeader(html.H2('Dataset selector')),
    html.Br(),
    html.Br(),
    dcc.Dropdown(id='dataset_selection',
                 placeholder='Select one dataset',
                 options=[{'label':'Tweets 2019', 'value':'Tweets 2019'},
                          {'label':'Medellin Development Plan', 'value':'Medellin Development Plan'},
                          {'label':'Tweets keywords 2019 - 2022', 'value':'Tweets keywords 2019 - 2022'},
                          {'label':'Dataset Model', 'value':'Dataset Model'}]),
    html.Br(),
    html.Div([
                dbc.Alert(f"Please choose a dataset from the dropdown to display its description.",
                         color='info',
                         fade=True,
                         is_open=True,
                         dismissable=True,)
                ],

                id='feedback_dataset'),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(lg=2),
        dbc.Col([
            dcc.Markdown(id='dataset_details_md',
                         style={'backgroundColor': '#FFFFFF'}),
            ],lg=8)

        ]),
    ])


@app.callback(Output('dataset_details_md', 'children'),
              Output('feedback_dataset', 'children'),
              Input('dataset_selection', 'value'))

def dataset_info_display(dataset):
    if (not dataset) and (not dataset):
        raise PreventUpdate

    if dataset == 'Tweets 2019':

        markdown = """

        ### Variables


        - **full_text** (string): *Full text of the tweet.*
        - **user** (string): *Username who posted the tweet.*
        - **location** (string): *Location where the tweet was post.*
        - **date** (datetime): *Time when the tweet was post.*
        - **tweet_id** (str): *Primary key, number id of the tweet.*
        - **number rt** (int): *Number of retweets of the tweet.*
        - **number likes** (int): *Number of likes of the tweet.*
        - **number reply** (int): *Number of likes in the reply.*
        - **conversation_id** (int): *Identification number of conversation.* 

        #### Size

        4.3 MB

        #### Shape

        Dataframe: (17700, 9)

        #### Creation

        desc

        #### Purpose

        desc
    """

    elif dataset == 'Medellin Development Plan':

        markdown = """

        ### Variables


        - **full_text** (string): *Full text of the tweet.*
        - **user** (string): *Username who posted the tweet.*
        - **location** (string): *Location where the tweet was post.*
        - **date** (datetime): *Time when the tweet was post.*
        - **tweet_id** (str): *Primary key, number id of the tweet.*
        - **number rt** (int): *Number of retweets of the tweet.*
        - **number likes** (int): *Number of likes of the tweet.*
        - **number reply** (int): *Number of likes in the reply.*
        - **conversation_id** (int): *Identification number of conversation.* 

        #### Size

        4.3 MB

        #### Shape

        PDF File: #### pages.

        #### Creation

        desc

        #### Purpose

        desc

        """
    elif dataset == 'Tweets keywords 2019 - 2022':

        markdown = """

        ### Variables


        - **full_text** (string): *Full text of the tweet.*
        - **user** (string): *Username who posted the tweet.*
        - **location** (string): *Location where the tweet was post.*
        - **date** (datetime): *Time when the tweet was post.*
        - **tweet_id** (str): *Primary key, number id of the tweet.*
        - **number rt** (int): *Number of retweets of the tweet.*
        - **number likes** (int): *Number of likes of the tweet.*
        - **number reply** (int): *Number of likes in the reply.*
        - **conversation_id** (int): *Identification number of conversation.* 

        #### Size

        4.3 MB

        #### Shape

        Dataframe: (17700, 9)

        #### Creation

        desc

        #### Purpose

        desc

        """
    elif dataset == 'Dataset Model':

        markdown = """

        ### Variables


        - **full_text** (string): *Full text of the tweet.*
        - **user** (string): *Username who posted the tweet.*
        - **location** (string): *Location where the tweet was post.*
        - **date** (datetime): *Time when the tweet was post.*
        - **tweet_id** (str): *Primary key, number id of the tweet.*
        - **number rt** (int): *Number of retweets of the tweet.*
        - **number likes** (int): *Number of likes of the tweet.*
        - **number reply** (int): *Number of likes in the reply.*
        - **conversation_id** (int): *Identification number of conversation.* 

        #### Size

        4.3 MB

        #### Shape

        Dataframe: (17700, 9)

        #### Creation

        desc

        #### Purpose

        desc

        """
    message = dbc.Alert(f"You have selected the dataset: {dataset}.",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True,)

    return markdown, message
