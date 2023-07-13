#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# 3.	(25 pontos) Em linguagem Python, Escreva um programa leia vários valores 
# inteiros (positivos ou negativos), até que seja informado o valor 0 ( ZERO) , 
# calcule média dos valores impares informados.

somaImpares = 0
contadorImpares = 0

while True:
    valor = int(input("Digite um valor inteiro (0 para sair): "))
    
    if valor == 0:
        break
    
    if valor % 2 != 0:
        somaImpares += valor
        contadorImpares += 1

if contadorImpares == 0:
    mediaImpares = 0
else:
    mediaImpares = somaImpares / contadorImpares

print("A média dos valores ímpares é:", mediaImpares)
