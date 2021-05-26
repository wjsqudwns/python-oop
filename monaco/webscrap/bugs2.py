import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Bugs2(object):

    url = ''
    class_name = []

    def get_url(self):

        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(self.url, headers=hdr)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        print('========가수========')
        ls = soup.find_all(name='p', attrs=self.class_name[0])
        for i in ls:
            print(f'가수 : {i.find("a").text}')
        print('========제목========')
        ls = soup.find_all(name='p', attrs=self.class_name[1])
        for i in ls:
            print(f'제목 : {i.find("a").text}')

    @staticmethod
    def main():
        bugs2 = Bugs2()
        while 1:
            menu = int(input('0: EXIT 1: INPUT 2: READ'))
            if menu == 0:
                break
            elif menu == 1:
                bugs2.url = input('URL :') #실수하지마라
            elif menu == 2:
                bugs2.class_name.append('artist')
                bugs2.class_name.append('title')
                bugs2.get_url()
            else:
                continue

Bugs2.main()