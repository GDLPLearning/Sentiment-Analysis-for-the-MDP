# import libraries
# from app import app
import dash
from dash import dcc as dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd



df = pd.read_csv('data/2019.csv')
df['num_chars'] = df['full_text'].str.len()
df['num_words'] = df['full_text'].str.split().str.len()

app = dash.Dash(__name__)

app.layout = html.Div([

    dbc.Label('EDA I'),
    dcc.Dropdown(id='hist_kind_dropdown',
                 options=[{'label': 'num_words', 'value': 'num_words'},
                          {'label': 'num_chars', 'value': 'num_chars'}]),
    dcc.Graph(id='freq_hist')
    ])

@app.callback(Output('freq_hist', 'figure'),
              Input('hist_kind_dropdown', 'value'))
def plot_hist(kind):
    if kind == 'num_words':
        fig = px.histogram(df,
                           x = 'num_words')
        return fig
        


    if kind == 'num_chars':
        fig = px.histogram(df,
                           x = 'num_chars')
        return fig



layout = 0

if __name__ == '__main__':
    app.run_server(debug=True, port=8041)