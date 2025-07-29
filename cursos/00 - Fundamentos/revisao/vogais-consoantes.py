frase = input("Insira uma frase: ").lower()
vogais = "aeiou"
numero_vogais = 0
numero_consoantes = 0
for letra in frase:
    if letra in vogais:
        print(f"vogal: {letra}")
        numero_vogais = numero_vogais + 1
    else:
        print(f"consoante: {letra}")
        numero_consoantes = numero_consoantes + 1
        
print(f"{numero_vogais} vogais encontrada.\n{numero_consoantes} consoantes encontrada.")