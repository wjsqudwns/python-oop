import pandas as pd
from bs4 import BeautifulSoup
import requests


class BugsMusic(object):

    url = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    df = None

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='p', attrs=({"class":self.class_name[1]}))
        ls2 = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))

        for i in ls1:
            self.title_ls.append(i.find("a").text)
        for j in ls2:
            self.artist_ls.append(j.find("a").text)

    def insert_title_dict(self):
        '''
        # 방법 1. range
        for i in range(0, len(self.title_ls)):
            self.dict[self.title_ls[i]] = self.artist_ls[i]
        # 방법 2. zip
        for i, j in zip(self.title_ls, self.artist_ls):
            self.title_dict[i] = j
        # 방법 3. enumerate
        for i, j in enumerate(self.title_ls):
            self.dict[j] = self.artist_ls[i]
        '''

        for i in range(0, len(self.title_ls)):
            for i in range(0, len(self.title_ls)):
                self.title_dict[self.title_ls[i]] = self.artist_ls[i]
            print(self.title_dict)
            for i in self.title_dict.keys():
                print(f'{self.title_dict[i]}')

    def dictionary_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt,orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/bugs2.csv'
        self.df_to_csv(path, sep='n', na_rap='NaN')

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit, 1-input time, 2-output, 3-print dict')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url('https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01')
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '4':
                bugs.dictionary_to_dataframe()
            elif menu == '5':
                bugs.df_to_csv()
            else:
                continue


BugsMusic.main()