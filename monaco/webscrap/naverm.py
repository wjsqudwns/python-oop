
'''c = Naverm() 같다 한번만 쓰기때문에 바꾼것
    c.scrap()
Naverm().scrap()  # dynamic 메소드 일땐 클래스 이름뒤에 ()가 붙고 static 일땐 붙지 않는다 self가 없기 때문에

@staticmethod
def Main():
    c = Naverm()
    c.scrap()

   while 1:
        menu = int(input('0:EXIT 1:C 2:R 3:U 4:D'))
        if menu == 0:
            print('종료')
            break

        elif menu == 1:
            c.scrap()

            pass
        elif menu == 2:

            pass
        elif menu == 3:

            pass

        else:
            print('잘못입력하셨습니다.')
            continue


Naverm.Main()'''
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


class Naverm(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = ''
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'  # 파일이름복붙 슬래쉬 방향바꿔주기
    dict = {}
    m_name =[]
    df = None

    def scrap(self):

        driver = webdriver.Chrome(self.driver_path) # 그렇기에 webdriver의 크롬 클래스를 이용하여 인스턴스로 만들어준다.
        driver.get(self.url)  # 프레임워크 구조이기때문에 넘겨주는것 driver는 str 형식이 들어가 있어 객체이지만 인스턴스는 아니기에 get을 쓸수없다
        soup = BeautifulSoup(driver.page_source, 'html.parser') # 자바 스크립트가져오는것
        all_div = soup.find_all("div", {"class": self.class_name}) # name과 attrs 생략가능 왜냐하면 첫번쩨 자리가 태그라고 정해져 있기 때문이다.두번째는 내가 찾고 싶은단어의 가장 가까운 클래스명
        # 대신 구조는 맞춰주어야 한다.("",{ : })딕셔너리 구조 (해시구조)

        [print(f'{i.find("a").text}')for i in all_div] # 컴프리핸션 연습 [수행할 작업, 반복]
        [self.m_name.append(i.find("a").text)for i in all_div]

        # print
        driver.close

    def to_dict(self):
        rank = 0
        for i in range(0, len(self.m_name)):
            rank += 1
            self.dict[rank] = self.m_name[i]

    def dict_to_df(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')

    def to_csv(self):
        path = './movie/NaverM.csv'
        self.df.to_csv(path, sep='n', na_rep='NaN')

    @staticmethod
    def csv_to_Excel():

        xlsxname = pd.ExcelWriter('NaverM.xlsx') # 저장할 엑셀 파일이름
        xlsxpath = pd.read_csv('./movie/NaverM.csv') # csv의 파일을 읽어옴
        xlsxpath.to_excel(xlsxname, index= False)
        xlsxname.save()


if __name__ == '__main__':

    c = Naverm()
    c.class_name = input('테그명을 입력하세요')
    c.scrap()
    c.to_dict()
    c.dict_to_df()
    c.to_csv()
    c.csv_to_Excel()
