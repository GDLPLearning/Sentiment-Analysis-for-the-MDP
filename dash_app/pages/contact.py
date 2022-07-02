# import libraries
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


style_div={
    'border':'#5BC0BE 0.03rem solid ',
    'border-radius':'1rem',
    'padding':'10px',
    #'background-color':'#CCC9DC'
}


layout=html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Contact us'),
    ], style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H4('Gustavo Vergara', style={'textAlign': 'center'}),
                html.Img(src='assets/profile/gv.png', style={'width': '45%', 'height': '45%', 'border-radius': '50%', 'margin-left': '25%'}),
                html.Ul([
                    html.Li('Matematician, Universidad Del Norte'),
                    html.Li('Professor of Mathematics, Universidad Del Norte'),
                    html.Li([
                        html.Img(src='https://api.iconify.design/arcticons/huawei-email.svg', style={'width': '20px', 'height': '20px'}),
                        ' gustavovergara238@gmail.com']),
                    html.Li([
                        html.Img(src="https://api.iconify.design/logos/linkedin-icon.svg", style={'width': '5%', 'height': '5%'}),  
                        ' ',                  
                        html.A('Gustavo Vergara', href='https://www.linkedin.com/in/gustavo-antonio-vergara-rolong-22b15a144/', style={'textDecoration': 'none'},target='_blank'),
                    ]),
                    html.Li([
                        html.Img(src='https://api.iconify.design/ant-design/github-filled.svg', style={'width': '5%', 'height': '5%'}),
                        ' ',                      
                        html.A('gvergaraa77', href='https://github.com/gvergaraa77', style={'textDecoration': 'none'},target='_blank'),
                    ]),
                    html.Li([
                        html.Img(src='https://api.iconify.design/academicons/google-scholar.svg', style={'width': '5%', 'height': '5%'}),
                        ' ',
                        html.A('Gustavo Vergara',href='https://scholar.google.es/citations?hl=es&pli=1&user=qumtL4IAAAAJ', style={'textDecoration': 'none'},target='_blank'),
                    ])
                ]),
            ],style=style_div)    
        ]),
        dbc.Col([
            html.Div([

            ], style=style_div),
        ]),
        dbc.Col([
            html.Div([

            ], style=style_div),
        ]),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([

            ], style=style_div),
        ]),
        dbc.Col([
            html.Div([

            ], style=style_div),
        ]),
        dbc.Col([]),
    ]),
])