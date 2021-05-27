from bs4 import BeautifulSoup
import requests


class BugsMusic2(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []  # keys
    artist_ls = []  # values
    dict = {}

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name="p", attrs=({"class":self.class_name[0]}))
        ls2 = soup.find_all(name="p", attrs=({"class": self.class_name[0]}))
        for i in ls1:
            self.title_ls.append(i.find("a").text)
        for i in ls2:
            self.title_ls.append(i.find("a").text)

    def insert_title_dict(self):
        '''
        for i in range(0, len(self.title_ls)): # 있는만큼 돌림
            self.dict[self.title_ls[i]] = self.artist_ls[i]


        for i, j in enumerate(self.title_ls):
            self.dict[self.title_ls[j]] = self.artist_ls[i]

        for i, j in zip(self.title_ls, self.artist_ls):
            self.dict[i] = j
        '''

    @staticmethod
    def main():
        bugs = BugsMusic2()
        while 1:
            menu = input('0-exit, 1-input time, 2-output, 3-print dict')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url('wl_ref=M_contents_03_01')
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.insert_title_dict()
            else:
                print('Wrong Number')
                continue


BugsMusic2.main()