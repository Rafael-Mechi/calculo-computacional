#
print ('\n'*2)
# Atribuir valores inteiros a duas variáveis
a = 6
b = 3
# Vamos fazer operações mais elaboradas
# usando as 4 operaçõe/s simples
soma = a+b
subtracao =a-b
multiplicacao = a*b
divisao =a/b
print ("Vamos mostrar todos os resultados")
print ("a=", a)
print ("b=", b)
print ("a+b=",soma)
print ("a-b=",subtracao)
print ("a*b=",multiplicacao)
print ("a/b=",divisao)

# O que podemos observar em relação aos números inteiros e a saída resultante da divisão?
# R:

#
print ('\n'*50)
a1=6.5
b1=2.5
# Vamos fazer operações mais elaboradas
# usando as 4 operações simples
soma = a1+b1
subtracao =a1-b1
multiplicacao = a1*b1
divisao =a1/b1
print ("Vamos mostrar todos os resultados")
print ("a1=", a1)
print ("b1=", b1)
print ("a1+b1=",soma)
print ("a1-b1=",subtracao)
print ("a*b=",multiplicacao)
print ("a/b=",divisao)

# Se houver algum erro apontado pelo interpretador nas operações acima corrija

# Exercício 1)
# Atribua o valor 2 a uma variável chamada a.

# • Calcule:
# o potencia_ao_quadrado como a elevado ao quadrado.
# o potencia_ao_cubo como a elevado ao cubo.
# o potencia_a_quarta como a elevado à quarta potência.

a = 2
potencia_ao_quadrado = a**2
potencia_ao_cubo = a**3
potencia_a_quarta = a**4

# • Imprima os resultados no seguinte formato:
# Potência ao quadrado: <valor>
# Potência ao cubo: <valor>
# Potência à quarta: <valor>
print(f"Potência ao quadrado: {potencia_ao_quadrado}")
print(f"Potência ao quadrado: {potencia_ao_cubo}")
print(f"Potência ao quadrado: {potencia_a_quarta}")

# Exercício 2)
# Crie um programa em Python que:
# • Importe a função pow do módulo math.
# • Atribua valores para duas variáveis:
# o c (ex.: 4)
# o d (ex.: 5)

import math
c_str = input("Digite o valor de c: ")
d_str = input("Digite o valor de d: ")

c = int(c_str)
d = int(d_str)

#• Calcule usando pow() e armazene em variáveis:
#o c_elevado_ao_quadrado → c²
#o c_elevado_ao_cubo → c³
#o c_elevado_a_quarta → c⁴
#o c_elevado_a_d → c elevado a d

c_elevado_ao_quadrado = pow(c, 2)
c_elevado_ao_cubo = pow(c, 3)
c_elevado_a_quarta = pow(c, 4)
c_elevado_a_d = pow(c, d)

#Exiba os resultados com mensagens no formato:

 #c elevado ao quadrado = <valor>
 #c elevado ao cubo = <valor>
 #c elevado a quarta = <valor>
 #c elevado a d = <valor>

print(f"c elevado ao quadrado = {c_elevado_ao_quadrado}\n")
print(f"c elevado ao cubo = {c_elevado_ao_cubo}\n")
print(f"c elevado a quarta = {c_elevado_a_quarta}\n")
print(f"c elevado a d = {c_elevado_a_d}\n")

"""
Exercício 3)
Faça um código em Python
• Cria uma variável x=512
• Calcule:
o raiz_quadrada_de_x =
o raiz_cúbica_de_x =
o raiz_quarta_de_x =
• Imprima o resultado das strings
"""

x = 512
raiz_quadrada_x = math.sqrt(x);
print(raiz_quadrada_x)

raiz_cubida_x = pow(x, 1/3)
print(raiz_cubida_x)

raiz_quarta_x = pow(x, 1/4)
print(raiz_quarta_x)

"""
Exercício 4)
Dado o valor de w anteriormente, import as funções floor, ceil da biblioteca math e determine o
piso, o teto e o arredondamento. (usar floor, ceil e round)

"""

w = 3345.61

w_piso = math.floor(w)
w_teto = math.ceil(w)
w_arredondado = round(w)

print(f"Salário: {w}")
print(f"Piso: {w_piso}")
print(f"Teto: {w_teto}")
print(f"Arredondado: {w_arredondado}")

"""
Exercício5)
• Teste a função round usando casas decimais, inclusive 0 casas
• Por que não importamos o round?
"""
w = 3345.6123849
w_arredondado = round(w)
print(w_arredondado)


w = 3345
w_arredondado = round(w)
print(w_arredondado)

# Não importamos o round porque ela, assim como outras funções (pow, print, len) já vem programadas em bibliotecas ao instalar o python

"""
Exercício 6)
Arredonde os números a seguir, exibindo sem casas decimais:
x1=1.456
x2=3.678
x3=7.5
"""

x1 = 1.456
x2 = 3.678
x3 = 7.5

print(round(x1))
print(round(x2))
print(round(x3))

"""
Exercício 7)
Voltando ao caso do floor e ceil, por padrão estas funções retornam valores inteiros. Podemos
determinar que os valores resultantes possuam ponto flutuante (float):
"""

# Faça o teste a seguir:
print('\n'*2)
resultado = math.floor(1.456)
print(resultado)
print(type(resultado))
resultado_float = float(math.floor(1.456))
print(resultado_float)
print(type(resultado_float))

# Creio que o enunciado pede para dizermos qual variável retorna um tipo float. Portanto, é a variável "resultado_float",
# pois a função "float()" garante que o número tenha casas decimais, enquanto floor arredonda para o piso

"""
Super Exercício 8)
Resolva em Python as expressões a seguir:
"""

q1 = pow(2, 3)
print(q1)

q2 = -(pow(2, 3))
print(q2)

q3 = pow(1, 0)
print(q3)

q4 = -(pow(1, 0))
print(q4)

q5 = pow(2, 0)
print(q5)

q6 = pow(2/5, 3)
print(q6)

q7 = pow(3, -2)
print(q7)

q8 = pow (1/2, -3)
print(q8)

q9 = pow(-1, 3) ** 4
print(q9)

q10 = pow(0.5, 3)
print(q10)

q11 = pow(0.25, 4)
print(q11)

q12 = pow(0, 4)
print(q12)

q13 = 1 + pow(0.41, 2)
print(q13)

q14 = 1/4 + pow(5, 2) - pow(-2, -4)
print(q14)

q15 = pow(2, -3) + pow(-4, -5)

q16v1 = (((4/5)-(1/2)+1)**-2) + (1 / (1 + 3**2 - (4-5)**-2))
print(q16v1)

q16v2 = pow((4/5-1/2)+1, -2) + (1 / (1 + pow(3, 2) - (pow(4-5, -2))))
print(q16v2)