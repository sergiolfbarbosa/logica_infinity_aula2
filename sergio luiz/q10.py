# Faça um Programa que pergunte em que turno você estuda. 
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

escolha = str(input("Digite M-Matutino ou V-Vespertino ou N- Noturno.\nEm que turno você estuda? ")).lower()

if escolha == 'm':
    print("Bom dia!")
elif escolha == 'v':
    print("Boa tarde!")
elif escolha == 'n':
    print("Boa noite!")
elif escolha != ('m, v, n'):
    print("Valor inválido")