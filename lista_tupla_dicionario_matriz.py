print('\n'*50) #quebra 50 linhas no terminal

# Lista ou vetor: É mutável, É ordenado, É indexado de 0..n
lista = [10,20,30]
print(lista[2])

# Tupla: NÃO é mutável, É ordenado, É indexado de 0..n
tupla = (10,20,30)
# tupla[1] = 5 # vai dar erro...

# Dicionário: É mutável, É ordenado (a partir da v3.7), É indexado pela chave
dicionario = {"num01": 10, "num02":20,"num02":25, "num03":30}
print(dicionario["num02"]) #retorna o último, nesse caso 25

dicionarioAluno = {"nome": "Bob", "idade": 42, "nota": 7.8}
print(dicionarioAluno["nome"])

# Vetor de vetor
# Ou vetor com mais de uma dimensão, nesse caso, 2 (matriz bidimencional)
matriz = [[10],[20],[30]]

# Matriz 3x3
matriz01 = [[10,20,30],
            [40,50,60],
            [70,80,90]]

print(type(lista))
print(type(tupla))
print(type(dicionario))
print(type(matriz))