from produto import Produto
from lista_invertida import ListaInvertida
from view import View

class Sistema:
    def __init__(self):
        self.indice = ListaInvertida()

    def menu(self):
        while True:
            View.mostrar_menu()
            opcao = View.obter_opcao()

            if opcao == "1":
                self.carga_dados()
            elif opcao == "2":
                self.incluir_produto()
            elif opcao == "3":
                self.buscar_por_id()
            elif opcao == "4":
                self.buscar_simples()
            elif opcao == "5":
                self.buscar_composta()
            elif opcao == "6":
                self.remover_produto()
            elif opcao == "7":
                self.exibir_todos()
            elif opcao == "8":
                View.exibir_mensagem("Saindo do sistema... Até logo!")
                break
            else:
                View.exibir_mensagem("Opção inválida! Tente novamente.")

    def carga_dados(self):
        produtos = [
            # Produtos de Vôlei
            Produto("1", "Bola de Vôlei", "Nike", "Vôlei", 150.0),
            Produto("2", "Bola de Vôlei", "Mizuno", "Vôlei", 140.0),
            Produto("3", "Bola de Vôlei", "Wilson", "Vôlei", 130.0),
            Produto("4", "Bola de Vôlei", "Nike", "Vôlei", 160.0),
            Produto("5", "Bola de Vôlei", "Puma", "Vôlei", 145.0),

            # Produtos de Basquete
            Produto("6", "Bola de Basquete", "Nike", "Basquete", 200.0),
            Produto("7", "Bola de Basquete", "Adidas", "Basquete", 190.0),
            Produto("8", "Bola de Basquete", "Spalding", "Basquete", 220.0),
            Produto("9", "Bola de Basquete", "Nike", "Basquete", 210.0),
            Produto("10", "Bola de Basquete", "Wilson", "Basquete", 180.0),

            # Produtos de Natação
            Produto("11", "Óculos de Natação", "Speedo", "Natação", 80.0),
            Produto("12", "Touca de Natação", "Speedo", "Natação", 30.0),
            Produto("13", "Máscara de Natação", "Arena", "Natação", 50.0),
            Produto("14", "Pala de Natação", "Mizuno", "Natação", 70.0),
            Produto("15", "Nadadeira", "Arena", "Natação", 100.0),

            # Produtos de Corrida
            Produto("16", "Tênis de Corrida", "Nike", "Corrida", 450.0),
            Produto("17", "Tênis de Corrida", "Asics", "Corrida", 500.0),
            Produto("18", "Tênis de Corrida", "Adidas", "Corrida", 400.0),
            Produto("19", "Tênis de Corrida", "Puma", "Corrida", 350.0),
            Produto("20", "Tênis de Corrida", "Nike", "Corrida", 380.0),

            # Produtos de Handebol
            Produto("21", "Bola de Handebol", "Kipsta", "Handebol", 120.0),
            Produto("22", "Bola de Handebol", "Molten", "Handebol", 130.0),
            Produto("23", "Bola de Handebol", "Nike", "Handebol", 140.0),
            Produto("24", "Bola de Handebol", "Adidas", "Handebol", 125.0),
            Produto("25", "Bola de Handebol", "Umbro", "Handebol", 110.0),

            # Produtos de Futebol
            Produto("26", "Bola de Futebol", "Nike", "Futebol", 120.0),
            Produto("27", "Bola de Futebol", "Adidas", "Futebol", 130.0),
            Produto("28", "Bola de Futebol", "Puma", "Futebol", 140.0),
            Produto("29", "Bola de Futebol", "Nike", "Futebol", 150.0),
            Produto("30", "Bola de Futebol", "Adidas", "Futebol", 160.0),
        ]
        for produto in produtos:
            self.indice.adicionar(produto)
        View.exibir_mensagem("Dados carregados com sucesso!")

    def incluir_produto(self):
        View.exibir_mensagem("Preencha os dados do novo produto:")
        id = input("ID do produto: ")
        nome = input("Nome do produto: ")
        marca = input("Marca: ")
        esporte = input("Esporte: ")
        preco = float(input("Preço: "))
        produto = Produto(id, nome, marca, esporte, preco)
        self.indice.adicionar(produto)
        View.exibir_mensagem("Produto incluído com sucesso!")

    def buscar_por_id(self):
        id = input("Digite o ID do produto: ")
        produto = self.indice.produtos.get(id)
        if produto:
            View.exibir_mensagem("Produto encontrado:")
            View.exibir_produto(produto)
        else:
            View.exibir_mensagem("Produto não encontrado!")

    def buscar_simples(self):
        campo = input("Campo [nome/marca/esporte/preco]: ")
        valor = input("Valor para busca (Confira maiúscula/minúscula): ")
        resultado = self.indice.buscar_simples(campo, valor)
        View.listar_produtos([self.indice.produtos.get(id) for id in resultado])

    def buscar_composta(self):
        View.exibir_mensagem("Busca composta: Defina dois critérios de busca.")

        # primeiro
        campo1 = input("Primeiro campo (nome/marca/esporte/preco): ")
        if campo1 == 'preco':
            minimo1 = float(input("Preço mínimo: "))
            maximo1 = float(input("Preço máximo: "))
            valor1 = (minimo1, maximo1)
        else:
            valor1 = input("Valor para o primeiro campo (Confira maiúscula/minúscula): ")

        # segundo
        campo2 = input("Segundo campo (nome/marca/esporte/preco): ")
        if campo2 == 'preco':
            minimo2 = float(input("Preço mínimo: "))
            maximo2 = float(input("Preço máximo: "))
            valor2 = (minimo2, maximo2)
        else:
            valor2 = input("Valor para o segundo campo (Confira maiúscula/minúscula): ")

        # filtra resultados para o primeiro critério
        if campo1 == 'preco':
            resultados1 = self.indice.buscar_intervalo_preco(valor1[0], valor1[1])
        else:
            resultados1 = self.indice.buscar_simples(campo1, valor1)

        # filtrar os resultados do primeiro critério pelo segundo critério
        resultados_finais = set()
        for id in resultados1:
            produto = self.indice.produtos.get(id)
            if produto:
                if campo2 == 'preco':
                    if valor2[0] <= produto.preco <= valor2[1]:
                        resultados_finais.add(id)
                else:
                    if getattr(produto, campo2) == valor2:
                        resultados_finais.add(id)

        # exibir resultados finais
        View.listar_produtos([self.indice.produtos.get(id) for id in resultados_finais])

    def remover_produto(self):
        id = input("ID do produto a ser removido: ")
        self.indice.remover(id)
        View.exibir_mensagem("Produto removido com sucesso!")

    def exibir_todos(self):
        View.listar_produtos(self.indice.produtos.values())

if __name__ == "__main__":
    sistema = Sistema()
    sistema.menu()
