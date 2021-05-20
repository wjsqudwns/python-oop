class menu(object):
    def __init__(self, coffee):
        self.coffee = coffee


    def get_coffee(self):
        return f'남은 커피의 양은 {self.coffee}개 입니다.'

    @staticmethod

    def main():
        a = menu(10)
        print(a.get_coffee())
        while 1:
            choice = int(input('1, 아메리카노 주문\n' '0. 종료 \n'))
            if choice == 0:
                print('주문 완료')
                break
            elif choice == 1:
                if a.coffee == 0:
                    print(f'현재 남은 커피의 양은 {a.coffee} \n 커피가 모두 소진되었습니다.')
                    break
                else :
                    a.coffee = a.coffee - 1
                    print(f'현재 남은 커피의 양은 {a.coffee}개 입니다.')

            else:
                print('잘못입력하셧습니다.')
                continue
    pass

menu.main()