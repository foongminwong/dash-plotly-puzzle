import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

dash.register_page(
    __name__,
    title='Dropdown',
    name='Dropdown'
)

layout = html.Div([
        html.P("This is the content of the dropdown page!")
])