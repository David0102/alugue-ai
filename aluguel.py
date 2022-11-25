import abc


class Aluguel(abc.ABC):

    @abc.abstractmethod
    def get_valor_aluguel(self, tempo):
        pass
