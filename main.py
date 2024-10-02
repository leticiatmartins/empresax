from departamentos import inserir_departamentos
from empregado import inserir_empregados

escolha = input('Comando: ')
if escolha.lower().strip() == 'departamentos':
    inserir_departamentos()
elif escolha.lower().strip()=='empregados':
    inserir_empregados()
