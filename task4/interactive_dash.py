import csv
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output 

app = Dash(__name__)

file_path = 'E:/forage/quantium_se/quantium-starter-repo/data/pink_morsel_sales_data.csv'

df = pd.read_csv(file_path)

app.layout = html.Div([
	html.H2(['Change of sale with time'], style = {'textAlign' : 'center', 'color':'#527b7c'}),
    html.Div([
        dcc.RadioItems(
            [{ "label" : html.Div(['All'], style = {'color': '#94acbc', 'display' :'inline-block', 'margin-left':'20px', 'margin-right':'90px'}),
            "value" : "all"},
            { "label" : html.Div(['North'], style = { 'color' : '#527b7c', 'display' :'inline-block', 'margin-left':'20px', 'margin-right':'90px'}),
            "value" : "north"},
            {"label" : html.Div(['South'], style = {'color' : '#cbacd9', 'display' :'inline-block', 'margin-left':'20px', 'margin-right':'90px'}),
            "value" : "south"},
            {"label" : html.Div(['East'], style = {'color' : '#8a7bab', 'display' :'inline-block', 'margin-left':'20px', 'margin-right':'90px'}),
            "value" : "east"},
            {"label" : html.Div(['West'], style = {'color' : '#3ea4af', 'display' :'inline-block', 'margin-left':'20px', 'margin-right':'90px'}),
            "value" : "west"}
            ], value = 'all',
            inline = True,
            id = 'radio_buttons'
        	)
    	]),
    dcc.Graph(id = 'graph')
	])

@app.callback(
    Output('graph', 'figure'),
    Input('radio_buttons', 'value'))

def update_graph(selected_region):
    if selected_region == "all":
        fig = px.line(df, x='date', y='sales')
    else:

        dff = df[df.region == str(selected_region)]

        fig = px.line(dff, x='date', y='sales')

    fig.update_traces(
    line_color = '#527b7c')

    fig.update_layout(
        font_color = '#527b7c',
        plot_bgcolor = '#d1ddd6')

    return fig



if __name__ == '__main__':
    app.run_server(debug = True)