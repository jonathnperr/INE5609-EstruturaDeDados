from ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()
    
print("=== Teste de inserção ===")
# Inserindo elementos
lista.inserirComoPrimeiro(10)
lista.inserirComoUltimo(20)
lista.inserirComoUltimo(30)
lista.inserirComoUltimo(40)

# Listando elementos
print("Lista após inserções (esperado: 10 -> 20 -> 30 -> 40):")
lista.irParaPrimeiro()
lista.listar()

print("\n=== Teste de inserção antes e depois do cursor ===")
# Posicionando o cursor no segundo elemento e inserindo antes e depois
lista.irParaPrimeiro()
lista.avancarKPosicoes(1)  
lista.inserirAntesDoAtual(15)  
lista.inserirAposAtual(25)    

# Listando elementos
print("Lista após inserir 15 antes de 20 e 25 após 20 (esperado: 10 -> 15 -> 20 -> 25 -> 30 -> 40):")
lista.irParaPrimeiro()
lista.listar()

print("\n=== Teste de exclusão de elementos ===")
# Removendo o primeiro, último e um elemento do meio
lista.excluirPrim()   
lista.excluirUlt()    
lista.irParaPrimeiro()
lista.avancarKPosicoes(2)  
lista.excluirAtual()  

# Listando elementos
print("Lista após exclusões (esperado: 15 -> 20 -> 30):")
lista.irParaPrimeiro()
lista.listar()

print("\n=== Teste de busca de elementos ===")
# Buscando por elementos
encontrado = lista.Buscar(20)
print(f"Elemento 20 {'encontrado' if encontrado is not None else 'não encontrado'} (esperado: encontrado)")

nao_encontrado = lista.Buscar(100)
print(f"Elemento 100 {'encontrado' if nao_encontrado is not None else 'não encontrado'} (esperado: não encontrado)")
