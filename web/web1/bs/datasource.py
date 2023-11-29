import requests
import psycopg2
from . import password as pw #from 從當前目錄 import package 

__all__=['update_render_data']

#-----------------download data-----------------#
def __download_youbike_data()->list[dict]:
    '''
    下載台北市youbike資料2.0
    https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    response.raise_for_status()
    print('下載成功')
    return response.json()

#---------------create sql table----------------#
def __create_table(conn)->None:
    cursor = conn.cursor()
    cursor.execute(
        '''
		CREATE TABLE IF NOT EXISTS 台北市youbike(
			"id"	SERIAL,
			"站點名稱"	TEXT NOT NULL,
			"行政區"	TEXT NOT NULL,
			"更新時間"	TEXT NOT NULL,
			"地址"	TEXT,
			"總車輛數"	INTEGER,
			"可借"	INTEGER,
			"可還"	INTEGER,
			PRIMARY KEY("id"),
            UNIQUE(站點名稱,更新時間)
		);
		'''
    )
    conn.commit()
    cursor.close()  

#-----------------insert data-------------------#
def __insert_data(conn,values:list[any])->None:
    cursor = conn.cursor()
    sql = '''
        INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (站點名稱,更新時間) DO NOTHING   
    '''
    cursor.execute(sql,values)
    conn.commit()
    cursor.close()

def update_render_data()->None:
    data = __download_youbike_data()

    #---------------連線到postgresql----------------#
    conn = psycopg2.connect(database=pw.DATABASE,
                                user=pw.USER, 
                                password=pw.PASSWORD,
                                host=pw.HOST, 
                                port="5432")
   
    __create_table(conn)
    for item in data:
        if threadRun == True:
            __insert_data(conn,values=[item['sna'],item['sarea'],item['mday'],item['ar'],item['tot'],item['sbi'],item['bemp']])
        else:
            break
    conn.close()

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

