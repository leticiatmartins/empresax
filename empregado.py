import psycopg2

def inserir_empregados():
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
        nome = input('Digite o nome do empregado: (ou "sair" para sair) ')
        if nome.lower().strip() == 'sair':
            break

        # LIDANDO COM EXCEÇÕES
        # No Python usamos o `try`, `except` e `finally`  para capturar exceções e tratá-las
        # Veja o exemplo abaixo
        try:
            salario = float(input('Informe o salário: '))
        except:
            print('> O valor do salário informado é inválido.')
            continue

        cursor.execute('insert into empregados(nome, salario) values(%s, %s)', (nome, salario))
        
        conn.commit()
        print('> Cadastro realizado com sucesso.')

    conn.close()
    print('Fim')

if __name__ == '__main__':
    inserir_empregados()


# TODO: Criar uma função modificar_empregado() que pergunte id do empregado, nome e salário e altere a linha da tabela com esse id
# DICA: Comando SQL: update empregados set nome = 'Flambo Framboesa Winston Martins', salario=15000 where id = 12;
