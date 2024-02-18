import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

app = DjangoDash('dashboard')   # replaces dash.Dash

app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-color',
        options=[{'label': x, 'value': x} for x in ['Gold', 'Green', 'Blue']],
        value='Gold'
    ),
    html.Div(id='output-color'),
    dcc.RadioItems(
        id='dropdown-size',
        options=[{'label': i, 'value': i} for i in ['L', 'M', 'S']],
        value='L'
    ),
    html.Div(id='output-size')

])

@app.callback(
    Output('output-color', 'children'),
    [Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value

@app.callback(
    Output('output-size', 'children'),
    [Input('dropdown-size', 'value')])
def callback_size(dropdown_value):
    return "The selected size is %s." % dropdown_value