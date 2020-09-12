#importing libraries

import pandas as pd
import numpy as np
import os


import plotly.express as px
import plotly.graph_objects as go
# import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import dash_bootstrap_components as dbc


# from app import app
from navbar import Navbar


# app = dash.Dash(__name__)


# server=app.server
df=pd.read_csv('new_data/merged_global_ranks.csv')
ranks_df=df.drop(['Region','Cluster','Unnamed: 0'], axis=1)
ranks_df.drop(ranks_df[ranks_df['Rank']>50]. index,axis=0, inplace=True)
def get_reco(row,col):
    # if col <2:
        # print(df.iat[row,2])
    song_cluster=df.iat[row,5]
    song_rank=df.iat[row,3]
    reco_song_1=df[df['Cluster']==song_cluster]['Track_Name']
    reco_song_1.drop(song_rank-1, inplace=True)
    # print(type(reco_song_df))
        # reco_song_df.drop(song_rank-1, inplace=True)
        # reco_song_df.drop('index', axis=1, inplace=True)
    # else:
    song_artist=df.iat[row,4]
    print(song_artist)
    song_rank=df.iat[row,3]
    reco_song_df=df[df['Artist']==song_artist]['Track_Name']
    reco_song_df.drop(song_rank-1, inplace=True)
    #    print(type(reco_song_df))
    return (reco_song_1.head(),reco_song_df.head())




nav = Navbar()


title=dbc.Container([
    # dbc.Row
    # ([
    #     dbc.Col(html.H3(children='Music Recommendations - Global'), className="mb-4 text-center"),
    # ],
    #     style={'padding-top':'30px'}
    # ),
    dbc.Row
    ([
        dbc.Col(html.H5(children='Top Ranked Songs - Global'), className="mb-4 text-center"),
        dbc.Col(html.H5(children='Recommendations'), className="mb-4 text-center")
    ],
    style={'padding-top':'30px'}
    ),
])

card_song_info = dbc.Card(
    dbc.CardBody(
        [   
            html.H4("Song Info", className="card-title text-center"),
            dbc.Row
            ([
                dbc.Col(html.H6(children='Track Name:'), className="mb-4", style = {'padding-top':"10px"}),
                dbc.Col(html.H6(id='track_name',className="mb-4", style = {'padding-top':"10px"})),
            # ]),
            # dbc.Row
            # ([
                dbc.Col(html.H6(children='Artist:'), className="mb-4",  style = {'padding-top':"10px"}),
                dbc.Col(html.H6(id='artist',className="mb-4",  style = {'padding-top':"10px"}))
            ]),
        ],
        
    ),
    style={"height":"200px"}
)   

# card_reco = dbc.CardDeck([
songs=   dbc.Card(
        dbc.CardBody(
        [
            # dbc.CardHeader("Similar Songs", className= "text-center",),
            html.H4("Similar Songs", className="card-title text-center"),
            dbc.Row
            ([
                dbc.Col(html.Div(id='similar_songs',className="mb-4 text-center",style = {'padding-top':"10px"}))
            ]),
        ],
        style={"height":"220px", }, ),
    )
artist =   dbc.Card(
        dbc.CardBody(
        [
            # dbc.CardHeader("By The Same Artist", className= "text-center"),
            html.H4("Same Artist", className="card-title text-center"),
            dbc.Row
            ([
                dbc.Col(html.Div(id='same_artist',className="mb-4 text-center",style = {'padding-top':"10px"})),
                
            ],  justify="around"),
        ],
         style={"height":"220px"}),
    # style={"width": "180px", "height":"180px", "justify":"around"}, color="Warning", outline=True
    )  
# ]) 

   
body=dbc.Container([
    dbc.Row
    ([
        dbc.Col
        (
        
            dash_table.DataTable
            (
                id='table',
                columns=[{"name": i, "id": i} for i in ranks_df.columns],
                data=ranks_df.to_dict('records'),style_cell=
                {
                    'height': 'auto',
                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                    'whiteSpace': 'normal'
                },
                style_data=
                {
                    'width': '100px',
                    'maxWidth': '100px',
                    'minWidth': '100px',
                    'border': '1px solid black'
                },
                style_cell_conditional=
                [
                         {'if': {'column_id': 'Artist'},
                          'textAlign': 'left'},
                        #  'width': '45%'},
                         {'if': {'column_id': 'Track_Name'},
                         'textAlign': 'left'}
                        #  'width': '45%'}
                ],
                page_action='none',
                style_table={'height': '360px', 'overflowY': 'auto'},
                style_header={ 'border': '1px solid black' },
            ),

        className = "table-bordered "
        ),
        dbc.Col
        ([
            html.Div(html.H6(children='Click on your favourtie track or artist from the table on the left, and we\'ll give you a recommendation!'), className="mb-4", style = {'padding-left':'40px'}),
            dbc.Row([dbc.Col(songs, width=6), dbc.Col(artist, width=6)],style = {'padding-bottom':'15px'}),
            # dbc.Row([
                # dbc.Col(card_reco, align="center",style = {'padding-bottom':'15px','padding-left':'100px'}),
            # ]),
            dbc.Row([dbc.Col(card_song_info, width=12)],style = {'padding-bottom':'15px', 'padding-left':'50px', })
            # html.Div(card_song_info,widthstyle = {'padding-left':'100px'})
            
                       
        ], 
        style= {"margin-left":"20px", "margin-right":"20px"})
        ],
    style= {"margin-bottom":"30px"})
])    

def App():
    layout = html.Div([
        nav,
        title,
        body

    ])
    
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = App()

