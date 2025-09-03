class View:
    @staticmethod
    def mostrar_menu():
        print("\n" + "=" * 50)
        print("\t\t  Sports//UFSC")
        print("=" * 50)
        print("Selecione uma opção:")
        print("1. • Carga de dados")
        print("2. • Incluir novo produto")
        print("3. • Buscar produto por ID")
        print("4. • Busca simples")
        print("5. • Busca composta")
        print("6. • Remover produto")
        print("7. • Exibir todos os produtos")
        print("8. • Sair")
        print("=" * 50)

    @staticmethod
    def obter_opcao():
        return input("\nEscolha uma opção: ")

    @staticmethod
    def exibir_produto(produto):
        print("\n" + "-" * 40)
        print(f"ID: {produto.id}")
        print(f"Nome: {produto.nome}")
        print(f"Marca: {produto.marca}")
        print(f"Esporte: {produto.esporte}")
        print(f"Preço: R${produto.preco:.2f}")
        print("-" * 40)

    @staticmethod
    def exibir_mensagem(mensagem):
        print(f"\n{mensagem}")

    @staticmethod
    def listar_produtos(produtos):
        if not produtos:
            print("\nNenhum produto encontrado.")
        else:
            print("\nProdutos encontrados:")
            for produto in produtos:
                View.exibir_produto(produto)
