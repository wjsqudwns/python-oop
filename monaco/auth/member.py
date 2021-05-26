class Member(object):
    id = ''
    password = ''
    name = ''
    email = ''

    def get_sign(self):  #"리펙토링을 처음부터 하기 위해서"
        pass

    def get_login(self):
        pass

    def get_join(self):
        pass

    def get_del(self):
        pass

    @staticmethod
    def main():
        member = Member()
        while 1:
            menu = int(input('0:EXIT 1:Sign 2:Login 3:Join 4:Del'))
            if menu == 0:
                break
            elif menu == 1:
                member.id = input('ID: ')
                member.password = int(input('PASSWORD: '))
                member.name = input('NAME: ')
                member.email = input('EMAIL: ')

            elif menu == 2:
                pass
            elif menu == 3:
                pass
            elif menu == 4:
                pass

            else:
                continue
Member.main()
