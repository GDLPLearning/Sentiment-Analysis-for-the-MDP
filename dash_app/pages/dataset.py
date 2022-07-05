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


layout = html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Dataset'),
        html.H2('Dataset selector'),
        ], style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    dcc.Dropdown(id='dataset_selection',
                 placeholder='Select one dataset',
                 options=[{'label':'Tweets 2019', 'value':'Tweets 2019'},
                          {'label':'Tweets keywords 2019 - 2022', 'value':'Tweets keywords 2019 - 2022'},
                          {'label':'Dataset Model', 'value':'Dataset Model'}]),
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
              Input('dataset_selection', 'value'))

def dataset_info_display(dataset):
    if (not dataset):
        raise PreventUpdate

    if dataset == 'Tweets 2019':

        markdown = """

        Column name (datatype): description.

        **Size:** 4.3 MB

        **Shape:** (17700, 9)

        **Creation:**

        **Purpose:**
    """
    elif dataset == 'Tweets keywords 2019 - 2022':

        markdown = """

        -----

        **Size:** 90.9 MB

        **Shape:** (17700, 9)

        **Creation:**

        **Purpose:**


        """
    elif dataset == 'Dataset Model':


        markdown = """

        **Size:** 4.3 MB

        **Shape:** (17700, 9)

        **Creation:**

        **Purpose:**


        """
    return markdown


# html.Div([
#     html.Div(html.H1(children="DATASET")),
#     html.Div([
#         html.H3(children="Data description",style={'text-align': 'left'}),
#         html.Br(),
#         DataTable(data=df_description.to_dict('records'),columns=[{"name": i, "id": i} for i in df_description.columns])
#     ])
# ])

# x = '''

#         | No    | column name (variable)    | datatype  | description                               |
#         |----   |------------------------   |---------- |---------------------------------------    |
#         | 1     | full text                 | string    | full text of the tweet                    |
#         | 2     | user                      | string    | username who posted the tweet             |
#         | 3     | location                  | string    | location where the tweet was post         |
#         | 4     | date                      | datetime  | time when the tweet was post              |
#         | 5     | tweet id                  | str       | primary key, number id of the tweet       |
#         | 6     | number rt                 | int       | number of retweets of the tweet           |
#         | 7     | number likes              | int       | number of likes of the tweet              |
#         | 8     | number reply              | int       | number of likes in the reply              |
#         | 9     | conversation id           | int       | identification number of conversation     |

#         -----

#     '''