import psycopg2

conn = psycopg2.connect(
    dbname = 'empresax',
    user = 'postgres',
    host = 'localhost',
    port = '5432'
)

cursor = conn.cursor()



while True:
    nome = input('Digite o nome do departamento: (ou "sair" para sair) ')
    if nome.lower().strip() == 'sair':
        break
    sigla = input('Informe a sigla: ')

    cursor.execute(
        'insert into departamentos(nome_departamento, sigla) values(%s, %s)', (nome, sigla)
    )
    conn.commit()

conn.close()
print('Fim')


