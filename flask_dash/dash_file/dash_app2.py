from dash import Dash, html, dash_table      #只有import後面的能用
import dash_bootstrap_components as dbc
import pandas as pd
from . import datasource  #在.py一定要用from . 根目錄 import


dash2 = Dash(requests_pathname_prefix="/dash/app2/", external_stylesheets=[dbc.themes.BOOTSTRAP])  #建立時一定要加路徑
dash2.title = "臺北市youbike及時資料"
lastest_data = datasource.lastest_datetime_data()
lastest_df = pd.DataFrame(lastest_data, columns=['站點名稱','更新時間','行政區','地址','總數','可借', '可還'])
lastest_df1 = lastest_df.reset_index()
lastest_df1['站點名稱'] = lastest_df1['站點名稱'].map(lambda name:name[11:])

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
                    data=lastest_df1.to_dict('records'), 
                    columns=[{"id": column, "name": column} for column in lastest_df1.columns],
                    page_size=20,
                    fixed_rows={'headers': True},
                    style_table={'height': '300px', 'overflowY': 'auto'}
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
