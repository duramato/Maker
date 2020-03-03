import requests
import re
from bs4 import BeautifulSoup

datas = []
lista_numeros = []
lista_estrelas = []

url_sorteio = ["https://www.resultados-euromilhoes.com/resultados-euromilhoes-2019.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2018-2.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2017.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2017-2.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2016.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2016-2.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2014.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2014-2.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2013.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2013-2.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2012.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2012-2.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2011.html",
               "https://www.resultados-euromilhoes.com/resultados-euromilhoes-2011-2.html"]

for i in range(0, len(url_sorteio)):
    page = requests.get(url_sorteio[i], verify=False)
    page_content = page.text

    soup = BeautifulSoup(page_content)

    resultados = soup.find(id="nav_menuLot")
    itens = list(resultados.find_all(class_="lotitem"))
    for i in range(0, len(itens)):
        data = itens[i].find("a").text[:15]
        data = re.match("(.*)(\d{2}-.*-\d{4})(.*)" , str(data))
        if data:
            data = data.group(2)
            datas.append(data)
        else:
            continue
        resultado = itens[i].find_all("span")
        numeros = resultado[1:][:-2]
        estrelas = resultado[6:]
        num = []
        star = []
        for i in range(0, len(numeros)):
            num.append(numeros[i].text)
        for i in range(0, len(estrelas)):
            star.append(estrelas[i].text)
        lista_estrelas.append(star)
        lista_numeros.append(num)
        print("\n")

import csv
with open('sorteios.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Data", "Num1", "Num2", "Num3", "Num4", "Num5", "Estre1", "Estre2"])
    for i in range(0, len(lista_numeros)):
        data_individual = datas[i]
        n_indi = lista_numeros[i]
        s_indi = lista_estrelas[i]
        print(data_individual, n_indi, s_indi)
        writer.writerow([data_individual, n_indi[0], n_indi[1], n_indi[2], n_indi[3], n_indi[4], s_indi[0], s_indi[1]])