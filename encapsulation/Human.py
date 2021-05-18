class Human(object):
    def __init__(self,name,sx,birth):
        self.name = name
        self.sx = sx
        self.birth = birth
    def pr(self):
        print(f'이름 : {self.name} ,성별 : {self.sx} ,나이 : {self.birth}')
    def info(self, name, sx, birth):
        self.name = name
        self.sx = sx
        self.birth = birth
    def death(self):
        print('사망')
p = Human('신원미상', '불명', 00)
p.pr()
p.info('전병준','남자',24)
p.pr()
p.death()
