#Faça um Programa que leia três números e mostre o maior deles.

numero1 = int(input("Digite o primeiro número ")) 
numero2 = int(input("Digite o segundo número "))
numero3 = int(input("Digite o terceiro número "))

if numero1 >= numero2 and numero1 >= numero3:
    print(numero1," é o maior!")
elif numero2 >= numero3:
    print(numero2," é o maior!")
else:
    print(numero3," é o maior!")