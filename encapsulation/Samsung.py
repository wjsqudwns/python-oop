class Samsung(object):
    def __init__(self, product, code, per, pbr,plus):
        self.product = product
        self.code = code
        self.per = per
        self.pbr = pbr
        self.plus = plus
    def set_product(self, product):
        self.product = product

    def set_code(self, code):
        self.code = code

    def get_product(self):
        return self.product

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_plus(self, plus):
        self.plus = plus

    def get_pr(self):
        print(self.product, self.code, self.pbr, self.per, self.plus)

sam = Samsung('삼성전자', "005930", 15.79, 1.33, 2.83) # 00이먼저나오면 숫자기 때문에 표현할수없다
lg = Samsung('lg전자', "009830", 17.79, 1.11, 4.53)
sk = Samsung('sk하이닉스', "001791", 18.19, 2.57,8.83)
sam.get_pr()
sam.set_per(12.75) # set메서드로 값을 수정
sam.get_pr()
lg.get_pr()
sk.get_pr()
