'''
 Fazer um programa que pergunte um valor em Dólares e apresente o equivalente em Reais. Considere U$1,00 =
R$3,80
'''

doll = float(input("Digite o valor em Dólares: "))
real = doll * 3.80
print(f"R${real:.2f}")