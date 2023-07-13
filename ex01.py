#
# autores: Cristiano, Michel
#
# data: 13/07/2023

# 1.	(25 pontos) Escreva um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até 
# que o usuário informe um valor válido.

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota >= 0 and nota <= 10:
        break
    else:
        print("Nota inválida. Digite novamente.")
        
