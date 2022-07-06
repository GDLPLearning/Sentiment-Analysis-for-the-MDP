# import libraries
from turtle import st
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


style_div={
    'border':'#5BC0BE 0.03rem solid ',
    'border-radius':'1rem',
    'padding':'10px',
    'height':'400px',
}


layout=html.Div([
    dbc.Col([
        html.Br(),
        html.H1('Contact us'),
    ], style={'textAlign': 'center'}),
    html.Br(),
    html.H2('Contributors', style={'textAlign': 'center'}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H4('Germán Luna', style={'textAlign': 'center'})),
                html.Br(),
                dbc.Row([
                    dbc.Col([]),
                    dbc.Col([
                        html.Div([
                            html.Img(src="assets/profile/gl.png",style={'width': '150px', 'height': '150px','border-radius':'100%'}),    
                        ], style={'textAlign': 'center'}),
                    ]),
                    dbc.Col([]),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([],lg=0.5),
                    dbc.Col([
                        html.Div([
                            html.Ul([
                                html.Li('International Business, Finance and Economics'),
                                html.Li([
                                    html.Img(src='https://api.iconify.design/arcticons/huawei-email.svg', style={'width': '15px', 'height': '15px'}),
                                    ' glunapuche@gmail.com']),
                                html.Li([
                                    html.Img(src="https://api.iconify.design/logos/linkedin-icon.svg", style={'width': '5%', 'height': '5%'}),  
                                    ' ',                  
                                    html.A('German Luna', href='https://www.linkedin.com/in/gerdlp/', style={'textDecoration': 'none'},target='_blank'),
                                ]),
                                html.Li([
                                    html.Img(src='https://api.iconify.design/ant-design/github-filled.svg', style={'width': '5%', 'height': '5%'}),
                                    ' ',                      
                                    html.A('GDLPLearning', href='https://github.com/GDLPLearning', style={'textDecoration': 'none'},target='_blank'),
                                ]),
                            ]),
                        ]),
                    ],lg=11),
                    dbc.Col([],lg=0.5),
                ]),
            ],style=style_div)    
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H4('Gustavo Vergara', style={'textAlign': 'center'})),
                html.Br(),
                dbc.Row([
                    dbc.Col([]),
                    dbc.Col([
                        html.Div([
                            html.Img(src="assets/profile/gv.png",style={'width': '150px', 'height': '150px','border-radius':'100%'}),    
                        ], style={'textAlign': 'center'}),
                    ]),
                    dbc.Col([]),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([],lg=0.5),
                    dbc.Col([
                        html.Div([
                            html.Ul([
                                html.Li('Mathematician'),
                                html.Li([
                                    html.Img(src='https://api.iconify.design/arcticons/huawei-email.svg', style={'width': '15px', 'height': '15px'}),
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
                            ]),
                        ]),
                    ],lg=11),
                    dbc.Col([],lg=0.5),
                ]),
            ], style=style_div),
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H4('Juan Arteaga', style={'textAlign': 'center'})),
                html.Br(),
                dbc.Row([
                    dbc.Col([]),
                    dbc.Col([
                        html.Div([
                            html.Img(src="assets/profile/jf.png",style={'width': '150px', 'height': '150px','border-radius':'100%'}),    
                        ], style={'textAlign': 'center'}),
                    ]),
                    dbc.Col([]),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([],lg=0.5),
                    dbc.Col([
                        html.Div([
                            html.Ul([
                                html.Li('Mechanical Engineer'),
                                html.Li([
                                    html.Img(src='https://api.iconify.design/arcticons/huawei-email.svg', style={'width': '15px', 'height': '15px'}),
                                    ' jf.arteaga@gmail.com']),
                                html.Li([
                                    html.Img(src="https://api.iconify.design/logos/linkedin-icon.svg", style={'width': '5%', 'height': '5%'}),  
                                    ' ',                  
                                    html.A('Juan Felipe Arteaga', href='https://www.linkedin.com/in/felipe-arteaga-r/', style={'textDecoration': 'none'},target='_blank'),
                                ]),
                                html.Li([
                                    html.Img(src='https://api.iconify.design/ant-design/github-filled.svg', style={'width': '5%', 'height': '5%'}),
                                    ' ',                      
                                    html.A('FelipeArteaga', href='https://github.com/FelipeArteaga', style={'textDecoration': 'none'},target='_blank'),
                                ]),
                            ]),
                        ]),
                    ],lg=11),
                    dbc.Col([],lg=0.5),
                ]),
           ], style=style_div),
        ]),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H4('Sergio Sosa', style={'textAlign': 'center'})),
                html.Br(),
                dbc.Row([
                    dbc.Col([]),
                    dbc.Col([
                        html.Div([
                            html.Img(src="assets/profile/ss.png",style={'width': '150px', 'height': '150px','border-radius':'100%'}),
                        ], style={'textAlign': 'center'}),
                    ]),
                    dbc.Col([]),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([],lg=0.5),
                    dbc.Col([
                        html.Div([
                            html.Ul([
                                html.Li('Economist'),
                                html.Li([
                                    html.Img(src='https://api.iconify.design/arcticons/huawei-email.svg', style={'width': '15px', 'height': '15px'}),
                                    ' sergioasb8@gmail.com',]),
                                html.Li([
                                    html.Img(src="https://api.iconify.design/logos/linkedin-icon.svg", style={'width': '5%', 'height': '5%'}),
                                    ' ',
                                    html.A('Sergio Sosa Bautista', href='https://www.linkedin.com/in/sergioasb8/', style={'textDecoration': 'none'},target='_blank'),
                                ]),
                                html.Li([
                                    html.Img(src='https://api.iconify.design/ant-design/github-filled.svg', style={'width': '5%', 'height': '5%'}),
                                    ' ',
                                    html.A('sergioasb8', href='https://github.com/sergioasb8', style={'textDecoration': 'none'},target='_blank'),
                                ]),
                            ]),
                        ]),
                    ],lg=11),
                    dbc.Col([],lg=0.5),
                ]),
            ], style=style_div),
        ]),
        dbc.Col([
            html.Div([
                dbc.CardHeader(html.H4('Wilson Caro', style={'textAlign': 'center'})),
                html.Br(),
                dbc.Row([
                    dbc.Col([]),
                    dbc.Col([
                        html.Div([
                            html.Img(src="assets/profile/wca.png",style={'width': '150px', 'height': '150px','border-radius':'100%'}),    
                        ], style={'textAlign': 'center'}),
                    ]),
                    dbc.Col([]),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([],lg=0.5),
                    dbc.Col([
                        html.Div([
                            html.Ul([
                                html.Li('Civil Engineer'),
                                html.Li([
                                    html.Img(src='https://api.iconify.design/arcticons/huawei-email.svg', style={'width': '15px', 'height': '15px'}),
                                    ' wgcarog@unal.edu.co']),
                                html.Li([
                                    html.Img(src="https://api.iconify.design/logos/linkedin-icon.svg", style={'width': '5%', 'height': '5%'}),  
                                    ' ',                  
                                    html.A('Wilson Caro', href='https://www.linkedin.com/in/wilson-guillermo-caro-gonzalez/', style={'textDecoration': 'none'},target='_blank'),
                                ]),
                                html.Li([
                                    html.Img(src='https://api.iconify.design/ant-design/github-filled.svg', style={'width': '5%', 'height': '5%'}),
                                    ' ',                      
                                    html.A('wilsoncaro07', href='https://github.com/wilsoncaro07', style={'textDecoration': 'none'},target='_blank'),
                                ]),
                            ]),
                        ]),
                    ],lg=11),
                    dbc.Col([],lg=0.5),
                ]),
        ], style=style_div),
        ]),
        dbc.Col([]),
    ]),
])
