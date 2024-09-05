import random


def normalSearch(n, list):
    contador = 0
    for number in list:
        contador = contador + 1
        if n == number:
            return True, contador
    return False, contador


def binarySearch(n, list):
    menor = 0
    maior = len(list) - 1
    contador = 0

    while menor <= maior:
        contador = contador + 1
        meio = (maior + menor) // 2
        if n == list[meio]:
            return True, contador
        elif n > list[meio]:
            menor = meio + 1
        elif n < list[meio]:
            maior = meio - 1

    return False, contador


# Gera uma lista de 100 números aleatórios entre 1 e 1000
listaDeNumerosAleatorios = random.sample(range(1, 10001), 10000)

# Ordena a lista
listaDeNumerosOrdenados = sorted(listaDeNumerosAleatorios)

print(listaDeNumerosOrdenados)

listaDeNumeros = [1, 2, 3, 4, 14, 22]

print(normalSearch(888, listaDeNumerosOrdenados))
print(binarySearch(888, listaDeNumerosOrdenados))
