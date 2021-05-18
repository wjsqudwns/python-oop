class Grade:
    def __init__(self, kor, math, eng): # 매게변수(파라미터), setter
        self.kor = kor #self.kor<-프로퍼티 = kor <- 매게변수 #
        self.math = math #self 나를 지칭하는 키워드(예약어),프로퍼티로 정의햊주는 것
        self.eng = eng #프로퍼티에 setter로 받은 값을 넣는다


    def sum(self): # getter는 파라미터가 없다.(입력을 받지 않는다.)
        return self.kor + self.math + self.eng # getter

    def avg(self):
        return self.sum() / 3 # 내 클래스 안에 있는 메소드


if __name__ == '__main__':
    g = Grade(70,60,80) # value,setter

    print(g.sum()) # getter
    print(g.avg())
