class Grade:
    def set_grade(self, kor, math, eng):
        self.kor = kor
        self.math = math
        self.eng = eng

    def sum(self):
        return self.kor + self.math + self.eng

    def avg(self):
        return self.sum() / 3 # 내 클래스 안에 있는 메소드


if __name__ == '__main__':
    g = Grade()
    g.set_grade(95, 75, 85) # 클래스 밖에 있는 메소드
    print(g.sum())
    print(g.avg())
