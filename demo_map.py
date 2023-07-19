from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

mydataset ="https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv"

df = pd.read_csv(dataset, encoding="latin")
df.dropna(inplace=true)
df["Clev"] = abs(df["Clev"])

app = Dash(__name__)
server = app.server

app.layout = html.Div([
  html.Header("Volcane Map Dash App", style={ "fontsize":40,
                                             "textAlign":"center"}),
  dcc.Dropdown(id="mydropdown",
               options=df["Type"].unique(),
               value="Stratovolcano",
               style={"width":"50%", "margin-left":"130px", "margin-top": "60px"}),
  dcc.Graph(id="my_demo_map")
])

@app.callback(Output("my_demo_map", "figure"),
              Input("mydropdown", "value"))
def sync_input(volcano_selection):
  fig = px.scatter_geo(df.loc[df["Type"] == volcano_selection],
                       lat="Latitude",
                       lon="Longitude",
                       size="Clev",
                       hover_name="Volcano Name")
  return fig

if __name__ == "__main__":
  app.run_server(debug=false)
