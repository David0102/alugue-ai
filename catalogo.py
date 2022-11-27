class Catalogo:

    # Método para verificar se há um determinado carro no tipo de catálogo passado por parâmetro.
    def procura_carros(modelo, catalogo):
        if catalogo.get(modelo):
            return 1
        else:
            return 0

    # Método para adcionar um carro no tipo de catálogo passado por parâmetro.
    def adciona_carro(modelo, catalogo, placa):
        catalogo[modelo] = placa

    # Método para remover o carro do tipo de catálogo passado por parâmetro.
    def remove_carro_catalogo(modelo, catalogo):
        catalogo.pop(modelo)
