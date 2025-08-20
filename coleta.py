import psutil
import pandas as pd
import time as time
import datetime as datetime

dados = {

}


metricasTimeStamp = []
metricasCpu = []
metricasRam = []
metricasDisco = []

while True:
    percentual_cpu = psutil.cpu_percent(interval=1, percpu=False)

    captura_memoria = psutil.virtual_memory()

    percentual_ram = round((captura_memoria.total - captura_memoria.available) / captura_memoria.total * 100, 2)

    dataHora = datetime.datetime.now()
    dataHoraFormatado = dataHora.strftime("%Y-%m-%d %H:%M:%S")

    captura_disco = psutil.disk_usage('/')
    percentual_disco = captura_disco.percent

    metricasTimeStamp.append(dataHoraFormatado)
    metricasCpu.append(percentual_cpu)
    metricasRam.append(percentual_ram)
    metricasDisco.append(percentual_disco)

    print(metricasTimeStamp)
    print(metricasCpu)
    print(metricasRam)
    print(metricasDisco)

    dados = {
    "timestamp": metricasTimeStamp,
    "cpu": metricasCpu,
    "ram": metricasRam,
    "disco": metricasDisco
    }

    df = pd.DataFrame(dados)
    df.to_csv("captura-de-dados", encoding="utf-8", index=False)
    
    time.sleep(9)