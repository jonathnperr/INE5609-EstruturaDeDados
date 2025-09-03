# INE5609 - Estruturas de Dados

## ℹ️ Sobre o Repositório
Repositório contendo os trabalhos desenvolvidos para a disciplina **INE5609 - Estruturas de Dados** da Universidade Federal de Santa Catarina (UFSC). Contém implementações de estruturas de dados clássicas com aplicações práticas.

## 🎯 Objetivo da Disciplina
Capacitar o estudante a compreender, do ponto de vista da utilização e da representação computacional, e a construir as estruturas de dados e algoritmos de busca e ordenação clássicos a partir da perspectiva orientada a objetos.

## 📚 Conteúdo Programático

### Módulos Abordados:
- **Estruturas Lineares**: Pilhas, Filas, Listas
- **Tabelas de Espalhamento (Hashing)**: Funções hash, tratamento de colisões
- **Árvores**: Árvores binárias de busca, árvores balanceadas, árvores B e B+
- **Grafos**: Noções básicas, representações computacionais
- **Métodos de Pesquisa e Ordenação**: Análise de complexidade
- **Organização de Arquivos**: Acesso sequencial, direto e indexado

## 📋 Trabalhos Desenvolvidos

### Trabalho 1 - Lista Duplamente Encadeada com Cursor

#### 📁 Estrutura de Arquivos:
```
├── ListaDuplamenteEncadeada.py  # Implementação da lista duplamente encadeada
├── no.py                        # Classe Nó para a lista
├── main.py                      # Programa de demonstração
└── T1 - Jonathan Pereira.pdf    # Relatório do trabalho
```

#### 🔧 Funcionalidades Implementadas:
- **Operações Públicas**:
  - `acessarAtual()` - Retorna o elemento atual
  - `inserirAntesDoAtual(novo)` - Insere antes do cursor
  - `inserirAposAtual(novo)` - Insere após o cursor
  - `inserirComoUltimo(novo)` - Insere no final
  - `inserirComoPrimeiro(novo)` - Insere no início
  - `inserirNaPosicao(k, novo)` - Insere na posição k
  - `excluirAtual()` - Remove o elemento atual
  - `excluirPrim()` - Remove o primeiro elemento
  - `excluirUlt()` - Remove o último elemento
  - `excluirElem(chave)` - Remove por chave
  - `excluirDaPos(k)` - Remove da posição k
  - `buscar(chave)` - Busca elemento por chave

- **Controle do Cursor**:
  - `avancarKPosicoes(K)` - Avança K posições
  - `retrocederKPosicoes(K)` - Retrocede K posições
  - `irParaPrimeiro()` - Posiciona no primeiro elemento
  - `irParaUltimo()` - Posiciona no último elemento

- **Operações de Apoio**:
  - `vazia()` - Verifica se a lista está vazia
  - `posicaoDe(chave)` - Retorna posição da chave
  - `listar()` - Exibe todos os elementos

### Trabalho 2 - Sistema de Indexação com Lista Invertida

#### 📁 Estrutura de Arquivos:
```
├── diretorio_continuo.py       # Diretório para dados contínuos (preços)
├── diretorio_discreto.py       # Diretório para dados discretos
├── lista_invertida.py          # Sistema principal de indexação
├── produto.py                  # Classe Produto
├── view.py                     # Interface de usuário
└── main.py                     # Programa principal
```

#### 🎯 Aplicação: Sistema de Produtos Esportivos "Sports//UFSC"

#### 🔧 Funcionalidades Implementadas:
- **Estrutura de Dados**:
  - Classe `Produto` com campos: ID, nome, marca, esporte, preço
  - Sistema de indexação com lista invertida
  - 3 diretórios de indexação (1 contínuo, 2 discretos)

- **Operações do Sistema**:
  - Carga inicial de dados (30 produtos pré-cadastrados)
  - Inclusão de novos produtos
  - Busca por ID
  - Busca simples por campo (nome, marca, esporte, preço)
  - Busca composta (combinação de dois critérios)
  - Remoção de produtos
  - Exibição de todos os produtos

- **Diretórios Implementados**:
  - **Contínuo**: Preço (com busca por intervalo)
  - **Discretos**: Nome, Marca, Esporte

## 👨‍💻 Como Executar

### Trabalho 1 - Lista Duplamente Encadeada
```bash
python main.py
```

### Trabalho 2 - Sistema de Indexação
```bash
python main.py
```

## 📖 Conceitos de Estruturas de Dados Aplicados
- **Listas encadeadas**: Implementação completa com cursor
- **Indexação**: Lista invertida com múltiplos diretórios
- **Busca e recuperação**: Algoritmos de busca simples e composta
- **Complexidade**: Análise de operações de inserção, remoção e busca
- **Modularização**: Design orientado a objetos com separação de responsabilidades

## 👨‍🏫 Disciplina
**INE5609 - Estruturas de Dados**  
Universidade Federal de Santa Catarina - Centro Tecnológico  
Departamento de Informática e Estatística

### Professor
José Eduardo de Lucca (jose.lucca@ufsc.br)

### Aluno
Jonathan Moraes Pereira (23205205)

*Trabalhos acadêmicos desenvolvidos para fins educacionais - UFSC 2024*
