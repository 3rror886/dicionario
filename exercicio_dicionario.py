#""

produto1 = {
    "nome": input("digite o produto: "),
    "preco": input("qual o preço: "),
    "estoque": input("digite o estoque do produto: "),
    "categoria": input("digite a categoria: ")
}

print(produto1)

print(f"produto ofertado {produto1["nome"]} ")
print(f"preço do produto{produto1["preco"]} ")
print()

produtos = [
    {"nome": "Pc", "preço": 1599},
    {"nome": "Mouse Gamer", "preço": 200},
    {"nome": "Teclado Gamer", "preço": 450}, 
    {"nome": "Monitor Full HD", "preço": 550}
]

print(produtos)
print()

for produto in produtos:
    print(f"o produto é {produto["nome"]}, e o preço é {produto["preço"]}")



