# manipulando vetores

# lista ou vetor:
listaVetor = [5, 10, 15, 17, 88, 21]

# Retornando um dos elementos
print(listaVetor[1])

# Percorendo os elementos
for elemento in listaVetor:
    print(f"Elemento: {elemento}")

# Percorrendo de acordo com chave ou índice
for i in range(len(listaVetor)):
    print(i)

# Percorrendo de acordo com valor
alvo = listaVetor[3]
for i in range(len(listaVetor)):
    if listaVetor[i] == alvo:
        print(f"Número {alvo} encontrado\n")

# Alterando valor dos elementos
listaVetor[5] = 100
print(listaVetor)

# Alterando valor dos elementos usando algum critério
for i in range(len(listaVetor)):
    if listaVetor[i] <= 15:
        listaVetor[i] = 1
print(listaVetor)

# Removendo os elementos
# removendo o primeiro elemento que aparece (se colocar "1", ele vai remover o primeiro 1)
listaVetor.remove(1)
# removendo o primeiro elemento do vetor
listaVetor.pop()
print(listaVetor)

# Removendo os elementos de acordo com algum critério
for i in range(len(listaVetor)):
    if listaVetor[i] >= 80:
        listaVetor.pop(i)
print(listaVetor)

# manipulando tupla

# tupla
listaTupla = (1, 2, 5, 2, 10, 65, 31)

# Retornando um dos elementos
print(listaTupla[0])

# Percorendo os elementos (de uma forma diferente em comparação ao vetor)
for i in range(len(listaTupla)):
    print(listaTupla[i])

# Percorrendo de acordo com chave ou índice
for i in range(len(listaTupla)):
    print(i)

# Percorrendo de acordo com valor
alvo = listaTupla[4]
for i in range(len(listaTupla)):
    if listaTupla[i] == alvo:
        print(f"Alvo da tupla encontrada: {alvo}")

# Alterando valor dos elementos

# DÁ ERRO, POIS TUPLAS SÃO IMUTÁVEIS

## listaTupla[0] = 9
## listaTupla[6] = 99

## print(listaTupla)

# Alterando valor dos elementos usando algum critério

#TAMBÉM DÁ ERRO!!

# if listaTupla[3] == 10:
#    listaTupla[3] = 5
# print(listaTupla)

# Removendo os elementos

# ERROOO

# listaTupla.remove(2)
# print(listaTupla)

# Removendo os elementos de acordo com algum critério

# TBM DÁ ERRO

# if listaTupla[5] == 12:
#    listaTupla[5] == 100


# Manipulando dicionarios

# Retornando um dos elementos
dicionario = {"personagem1": "Naruto", "personagem2": "Kira", "personagem3": "Isagi", "personagem4": "Mordecai", "personagem5": "Gumball"}
print(dicionario["personagem1"])

# Percorendo os elementos
for personagem in dicionario.values(): # Percorre os VALORES do dicionario
    print(personagem)

# Percorrendo de acordo com chave ou índice
for i in range(len(dicionario)):
    print(i)

# Percorrendo de acordo com valor
# Não consegui :(
# alvo = dicionario[2].values()
# for i in range(len(dicionario)):
#    if dicionario[i].values() == alvo:
#        print(alvo)

# Alterando valor dos elementos
# *Só é possível alterar os valores dos valores (Sim, chave-VALOR)
dicionario['personagem3'] = 'Goku'
print(dicionario)

# Alterando valor dos elementos usando algum critério
for chave, valor in dicionario.items():
    if valor == 'Mordecai':
        dicionario[chave] = 'Rigby'

print(dicionario)

# Removendo os elementos
del dicionario['personagem1']
print(dicionario)

# Removendo os elementos de acordo com algum critério
if dicionario['personagem5'] == 'Gumball':
    del dicionario["personagem5"]
print(dicionario)


# Manipulando matriz
matriz =   [[10,20,30],
            [40,50,60],
            [70,80,90]]

# Retornando um dos elementos
print(matriz[2][1])

# Percorendo os elementos
for elemento in matriz:
    print(elemento)

# Percorrendo de acordo com chave ou índice
for i in range(len(matriz)):
    print(i)

# Percorrendo de acordo com valor
alvo = matriz[1][0] # 40
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == alvo:
            print(f"Alvo encontrado: {alvo}")

# Alterando valor dos elementos
matriz[1][2] = 65
matriz[2][0] = 75
print(matriz)

# Alterando valor dos elementos usando algum critério
if matriz[0][0] == 10:
    matriz[0][0] = 15

# Removendo os elementos
matriz[2].remove(80)
matriz[1].pop();

# Removendo os elementos de acordo com algum critério
if matriz[0][0] == 10:
    matriz[0].remove(10)
    print(matriz)