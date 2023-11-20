class Person:
    def __init__(self,name:str,weight:int,height:int):
        self.name = name
        self.weight = weight
        self.height = height

    #自訂method
    def bmi(self) -> float: #要有self才會傳送資料過來
        return round(self.weight / (self.height / 100) ** 2,ndigits=2)

    def __str__(self):  #print輸出__str__
        return f"name = {self.name}\nweight = {self.weight}\nheight = {self.height}"
        #一定要return
    

if __name__ == '__main__':  #文件預設屬性__main__
    p1 = Person("robert",78,183)    #實體 p1
    print(p1)   #傳出字串
    print(p1.bmi())
