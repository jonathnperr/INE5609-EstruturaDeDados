from no import No

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0
        self.__cursor = None

    @property
    def primeiro(self):
        return self.__primeiro

    @property
    def ultimo(self): 
        return self.__ultimo
    
    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def cursor(self):
        return self.__cursor

    def acessarAtual(self):
        if self.__cursor is not None:
            return self.__cursor.dado
        
    def inserirAntesDoAtual(self, elemento):
        if self.__cursor is not None:
            no = No(elemento)

            if self.__cursor.ant is not None:
                self.__cursor.ant.prox = no
                no.ant = self.__cursor.ant
            else:
                self.__primeiro = no
                
            no.prox = self.__cursor
            self.__cursor.ant = no
            self.__tamanho += 1
            
    def inserirAposAtual(self, elemento):
        if self.__cursor is not None:
            no = No(elemento)
            
            if self.__cursor.prox is not None:
                self.__cursor.prox.ant = no
                no.prox = self.__cursor.prox
            else:
                self.__ultimo = no

            no.ant = self.__cursor
            self.__cursor.prox = no
            self.__tamanho += 1
            
    def inserirComoUltimo(self, elemento):
        no = No(elemento)
        
        if self.__ultimo is not None:
            self.__ultimo.prox = no
            no.ant = self.__ultimo
        else:
            self.__primeiro = no
            
        self.__ultimo = no
        self.__tamanho += 1
        
    def inserirComoPrimeiro(self, elemento):
        no = No(elemento)
        
        if self.__primeiro is not None:
            self.__primeiro.ant = no
            no.prox = self.__primeiro
        else:
            self.__ultimo = no
        
        self.__primeiro = no
        self.__tamanho += 1
        
    def inserirNaPosicao(self, k, novo):
        if k < 1 or k > self.__tamanho:
            raise ValueError("Posição inválida")
        
        if k == 1:
            self.inserirComoPrimeiro(novo)
        elif k == self.__tamanho + 1:
            self.inserirComoUltimo(novo)
        else:
            no = No(novo)
            atual = self.__primeiro
            
            for i in range(1, k - 1):
                atual = atual.prox
            
            no.anterior = atual
            no.prox = atual.prox
            
            if atual.prox is not None:
                atual.prox.anterior = no
            
            atual.prox = no
            self.__tamanho += 1
            
    def excluirAtual(self):
        
        if self.vazia():
            return

        if self.__primeiro is self.__ultimo:
            self.reset()
            return

        if self.__cursor == self.__ultimo:
            self.excluirUlt()
            return

        if self.__cursor == self.__primeiro:
            self.excluirPrim()
            return

        if (self.__cursor.prox is not None) and (self.__cursor.ant is not None):
            prox = self.__cursor.prox
            ant = self.__cursor.ant
            
            self.__cursor = self.__cursor.ant
            self.__cursor.prox = prox
            
            self.avancarKPosicoes(1)
            self.__cursor.ant = ant
            
            self.__tamanho -= 1
            return
        
    def excluirPrim(self):
        if self.vazia():
            return

        if self.__primeiro is self.__ultimo:
            self.reset()
            return
        else:
            if self.__cursor == self.__primeiro:
                self.avancarKPosicoes(1)
                
            self.__primeiro = self.__primeiro.prox
            self.__primeiro.ant = None
            self.__tamanho -= 1
            return  
        
    def excluirUlt(self):
        if self.vazia():
            return

        if self.__ultimo is self.__primeiro:
            self.reset()
            return

        else:
            if self.__cursor == self.__ultimo:
                self.retrocederKPosicoes(1)
                
            self.__ultimo = self.__ultimo.ant
            self.__primeiro.ant = None
            self.__tamanho -= 1
            return
        
    def excluirElem(self, chave):
        if (chave is None) or (self.vazia()):
            return

        tempCursor = self.__cursor 
        self.irParaPrimeiro()
        
        for i in range(self.__tamanho):
            if str(chave) == str(self.__cursor.dado):
                self.excluirAtual()
                break
            self.avancarKPosicoes(1)

        self.__cursor = tempCursor
        return
    
    def excluirDaPos(self, posicao):
        if (0 > posicao) or (posicao is None) or self.vazia():
            return

        tempCursor = self.__cursor
        self.irParaPrimeiro()
        
        if posicao <= (self.__tamanho - 1):
            self.avancarKPosicoes(posicao)
            self.excluirAtual()

        self.__cursor = tempCursor
        return
    
    
    
    def Buscar(self,chave):
        
        if (chave is None) or self.vazia():
            return False

        tempCursor = self.__cursor
        self.irParaPrimeiro()
        
        for i in range(self.__tamanho):
            if str(chave) == str(self.__cursor.dado):
                retorno = self.cursor.dado
                self.__cursor = tempCursor
                return retorno
            self.avancarKPosicoes(1)
            
        self.__cursor = tempCursor
        return None
    
    def avancarKPosicoes(self, k):
        
        if not self.__cursor:
            return

        for i in range(k):
            if not self.__cursor.prox:
                break
            self.__cursor = self.__cursor.prox
            
    def retrocederKPosicoes(self, k):
        
        if not self.__cursor:
            return

        for i in range(k):
            if not self.__cursor.ant:
                break
            self.__cursor = self.__cursor.ant
            
    def irParaPrimeiro(self):
        self.__cursor = self.__primeiro
        
    def irParaUltimo(self):
        self.__cursor = self.__ultimo
        
    def vazia(self):
        if self.__tamanho == 0:
            return True
        else:
            return False
        
    def posicao(self, chave):
        
        if (chave is None) or (self.vazia()):
            return

        tempCursor = self.__cursor
        self.irParaPrimeiro()
        
        for i in range(self.__tamanho):
            if str(chave) == str(self.__cursor.dado):
                self.__cursor = tempCursor
                return i
            self.avancarKPosicoes(1)

        self.__cursor = tempCursor
        return

    def reset(self):
        
        self.__cursor = None
        self.__ultimo = None
        self.__primeiro = None
        self.__tamanho = 0
        
        return
    
    def listar(self):
        for i in range(self.tamanho):
            print(
                f"Pos. {i}: {self.acessarAtual()}",
                f"Anterior: {self.cursor.ant.dado if self.cursor.ant is not None else '-'}",
                f"Próximo: {self.cursor.prox.dado if self.cursor.prox is not None else '-'}")
            self.avancarKPosicoes(1)
