'''
def bmi_function(kg,cm): #루틴,함수형 프로그래밍
    result = kg / (cm ** 2) * 10000
    return result
'''


class Bmi(object):

    def __init__(self, kg, cm):  # setter __init__ 나를 지칭하는 것 서브루틴
        self.kg = kg  # 프로퍼티
        self.cm = cm

    def get_bmi(self):  # getter 서브루틴
        return self.kg / (self.cm ** 2) * 10000  # **제곱

    def get_stat(self):
        a = self.get_bmi()

        if a >= 30:
            stat = '고도비반'
        elif a >= 25:
            stat = '비만'
        elif a >= 23:
            stat = '과체중'
        elif a >= 18.5:
            stat = "정상"
        else:
            stat = "저체중"

        return stat

    @staticmethod
    def main():
        a = Bmi(int(input('체중을 입력(kg): ')), int(input('키를 입력(cm): ')))
        print(f'Bmi 지수: {a.get_bmi()}')
        print(f'현재 상태: {a.get_stat()}')


Bmi.main()
# print(bmi_function(80,170))

# a = Bmi(80,170)
# print(a.get_Bmi())
