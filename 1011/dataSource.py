import requests
import csv
import io

__cities = []   #變數

def __download() -> list[list]:
    url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CA18EE06-4A50-4861-9D97-7853353D7108'
    response = requests.request('GET',url)
    try:
        response.raise_for_status()
    except:
        raise Exception("連線發生錯誤","網路中斷") #raise 就會停下,不會繼續
        #return None #不需要return
        
    else:
        if not response.ok:
            raise Exception("下載失敗","伺服器錯誤訊息!")
        else:
            file = io.StringIO(response.text)
            csv_reader = csv.reader(file)
            next(csv_reader)    #跳讀下一行 #第一行不要
            return list(csv_reader)   #取得內容
        
def cities_info() -> list:
    if len(__cities) == 0:   #查list長度    #檢查list是否是空字串
        try:
            data_list = __download()
        except Exception as e:   #如果傳出Exception會輸出    #except就所有錯誤
            print(f"錯誤:{e}")
        else:
            for row in data_list:   #row 變量名
                if row[0] == '111':
                    __cities.append(row)    #資料加進去
    return __cities   #如果出錯會傳出空list

def cityNames() -> list[str]:
    cities = cities_info()
    names = []
    for row in cities:  #一個一個抓出來放入list
        cityName = row[1]
        names.append(cityName)  
    return names

def info(name:str) -> list[str]:
    cities = cities_info()
    #print(type(cities))
    for city in cities:
        #print(city1[1])
        if city[1] == name: #比對是否相同(index.py裡的name)
            return city

    return []   #for in 跑完沒找到相同的就會輸出空[]
   
    