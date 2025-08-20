import csv
from datetime import datetime, timedelta

while True:
    print()
    str_interacao = input("Insira sua interação: (Exibir o uso médio de RAM da última hora = 1, Exibir o pico de uso de CPU em determinado período. = 2, Exibir a média de uso de disco nos últimos N minutos = 3)")

    interacao = int(str_interacao)

    if interacao == 1:
        with open('captura-de-dados.csv', 'r', encoding='utf-8') as arquivo:
            leitor = list(csv.reader(arquivo))
            ultima_media_ram = leitor[-1][2]
            print(leitor)
            print(f"Uso médio da útlima hora {leitor[-1][0]}: {ultima_media_ram}%")

    elif interacao == 2:
        econtrou = False
        data = input("Insira um determinado período para ver o pico de CPU (exemplo: YYYY-mm-dd 00:00:00)")
        with open('captura-de-dados.csv', 'r', encoding='utf-8') as arquivo:
            leitor = list(csv.reader(arquivo))
            for i in range(len(leitor)):
                if(data == leitor[i][0]):
                    print(f"Pico de CPU nesse período: {leitor[i][1]}")
                    econtrou = True
                    break
            if not econtrou:
                print("Horário não encontrado")

    
        