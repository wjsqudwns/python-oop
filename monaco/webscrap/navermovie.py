import requests
from bs4 import BeautifulSoup


class Navermovie(object):
    url = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, url):
        self.url = requests.get(f'{self.url}',headers= self.headers).text

    def get_rank(self):
        soup = BeautifulSoup(self.url,'lxml')
        print('========= 영화 제목 =========')
        ls = soup.find_all("strong",{"class":self.class_name[0]})
        for i in ls :
            print(f'{i.find("a").text}')
        print('========= 평점 =========')
        ls = soup.find_all("span", {"class": self.class_name[1]})
        for i in ls :
            print(f'{i.find("span").text}')

    @staticmethod
    def main():
        navermovie = Navermovie()
        while 1:
            menu = int(input("0:나가기 1:URL입력 2:영화순위보기"))
            if menu == 0:
                break
            elif menu == 1:
                navermovie.url = input("URL : ")

            elif menu == 2:
                navermovie.class_name.append("tit_item")
                navermovie.class_name.append("txt_num")
                navermovie.get_rank()
            else:
                continue


Navermovie.main()