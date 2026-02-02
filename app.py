import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Create Dash app
app = dash.Dash(__name__)

# Load data
df = pd.read_csv("output/pink_morsel_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

price_date = pd.to_datetime("2021-01-15")

# Layout
app.layout = html.Div(
    style={"padding": "20px", "backgroundColor": "#f2f2f2"},
    children=[
        html.H2("Pink Morsels Sales", style={"color": "purple"}),

        dcc.RadioItems(
            id="region-radio",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True
        ),

        dcc.Graph(id="line-chart")
    ]
)

# Callback
@app.callback(
    Output("line-chart", "figure"),
    Input("region-radio", "value")
)
def update_chart(region):
    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == region]

    fig = px.line(
        filtered_df,
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

    # Add vertical price increase line
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

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)
