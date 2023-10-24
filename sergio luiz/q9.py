#Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

posicao1 = 0
posicao2 = 0
posicao3 = 0

if numero1 >= numero2 and numero3 <= numero2:
    posicao1 = numero1
    posicao2 = numero2
    posicao3 = numero3
elif numero2 >= numero3 and numero1 <= numero3:
    posicao1 = numero2
    posicao2 = numero3
    posicao3 = numero1
elif numero3 >= numero2 and numero1 <= numero2:
    posicao1 = numero3
    posicao2 = numero2
    posicao3 = numero1 
elif numero3 >= numero1 and numero1 >= numero2:
    posicao1 = numero3
    posicao2 = numero1
    posicao3 = numero2
elif numero1 >= numero3 and numero3 >= numero2:
    posicao1 = numero1
    posicao2 = numero3
    posicao3 = numero2
elif numero2 >= numero1 and numero1 >=numero3:
    posicao1 = numero2
    posicao2 = numero1
    posicao3 = numero3


print(f"{posicao1},{posicao2},{posicao3}")

