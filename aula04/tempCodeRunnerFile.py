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
