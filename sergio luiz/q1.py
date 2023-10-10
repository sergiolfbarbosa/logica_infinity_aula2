numero1 = int(input("Digite um número "))
numero2 = int(input("Digite um segundo número "))

if numero1 > numero2:
    print(f"O {numero1} é maior {numero2}")
elif numero1 < numero2:
    print(f"O {numero2} é maior {numero1}")
else:
    print(f"Os valores digitados são iguas.")