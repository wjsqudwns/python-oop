import requests
from bs4 import BeautifulSoup



class Bugs4(object):
    url = 'https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self,detail):
        self.url = requests.get(f'{self.url}{detail}',headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url,'lxml')
        print('제목')
        ls = soup.find_all("p",{"class":self.class_name[0]})
        for i in ls:
            print(i.find("a").text)
        print('가수')
        ls = soup.find_all("p", {"class": self.class_name[1]})
        for i in ls:
            print(i.find("a").text)

    @staticmethod
    def main():
        b = Bugs4()
        while 1:
            menu = input('0, 1-input time, 2-output')
            if menu == '1':
                b.set_url(input('스크래핑할 날짜 입력'))  # '2021052511'
            elif menu == '2':
                b.class_name.append('title')
                b.class_name.append('artist')
                b.get_ranking()
            else:
                print('Wrong number')


Bugs4.main()