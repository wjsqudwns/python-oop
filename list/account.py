import random


class account(object):
    def __init__(self, name, money):
        self.bname = 'SC은행'
        self.name = name
        self.money = money
        self.number = f'{int(random.uniform(0, 999))}-{int(random.uniform(0, 99))}-{int(random.uniform(0, 999999))}'

    def get_account_num(self):
        return f'은행이름 : {self.bname} \n 예금주 : {self.name} \n 계좌번호 : {self.number} \n 잔액 : {self.money}'


    @staticmethod
    def main():
        ls = []
        while 1 :
            choice = int(input('0. 종료\n 1. 입금 \n 2. 출금 \n 3. 잔액확인 \n 4. 계좌생성 \n 5. 계좌목록 확인\n'))
                if choice == 0 :
                    break
                elif choice == 1:
                    pass
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    ls.append(input('이름 : '), input('잔액 : '))
                elif choice == 5:
                    for i in ls:
                        print(i.get_account_num())


account.main()
