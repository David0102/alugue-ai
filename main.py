from ast import Break
from aluguelCarro import Carro, CarroComum, CarroVip
from aluguel import Aluguel
from catalogo import Catalogo

N = 0

Aluguel.register(CarroComum)
Aluguel.register(CarroVip)

catalogo = {'Gol': 111, 'Corola': 222,
            'Celta': 333, 'Camaro': 444, 'Civic': 555, 'S10': 666, 'Fox': 777, 'HB20': 888}

alugados = {}


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
        modelo = input("Digite o modelo do carro: ")
        placa = input("Digite a placa do carro de acordo com o catálogo: ")
        tempo = int(input("Digite o tempo de aluguel do carro em horas: "))

        cont = Catalogo.catalogo_carros(modelo, catalogo)
        cont1 = Catalogo.carros_alugados(modelo, alugados)

        if cont == 1:
            if tipo == 'comum':
                carro = CarroComum(modelo, placa, tempo)
                valor = carro.get_valor_aluguel()

                if valor != 0:
                    print("\nCarro alugado com sucesso!")
                    print("O valor do aluguel será de %d reais!\n" % (valor))
                    Catalogo.remove_carro_catalogo(modelo, catalogo)
                    alugados[modelo] = placa
                else:
                    print("\nTempo inválido!\n")
            elif tipo == 'vip':
                carro = CarroVip(modelo, placa, tempo)
                valor = carro.get_valor_aluguel()

                if valor != 0:
                    print("\nCarro alugado com sucesso!")
                    print("O valor do aluguel será de %d reais!\n" % (valor))
                    Catalogo.remove_carro_catalogo(modelo, catalogo)
                    alugados[modelo] = placa
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
        cont = Catalogo.catalogo_carros(modelo, catalogo)
        cont1 = Catalogo.carros_alugados(modelo, alugados)

        if cont == 1:
            print("\nO carro já foi devolvido!\n")
        elif cont1 == 1:
            Catalogo.devolve_carro(modelo, catalogo, placa)
            alugados.pop(modelo)
            print("\nCarro devolvido!\n")
        else:
            print("\nCarro inválido!\n")

    if N == 3:
        print("Programa encerrado!")
        break
    menu()
    N = int(input("Digite a opção: "))
