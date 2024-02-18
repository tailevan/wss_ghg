import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

# app = DjangoDash('dashboard')  
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css']

app = DjangoDash('dashboard', external_stylesheets=external_stylesheets)

def create_dashboard(years, refrigerants_df):
    dropdown_year = dcc.Dropdown(
        id='dropdown-year',
        options=[{'label': year, 'value': year} for year in years],
        value=years[0]
    )

    app.layout = html.Div([
        html.Div([
            html.P('Select year:'),
        ], className='col-1'),

        html.Div([
            dropdown_year,
        ], className='col-1'),

        html.Div([
            html.P('Total Emission:'),
        ], className='col-1'),

        html.Div([
            html.P(id='total-emission'),    
        ], className='col-1'),
    ], className='row')

    @app.callback(
        Output('total-emission', 'children'),
        [Input('dropdown-year', 'value')]
    )
    def calculate_total_emission(year):
        # Calculate the total emission for the given year from the refrigerants_df
        total_emission = refrigerants_df.groupby('inventory_year')['emission'].sum().loc[year]
        return total_emission

    return app
