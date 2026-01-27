import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load data
df = pd.read_csv("output/sales_1.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Filter only Pink Morsel
df = df[df['product'] == 'Pink Morsel']

# Create sales column
df['sales'] = df['quantity'] * df['price']

# Group by date (important!)
df = df.groupby('date', as_index=False)['sales'].sum()

# Sort by date
df = df.sort_values('date')

# Create Dash app
app = Dash(__name__)

fig = px.line(
    df,
    x='date',
    y='sales',
    title='Pink Morsel Sales Over Time',
    labels={
        'date': 'Date',
        'sales': 'Total Sales ($)'
    }
)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)

