class Catalogo:

    def catalogo_carros(modelo, catalogo):
        if catalogo.get(modelo):
            return 1
        else:
            return 0

    def carros_alugados(modelo, catalogo):
        if catalogo.get(modelo):
            return 1
        else:
            return 0

    def devolve_carro(modelo, catalogo, placa):
        catalogo[modelo] = placa

    def remove_carro_catalogo(modelo, catalogo):
        catalogo.pop(modelo)
