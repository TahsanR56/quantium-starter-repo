import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the output data
df = pd.read_csv("data/output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),

    html.Div([
        html.Label("Filter by Region:"),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True
        )
    ]),

    dcc.Graph(id="sales-chart"),
])

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    if region == "all":
        filtered = df.groupby("date", as_index=False)["sales"].sum()
    else:
        filtered = df[df["region"] == region].groupby("date", as_index=False)["sales"].sum()

    fig = px.line(
        filtered, 
        x="date", 
        y="sales",
        title=f"Sales — {region.capitalize()}"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)
