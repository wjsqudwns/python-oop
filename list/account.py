import random
class Account(object):

    def __init__(self, account_number, name, money):
        self.name = name
        self.money = money
        self.BNAME = 'SC은행'
        self.account_number = account_number

    def to_string(self):
        return f'은행이름 : {self.BNAME} \n 이름 : {self.name} \n 계좌번호 {self.account_number} \n 잔액 {self.money}'

    @staticmethod # 사용하는 곳이 동적 메소드에서 정적메소드로 바뀌였기 때문이다. 원래는 setter에서 바로 넣어주려고 했음
    def create_account_number():
        # ls = [str(random.randit(0,9)) for i in range(3)]
        ls = []
        for i in range(3):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0,9)))

        return "".join(ls) # 공백없이 붙여라


    @staticmethod
    def del_element(ls,account_number):

        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]
    @staticmethod #리펙토링
    def c_money(menu,ls,account_number,money):

        if menu == 3:
            for i, j in enumerate(ls):
                if j.account_number == account_number:
                    replace = Account(account_number, j.name, int(j.money) + int(money))
                    Account.del_element(ls, account_number)
                    ls.append(replace)
        elif menu == 4:

            for i, j in enumerate(ls):
                if j.account_number == account_number:  # 계좌번호비교
                    replace = Account(account_number, j.name, int(j.money) - int(money))  # 인스턴스 생성
                    Account.del_element(ls, account_number)
                    ls.append(replace)  # 데이터 추가
    @staticmethod
    def main():
        ls =[]
        while 1:
            menu = int(input('0.Exit 1.계좌 생성 2.계좌 출력 3.입금 4.출금 5.탈퇴'))
            if menu == 0:
                break
            elif menu == 1:
                ls.append(Account(Account.create_account_number(), input('name '), input('money ')))
            elif menu == 2:
                for i in ls:
                    print(i.to_string())
            elif menu == 3:

                account_number = input('입금할 계좌번호 ')
                money = input('입금액 : ')
                Account.c_money(menu, ls, account_number,money)

            elif menu == 4:

                account_number = input('출금할 계좌번호 ')
                money = input('출금액 : ')
                Account.c_money(menu, ls, account_number, money)

            elif menu == 5:
                Account.del_element(ls, input('탈퇴할 계좌번호'))


Account.main()

