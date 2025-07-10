# Criando uma lista em python
lista_tarefas = [
    "Estudar Python das 14h às 16h",
    "Fazer o planejamento para a próxima semana",
    "Pagar conta da luz (urgente)"
    "Realizar compras no supermercado",
]

primeira_tarefa = lista_tarefas[0]
print(primeira_tarefa)

inicio_horario = primeira_tarefa.rfind("das")
print(inicio_horario)

horario = primeira_tarefa[inicio_horario:]
