import urllib

from bs4 import BeautifulSoup
from urllib.request import urlopen

class MelonMusic(object):

    url = ''
    class_name = []

    def get_scrap(self):
        hdr = {'User-Agent': 'Mozilla/5.0'}

        req = urllib.request.Request(self.url, headers=hdr)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        count = 0

        for i in soup.find_all(name = 'div', attrs= self.class_name[0]) : #url안에서 전부 다 찾음
            count += 1
            print(f'{str(count)}')
            print(f'title: {i.find("a").text}')
        count = 0
        for i in soup.find_all(name = 'div', attrs= self.class_name[1]) :
            count += 1
            print(f'{str(count)}')
            print(f'singer: {i.find("a").text}')

    @staticmethod
    def main():
        melon = MelonMusic()
        while 1:
            menu = int(input('0:EXIT 1:CREAT 2:READ'))
            if menu == 0:
                print('종료하시겠습니까')
                break
            elif menu == 1:
                melon.url = input('URL 입력:')
            elif menu == 2:
                melon.class_name.append('ellipsis rank01')
                melon.class_name.append('ellipsis rank02')
                melon.get_scrap()
            else:
                print('잘못입력하였습니다.')
                continue


MelonMusic.main()