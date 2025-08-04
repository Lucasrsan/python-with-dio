with open("cursos/05 - Manipulação de Arquivos/lista_tarefas.txt", "w") as arquivo:
    arquivo.write("- Ir ao mercado fazer compras\n") # O \n para pular para a próxima linha
    arquivo.write("- Fazer planejamento semanal\n")
    arquivo.write("- Anotar aniversário de fulano de tal\n")


print("Tarefas adicionadas.") # caso não exista o arquivo é criado.