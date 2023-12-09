import requests
import psycopg2
from . import password as pw #from 從當前目錄 import package 



def lastest_datetime_data()->list[tuple]:
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER, 
                            password=pw.PASSWORD,
                            host=pw.HOST, 
                            port="5432")
    cursor = conn.cursor()              
    sql = '''
        select a.站點名稱, a.更新時間, a.行政區, a.地址, a.總車輛數, a.可借, a.可還  
        from 台北市youbike a join (select distinct 站點名稱,max(更新時間) 更新時間
        from 台北市youbike group by 站點名稱) b
        on a.更新時間=b.更新時間 and a.站點名稱=b.站點名稱
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows

def search_sitename(word:str) -> list[tuple]:
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER, 
                            password=pw.PASSWORD,
                            host=pw.HOST, 
                            port="5432")
    cursor = conn.cursor()
    sql = '''
        SELECT 站點名稱, MAX(更新時間) AS 更新時間,行政區,地址,總車輛數,可借,可還
        FROM 台北市youbike
        GROUP BY 站點名稱,行政區,地址,總車輛數,可借,可還
        HAVING 站點名稱 like %s
        '''
    cursor.execute(sql,[f'%{word}%'])
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

