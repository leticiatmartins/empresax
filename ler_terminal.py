while True:
    nome = input('Digite o seu nome: (ou "sair" para sair) ')
    if nome.lower().strip() == 'sair':
        break
    salario = float(input('Informe o salário: '))
    print(nome, salario)
    print(type(salario))

print('Fim')