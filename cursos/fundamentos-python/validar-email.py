email = input().strip()

if (
    "@" in email and
    not email.startswith("@") and
    not email.endswith("@") and
    " " not in email
):
    print("E-mail válido")
else:
    print("E-mail inválido")
