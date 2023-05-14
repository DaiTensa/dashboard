from dash import Dash, html, dcc, callback, Output, Input, State
import requests
import time as t


url_server = 'http://localhost:5000'

app_dash = Dash(__name__)

app_dash.layout = html.Div([
    html.H1('Dashboard Client'),
    dcc.Input(
        id='id_client',
        type='text',
        value=''
    ),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='output-data'),
])

@app_dash.callback(
    Output(component_id='output-data', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks')],
    [State(component_id='id_client', component_property='value')]
)
def get_data_client(n_clicks, id_client):
    if n_clicks:
        time_0 = t.time()
        # response_data_client = requests.get(f'{url_server}/data/{id_client}')
        response_pred_client = requests.get(f'{url_server}/prediction/{id_client}')
        # data_client = json.loads(response_data_client.text)
        # df = pd.DataFrame(data_client[0])
        time_1 = t.time() - time_0
        return (
            response_pred_client.text, 
            time_1
            # response_data_client.text,
            # print(response_pred_client.text),
            # print(type(data_client[0])),
            # print(data_client[0].keys()),
            # print(data_client[0].items()) 
            # print(type(df))
        )



   
if __name__ == '__main__':
    app_dash.run_server(debug=True)