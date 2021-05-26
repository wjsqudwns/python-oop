class TestVector(object):

    ls = ['abcd', 123, 4.25, 'alice', 10.5]
    tinylist = [12553, 'chris']

    tp = ('abcd', 786, 2.23, 'john', 70.2)
    tinytp = (123, 'john')

    def ls_read(self):
        return print(self.ls)

    def ls_create(self, choice):
        self.ls.append(choice)  # 맨 뒷자리에 추가되는것

    def ls_update(self):
        self.ls += self.tinylist  # ls.extends(tinylist)

    def ls_deleete(self, choice):
        self.ls.remove(choice)

    def tp_read(self):
        return print(self.tp)

    def tp_create(self,choice):
        x = list(self.tp)
        x.append(choice)
        self.tp = tuple(x)

    def tp_update(self):
        self.tp += self.tinytp

    def tp_deleete(self, choice):
        x = list(self.tp)
        x.remove(choice)
        self.tp = tuple(x)

    @staticmethod
    def main():
        testvector = TestVector()

        while 1:
            menu = int(input('ls 1:C 2:R 3:U 4:D \n'
                             'tp 5:C 6:R 7:U 8:D \n'
                             'dt 1:C 2:R 3:U 4:D \n'))
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
                testvector.ls_deleete(choice)
                testvector.ls_read()

            elif menu == 5:
                choice = input("입력하신 데이터")
                testvector.tp_create(choice)
                testvector.tp_read()

            elif menu == 6:
                testvector.tp_read()

            elif menu == 7:
                testvector.tp_update()
                testvector.tp_read()
            elif menu == 8:
                choice = input("삭제하실 데이터")
                testvector.tp_deleete(choice)
                testvector.tp_read()

            elif menu == 9:
                pass

            elif menu == 10:
                pass

            elif menu == 11:
                pass

            elif menu == 12:
                pass
            else:
                continue


TestVector.main()
