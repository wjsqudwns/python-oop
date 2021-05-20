'''

이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.

'''


class contacts(object):
    def __init__(self, name, phone, email, adr):
        self.name = name
        self.phone = phone
        self.email = email
        self.adr = adr

    def get_contacts(self):
        return f'주소록 : 이름 {self.name}, 전화번호 {self.phone}, 이메일 {self.email}, 주소 {self.adr}'

    @staticmethod
    def main():
        ls = [] # 리스트

        while 1:
            choice = int(input('0. 종료 \n' '1, 주소록 추가\n' '2. 출력 \n' '3. 삭제 \n' '4. 수정'))
            if choice == 0:
                print('작업완료')
                break
            elif choice == 1:
                ls.append(contacts(input('이름을 입력하세요 '), int(input('전화번호를 입력하세요 ')), input('이메일을 입력하세요 '), input('주소를 입력하세요 '))) # 추가하라
            elif choice == 2:
                for i in ls:
                    print(i.get_contacts())
            elif choice == 3:
                del_name = input('삭제할 이름 : ')
                for i, j in enumerate(ls): #i는 인덱스번호  j인덱스에 해당하는 개체 -> 비교할때는 개체값 지울때는 인덱스 번호가 필요하기 때문
                    if j.name == del_name: #이너머레이터 인덱스 값을 돌려받기 위해
                        del ls[i]
            elif choice == 4:
                edit_name = input('수장할 이름 :')
                edit_info =
            else:
                print('잘못입력하셧습니다.')
                continue


contacts.main()
