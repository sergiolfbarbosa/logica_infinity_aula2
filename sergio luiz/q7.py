#Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
menor = 0
maior = 0

if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1 # 
elif numero2 >= numero3:
    maior = numero2 #
else:
    maior = numero3 #
if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
    print (f"{maior} é o maior número e o {menor} é o menor número!")
elif numero2 <= numero3:
    menor = numero2
    print (f"{maior} é o maior número e o {menor} é o menor número!")
else:
    menor = numero3
    print (f"{maior} é o maior número e o {menor} é o menor número!")
