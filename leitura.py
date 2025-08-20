import csv

while True:
    str_interacao = input("Insira sua interação: (Exibir o uso médio de RAM da última hora = 1, Exibir o pico de uso de CPU em determinado período. = 2, Exibir a média de uso de disco nos últimos N minutos = 3)")

    interacao = int(str_interacao)

    if interacao == 1:
        with open('captura-de-dados.csv', 'r', encoding='utf-8') as arquivo:
            leitor = list(csv.reader(arquivo))
            ultima_media_ram = leitor[-1][2]
            print(leitor)
            print(f"Uso médio da útlima hora {leitor[-1][0]}: {ultima_media_ram}%")