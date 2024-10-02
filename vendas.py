import psycopg2

try: 
    conn = psycopg2.connect(
        dbname = 'empresax',
        user = 'postgres',
        host = 'localhost',
        port = '5432'
    )
except:
    print('Falha ao conectar no Banco de Dados.')
    exit
    
cursor = conn.cursor()

while True:
    produto = input('Digite o Produto: (ou "sair" para sair) ')
    if produto.lower().strip() == 'sair':
        break

    # LIDANDO COM EXCEÇÕES
    # No Python usamos o `try`, `except` e `finally`  para capturar exceções e tratá-las
    # Veja o exemplo abaixo
    try:
         quantidade = int(input('Informe a quantidade: '))
         valor_unitario = float(input('Informe o valor unitário: '))
    except:
        print('> O valor informado é inválido.')
        continue

    cursor.execute('insert into vendas(produto, quantidade, valor_unitario) values(%s, %s, %s)', (produto, quantidade, valor_unitario))
    
    conn.commit()
    print('> Cadastro realizado com sucesso.')

conn.close()
print('Fim')


