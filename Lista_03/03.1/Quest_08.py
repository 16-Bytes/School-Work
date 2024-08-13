'''
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro.
'''

distancia = float(input("Qual a distância de sua viagem em (Km): "))
consumo = float(input("Quantos litros por kilometro sem automóvel consome: "))
print(f"O total em litros que seu automóvel gastará nessa viagem para dirigir {distancia} Km { distancia/consumo :.1f} litros ")