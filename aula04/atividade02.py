


valor = int(input('Valor da Compra: '))
forma_de_pagamento = input ('Qual a forma de pagamento? ').lower()
if valor > 250 and forma_de_pagamento == "à vista":
    desconto = valor * 0.16
    valor_final= valor - desconto
    print (f'Valor do Desconto: {desconto}')
    print (f'Valor a pagar: {valor_final}')
else:
    print(f'Valor a pagar sem desconto: {valor} ')

