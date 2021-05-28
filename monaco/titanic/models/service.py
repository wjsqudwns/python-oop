from titanic.models.dataset import Dataset
import pandas as pd


class Service(object):

    dataset = Dataset()

    def new_model(self, payload):
        this = self.dataset # this변수명 데이터셋 인스턴스를 디스에 넣어줌
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)
