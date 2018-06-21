#importing packages
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

#layout part where we define the html components
app.layout = html.Div(children=[
    html.H1(children='Dash101'),
     dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 5, 7, 3, 8], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [1, 9, 6, 2, 4], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Dash Sample'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)

