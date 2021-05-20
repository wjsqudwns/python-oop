import random


class Account(object):
    def __init__(self, name, money, plus, month):
        self.bname = 'SC은행'
        self.name = name
        self.money = money
        self.number = f'{int(random.uniform(0, 999))}-{int(random.uniform(0, 99))}-{int(random.uniform(0, 999999))}'
        self.plus = plus
        self.month = month

    def get_account_num(self):
        return f'은행이름 : {self.bname} \n 예금주 : {self.name} \n 계좌번호 : {self.number} \n 잔액 : {self.money}'

    @staticmethod
    def main():
        ls = []
        while 1 :
            choice = int(input('0. 종료\n 1. 입금 \n 2. 출금 \n 3. 잔액확인 \n 4. 계좌생성 \n 5. 계좌목록 확인\n'))
            if choice == 0 :
                print('종료합니다.')
                break
            elif choice == 1:

                edit_name = input('입금할 사람 이름')
                edit_num = int(input('입금할 사람 계좌번호'))
                edit_info = Account(edit_name, edit_num, input('입금할 금액'))

                for i, j in enumerate(ls):
                    if j.num == edit_num:
                        del ls[i]
                        ls.append(edit_info)
            elif choice == 3:

                for i, j in enumerate(ls):
                    if j.num == edit_num:
                        print()
            elif choice == 4:
                ls.append(Account(input('이름 : '), input('잔액 : ')))
            elif choice == 5:
                for i in ls:
                    print(i.get_account_num())

Account.main()
