from dash import Dash, html, dcc
import plotly.express as ps
import csv

plot = Dash(__name__)

with open ('quantium-starter-repo/data/pink_morsel_sales_data.csv', 'r') as csv_read:
	csv_reader = csv.DictReader(csv_read)

	fig = ps.line(csv_reader, x='date', y='sales')

	fig.update_traces(
		line_color = '#bf7b68')

	plot.layout = html.Div(style={'backgroundColor':'#f6ccb3'},children=[
		html.H2(children = 'Change of pink morsel sales with time', style={'textAlign':'center'}),
		dcc.Graph(
			id = 'sales line chart',
			figure = fig)
		])

if __name__ == '__main__':
	plot.run_server(debug=True)
