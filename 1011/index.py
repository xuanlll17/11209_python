import dataSource   #自訂module

def main():
    try:
        data_list = dataSource.download()
    except Exception as e:   #如果傳出Exception會輸出    #except就所有錯誤
        print(f"錯誤:{e}")
    else:
        for row in data_list:   #row 變量名
            print(row)
if __name__ == "__main__":
    main()  #呼叫main function