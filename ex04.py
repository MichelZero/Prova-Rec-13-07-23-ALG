#
# autores: Cristiano, Michel
#
# data: 13/07/2023

# 4.	(25 pontos) Faça um programa que leia um número n e imprima se ele 
# é primo ou não. (um número primo tem apenas 2 divisores: 1 e ele 
# mesmo! O número 1 não é primo!


# entrada de dados
num = int(input("Digite um número: "))

# processamento
divisor = 2 # para encontrar um divisor de num entre 2 e num-1 (inclusive) 
while divisor < num: # enquanto o divisor for menor que num 
    if num % divisor == 0: # se o resto da divisão de num por divisor for 0 
        print("Não é primo") # num não é primo
        break # interrompe o laço 
    divisor += 1 # incrementa o divisor em 1 
else:
    print("É primo") # se o laço terminar sem interrupção, num é primo 
    