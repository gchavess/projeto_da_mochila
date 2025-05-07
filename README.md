# Problema da Mochila 0/1 com Algoritmo Genético

**Equipe:** Filipe Orlamünder, Guilherme Melato, Lucas M Venero.

---

## 🎯 Objetivo Geral

O principal objetivo deste trabalho é aplicar um algoritmo bio-inspirado para resolver o clássico **Problema da Mochila 0/1 (Knapsack Problem)**. A proposta permite compreender, na prática, como técnicas inspiradas na natureza podem ser utilizadas para encontrar boas soluções em problemas complexos de otimização, nos quais métodos exatos se tornam inviáveis em grande escala.

---

## 📌 Definição do Problema da Mochila 0/1

O problema consiste em selecionar um subconjunto de itens com **peso** e **valor**, de forma a **maximizar o valor total carregado na mochila**, respeitando uma capacidade máxima.

**Entrada:**
- Lista de pesos: `w[i]`
- Lista de valores: `v[i]`
- Capacidade máxima da mochila: `W`

**Saída esperada:**
- Conjunto de itens selecionados (em forma binária)
- Valor total máximo alcançado

### 🔍 Exemplo Clássico

```python
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5
```

Solução ótima esperada:  
Itens escolhidos: 1 e 2 → Vetor: `[1, 1, 0, 0]`  
Valor total: **7**

---

## 🤖 Algoritmo Escolhido: Algoritmo Genético (Genetic Algorithm - GA)

O algoritmo genético é uma técnica bio-inspirada baseada nos processos naturais de **seleção, reprodução e mutação genética**. Neste trabalho, cada **indivíduo** representa uma **solução possível para o problema**, codificada como um vetor binário.

### Etapas do Algoritmo

1. **Codificação:** vetor binário de `n` posições (0 = item fora da mochila, 1 = item incluído).
2. **População Inicial:** soluções geradas aleatoriamente.
3. **Avaliação (Fitness):** calcula-se o valor total dos itens, penalizando soluções que ultrapassem a capacidade da mochila.
4. **Seleção:** método de torneio entre 3 indivíduos.
5. **Crossover:** cruzamento de um ponto entre dois pais para gerar dois filhos.
6. **Mutação:** alteração aleatória de bits com baixa probabilidade.
7. **Elitismo:** o melhor indivíduo da geração é mantido.
8. **Parada:** após número fixo de gerações (ex: 100).

---

## 🧪 Conjuntos de Teste Utilizados

### 1. Teste Básico (4 itens)

```python
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5
```

Resultado esperado: `[1, 1, 0, 0]`  
Valor total: **7**

### 2. Teste Intermediário (6 itens)

```python
pesos = [2, 3, 1, 4, 6, 2]
valores = [5, 8, 3, 7, 9, 4]
capacidade = 10
```

Resultado médio após várias execuções: **20 a 23**

### 3. Teste com 1000 e 10.000 itens

- Itens gerados aleatoriamente.
- Tempo de execução aumenta, mas o algoritmo ainda encontra soluções com bom valor total.
- Média das execuções foi avaliada para validar a estabilidade da solução.

---

## ⚙️ Estratégia de Avaliação

Soluções que ultrapassam a capacidade da mochila são penalizadas com **fitness zero**. Essa abordagem garante que apenas soluções viáveis evoluam ao longo das gerações.

A função de aptidão considera:

```python
if peso_total > capacidade:
    return 0
else:
    return valor_total
```

---

## ⏱️ Comparativo de Desempenho

| Conjunto de Dados   | Tempo Médio | Valor Médio Obtido |
|---------------------|-------------|---------------------|
| 4 itens             | < 1s        | 7 (ótimo)           |
| 6 itens             | < 1s        | ~22                 |
| 1000 itens          | ~2s         | Depende da aleatoriedade |
| 10.000 itens        | ~10-20s     | Boa solução, não ótima |

---

## 📉 Complexidade

- **Tempo estimado:** `O(P * G * n)`  
  (P = tamanho da população, G = número de gerações, n = número de itens)
- **Espaço:** `O(P * n)`  
  (armazenamento de toda a população e seus cromossomos)

---

## 📚 Dificuldades e Soluções

- **Validação de soluções:** foi necessário penalizar fortemente soluções inválidas.
- **Convergência precoce:** solucionado com mutações e seleção por torneio.
- **Escalabilidade:** ajustar população e gerações conforme o número de itens foi essencial.
- **Aleatoriedade:** por ser estocástico, os resultados variam. Foram feitas múltiplas execuções e média dos valores obtidos.

---

## 🧠 Aprendizados

- Compreensão profunda do funcionamento de um algoritmo genético na prática.
- Importância da representação correta da solução (vetor binário).
- Estratégias para manter diversidade populacional e evitar mínimos locais.
- Controle de complexidade computacional em problemas com muitos elementos.
- Adaptação de algoritmos bio-inspirados a problemas clássicos da computação.

---

## ✅ Conclusão

O algoritmo genético demonstrou ser eficaz para resolver o Problema da Mochila 0/1, especialmente em casos com muitos itens, onde métodos exatos se tornam inviáveis. A implementação, apesar de simples, mostrou resultados satisfatórios, com boa performance e qualidade nas soluções encontradas.

Este trabalho proporcionou um entendimento prático das técnicas de otimização bio-inspiradas e reforçou a importância de soluções aproximadas em problemas NP-difíceis.
