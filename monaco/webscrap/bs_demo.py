from bs4 import BeautifulSoup


class BsDemo(object):
    html_doc = ''  # = __init__

    def __str__(self):
        return f'입력된 코드{self.html_doc}'

    @staticmethod
    def main():
        bs = BsDemo()
        while 1:
            menu = int(input('0: EXIT 1: INPUT 2: ALL HTML OUTPUT 3: TITLE OUTPUT'))
            if menu == 0:
                print('종료')
                break

            elif menu == 1:
                bs.html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

            elif menu == 2:
                soup = BeautifulSoup(bs.html_doc, 'html.parser')
                print(soup.prettify())
            elif menu == 3:
                soup = BeautifulSoup(bs.html_doc, 'html.parser')
                print(soup.title.string)
            else:
                print('잘못입력하였습니다.')
                continue

    pass


BsDemo.main()
