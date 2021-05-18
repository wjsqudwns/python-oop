class bank(object):
    def __init__(self,bname,name,number,money):
        self.bname = bname
        self.name = name
        self.number = number
        self.money = money
    def set_bname(self,bname):
        self.bname = bname

jun = bank('국민은행', '전병준',100)