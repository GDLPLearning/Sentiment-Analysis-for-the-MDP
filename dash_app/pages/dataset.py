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


p = f"""
Welcome to the dataset, in this section you can  access to a description of the data 
used for this project,  the consolidation of the information in different datasets, 
the variables used, the size of the data, how the dataframes were created and the 
purpose of their creations within the execution of the project."
"""

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
    if (not dataset):
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

        This dataset was created by the search query in the API, which was performed by 
        putting ``Medellin" as a parameter in the search, and 01 January to 31 December 
        of the 2019 year as the beginning and end date points. The file size of this 
        dataset was 4.3 MB and contained a total of 17700 tweets.

        #### Purpose

        This dataset was created to make a first exploratory analysis in order 
        to obtain a first approach and data understanding about the most relevant 
        issues and concerns of the population about Medellin on Twitter. This was 
        done to verify if these issues are correlated or included in the projects 
        and strategic lines of work proposed in the MPD.

    """

    elif dataset == 'Medellin Development Plan':

        markdown = """

        ### Variables


        In this case, this dataset was formed only with the raw text from the 
        document Medellin Development Plan of Medellin 2020-2023 (DPM). Within 
        DMP document there is a chapter called “Líneas Estratégicas” which establishes 
        the different strategic lines of action that encompass the proposals of the 
        government plan and its execution in relation to the most important issues 
        for the city future. For this reason, it was performed a text analysis in 
        order to obtain the most relevant words (the words with higher frequency in 
        the text) for each PDM strategic line This dataset contains all the words 
        contained in the 5 strategic lines of this document.   

        #### Size

        966 KB

        #### Shape

        PDF File: 1543 pages (Full document)
        PDF FIle: 268 pages (Chapter of Strategic Lines)

        #### Creation

        This dataset was formed from the extraction of all the words contained in 
        the strategic lines of PDM document.

        #### Purpose

        Obtain the most relevant words (the words with the highest frequency 
        in the text) for each strategic line of the MDP. This dataset contains 
        all the words contained in the 5 strategic lines of this document. It also 
        helps us to answer our first hypothesis: Is the MDP aligned with the 
        expressed by the population?

        """
    elif dataset == 'Tweets keywords 2019 - 2022':

        markdown = """

        ### Variables


        - **full_text** (string): *Full text of the tweet.*
        - **user** (string): *Username who posted the tweet.*
        - **location** (string): *Location where the tweet was post.*
        - **date** (datetime): *Time when the tweet was post.*
        - **tweet_id** (str): *Primary key, number id of the tweet.*
        - **number_rt** (int): *Number of retweets of the tweet.*
        - **number_likes** (int): *Number of likes of the tweet.*
        - **number_reply** (int): *Number of likes in the reply.*
        - **conversation_id** (int): *Identification number of conversation.*
        - **id_key_word** (int): *Primary key*
        - **key_word** (string): *Key word used to search the tweet*

        #### Size

        90.9 MB

        #### Shape

        Dataframe: (303008, 11)

        #### Creation

        This second dataset was created after the data understanding was performed, 
        this stage included the exploratory data analysis of the Tweets 2019 and 
        the MDP document. In order to consolidate this first dataset, denominated 
        in this project such as **Tweets keywords 2019 - 2022**, various search 
        queries were done in the API for the years 2019, 2020, 2021, and so far 
        2022 taking search parameters a list of strategic keywords extracted 
        from the MDP document, oriented to the lines of the plan to be measured.

        #### Purpose

        This dataset was created in order to make the exploratory data analysis for the **Tweets 2019 - 2022**.

        """
    elif dataset == 'Dataset Model':

        markdown = """

        ### Variables


        - **full_text** (string): *Full text of the tweet.*
        - **user** (string): *Username who posted the tweet.*
        - **location** (string): *Location where the tweet was post.*
        - **date** (datetime): *Time when the tweet was post.*
        - **tweet_id** (str): *Primary key, number id of the tweet.*
        - **number_rt** (int): *Number of retweets of the tweet.*
        - **number_likes** (int): *Number of likes of the tweet.*
        - **number_reply** (int): *Number of likes in the reply.*
        - **conversation_id** (int): *Identification number of conversation.*
        - **id_key_word** (int): *Primary key.*
        - **key_word** (string): *Key word used to search the tweet.* 

        #### Size

        90.9 MB

        #### Shape

        Dataframe: (303008, 11)

        #### Creation

        This dataset was created as a result of the data preparation stage on  
        the **Tweets keywords 2019 - 2022** after a cleaning an preparing text process.

        #### Purpose

        This dataset was created as a result of the data preparation stage on  
        the **Tweets keywords 2019 - 2022** after a cleaning an preparing text process.

        """
    message = dbc.Alert(f"You have selected the dataset: {dataset}.",
                        color='success',
                        fade=True,
                        is_open=True,
                        duration=4000,
                        dismissable=True,)

    return markdown, message
