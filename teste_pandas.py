import pandas as pd

s = pd.Series([10, 20, 30])
print(s)

df = pd.DataFrame({
    "nome": ["Meki", "João", "Isa", "Treviz", "Davi"],
    "idade": [18, 18, 19, 19, 18]
})
print(df)

nomes = []
idades = []

#for i in range(3):
#    nome = input("Digite o nome: ")
#    nomes.append(nome)

#df2 = pd.DataFrame({
#    "Nome": nomes
#})

df3 = pd.read_csv("captura-de-dados.csv")
print(df3)

print()

print(df3["cpu"])

print()

print(df3.iloc[1])

print()
print()
print()

print(f"DADOS: {df3}")

print()
print()

df = pd.read_csv("captura-de-dados.csv", parse_dates=["timestamp"])
print(df.dtypes)