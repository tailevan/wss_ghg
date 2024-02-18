import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import plotly.graph_objs as go

# app = DjangoDash('dashboard')  
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css']

app = DjangoDash('dashboard', external_stylesheets=external_stylesheets)

def create_dashboard(years, refrigerants_df, electricities_df):

    dropdown_year = dcc.Dropdown(
        id='dropdown-year',
        options=[{'label': year, 'value': year} for year in years],
        value = years[0]
    )
    
    refrigerant_emission_textbox = dcc.Input(
        id='total-emission',
        type='text',
        disabled=True
    )

    # bar_chart = dcc.Graph(
    #     id='bar-chart',
    #     figure= go.Figure
    # )

    gauge_chart = dcc.Graph(
        id='gauge-chart',
        figure= go.Figure()
    )

    @app.callback(
        Output('gauge-chart', 'figure'),
        [Input('dropdown-year', 'value')]
    )
    def update_gauge_chart(selected_year):
        filtered_df = refrigerants_df[refrigerants_df['inventory_year__year'] == selected_year]
        total_emission = filtered_df['emission'].sum()

        # Create gauge chart figure
        gauge_chart_figure = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=total_emission,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': 'Total Emission (tonne of CO2e)'}
            )
        )

        return gauge_chart_figure

    @app.callback(
        Output('total-emission', 'value'),
        [Input('dropdown-year', 'value')]
    )
    def update_total_emission(selected_year):
        print(f"Selected year: {selected_year}")
        filtered_df = refrigerants_df[refrigerants_df['inventory_year__year'] == selected_year]
        total_emission = filtered_df['emission'].sum()
        return str(total_emission)

    app.layout = html.Div([
        html.Div([
            html.Label('Select Year'),
            dropdown_year
        ]),
        gauge_chart,
    ], style={'height': '100vh'})    
    return app
