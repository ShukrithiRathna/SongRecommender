import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

from navbar import Navbar
nav = Navbar()

card = [
    dbc.CardBody(
        [   
            html.H5("Music Recommendation System", className="card-title text-center"),
            html.P("This is a mini-application that recommends songs based on your chosen tracks and artists. See where your favourite track stands in Spotify's Global Rankings, view past trends and get predictions for your favourites!" , className="text-center"),
            dbc.Row([
                dbc.Col([dbc.Button("Get Recommendations", color="warning",href="/app")], style={"padding-left":"380px",}) ,
                # dbc.Col([dbc.Button("Get Recommendations", color="warning",href="/app")], style={"padding-left":"250px"}),
                ],)
        ],        
    # style={"width": "22rem", "height":"300px", "justify":"around", 'padding-left':'20px'}, 
    ), 
]

row_1 = dbc.Row(
    [
        # dbc.Col(html.Img(src='assets/img/brand_img.png')),
        dbc.Col(dbc.Card(card), width=12, style={'padding-left':'200px', 'padding-right':'200px','padding-top':'10px'}),
        
        # dbc.Col(dbc.Card(card)),
        # dbc.Col(dbc.Card(card))
          
    ],
    className="mb-4",  style={"padding-top":"50px", 'padding-left':'20px'},
)

def Homepage():
    
    layout = html.Div([
        nav,
        row_1
        
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Homepage()

