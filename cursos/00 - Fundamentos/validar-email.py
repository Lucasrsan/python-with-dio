email = input("Insira o email: ").strip()

#Verifica se o "@" esta presente no email e suas outras outras condições
if (
    "@" in email and
    not email.startswith("@") and
    not email.endswith("@") and
    " " not in email
):
    print("E-mail válido")
else:
    print("E-mail inválido")
