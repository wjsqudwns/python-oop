import requests
from bs4 import BeautifulSoup


class Bugs2(object):

    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent':'Mozilla/5.0'}
    class_name = []
    artist_ls = []
    title_ls = []
    title_dict = {}

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}',headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------- 제목 --------')
        ls = soup.find_all("div", {"class": self.class_name[0]}) #찾은것을 리스트에넣고 반복시켜 출력
        for i in ls:
            print(f' {i.find("a").text}')
            self.title_ls.append(i.find("a").text)

        print('------ 가수 --------')
        ls = soup.find_all("div", {"class": self.class_name[1]})
        for i in ls:
            print(f' {i.find("a").text}')
            self.artist_ls.append(i.find("a").text)

    def get_dict(self):
        for i in range(0, len(self.title_ls)):
            self.title_dict[self.title_ls[i]] = self.artist_ls[i]
        rank1 = 0
        print(self.title_dict)
        for i in self.title_dict.keys():
            rank1 += 1
            print(f'{rank1} - {self.title_dict[i]}')

    @staticmethod
    def main():
        b = Bugs2()
        while 1:
            menu = input('0, 1-input time, 2-output 3-DICT')
            if menu == '1':
                b.set_url(input('스크래핑할 날짜 입력')) # '2021052511'
            elif menu == '2':
                b.class_name.append('ellipsis rank01')
                b.class_name.append('ellipsis rank02')
                b.get_ranking()
            elif menu == '3':
                b.get_dict()
            else:
                print('Wrong number')

Bugs2.main()