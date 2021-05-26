import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Melon2(object):
    url = ''
    class_name = []

    def get_url(self):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(self.url, headers=hdr)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        ls = soup.find_all(name= 'div',attrs=self.class_name[0])
        count = 0
        print("====곡 제목====")
        for i in ls:
            count += 1
            print(f'순위 : {count}')
            print(f'곡명:{i.find("a").text}')
        count = 0
        print("====가수명====")
        ls = soup.find_all(name='div', attrs=self.class_name[1])
        for i in ls:
            count += 1
            print(f'순위 : {count}')
            print(f'가수명:{i.find("a").text}')
    @staticmethod
    def main():
        melon2 = Melon2()
        while 1:
            menu = int(input('0:EXIT 1:INPUT 2:READ'))
            if menu == 0:
               break
            elif menu == 1:
                melon2.url = input('URL : ')

            elif menu == 2:
                melon2.class_name.append('ellipsis rank01')
                melon2.class_name.append('ellipsis rank02')#실수적당히해라
                melon2.get_url()
            else:
                continue

Melon2.main()
