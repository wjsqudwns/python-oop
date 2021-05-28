from titanic.views.controller import Controller
# 이닛 파일은 객체가 아니라서 클래스가 필요없다, 같은 레벨에 이닛에 가져와서 테스트해야함 -> 패키지와 같은 레벨
if __name__ == '__main__':
    controller = Controller()
    while 1:
        menu = int(input('0:EXIT 1:Preprocess'))

        if menu == 0:
            break
        elif menu == 1:
            controller.preprocess('train.csv')

        else:
            continue

