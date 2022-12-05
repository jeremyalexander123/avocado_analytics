#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:42:43 2022

@author: jeremyalexander
"""

#import pandas as pd

#url_data = (r'https://raw.githubusercontent.com/realpython/materials/master/python-dash/additional_files/avocado.csv')

#data_csv = pd.read_csv(url_data, index_col = 0)

#data_csv.to_csv('/Users/jeremyalexander/avocado_analytics/avocado.csv', index = False)

#print(data_csv)

from dash import Dash
from dash import dcc
from dash import html
import pandas as pd

data = pd.read_csv('avocado.csv')
data = data.query("type == 'conventional' and region == 'Albany'")
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
data.sort_values('Date', inplace = True)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children='Avocado Analytics',),
        html.P(
            children='Analyse the behaviour of avocado prices'
            ' and the number of avos sold in the us'
            ' between x and y',
        ),
        dcc.Graph(
            figure = {
                'data': [
                    {
                        'x': data['Date'],
                        'y': data['AveragePrice'],
                        'type': 'lines',
                        },
                    ],
                    'layout': {'title': 'Avg Price'},
                },
            ),
            dcc.Graph(
                figure = {
                    'data': [
                        {
                            'x': data['Date'],
                            'y': data['Total Volume'],
                            'type': 'lines',
                            },
                        ],
                        'layout': {'title': 'Avos Sold'},
                   },
                ),                  
            ]
    )
                    
                    
if __name__ == "__main__":
    app.run_server(debug=True)
    
    
