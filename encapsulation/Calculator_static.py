class CalculatorStatic(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return  self.first + self.second
    def sub(self):
        return  self.first - self.second
    def mul(self):
        return  self.first * self.second
    def div(self): # dynamic 동적 메소드
        return  self.first / self.second

    @staticmethod # @ 어노테이션 기능을 부여하는것 정적메소드 self 없다.
                # 클래스 내부에서 인스턴트를 만들수 있다
                #외부작업을 그대로 넣을수 있다 그리고 그걸 다른곳에 가져다 쓸 때 간편해진다.

    def main(): # 실행하는 코드를 클래스 내부에 둘수있는것
        cal = CalculatorStatic(int(input('첫번쨰 수 입력')), int(input('두번째 수 입력'))) # input 값을 입력받음, 스트링형식으로 반환되기 때문에 int 사용
        print(f'{cal.first} + {cal.second} = {cal.add()}') # cal에서 인스턴트를 생성했기 때문에 cal에서 받아온다
        print(f'{cal.first} - {cal.second} = {cal.sub()}')
        print(f'{cal.first} * {cal.second} = {cal.mul()}')
        print(f'{cal.first} / {cal.second} = {cal.div()}')

CalculatorStatic.main() #다른곳에서 작업을 가져올수있다
