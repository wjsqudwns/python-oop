class Grade:
    def __init__(self, kor, math, eng): #생성자 setter 요소들은 0차원 묶은 집합은 1차원
        self.kor = kor  #프로퍼티
        self.math = math
        self.eng = eng

    def sum(self): #getter
        return self.kor + self.math + self.eng

    def avg(self):
        return self.sum() / 3 # 내 클래스 안에 있는 메소드90

    def get_grade(self): # getter
        score = int(self.avg())
            
        if score >= 90:
            grade = 'A학점'   #str 형식의 변수 생성 자동으로 초가화
        elif score >= 80:
            grade = 'B학점'
        elif score >= 70:
            grade = 'C학점'
        elif score >= 60:
            grade = 'D학점'
        elif score >= 50:
            grade = 'E학점'
        else:
            grade = 'F학점'
        return grade #평균을 비교하여 학점을 반환
    @staticmethod
    def main():
        g = Grade(int(input('국어점수 입력: ')), int(input('수학점수 입력: ')), int(input('영어점수 입력: '))) #str형식으로 입력 되기 때문에 int를 사용하여 정수로 변환
        print(f'총점 :{g.sum()}')  # getter
        print(f'평균 :{int(g.avg())}')
        print(f'학점 :{g.get_grade()}')

Grade.main() #클래스 실행

