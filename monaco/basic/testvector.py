class TestVector(object):
    #  필드 프로퍼티 -> ()는 붙을 수 없다 메서드가 아니기 때문이다.
    ls = ['abcd', 123, 4.25, 'alice', 10.5]
    tinylist = [12553, 'chris']

    tp = ('abcd', 786, 2.23, 'john', 70.2)
    tinytp = (123, 'john')

    dt = {'abcd': 786, 'john': 70.2}
    tinydt = {'홍': 0, 'abc': 0}

    def ls_read(self):
        print(self.ls)  # self -> 나의

    def ls_create(self, choice):
        self.ls.append(choice)  # 맨 뒷자리에 추가되는것

    def ls_update(self):
        self.ls += self.tinylist  # ls.extends(tinylist)

    def ls_delete(self, choice):
        self.ls.remove(choice)

    def tp_read(self):
        print(self.tp)

    def tp_create(self, choice):  # 튜플은 요소의 값은 수정삭제가 불가능하지만 리스트로 바꾸거나 튜플을 덮어씌워 바꿀수있다.
        li = list(self.tp)
        li.append(choice)
        self.tp = tuple(li)

    def tp_merge(self):
        self.tp += self.tinytp #-> 수정보다는 merge 병합

    def tp_delete(self, choice):
        li = list(self.tp)
        li.remove(choice)
        self.tp = tuple(li)

    def dt_read(self):
        print(self.dt)

    def dt_create(self, choice, choice2):
        self.dt[f'{choice}'] = choice2 # 키값 안에 값 넣기

    def dt_update(self):
        self.dt.update(self.tinydt) # 메소드

    def dt_delete(self, choice):
        del self.dt[f'{choice}'] #

    @staticmethod
    def main():
        testvector = TestVector()

        while 1:
            menu = int(input('list 1:C 2:R 3:U 4:D \n'
                             'tuple 5:C 6:R 7:M 8:D \n'
                             'dictionary 9:C 10:R 11:U 12:D \n'))

            if menu == 0:
                break

            elif menu == 1:
                choice = input("입력하신 데이터")
                testvector.ls_create(choice)
                testvector.ls_read()

            elif menu == 2:
                testvector.ls_read()

            elif menu == 3:
                testvector.ls_update()
                testvector.ls_read()

            elif menu == 4:
                choice = input("삭제하실 데이터")
                testvector.ls_delete(choice)
                testvector.ls_read()

            elif menu == 5:
                choice = input("입력하신 데이터")
                testvector.tp_create(choice)
                testvector.tp_read()

            elif menu == 6:
                testvector.tp_read()

            elif menu == 7:
                testvector.tp_merge()
                testvector.tp_read()

            elif menu == 8:
                choice = input("삭제하실 데이터")
                testvector.tp_delete(choice)
                testvector.tp_read()

            elif menu == 9:
                choice = input("키값 : ")
                choice2 = input("넣을 데이터 : ")
                testvector.dt_create(choice, choice2)
                testvector.dt_read()

            elif menu == 10:
                testvector.dt_read()

            elif menu == 11:
                testvector.dt_update()
                testvector.dt_read()

            elif menu == 12:
                choice = input("삭제하실 데이터")
                testvector.dt_delete(choice)
                testvector.dt_read()

            else:
                continue


TestVector.main()
