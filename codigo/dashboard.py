# -*- coding: utf-8 -*-

# Ejecute esta aplicación con 
# python app1.py
# y luego visite el sitio
# http://127.0.0.1:8050/ 
# en su navegador.
from dash import Dash, dcc, html, Input, Output,dash_table         
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import os

cwd = os.getcwd()
# Print the current working directory
print("Current working directory: {0}".format(cwd))


list_of_crimes =[
    "Homicidios",
    "Hurto a celulares",
    "Hurto a personas"
]


df = pd.read_csv('https://raw.githubusercontent.com/SergioSalazarI/DatosThesis/main/Datos/homicidios_unificado.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Crime Analysis Tool"
server = app.server

app.layout = html.Div(children=[
    
                html.Div(children=[
                        dbc.Row(
                            dbc.Col(
                                html.H1('Crime Analysis Tool'),
                                width={'size':6,'offset':5},
                            )
                        ),
                        dbc.Row(children=[
                            dbc.Col(
                                dcc.Dropdown(
                                    id='crime_type',
                                    placeholder='Seleccione el tipo de crimen que desea analizar.',
                                    options=[
                                        {'label':i,'value':i} for i in list_of_crimes
                                    ],
                                ),
                                width={'size':2,'offset':2},
                            )
                        ]
                        )
                    ])
                ]
            )

# app.layout = dash_table.DataTable(
#     df.to_dict('records'),
#     [{"name": i, "id": i} for i in df.columns],
#     fixed_columns={'headers': True, 'data': 1},
#     page_size=20,  # we have less data in this example, so setting to 20
#     style_table={'height': '300px',
#                 'overflowX': 'auto',
#                 'overflowY': 'auto'},
#     style_cell={
#             'padding': '5px',
#             'textAlign': 'left',
#             'height': 'auto',
#             # all three widths are needed
#             #'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
#             'whiteSpace': 'normal'
#         },
#     style_as_list_view=True,
#     style_header={
#         "backgroundColor": "rgb(25, 36, 68)",
#         "fontWeight": "bold",
#         "color": "white",
#     },
#     style_data_conditional=[
#         {
#             'if': {'row_index': 'odd'},
#             'backgroundColor': 'rgb(242, 239, 233)',
#         }
#     ]
# )


if __name__ == '__main__':
    app.run(debug=True)
