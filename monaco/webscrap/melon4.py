import requests
from bs4 import BeautifulSoup


class Melon4(object):
    url = 'https://www.melon.com/chart/index.htm?dayTime='  # str
    headers = {'User-Agent': 'Mozilla/5.0'}  # dictionary(컬그레이스)
    class_name = []  # list(스퀘어)

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}',headers= self.headers).text

    def get_url(self):
        soup = BeautifulSoup(self.url,'lxml')
        ls = soup.find_all("div",{"class" : self.class_name[0]})  #  함수안에 들어갈땐 ""
        count = 0
        print("제목")
        for i in ls:
            count += 1
            print(f'RANK{count}')
            print(i.find("a").text)
        ls = soup.find_all("div", {"class": self.class_name[1]})
        count = 0
        print("가수")
        for i in ls:
            count += 1
            print(f'RANK{count}')
            print(i.find("a").text)

    @staticmethod
    def main():
        melon4 = Melon4()
        while 1:
            menu = int(input('0:EXIT 1:INPUT 2:READ'))
            if menu == 0:
                break
            elif menu == 1:
                melon4.set_url(input('시간을 입력해주세요 에시: 2021052511'))
            elif menu == 2:
                melon4.class_name.append("ellipsis rank01")
                melon4.class_name.append("ellipsis rank02")
                melon4.get_url()

            else:
                continue



Melon4.main()