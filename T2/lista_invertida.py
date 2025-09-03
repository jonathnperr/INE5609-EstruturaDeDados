from diretorio_continuo import DiretorioContínuo
from diretorio_discreto import DiretorioDiscreto

class ListaInvertida:
    def __init__(self):
        self.nome_indice = DiretorioDiscreto() 
        self.marca_indice = DiretorioDiscreto() 
        self.esporte_indice = DiretorioDiscreto()  
        self.preco_indice = DiretorioContínuo()  
        self.produtos = {}

    def adicionar(self, p):
        self.produtos[p.id] = p

        self.nome_indice.adicionar(p.nome, p.id)
        self.marca_indice.adicionar(p.marca, p.id)
        self.esporte_indice.adicionar(p.esporte, p.id)
        self.preco_indice.adicionar(p.preco, p.id)

    def remover(self, id):
        if id in self.produtos:
            p = self.produtos[id]
            del self.produtos[id]

            self.nome_indice.remover(p.nome, id)
            self.marca_indice.remover(p.marca, id)
            self.esporte_indice.remover(p.esporte, id)
            self.preco_indice.remover(p.preco, id)

    def buscar_simples(self, campo, valor):
        if campo == 'nome':
            return self.nome_indice.buscar(valor)
        elif campo == 'marca':
            return self.marca_indice.buscar(valor)
        elif campo == 'esporte':
            return self.esporte_indice.buscar(valor)
        elif campo == 'preco':
            return self.preco_indice.buscar(valor)

    def buscar_intervalo_preco(self, minimo, maximo):
        return self.preco_indice.buscar_intervalo(minimo, maximo)

    def buscar_composta(self, campo1, valor1, campo2, valor2):
        if campo1 == 'preco' and isinstance(valor1, tuple):
            resultado1 = self.buscar_intervalo_preco(valor1[0], valor1[1])
        else:
            resultado1 = self.buscar_simples(campo1, valor1)

        if campo2 == 'preco' and isinstance(valor2, tuple):
            resultado2 = self.buscar_intervalo_preco(valor2[0], valor2[1])
        else:
            resultado2 = self.buscar_simples(campo2, valor2)

        return resultado1.intersection(resultado2)
