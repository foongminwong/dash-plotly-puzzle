import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback
import dash
from flask import Flask
from dash.dependencies import Input, Output
from src.components import navmenu

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

server = Flask(__name__)
app = Dash(__name__, server=server, use_pages=True, suppress_callback_exceptions=True, title='Dash Plotly Puzzle ', external_stylesheets=[dbc.themes.FLATLY, dbc.icons.BOOTSTRAP])

def serve_app_layout():
    return html.Div([
        navmenu.sidebar(),
        html.P(dash.page_container, style=CONTENT_STYLE)
    ])

app.layout = serve_app_layout

if __name__ == '__main__':
    app.run_server()