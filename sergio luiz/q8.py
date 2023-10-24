# Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

if produto1 <= produto2 and produto1 <= produto3:
    print (f"O produto 1 seria a oferta mais batara, R${produto1:,.2f}")  #O ":,.2f" formato de duas
                                                                          #casas decimais e com ponto e vírgula 
elif produto2 <= produto3:
    print (f"O produto 2 seria a oferta mais batara, R${produto2:,.2f}")
else:
    print (f"O produto 3 seria a oferta mais batara, R${produto3:,.2f}")