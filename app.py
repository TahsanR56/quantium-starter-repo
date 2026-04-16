import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the output data
df = pd.read_csv("data/output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)

app.layout = html.Div(style={"backgroundColor": "#f8f9fa", "padding": "40px", "fontFamily": "Segoe UI, sans-serif"}, children=[
    
    html.Div(style={"maxWidth": "1000px", "margin": "0 auto"}, children=[
        
        html.H1("Pink Morsel Sales", 
                style={"textAlign": "left", "color": "#2d3436", "fontWeight": "300", "letterSpacing": "1px"}),

        html.Div([
            html.Label("Region Selection", style={"display": "block", "marginBottom": "10px", "color": "#636e72"}),
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
                inline=True,
                labelStyle={"marginRight": "25px", "color": "#0984e3", "fontWeight": "500"}
            )
        ], style={"padding": "20px 0", "borderBottom": "1px solid #dfe6e9"}),

        html.Div([
            dcc.Graph(id="sales-chart")
        ], style={"marginTop": "30px", "borderRadius": "15px", "overflow": "hidden", "boxShadow": "0 10px 30px rgba(0,0,0,0.05)"})
    ])
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
        template="plotly_white"
    )

    # Styling the graph to match the minimalist blue theme
    fig.update_traces(line_color="#0984e3", line_width=3)
    fig.update_layout(
        margin=dict(l=40, r=40, t=40, b=40),
        font=dict(family="Segoe UI, sans-serif", size=12, color="#636e72"),
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="#f1f2f6")
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)
