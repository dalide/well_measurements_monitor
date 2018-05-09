import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly as py
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.title = 'Well Measurements Monitoring'
app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})  # noqa: E501
server = app.server

raw_data = pd.read_csv('sample_data.csv', nrows = 40000)

raw_data['TimeStamp'] = pd.to_datetime(raw_data['TimeStamp'])
# raw_data = raw_data.set_index('TimeStamp')
columns = raw_data.columns.tolist()
columns.remove('TimeStamp')

colors = [
	'rgb(31, 119, 180)',
	'rgb(255, 127, 14)',
	'rgb(44, 160, 44)',
	'rgb(214, 39, 40)',
	'rgb(148, 103, 189)',
	'rgb(140, 86, 75)',
	'rgb(0,0,0)'
]

layout = dict(
    autosize=True,
    height=500,
    font=dict(color='#CCCCCC'),
    titlefont=dict(color='#CCCCCC', size='14'),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor="#191A1A",
    paper_bgcolor="#020202",
    legend=dict(font=dict(size=10), orientation='h'),
)

app.layout = html.Div([
	# title row
	html.Div([
		html.H1(
			'Well Measurements - Dashboard',
			className='eight columns'
			),
		html.Img(
			src = "http://www.afr.com/content/dam/images/g/m/a/f/r/e/image.related.afrArticleLead.620x350.gqq0nn.png/1470889541633.jpg",
			className = 'one columns',
			style = {
				'height':'100',
				'width': '225',
				'float':'right',
				'position':'relative'
			},
			),
		],
		className='row'),
	html.Div(
            [
                html.H5(
                    'A simple dashboard to monitor well center measurments',
                    className='eight columns'
                ),

            ],
            className='row'
        ),
	# status row
	html.Div([
		html.Div([
			html.H2('Pressure Status')
			],
			style = {'background-color': 'green', 'text-align':'center'},
			className = 'four columns'),
		html.Div([
			html.H2('Temperature Status')
			],
			style = {'background-color': 'green', 'text-align':'center'},
			className = 'four columns'),
		html.Div([
			html.H2('FlowRate Status')
			],
			style = {'background-color': 'green', 'text-align':'center'},
			className = 'four columns'),
		],
		style = {
			'margin-top': '20',
			'margin-bottom': '20'
			},
		className='row'),

	# selection and plot
	html.Div([
		html.Div(
			[
			dcc.Checklist(
				id = 'measurements',
				options = [
					{'label': item, 'value': item} for item in columns
				],
				values=columns
				)
			],
			style = {'background-color': 'cyan', 'margin-top': '20', 'line-height': '50'},
			className='three columns'
			),
		html.Div([
			dcc.Graph(
				id='well-plot',
			),
			dcc.Interval(
				id='interval-component',
				interval = 1*200,
				n_intervals = 0
				)
			],
			style = {'margin-top': '20'},
			className = 'nine columns')
		],
		className='row')
	],
	className = 'ten columns offset-by-one')

@app.callback(
	Output('well-plot','figure'),
	[Input('measurements', 'values'),
	Input('interval-component', 'n_intervals')])
def update_graph(values, n):
	fig = py.tools.make_subplots(rows = 3, cols = 1, vertical_spacing=0.2)
	fig['layout']['margin']={
		'l': 80,
		'r': 10,
		'b': 50,
		't': 10
	}

	data = raw_data[10000+n:12000+n]

	fig['layout'].update(showlegend=False)

	fig.append_trace({
			'x': [],
			'y' : [],
			'name': 'Pressure',
			'mode': 'lines',
			'type': 'scatter',
			'marker': {'color':'red'},
			}, 1,1)

	fig.append_trace({
			'x': [],
			'y' : [],
			'name': 'Temperature',
			'mode': 'lines',
			'type': 'scatter',
			'marker': {'color':'red'}
			}, 2,1)

	fig.append_trace({
			'x': [],
			'y' : [],
			'name': 'FlowRate',
			'mode': 'lines',
			'type': 'scatter',
			'marker': {'color':'red'}
			}, 3,1)

	for i, v in enumerate(values):
		if 'Pressure' in v:
			ax = 1
		elif 'Temperature' in v:
			ax = 2
		else:
			ax = 3
		fig.append_trace({
			'x': data['TimeStamp'],
			'y' : data[v],
			'name': v,
			'mode': 'lines',
			'type': 'scatter',
			'marker': {'color': colors[columns.index(v)]}
			}, ax ,1)



	return fig

if __name__ == '__main__':
        app.run_server(debug=False)