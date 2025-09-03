class DiretorioContínuo:
    def __init__(self):
        self.diretorio = {}

    def adicionar(self, chave, id_produto):
        """adiciona um produto ao diretorio para uma chave de preço especifica"""
        if chave not in self.diretorio:
            self.diretorio[chave] = set()
        self.diretorio[chave].add(id_produto)

    def buscar(self, chave):
        """busca os produtos associados a uma chave especifica (preço) """
        return self.diretorio.get(chave, set())

    def remover(self, chave, id_produto):
        """remov um produto do diretorio para uma chave especifica (preço)"""
        if chave in self.diretorio:
            self.diretorio[chave].remove(id_produto)
            if not self.diretorio[chave]:
                del self.diretorio[chave]

    def buscar_intervalo(self, minimo, maximo):
        """ busca por produtos dentro de um intervalo de preços"""
        resultado = set()
        for preco, ids in self.diretorio.items():
            if minimo <= preco <= maximo:
                resultado.update(ids)
        return resultado
