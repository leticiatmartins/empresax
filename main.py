from departamentos import inserir_departamentos
from empregado import inserir_empregados, update_empregados
from vendas import inserir_produto, update_produto

""""
menu antigo

escolha = input('Comando: ')
if escolha.lower().strip() == 'departamentos':
    inserir_departamentos()
elif escolha.lower().strip()=='empregados':
    inserir_empregados()
elif escolha.lower().strip()=='update_empregados':
    update_empregados()
elif escolha.lower().strip()=='vendas':
    inserir_produto()
elif escolha.lower().strip()=='update_produto':
    update_produto()
"""

def menu ():
    print("Menu de opções:")
    print("1. Inserir empregados")
    print("2. Inserir departamentos")
    print("3. Inserir produto (vendas)")
    print("4. Atualizar empregados")
    print("5. Atualizar produto (vendas)")
    print("6. Sair")

    opcoes = {
        "1": inserir_empregados,
        "2": inserir_departamentos,
        "3": inserir_produto,
        "4": update_empregados,
        "5": update_produto}

    while True:
        menu()
        escolha = input("\nEscolha o comando (1-6): ").strip()

        if escolha == "6":
            print("Saindo do programa...")
            break
        elif escolha in opcoes:
            opcoes[escolha]()  
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    menu()