import psycopg2

def inserir_produto(): 
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

if __name__ == '__main__':
    inserir_produto()

def update_produto():
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
        emp_id = input('Digite o ID do produto que deseja atualizar: (ou "sair" para sair) ')
        if emp_id.lower().strip() == 'sair':
            break
        novo_produto = input('Digite o novo nome: ')

        try:
            nova_quantidade = float(input('Informe o nova quantidade de produto: '))
            novo_valor = float(input('Informe o novo valor unita do produto: '))
        except:
            print('> O valor informado é inválido.')
            continue
        cursor.execute('UPDATE vendas SET produto = %s, quantidade = %s, valor_unitario = %s  WHERE id = %s', (novo_produto, nova_quantidade, novo_valor, emp_id))
        
        conn.commit()
        print('> Cadastro realizado com sucesso.')

    conn.close()
    print('Fim')

if __name__ == '__main__':
    update_produto()

