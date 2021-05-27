class Mydataframe(object):
    def __init__(self, column, row):
        self.column = column
        self.row = row

    @staticmethod
    def main():
        df = Mydataframe(10, 3)
        print(df)

Mydataframe.main()