# Problema da Mochila 0/1 com Algoritmo Genético

**Equipe:** Filipe Orlamünder, Guilherme Melato, Lucas M Venero.

## Descrição

Este trabalho implementa o Algoritmo Genético para resolver o Problema da Mochila 0/1, modelando indivíduos como vetores binários e aplicando operadores de seleção, crossover e mutação.

## Funcionamento

1. População inicial gerada aleatoriamente
2. Avaliação por função de aptidão com penalização por excesso de peso
3. Seleção por torneio
4. Crossover de um ponto
5. Mutação probabilística
6. Evolução ao longo de gerações

## Exemplo de Entrada

- pesos = [2, 3, 4, 5]
- valores = [3, 4, 5, 6]
- capacidade = 5

**Saída esperada:**

- vetor binário: [1, 1, 0, 0]
- valor total: 7

## Dificuldades

- Ajuste da taxa de mutação para evitar convergência prematura
- Controle de soluções inválidas (peso > capacidade)
- Performance em problemas com muitos itens

## Aprendizados

- Aplicação prática de algoritmos evolucionários
- Importância do balanceamento entre exploração e exploração
- Técnicas de otimização combinatória
