from dataclasses import dataclass


@dataclass()
class Dataset(object):
    context: str
    fname: str
    train: str
    text: str
    id: str  # 값이 숫자로 보여도 외부에서 넘어오는 값이나 내부에서 입력하는 값은 다 str 형식
    label: str

    @property
    def context(self) -> str: return self._context  # _는 접근제한의 의미 프로퍼티 하나하나 다 추가해주어야함 getter

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def text(self) -> str: return self._text

    @text.setter
    def text(self, text): self._text = text

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label