import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
	html.H1(children='NYC Inmates'),
	dcc.Graph(
		id='Plot',
		figure={
		'data': {
		'x': [18,19,20],'y':[1,2,3],'type':'bar','name':'random stats','layout':{'title': 'Dash Data Visualisation'}
		}

		})
	])

if __name__ == '__main__':
	app.run_server(debug=True)