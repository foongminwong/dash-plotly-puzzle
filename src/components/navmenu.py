import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc, html, callback
from flask import session

from src.pages import HOME_URL, TABLE_URL, DROPDOWN_URL
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

def sidebar():
    return html.Div([
        html.I(className="bi bi bi-puzzle display-4"),
        html.Hr(),
        html.P(
            "Dash Plotly Puzzle", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href=HOME_URL, active="exact"),
                dbc.NavLink("Table", href=TABLE_URL, active="exact"),
                dbc.NavLink("Dropdown", href=DROPDOWN_URL, active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
