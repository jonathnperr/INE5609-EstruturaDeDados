class DiretorioDiscreto:
    def __init__(self):
        self.diretorio = {}

    def adicionar(self, chave, id_produto):
        """adiciona um produto ao diretorio para uma chave especifica"""
        if chave not in self.diretorio:
            self.diretorio[chave] = set()
        self.diretorio[chave].add(id_produto)

    def buscar(self, chave):
        """busca os produtos associados a uma chave especifica"""
        return self.diretorio.get(chave, set())

    def remover(self, chave, id_produto):
        """remove um produto do diretorio para uma chave especifica"""
        if chave in self.diretorio:
            self.diretorio[chave].remove(id_produto)
            if not self.diretorio[chave]:
                del self.diretorio[chave]
