class Wikipedia(object):
    def __init__(self, uni):
        self.uni = uni

    def __str__(self):
        return f'INPUT : {self.uni}'

    @staticmethod
    def main():
        while 1:
            menu = int(input('0:EXIT 1:INPUT 2:OUTPUT'))
            if menu == 0:
                print('종료하겟습니다.')
                break

            elif menu == 1:
                wiki = Wikipedia(input('URL 입력하세요 '))

            elif menu == 2:
                print(wiki)

            else:
                print('잘못입력하였습니다.')
                continue


Wikipedia.main()
