from dash import Dash, html      #只有import後面的能用
import dash_bootstrap_components as dbc
import pandas as pd


dash2 = Dash(requests_pathname_prefix="/dash/app2/", external_stylesheets=[dbc.themes.BOOTSTRAP])  #建立時一定要加路徑

#property layout
dash2.layout = html.Div(
    [html.H1("Bootstrap Layout"),
     html.P("這是段落1"),
     html.P("這是段落2")],   #要放多個,所以用list代替  #一定要把layout内容對齊
    className="container-lg",
    style={'backgroundColor':'#666'}   #使用駝峰式命名法
    )


#if __name__ == '__main__':
#    dash1.run(debug=True)
