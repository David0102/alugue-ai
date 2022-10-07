import abc
from aluguel import Aluguel


class Carro(abc.ABC):
    def __init__(self, modelo, placa):
        self._modelo = modelo
        self._placa = placa


class CarroComum(Carro):
    def __init__(self, modelo, placa, tempo):
        super().__init__(modelo, placa)
        self._tempo = tempo

    def get_valor_aluguel(self):
        if (self._tempo > 0):
            return self._tempo * 20
        else:
            return 0


class CarroVip(Carro):
    def __init__(self, modelo, placa, tempo):
        super().__init__(modelo, placa)
        self._tempo = tempo

    def get_valor_aluguel(self):
        if (self._tempo > 0):
            return self._tempo * 40
        else:
            return 0
