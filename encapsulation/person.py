'''
이름, 출생연도, 주소를  입력받아서
회원가입한 사람의 이름 나이 주소를 출력하시오

'''


class person(object):

    def __init__(self, name, birth, adr):  # 생성자
        self.name = name
        self.birth = birth
        self.adr = adr

    def get_name(self):
        return self.name

    def get_birth(self):
        return self.birth

    def get_adr(self):
        return self.adr

    @staticmethod
    def main():
        p = person(input('이름을 입력하세요 : '), int(input('생년월일을 입력하세요 : ')), input('주소를 입력하세요 : '))
        print(f'이름 :{p.get_name()}')
        print(f'생년월일 :{p.get_birth()}')
        print(f'주소 :{p.get_adr()}')


person.main()
