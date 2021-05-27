import urllib
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup


class Melon2(object):
    url = ''
    class_name = []
    artist_ls = []
    title_ls = []
    title_dict = {}
    df = None

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
            self.title_ls.append(i.find("a").text)
        count = 0
        print("====가수명====")
        ls = soup.find_all(name='div', attrs=self.class_name[1])
        for i in ls:
            count += 1
            print(f'순위 : {count}')
            print(f'가수명:{i.find("a").text}')
            self.artist_ls.append(i.find("a").text)

    def get_dict(self):
        for i in range(0, len(self.title_ls)):
            self.title_dict[self.title_ls[i]] = self.artist_ls[i]
        print(self.title_dict)
        for i in self.title_dict.keys():
            print(f'{self.title_dict[i]}')

    def dictionary_to_dataframe(self):

        dt = self.title_dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/melon2.csv'
        self.df.to_csv(path,sep = 'n',na_rep='NaN')
    @staticmethod
    def main():
        melon2 = Melon2()
        while 1:
            menu = int(input('0:EXIT 1:INPUT 2:READ 3:DICT'))
            if menu == 0:
               break
            elif menu == 1:
                melon2.url = input('URL : ')

            elif menu == 2:
                melon2.class_name.append('ellipsis rank01')
                melon2.class_name.append('ellipsis rank02')#실수적당히해라
                melon2.get_url()
            elif menu == 3:
                melon2.get_dict()
            elif menu == 4:
                melon2.dictionary_to_dataframe()
            elif menu == 5:
                melon2.df_to_csv()
            else:
                continue

Melon2.main()
