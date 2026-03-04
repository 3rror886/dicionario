#""

produtos = []

while True:

    produto = {
        "nome": input("digite o produto: "),
        "preco": input("qual o preço: "),
        "estoque": input("digite o estoque do produto: "),
        "categoria": input("digite a categoria: ")
    }

    print(produtos)
    print()

    for produto in produtos:
        print(f"o produto é {produto["nome"]}, e o preço é {produto["preço"]}")

        produtos.append(produto)

    print(produto)

    print(f"produto ofertado {produto["nome"]} ")
    print(f"preço do produto {produto["preco"]} ")
    print()

    pergunta = input("deseja digitar mais um produto: ")

    if pergunta != "S":
        print("Ok")
    else:
        print("Bye")
        break