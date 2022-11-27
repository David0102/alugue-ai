from ast import Break
from aluguelCarro import Carro, CarroComum, CarroVip
from aluguel import Aluguel
from catalogo import Catalogo

N = 0

Aluguel.register(CarroComum)
Aluguel.register(CarroVip)


# Catálogo dos carros disponíveis
catalogo = {'Gol': 111, 'Corola': 222,
            'Celta': 333, 'Camaro': 444, 'Civic': 555, 'S10': 666, 'Fox': 777, 'HB20': 888}

# Catálogo dos carros alugados(Inicialmente vazio).
alugados = {}


# Menu interativo.
def menu():
    print("\n|CARRO COMUM = 20R$ A HORA|")
    print("|CARRO VIP = 40R$ A HORA|\n")
    print("|CATALOGO DE CARROS|")
    print("MODELO      PLACA")
    for i, z in catalogo.items():
        print("{0:10}{1:6}".format(i, catalogo[i]))
    print("\n")
    print("|CARROS EM USO|")
    print("MODELO      PLACA")
    for i, z in alugados.items():
        print("{0:10}{1:6}".format(i, alugados[i]))
    print("\n")
    print("1 - Alugar carro\n2 - Devolver carro\n3 - Sair\n")


menu()
N = int(input("Digite a opção: "))

while (N != 3):
    if N == 1:
        tipo = input("Deseja alugar um carro comum ou vip: ")
        modelo = input("Digite o modelo do carro de acordo com o catálogo: ")
        placa = input("Digite a placa do carro de acordo com o catálogo: ")
        tempo = int(input("Digite o tempo de aluguel do carro em horas: "))

        # Verifica se o determinado modelo está disponível para aluguel.
        cont = Catalogo.procura_carros(modelo, catalogo)

        # Verifica se o determinado modelo já foi alugado.
        cont1 = Catalogo.procura_carros(modelo, alugados)

        if cont == 1:
            if tipo == 'comum':
                carro = CarroComum(modelo, placa, tempo)
                valor = carro.get_valor_aluguel()

                if valor != 0:
                    print("\nCarro alugado com sucesso!")
                    print("O valor do aluguel será de %d reais!\n" % (valor))

                    # Remove carro dos disponíveis e adiciona no catálogo dos alugados.
                    Catalogo.remove_carro_catalogo(modelo, catalogo)
                    Catalogo.adciona_carro(modelo, alugados, placa)
                else:
                    print("\nTempo inválido!\n")
            elif tipo == 'vip':
                carro = CarroVip(modelo, placa, tempo)
                valor = carro.get_valor_aluguel()

                if valor != 0:
                    print("\nCarro alugado com sucesso!")
                    print("O valor do aluguel será de %d reais!\n" % (valor))
                    Catalogo.remove_carro_catalogo(modelo, catalogo)
                    Catalogo.adciona_carro(modelo, alugados, placa)
                else:
                    print("\nTempo inválido!\n")
            else:
                print("\nTipo de carro indisponível!\n")

        elif cont1 == 1:
            print("\nO carro ja foi alugado!\n")
        else:
            print("\nO carro não está no catálogo!\n")

    if N == 2:
        placa = input("Digite a placa do carro a ser devolvido: ")
        modelo = input("Digite o modelo do carro a ser devolvido: ")

        # Verifica se o carro já foi devolvido.
        cont = Catalogo.procura_carros(modelo, catalogo)
        cont1 = Catalogo.procura_carros(modelo, alugados)

        if cont == 1:
            print("\nO carro já foi devolvido!\n")
        elif cont1 == 1:
            Catalogo.remove_carro_catalogo(modelo, alugados)
            Catalogo.adciona_carro(modelo, catalogo, placa)
            print("\nCarro devolvido!\n")
        else:
            print("\nCarro inválido!\n")

    if N == 3:
        break
    menu()
    N = int(input("Digite a opção: "))
