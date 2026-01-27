import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load clean processed data
df = pd.read_csv("output/pink_morsel_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create Dash app
app = dash.Dash(__name__)

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    labels={
        "date": "Date",
        "sales": "Total Sales",
        "region": "Region",
    },
    title="Pink Morsel Sales Before and After Price Increase",
)

# Add vertical line (SAFE method)
price_date = pd.to_datetime("2021-01-15")

fig.add_shape(
    type="line",
    x0=price_date,
    x1=price_date,
    y0=0,
    y1=1,
    xref="x",
    yref="paper",
    line=dict(color="red", dash="dash", width=2),
)

fig.add_annotation(
    x=price_date,
    y=1,
    xref="x",
    yref="paper",
    text="Price Increase (15 Jan 2021)",
    showarrow=False,
    xanchor="left",
    yanchor="bottom",
    font=dict(color="red"),
)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig),
])

if __name__ == "__main__":
    app.run(debug=True)
