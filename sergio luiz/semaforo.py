cor = str(input("Digite uma cor ")).lower().strip() 
#A expressão ".lower()" converte a entrada de texto do usuário em minúsculo
#A expressão ".strip()" remove a entrada de espaços do texto que estão antes dos dados.  

if cor == 'vermelho':
    print("PARE")
elif cor == 'verde':
    print("ACELERAR")
elif cor == 'amarelo':
    print("Atenção")
else:
    print("Cor inválida")