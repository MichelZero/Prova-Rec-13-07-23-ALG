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
        

# outra solução

# entrada de dados
num = int(input("Digite um número entre 1 e 10: "))

# processamento
while num < 1 or num > 10:
    num = int(input("Número inválido. Digite novamente: "))

print(f"o número foi {num}")
print("fim do programa!")