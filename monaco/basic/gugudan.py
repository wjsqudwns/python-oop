'''
구구단프로그램은 단을 입력받아 입력받는 단의 1~9의 곱을 출력하는 어플이다
단은 정수이다

class Gugudan(object):
    dan = 0 # __init__을 포함하기때문에 안쓴다 self.dan = dan 과 같다.

    def get_gugudan(self): # 만약 매개변수로 dan을 선언한다면 위에 먼저  선언한 dan은 의미가 없어져 버린다.
        for i in range(1, 10):
            print(f'{self.dan} * {i} = {self.dan * i}')

    @staticmethod
    def main():
        gugudan = Gugudan() # 인스턴스 만들기, __init__이 없기때문에 굳이 채울 필요가 없다.

        while 1:
            gugudan.dan = int(input('단: '))  # input을 그냥 스면 1이라도 str 1이기 때문에 int로 감싼다.
            gugudan.get_gugudan()
            break
Gugudan.main()

'''


class Gugudan(object):
    dan = 0
    dict = {}
    def get_gugudan(self):
        for i in range(1,10):
            print(f'{self.dan} * {i} = {self.dan * i}')

    def get_alldan(self):
        for i in range(2, 10):
            print(f'{i}단')
            for j in range(1, 10):
                print(f'{i} * {j} = {i * j}')
    def print_dict_dan(self):
        d = self.dict
        for i in range(1, 10):
            d[i] = self.dan * i  # 키값 선택시 중복안되도록, 키값의 구조는 리스트 []
        print('딕셔너리 출력')

        print(d)
        for k in d.keys():
            print(f'{self.dan} * {k} = {d.get(k)}') # get: 값을 가져오는 메소드
    @staticmethod
    def main():
        gugudan = Gugudan()
        while 1:
            menu = int(input('0: EXIT 1:INPUT 2:ALLDAN 3:DICTOUTPUT'))
            if menu == 0:
                break

            elif menu == 1:
                gugudan.dan = int(input('단 : '))
                gugudan.get_gugudan()

            elif menu == 2:
                gugudan.get_alldan()

            elif menu == 3:
                gugudan.dan = int(input('단 : '))
                gugudan.print_dict_dan()
            else:
                continue


Gugudan.main()