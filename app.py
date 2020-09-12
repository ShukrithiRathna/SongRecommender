import pandas as pd
import numpy as np


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from recommender import App
# from peaks import Peak
from homepage import Homepage

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])


app.title="Music Recommnedations"
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])


@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/app':
        return App()
    # if pathname == '/peaks':
    #     return Peak() 
    else:
        return Homepage()



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


@app.callback ([
    Output(component_id='track_name', component_property='children'),
    Output(component_id='artist', component_property='children'),
    Output(component_id='similar_songs', component_property='children'),
    Output(component_id='same_artist', component_property='children')],
    [Input('table', 'active_cell')]
)

def multi_output(active_cell):
    if active_cell:
        song_reco,artist_reco=get_reco(active_cell['row'], active_cell['column'])
        return (df.iloc[active_cell['row'],[2]],df.iloc[active_cell['row'],[4]],', '.join(song_reco),', '.join(artist_reco))
    else:
        return ('No selection','No selection','Make a selection, to get a recommendation here','Make a selection, to get a recommendation here')


if __name__ == '__main__':
    app.run_server(debug=True)