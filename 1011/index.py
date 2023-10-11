import dataSource   #自訂module

def main():
   cities = dataSource.cities_info() #function要括號
   for city in cities: #輸出會一行一行輸
    print(city) #不用for in -> 會輸出二維list

if __name__ == "__main__":
    main()  #呼叫main function