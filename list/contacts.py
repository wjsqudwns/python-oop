'''

이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.

'''


class Contacts(object):
    def __init__(self, name, phone, email, adr):
        self.name = name
        self.phone = phone
        self.email = email
        self.adr = adr

    def get_contacts(self):
        return f'주소록 : 이름 {self.name}, 전화번호 {self.phone}, 이메일 {self.email}, 주소 {self.adr}'

    @staticmethod
    def del_name(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

    @staticmethod
    def main():
        ls = [] # 리스트

        while 1:
            choice = int(input('0. 종료 \n' '1, 주소록 추가\n' '2. 출력 \n' '3. 삭제 \n' '4. 수정\n'))
            if choice == 0:
                print('작업완료')
                break
            elif choice == 1:
                ls.append(Contacts(input('이름을 입력하세요 '), int(input('전화번호를 입력하세요 ')), input('이메일을 입력하세요 '), input('주소를 입력하세요 '))) # 추가하라
            elif choice == 2:
                for i in ls:
                    print(i.get_contacts())
            elif choice == 3:
                dname = Contacts(input('삭제할 이름 : '), None, None, None)
                dname.del_name(ls, dname.name)

            elif choice == 4:
                name = input('수정할 이름 :')
                cname = Contacts(name, input('수정 전화번호'),input('수정 이메일'),input('수정 주소'))
                cname.del_name(ls, cname.name)
                ls.append(cname)

            else:
                print('잘못입력하셧습니다.')
                continue


Contacts.main()

# 수정하고 출력이안됨
