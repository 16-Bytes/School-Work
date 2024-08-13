'''
 Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:
a) Resultado de suas adições
b) Resultado de suas multiplicações
'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
soma = num1 + num2 + num3 + num4
mult = num1 * num2 * num3 * num4
print(f"Soma: {soma}\nMultiplicação: {mult}")