texto = input("Insira um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper(),end="") # retorna e converte as vogais encontradas no texto
else:
    print()



# # Exemplo utilizando a função built-in range
# for numero in range(0,51,5): #inicia no 0 até 51, de 5 em 5, inicio,fim, contagem
#     print(numero, end=" ")