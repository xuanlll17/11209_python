from dash import Dash, html      #只有import後面的能用
import dash_bootstrap_components as dbc
import pandas as pd


dash2 = Dash(requests_pathname_prefix="/dash/app2/", external_stylesheets=[dbc.themes.BOOTSTRAP])  #建立時一定要加路徑

#property layout
dash2.layout = html.Div(children=[  #children可打可不打
    html.H1("Dash H1"),
    html.P("段落1"),
    html.P("段落2"),

])


#if __name__ == '__main__':
#    dash1.run(debug=True)
