import abc


class Aluguel(abc.ABC):  # Classe abstrata(abstração).

    # Método abstrato que será implementado pelas classes CarroComum e CarroVip para calcular o valor do aluguel.
    # O método será implementado de maneira diferente nas classes(Polimorfismo).
    @abc.abstractmethod
    def get_valor_aluguel(self, tempo):
        pass
