#
# autores: Cristiano, Michel
#
# data: 13/07/2023

# 2.	(25 pontos) Escreva um programa em Python que leia vários valores
# inteiros (positivos ou negativos), até que seja informado o valor 0 ( ZERO) ,
# encontra o maior e o menor deles e mostra o resultado.

valor = int(input("Digite um valor inteiro: "))
maior = -10000000
menor = 10000000

while valor != 0:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    valor = int(input("Digite um valor inteiro: "))
    
print("O maior valor é: ", maior)
print("O menor valor é: ", menor)

