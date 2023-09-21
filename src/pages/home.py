import dash
import dash_bootstrap_components as dbc
from dash import dash_table, dcc, html, callback
from dash.dependencies import Output, Input, State

import dash_ag_grid as dag

dash.register_page(
    __name__,
    title='Home',
    name='Home',
    path='/'
)

def serve_layout():
    return html.P("This is the content of the home page!")

layout = serve_layout