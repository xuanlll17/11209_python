from dash import Dash, html, dash_table      #只有import後面的能用
import dash_bootstrap_components as dbc
import pandas as pd
from collections import OrderedDict


dash2 = Dash(requests_pathname_prefix="/dash/app2/", external_stylesheets=[dbc.themes.BOOTSTRAP])  #建立時一定要加路徑
dash2.title = "臺北市youbike及時資料"

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

df = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)

#property layout
dash2.layout = html.Div(
    #要放多個,所以用list代替  #一定要把layout内容對齊
    [
        #html.H1("Bootstrap Layout"),
        #html.P("這是段落1"),
        #html.P("這是段落2"),
        #html.A("Icon by doraclub", href="https://www.freepik.com/icon/bicycle_3918391#fromView=search&term=Favicon++bike&page=1&position=8&track=ais&uuid=4cefbc82-a159-4736-a7d2-705faa293b14", target='_blank')
        
        dbc.Container([
            #row
            html.Div([
                html.Div([
                    html.H1("台北市youbike及時資料")
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'}),
            html.Div([
                html.Div([
                dash_table.DataTable(
                    data=df.to_dict('records'), 
                    columns=[{"id": column, "id": column} for column in df.columns],
                    page_size=20
                ),  #先轉list dict 才能輸出
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'}),
        ])
    ],
    className="container-lg",
    #style={'backgroundColor':'#666'}   #使用駝峰式命名法
    )


#if __name__ == '__main__':
#    dash1.run(debug=True)
