# Os critérios de IMC foram pegos no mesmo site que contém o gráfico:
#https://www.mdsaude.com/obesidade/calcule-o-seu-peso-ideal-e-imc/

calcular_outro_imc = 's'

while calcular_outro_imc == 's':
    peso_str = input("Digite seu peso (kg): ")
    altura_str = input("Digite sua altura (m): ")

    peso = float(peso_str)
    altura = float(altura_str)

    imc = round(peso/(altura**2), 2)

    classificacao = "- Baixo peso muito grave"
    frase = "Seu IMC é"

    if imc >= 16 and imc <= 16.99:
        classificacao = "- Baixo peso grave"

    elif imc >= 17 and imc <= 18.49:
        classificacao = "- Baixo peso"

    elif imc >= 18.50 and imc <= 24.99:
            classificacao = "- Peso normal"

    elif imc >= 18.50 and imc <= 24.99:
            classificacao = "- Peso normal"
            
    elif imc >= 25 and imc <= 29.99:
            classificacao = "- Sobrepeso" 

    elif imc >= 30 and imc <= 34.99:
            classificacao = "- Obesidade grau I"

    elif imc >= 35 and imc <= 39.99:
            classificacao = "- Obesidade grau II"

    elif imc >= 40:
            classificacao = "- Obesidade mórbida"  


    print(frase, imc, classificacao)

    calcular_outro_imc = input("Deseja calcular o IMC de outra pessoa? (s/n)")

print("Encerrando a calculadora...")