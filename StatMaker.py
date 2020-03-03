import csv
from random import choices
from collections import Counter

def gerar_sorteio():

    with open('sorteios.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        data = []
        num1 = []
        num2 = []
        num3 = []
        num4 = []
        num5 = []
        star1 = []
        star2 = []
        for row in spamreader:
            row = row[0].split(",")
            if row[0] == "Data":
                continue
            data.append(row[0])
            num1.append(row[1])
            num2.append(row[2])
            num3.append(row[3])
            num4.append(row[4])
            num5.append(row[5])
            star1.append(row[6])
            star2.append(row[7])
    num1_stat = {k: v for k, v in sorted(dict(Counter(num1)).items(), key=lambda item: item[1], reverse=True)}
    num2_stat = {k: v for k, v in sorted(dict(Counter(num2)).items(), key=lambda item: item[1], reverse=True)}
    num3_stat = {k: v for k, v in sorted(dict(Counter(num3)).items(), key=lambda item: item[1], reverse=True)}
    num4_stat = {k: v for k, v in sorted(dict(Counter(num4)).items(), key=lambda item: item[1], reverse=True)}
    num5_stat = {k: v for k, v in sorted(dict(Counter(num5)).items(), key=lambda item: item[1], reverse=True)}
    star1_stat = {k: v for k, v in sorted(dict(Counter(star1)).items(), key=lambda item: item[1], reverse=True)}
    star2_stat = {k: v for k, v in sorted(dict(Counter(star2)).items(), key=lambda item: item[1], reverse=True)}

    numeros = [*num1, *num2, *num3, *num4, *num5]
    estrelas = [*star1, *star2]
    amostra_n = len(numeros)
    amostra_e = len(estrelas)

    numeros_dict = dict(Counter(numeros))
    numeros = {k: v for k, v in sorted(numeros_dict.items(), key=lambda item: item[1], reverse=True)}

    lista_num = range(1, 51)

    missing_numbers = [i for i in lista_num if i not in map(int, list(numeros.keys()))]
    #print("A verificar numeros:\n")
    #print(list(lista_num))
    #print(list(map(int, list(numeros.keys()))))
    #print(missing_numbers)

    estrelas_dict = dict(Counter(estrelas))
    estrelas = {k: v for k, v in sorted(estrelas_dict.items(), key=lambda item: item[1], reverse=True)}

    lista_stars = range(1, 13)

    missing_stars = [i for i in lista_stars if i not in map(int, list(estrelas.keys()))]
    #print("A verificar estrelas:\n")
    #print(list(lista_stars))
    #print(list(map(int, list(estrelas.keys()))))
    #print(missing_stars)

    prob_numeros = [x / amostra_n for x in numeros.values()]

    lista_numeros = []

    for i in range(0, len(list(numeros.keys()))):
        lista_numeros.append(int(list(numeros.keys())[i]))

    numeros = []
    for i in range(0, 5):
        numero = choices(lista_numeros, prob_numeros)[0]
        numeros.append(numero)

    print("Numeros:")
    print(tuple(numeros))

    prob_estrelas = [x / amostra_n for x in estrelas.values()]

    lista_estrelas = []

    for i in range(0, len(list(estrelas.keys()))):
        lista_estrelas.append(int(list(estrelas.keys())[i]))

    estrelas = []
    for i in range(0, 2):
        estrela = choices(lista_estrelas, prob_estrelas)[0]
        estrelas.append(estrela)

    print("Estrelas:")
    print(tuple(estrelas))

for i in range(0, 5):
    gerar_sorteio()
    print(" ")