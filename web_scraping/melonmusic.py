from bs4 import BeautifulSoup
from urllib.request import urlopen


# 라이브러리를 임포트 시켜온다.


class MelonMusic(object):
    # class 디스크에 저장 ,가상 ,값을 가질 수 없다.self 메모리에 저장
    uni = ''

    # init의 약어 생성자에 값을 넣을때는 init필요'''

    def __str__(self):  # = to string
        return f'입력하신 URL {self.uni}'

    def scrap(self, url):
        pass

    @staticmethod
    def get_ranking(soup, texts):
        count = 0

        print(f'==========={texts} RANKING ===========')

        for i in soup.find_all(name='p', attrs=({"class": texts})):  # <p class = "artist">
            count += 1
            print(f'{str(count)} RANKING')
            print(f'{texts}:{i.find("a").text}')


    @staticmethod  # 클래스 안에 실행파일 느낌.
    def main():
        bugs = MelonMusic()  # 클래스를 생성해주고 아래서 값을 넣는다

        while 1:
            menu = int(input('0, EXIT  1. INPUT URL 2. GET RANK'))
            if menu == 0:
                print('종료하겟습니다.')
                break
            elif menu == 1:
                bugs.uni = input('URL 입력하세요 ')

            elif menu == 2:
                print(f'Input URL is{bugs}')
                soup = BeautifulSoup(urlopen(bugs.uni), 'lxml')  # url 오픈
                choice = int(input('0: 가수 1: 제목'))
                if choice == 0:
                    texts = 'artist'
                    MelonMusic.get_ranking(soup, texts)
                elif choice == 1:
                    texts = 'title'
                    MelonMusic.get_ranking(soup, texts)
            elif menu == 3:
                pass
            else:
                print('잘못입력하였습니다.')
                continue


MelonMusic.main() #태그값이 다르고 html 호환이 되는지 모르겟다.
