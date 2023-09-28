class Person:
    def __init__(self,name:str,weight:int,height:int):
        self.__name = name
        self.weight = weight
        self.height = height

    #property 使用者只能讀不能改
    @property
    def name(self) -> str:
        return self.__name

    #自訂method
    def bmi(self) -> float: #要有self才會傳送資料過來
        return round(self.weight / (self.height / 100) ** 2,ndigits=2)

    def __str__(self):  #print輸出__str__
        return f"name = {self.__name}\nweight = {self.weight}\nheight = {self.height}"
        #一定要return
    

if __name__ == '__main__':  #文件預設屬性__main__
    p1 = Person("robert",78,183)    #實體 p1
    #p1.name = "vivian" #動態 #沒有就會自己建立一個
    print(p1.name)   #property呼叫不需要()
    print(p1.bmi())  #method呼叫需要()
