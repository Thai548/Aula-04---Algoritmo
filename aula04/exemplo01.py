# Estrutura If
idade = int(input('Insira a idade:  '))

# idade = 18

if idade >= 18:
    print('Você é Adulto')

else:
    print("Você não é Adulto")

#--------------------------------------------------------------------#   (*Elif : Se não,se)   (*else não recebe condições para análise)
    
pontos = int(input('Informe os pontos:  '))

if pontos >= 100:
    print('Excelente')

elif pontos >= 50:
    print('Bom Desempenho')

elif pontos >= 25:
    print ('Satisfatório')

else:
    print('Pratique mais...')

#-------------------------------------------------------------------------#
    # Operadores AND E OR

usuario = input ('Nome: ')
senha = input ('Senha: ')

if usuario == 'admin' and senha == '1234':
    print ('Login realizado com sucesso')

else:
    print ('USUÁRIO OU SENHA INCORRETO')


# IF ENCADIADO 

nota= float(input('Informe a nota do Aluno:  '))
    
if nota >= 9:
    print('A')
elif nota >= 7:
    print('B')
elif nota >= 5:
    print('C')
elif nota >= 3:
    print('D')
else:
    print('E')



#  IF Aninhados
    
nota = float (input('Informe a nota od aluno'))
frequencia = float (input('Informe a frequencia'))

if nota >= 7:
    # Aprovado por nota, mas precisa chegar a frequência
    if frequencia >= 75:
        print('Aluno aprovado por nota e frequência')
    else:
        print('Reprovado por frequência baixa')
else:
    print('Reprovado por nota baixa.')
