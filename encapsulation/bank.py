class bank(object):
    def __init__(self,BNAME,name,number,money):
        self.BNAME = BNAME
        self.name = name
        self.number = number
        self.money = money
    def set_BNAME(self,BNAME):
        self.BNAME = BNAME

jun = bank('국민은행', '전병준',100)