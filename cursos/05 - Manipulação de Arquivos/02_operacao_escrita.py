file = open(r"C:\python-with-dio\cursos\05 - Manipulação de Arquivos\teste.txt", "w")
file.write("Escrevendo dados em um outro arquivo.")
file.writelines(["\nEscrevendo ","um novo ", "texto."])
file.close()
