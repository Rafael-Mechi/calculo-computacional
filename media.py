entradaNota = 1
listaNotas = []
novaTurma = 's'

while novaTurma == 's':
    while entradaNota > 0:
        nota_str = input("Digite as notas dos alunos (digite um valor negativo para encerrar): ")
        entradaNota = int(nota_str)
        if entradaNota >= 0:
            listaNotas.append(entradaNota)

    print(listaNotas)

    media = 0
    aprovados = 0
    reprovados = 0
    maiorNota = listaNotas[0]
    menorNota = listaNotas[0]

    for i in range(len(listaNotas)):
        media += listaNotas[i]

        if listaNotas[i] > maiorNota:
            maiorNota = listaNotas[i]

        if listaNotas[i] < menorNota:
            menorNota = listaNotas[i]

        if listaNotas[i] < 6:
            reprovados +=1
        else:
            aprovados +=1

    media /= len(listaNotas)
    media = round(media, 2)

    diagnostico = "Desempenho muito fraco"

    if media >= 5 and media < 7:
        diagnostico = "Desempenho razoável"

    elif media >= 7 and media < 9:
        diagnostico = "Bom desempenho"

    elif media >= 9:
        diagnostico = "Excelência!"

    print("Média da turma: ", media)
    print("Maior nota: ", maiorNota)
    print("Menor nota: ", menorNota)
    print("Aprovados: ", aprovados)
    print("Reprovados: ", reprovados)
    print("Diagnóstico: ", diagnostico)
    novaTurma = input("Deseja analisar outra turma? (s/n): ")
    if novaTurma != 's':
        break

    entradaNota = 1
    listaNotas = []

print("Encerrando programa...")