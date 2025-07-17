# Execitando conceitos de Orientação ao Objeto em Python [Classes e Objetos]

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def aplicar_desconto(self, percentual):
        # Calcular o valor do desconto usando o percentual recebido.
        valor_desconto = self.preco * (percentual / 100)

        # Atualizar o preço DESTE objeto.
        self.preco -= valor_desconto

        # Imprimir uma mensagem formatando o novo preço.
        print(f"Desconto de {percentual}% aplicado! Novo preço: R$ {self.preco:.2f}")
        
        
# Criando duas instâncias (objetos) da classe Produto
notebook = Produto(nome="Notebook Gamer", preco=3500.00, categoria="Eletrônicos")
livro = Produto(nome="Python para Leigos", preco=80.00, categoria="Livros")

print(f"--- Testando o {notebook.nome} ---")
# Imprimindo o preço inicial
print(f"Preço inicial: R$ {notebook.preco:.2f}")

# Aplicando o desconto de 15%
notebook.aplicar_desconto(15)
        