import dash
from dash import Dash, html,dcc
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def test_001_header(dash_duo):
	app = dash.Dash(__name__)
	app.layout = html.Div(id = 'header2', children = 0)

	dash_duo.start_server(app)

	assert dash_duo.find_element("#header2").text == '0'


def test_002_button(dash_duo):
	app = dash.Dash(__name__)
	app.layout = html.Div([
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
    	])
	dash_duo.start_server(app)
	dash_duo.wait_for_element('#radio_buttons', timeout = 10) 

def test_003_graph(dash_duo):
	app = dash.Dash(__name__)
	app.layout = html.Div([dcc.Graph(id = 'graph')])

	dash_duo.start_server(app)

	dash_duo.wait_for_element('#graph', timeout = 10)




