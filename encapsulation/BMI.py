class Bmi :
    def set_bmi(self, kg, cm):
        self.kg = kg
        self.cm = cm
    def bmi(self):

        return self.kg / ((self.cm / 100) * (self.cm / 100))


if __name__ == '__main__':

    a = Bmi()
    a.set_bmi(80, 170)
    print(a.bmi())