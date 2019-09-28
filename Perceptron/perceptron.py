import csv

def readData(file):
    data_set = []

    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')

        index = 0

        for row in readCSV:
            if index == 0:
                index = 1
                continue
            data_set.append(row)

    return data_set

def error(valor_esperado,valor_recebido):
        return valor_esperado-valor_recebido

def ativacao(vi):
    if vi >= 0:
        return 1
    return 0

def conversao_classe_para_inteiro(classe):
    if classe == "preto":
        return  1
    return 0
    
def perceptron(dados,w):
    valor_esperado, i = 0, 0
    M = 0.3

    while i < (len(dados)):
        j, vi = 0, 0.0
        while j < (len(dados[i]) - 2):
            vi += ( ( w[j] * float(dados[i][j])))
            j += 1
        vi += w[2]
        valor_esperado = conversao_classe_para_inteiro(dados[i][3])
        valor_recebido = ativacao(vi)

        if valor_recebido != valor_esperado:
            e = error(valor_esperado,valor_recebido)
            if e !=0:
                key = 0
                while  key < len(w):
                    w[key] +=  (M*e*float(dados[i][key]))
                    key += 1 
        i+=1
    print(w)
    
pesos = [1, 1, 1]
dados = readData('./dados.csv')

perceptron(dados,pesos)