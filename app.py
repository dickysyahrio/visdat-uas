from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

dataset = pd.read_csv('gabungan3.csv')

app = Dash()

wilayah_dropdown = dcc.Dropdown(options=dataset['Wilayah'].unique(),
                            value='Bidang Dalops')

app.layout = html.Div(children=[
    html.H1(children='Dashboard Penindakan Tilang DKI Jakarta', style = {'textAlign':'center',}),
    wilayah_dropdown,
    dcc.Graph(id='tilang'),
    html.H5('Created by Dicky Syahrio - 1900018186',style = {'textAlign':'center','color':'blue',}),
])

@app.callback(
    Output(component_id='tilang', component_property='figure'),
    Input(component_id=wilayah_dropdown, component_property='value')
)
def update_graph(wilayah_terpilih):
    filtered_wilayah = dataset[dataset['Wilayah'] == wilayah_terpilih]
    fig_bar = px.bar(filtered_wilayah,
                       x='Bulan',y='bap_tilang',barmode='group',
                       title=f'Grafik Penindakan Tilang di Daerah {wilayah_terpilih}')
    return fig_bar

if __name__ == '__main__':
    app.run_server(debug=True)
