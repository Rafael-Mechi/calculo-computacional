import psutil
import pandas as pd
import time as time
import datetime as datetime

dados = []

while True:
    percentual_cpu = psutil.cpu_percent(interval=1, percpu=False)

    captura_memoria = psutil.virtual_memory()

    percentual_ram = round((captura_memoria.total - captura_memoria.available) / captura_memoria.total * 100, 2)

    dataHora = datetime.datetime.now()
    dataHoraFormatado = dataHora.strftime("%Y-%m-%d %H:%M:%S")

    captura_disco = psutil.disk_usage('/')
    percentual_disco = captura_disco.percent

    print(dataHoraFormatado)
    print(percentual_cpu)
    print(percentual_ram)
    print(percentual_disco)

    metricas = {
    "timestamp": dataHoraFormatado,
    "cpu": percentual_cpu,
    "ram": percentual_ram,
    "disco": percentual_disco
    }

    dados.append(metricas)

    print(dados)

    df = pd.DataFrame(dados)
    df.to_csv("captura-de-dados.csv", encoding="utf-8", index=False)
    
    time.sleep(9)