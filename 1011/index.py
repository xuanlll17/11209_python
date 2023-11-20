import dataSource   #自訂module

def main():
   names = dataSource.cityNames() #function要括號
   city = dataSource.info(name='屏東縣佳冬鄉')
   #for name in names:
   #print(names)
   print(city)
  

if __name__ == "__main__":
    main()  #呼叫main function