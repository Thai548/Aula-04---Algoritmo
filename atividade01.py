valor = int(input('Valor da Compra: '))

if valor > 250:
    desconto = valor * 0.16
    valor_final= valor - desconto
    print (f'Valor do Desconto: {desconto}')
    print (f'Valor a pagar: {valor_final}')
else:
    print(f'Valor a pagar sem desconto: {valor} ')

