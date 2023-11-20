class Person:
    def __init__(self,n:str,w:int,h:int): #建立一個person的實體
        self.__name = n  #self.__name (private attribute) = n (參數)
        self.weight = w
        self.height = h

    #property 使用者只能讀不能改(readonly)
    @property
    def name(self) -> str:  # def name(property) 和前面參數name 無關
        return self.__name  # 看誰執行.name //這裡是p1 #self是實體本身，對於實體P1來說，就是P1；對於實體P2來說，就是P2

    @property
    def getBMI(self) -> float:
        return self.bmi() #self 實體 -> p1  #bmi執行實體method

    #自訂method
    def bmi(self) -> float: #要有self才會傳送資料過來 #實體method
        return round(self.weight / (self.height / 100) ** 2,ndigits=2)

    def __str__(self) -> str:  #print輸出__str__
        return f"name = {self.__name}\nweight = {self.weight}\nheight = {self.height}"
        #一定要return
    

if __name__ == '__main__':  #文件預設屬性__main__
    p1 = Person("robert",78,183)    #引數值傳給def init裡的name #p1管理person
    #p2 = Person("robe",78,188)
    #p1.name = "vivian" #動態 #沒有就會自己建立一個
    print(p1.name)   #property呼叫不需要()
    #print(p1.bmi())  #method呼叫需要()
    print(p1.getBMI)
