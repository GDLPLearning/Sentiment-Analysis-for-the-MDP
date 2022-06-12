# import libraries
import dash
from dash.dash_table import DataTable
from dash import dcc as dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd

#Create data description
data_description={
    'column_name':['full_text','user','location','date','tweet_id','number_rt','number_likes','id_key_word'],
    'data_type':['string','string','string','datetime','int','int','int','int'],
    'description':['full text of the tweet','username who posted the tweet','location where the tweet was post','time when the tweet was post','primary key, number id of the tweet','number of retweets of the tweet','number of likes of the tweet','foreign key with the id that represent the key word']
    }
df_description=pd.DataFrame(data_description)


layout = html.Div([
    html.Div(html.H1(children="DATASET")),
    html.Div([
        html.H3(children="Data description",style={'text-align': 'left'}),
        html.Br(),
        DataTable(data=df_description.to_dict('records'),columns=[{"name": i, "id": i} for i in df_description.columns])
    ])
])