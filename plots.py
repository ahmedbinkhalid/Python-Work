
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Load the dataset
file_path = r'E:\data.csv\data.csv'  # Update with your file path
df = pd.read_csv(file_path, encoding='latin1', low_memory=False)  # Specify encoding

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create Dash app with Bootstrap CSS
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Custom CSS styling for background
app.css.append_css({
    'external_url': 'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css'
})

# Define layout
app.layout = html.Div(style={'background': 'linear-gradient(to right, black, #17202A)', 'height': '100vh'}, children=[
    dbc.Container([
        dbc.Navbar(
            [
                html.H1("Sales Dashboard", className="navbar-brand")
            ],
            color="dark",
            dark=True,
        ),
        html.Div(className="container-fluid", children=[
            dbc.Row(className="row", children=[
                dbc.Col(className="col-md-6", children=[
                    dcc.Graph(
                        id='traffic-over-time',
                        figure=px.line(df['InvoiceDate'].value_counts().sort_index(), title='Website Traffic Over Time')
                    )
                ]),
                dbc.Col(className="col-md-6", children=[
                    dcc.Graph(
                        id='traffic-sources',
                        figure=px.bar(df['Country'].value_counts(), title='Top Traffic Sources', labels={'value': 'Number of Sessions', 'index': 'Traffic Source'})
                    )
                ]),
            ]),
            dbc.Row(className="row", children=[
                dbc.Col(className="col-md-6", children=[
                    dcc.Graph(
                        id='device-distribution',
                        figure=px.histogram(df, x='Quantity', title='Device Category Distribution', labels={'Quantity': 'Device Category', 'count': 'Number of Sessions'})
                    )
                ]),
                dbc.Col(className="col-md-6", children=[
                    dcc.Graph(
                        id='user-type-distribution',
                        figure=px.histogram(df, x='CustomerID', title='User Type Distribution', labels={'CustomerID': 'User Type', 'count': 'Number of Sessions'})
                    )
                ]),
            ]),
            dbc.Row(className="row", children=[
                dbc.Col(className="col-md-12", children=[
                    dcc.Graph(
                        id='session-quality-distribution',
                        figure=px.histogram(df, x='UnitPrice', title='Session Quality Distribution', labels={'UnitPrice': 'Session Quality', 'count': 'Frequency'})
                    )
                ]),
            ]),
        ]),
    ], fluid=True)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
