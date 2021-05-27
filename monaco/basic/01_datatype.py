#***************
#---datatype---
#***************

'''
python has Five standard types

scalar
Number : int, float, (complex)
String :  str -> 기본적으로 list 구조

vector
Collection : List, Tuple, Dictionary, Set
인덱스의 유무의 따라서
-> list tuple 시퀀스구조
-> Dictionary set 해쉬구조

ATOM(원자) = 구조가 있는 가장 작은단위

HelloWorld = 'Hello'
print(HelloWorld)
print(HelloWorld[0])
print(HelloWorld[2:5])
print(HelloWorld[2:])  #  끝까지 출력

객체는 메소드(기능)을 갖는다.

Python list


ls = ['abcd', 123, 4.25, 'elice', 10.5]
tinylist = [12553, 'chris']

# ls에 목록을 출력 read

print(ls[1])

# ls에 값을 추가하는것, 100추가 create
ls.append(100) # 맨 뒷자리에 추가되는것
ls.insert(0, 50) # 특정 자리에 추가하는것
print(ls)
# ls 에서 123을 제거 delete ls.pop(4) 요소 지정해서 삭제
ls.remove(123)
print(ls)
# ls와 tinylist 의 결합
ls += tinylist # ls.extends(tinylist)
print(ls)
'''

#tuple crud

tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')
# Create: tp 에 '100'을 추가 Create
x = list(tp)
x.insert(0,100)
tp = tuple(x)
print(tp)
# Read: tp 의 목록을 출력

print(tp)
# Update: tp와 tinytp 의 결합

tp += tinytp
print(tp)

# Delete: tp 에서 786을 제거
x = list(tp)
x.remove(786)
tp = tuple(x)
print(tp)


'''
dt = {'abcd' : 786, 'john': 70.2}
tinydt = {'홍':0, 'abc':0}
# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
dt['tom'] = 100
print(dt)

# Read: dt 의 목록을 출력
print(dt)
# Update: dt와 tinydt 의 결합
dt.update(tinydt)
print(dt)

# Delete: dt 에서 'abcd' 제거
del dt['홍']
print(dt)
'''