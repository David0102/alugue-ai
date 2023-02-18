import abc
from aluguel import Aluguel


class Carro(abc.ABC):  # Classe abstrata(abastração).
    def __init__(self, modelo, placa):
        self._modelo = modelo
        self._placa = placa


class CarroComum(Carro):  # CarroComum herda da classe Carro(Herança).
    def __init__(self, modelo, placa, tempo):
        super().__init__(modelo, placa)
        self._tempo = tempo

    # Foi utilizado property e setter para fazer o encapsulamento na classe CarroComum(encapsulamento).
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @property
    def tempo(self):
        return self._tempo

    @tempo.setter
    def tempo(self, tempo):
        self._tempo = tempo

    # Método para calcular o valor do aluguel na classe CarroComum.
    def get_valor_aluguel(self):
        if (self._tempo > 0):
            return self._tempo * 20
        else:
            return 0


class CarroVip(Carro):  # CarroVip herda da classe Carro(Herança).
    def __init__(self, modelo, placa, tempo):
        super().__init__(modelo, placa)
        self._tempo = tempo

    # Foi utilizado property e setter para fazer o encapsulamento na classe CarroVip(encapsulamento).
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @property
    def tempo(self):
        return self._tempo

    @tempo.setter
    def tempo(self, tempo):
        self._tempo = tempo

    # Método para calcular o valor do aluguel na classe CarroVip.
    def get_valor_aluguel(self):
        if (self._tempo > 0):
            return self._tempo * 40
        else:
            return 0
