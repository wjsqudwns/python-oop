from bs4 import BeautifulSoup
import requests

import pandas as pd

class BugsMusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    df = None
    dt = {}
    title_ls = []
    artist_ls = []
    title_dict = {}
    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------- 제목 --------')
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[1]}))
        for i in ls:
            print(f' {i.find("a").text}')
            self.title_ls.append(i.find("a").text)
        print('------ 가수 --------')
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls:
            print(f'{i.find("a").text}')
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
        path = './data/bugs3.csv'
        self.df.to_csv(path, sep='n', na_rep='NaN')

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit, 1-input time, 2-output')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url(input('상세정보 입력')) # wl_ref=M_contents_03_01
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.get_dict()
            elif menu == '4':
                bugs.dictionary_to_dataframe()
            elif menu == '5':
                bugs.df_to_csv()

            else:
                print('Wrong Number')
                continue


BugsMusic.main()