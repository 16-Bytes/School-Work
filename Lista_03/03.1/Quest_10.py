'''
Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias)
'''
valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa de juros: "))
dias = int(input("Digite a quantidade de dias em atraso: "))
prestacao = valor + (valor * (taxa / 100) * dias)
print(f"Valor da prestação em atraso: R${prestacao:.2f}")