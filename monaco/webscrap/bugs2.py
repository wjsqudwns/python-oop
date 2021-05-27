import urllib
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup


class Bugs2(object):

    url = ''
    class_name = []
    title_ls = []
    artist_ls = []
    title_dict = {}

    df = None

    def get_url(self):

        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(self.url, headers=hdr)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        print('========가수========')
        ls = soup.find_all(name='p', attrs=self.class_name[0])
        for i in ls:
            print(f'가수 : {i.find("a").text}')
            self.title_ls.append(i.find("a").text)
        print('========제목========')
        ls = soup.find_all(name='p', attrs=self.class_name[1])

        for j in ls:
            print(f'제목 : {j.find("a").text}')
            self.artist_ls.append(j.find("a").text)

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
        path = './data/bugs.csv'
        self.df.to_csv(path, sep='n', na_rep='NaN')

    @staticmethod
    def main():
        bugs2 = Bugs2()
        while 1:
            menu = int(input('0: EXIT 1: INPUT 2: READ 3:DICT'))
            if menu == 0:
                break
            elif menu == 1:
                bugs2.url = input('URL :') #실수하지마라
            elif menu == 2:
                bugs2.class_name.append('artist')
                bugs2.class_name.append('title')
                bugs2.get_url()
            elif menu == 3:
                bugs2.get_dict()
            elif menu == 4:
                bugs2.dictionary_to_dataframe()
            elif menu == 5:
                bugs2.df_to_csv()
            else:
                continue


Bugs2.main()