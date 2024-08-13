'''
Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e apresente esta
temperatura convertida em graus Celsius. A fórmula da conversão é c	= (f–32) x 5 : 9 , onde c é a temperatura
em graus Celsius e f em Fahrenheit.
'''
F = float(input("Digite a temperatura em Fahrenheit: "))
print(f"Temperatura em Celsius: {(F - 32) * 5 / 9:.2f}")