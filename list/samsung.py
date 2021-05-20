class samsung(object):
    def __init__(self, name, code, per, pbr, plus):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.plus = plus

    def get_name(self):
        return f'종목명 : {self.name}  종목코드 : {self.code}  per : {self.per}  pbr : {self.pbr}  배당수익률 {self.plus} \n'

    @staticmethod
    def main():
        ls = []

        while 1:
            choice = int(input('0 : 종료하기 \n1 : 입력하기 \n2 : 출력하기 \n3 : 삭제하기 \n'))
            if choice == 0:
                print('종료하겟습니다.')
                break
            elif choice == 1:
                ls.append(samsung(input(' 종목명: '), input('종목코드: '), input('per: '), input('pbr: '), input('배당수익률: ')))
            elif choice == 2:
                for i in ls:
                    print(i.get_name())
            elif choice == 3:
                del_name = input('삭제할 회사명 : ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            else:
                print('잘못입력하셧습니다.')
                continue


samsung.main()
