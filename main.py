from functools import reduce


def main():
    listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sumaImpares = reduce(lambda a, b: a + b, list(filter(lambda x: x % 2 != 0, listaNumeros)))
    print(sumaImpares)


if __name__ == '__main__':
    main()
