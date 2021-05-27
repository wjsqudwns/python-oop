import  pandas as pd

''' def get_tuple(self):
        self.tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        return self.tp

값의 전달 -> 프로퍼티 활용: self
            -> 파라미터 활용: request값등 외부 값을 받을때 활용


컴프리핸선 : 
        f_ls = []
        for i in range(9)
            f_ls.append(floa(li[i])
        return f_ls

        return [float(ls[i]) for i in range(9)]
'''
'''   @staticmethod
    def get_dataframe():
        pass
'''


class Conversion(object):

    @staticmethod
    def dictionary_to_dataframe(dt) -> object:
        return pd.DataFrame.from_dict(dt, orient='index')

    @staticmethod
    def get_slist(tp) -> []:
        return list(tp)

    @staticmethod
    def get_string(s) -> ():
        return tuple(s)

    @staticmethod
    def get_dictionary(ls) -> {}:

        return dict(zip([str(i) for i in ls], ls)) # 리스트를 딕셔너리를 만드려먼 카와 벨류가 필요한데 따로 없기 때문에 최소 2개가 필요하다 ls 두개 넣은건 의미없음

    @staticmethod
    def get_int(ls) -> []:
        return list(map(int, ls))

    @staticmethod
    def get_float(ls) -> []:
        return [float(i) for i in ls]  # i는 ls안에 값을 의미
        # [float(i) for i in ls]
    @staticmethod
    def get_list(tp) -> []:
        return list(tp)

    @staticmethod
    def get_tuple() -> ():  # 튜플로 반환
        return 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    @staticmethod
    def main():
        # 콜백 지옥 나오는법

        ls = []
        tp = ()
        dt = {}

        c = Conversion()
        while 1:
            m = input('0-exit 1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list\n'
                      '8-dataframe\n')
            if m == '0':
                break
            # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
            elif m == '1':
                tp = c.get_tuple()
                print(tp)
            # 1번 튜플을 리스트로 전환하시오 (return)
            elif m == '2':
                ls = c.get_list(tp)
                print(ls)
            # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '3':
                ls = c.get_float(ls)
                print(ls)
            # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
            elif m == '4':
                ls = c.get_int(ls)
                print(ls)
            # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == '5':
                dt = c.get_dictionary(ls)
                print(dt)
            # 'hello' 를 튜플로 전환하시오
            elif m == '6':
                tp = c.get_string('hello')
                print(tp)
            # 6번 튜플을 리스트로 전환하시오
            elif m == '7':
                ls = c.get_slist(tp)
                print(ls)
            # 5번 딕셔너리를 데이터프레임으로 전환
            elif m == '8':
                tp = c.get_tuple()
                ls = c.get_list(tp)
                dt = c.get_dictionary(ls)
                print(dt)
                df = c.dictionary_to_dataframe(dt)
                print(f'df의 타입 : {type(df)}')
                print(df)
            else:
                continue


Conversion.main()
