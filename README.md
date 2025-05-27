# 📊 Relatório de Refatoração: Projeto da Mochila
Alunos: Gustavo João Chaves, Cristian Domingues e Michael Varaldo

## ✅ Melhorias Realizadas

### 1. **Modularização do Código**
**Antes:**  
- Todo o código estava concentrado em um único arquivo, dificultando a legibilidade e manutenção.

**Depois:**  
- O código foi dividido em módulos, cada um responsável por uma parte específica da lógica:
  - `algorithm.py`: lógica principal do algoritmo genético.
  - `individual.py`: funções relacionadas ao indivíduo (geração, avaliação, mutação).
  - `selection.py`: funções de seleção e crossover.
  - `config.py`: parâmetros de configuração centralizados.
  - `main.py`: ponto de entrada, executa o algoritmo e exibe os resultados.

**✅ Benefício:** Facilita a manutenção, testes unitários, reuso de código e clareza na estrutura.

---

### 2. **Parametrização de Itens e Configurações**
**Antes:**  
- Itens, capacidade e parâmetros do algoritmo estavam diretamente definidos no código principal.

**Depois:**  
- Todas as configurações foram extraídas para o arquivo `config.py`:
  ```python
  ITEMS = [(2, 3), (3, 4), (4, 5), (5, 6)]
  CAPACITY = 5
  POPULATION_SIZE = 20
  GENERATIONS = 100
  MUTATION_RATE = 0.1
  TOURNAMENT_SIZE = 3
  ```

**✅ Benefício:** Torna o ajuste dos parâmetros mais simples e centralizado, sem necessidade de alterar a lógica do código.

---

### 3. **Tipagem Estática com `typing`**
**Antes:**  
- Não havia especificação de tipos, o que poderia gerar erros difíceis de identificar.

**Depois:**  
- Todos os módulos foram enriquecidos com **anotações de tipos** (`List`, `Tuple`), como:
  ```python
  def genetic_algorithm(
      items: List[Tuple[int, int]],
      capacity: int,
      population_size: int,
      generations: int,
      mutation_rate: float
  ) -> Tuple[List[int], int]:
  ```

**✅ Benefício:** Melhora a legibilidade, reduz erros e facilita o uso de linters e ferramentas de análise.

---

### 4. **Separação de Responsabilidades**
**Antes:**  
- As funções estavam misturadas: geração de indivíduos, cálculo de aptidão, seleção, mutação, crossover e execução.

**Depois:**  
- Cada módulo trata exclusivamente de sua responsabilidade:
  - `individual.py`: geração, fitness e mutação.
  - `selection.py`: seleção e crossover.
  - `algorithm.py`: evolução da população.
  - `main.py`: execução e exibição do resultado.

**✅ Benefício:** Facilita testes unitários, entendimento e extensão do código.

---

### 5. **Função Principal `main`**
**Antes:**  
- A execução do algoritmo estava no escopo global.

**Depois:**  
- Foi criada uma função `main()` clara e organizada, chamando o algoritmo e exibindo os resultados.

**✅ Benefício:** Boa prática de programação, melhora a organização e a legibilidade.

---

### 6. **Centralização da Taxa de Torneio**
**Antes:**  
- O tamanho do torneio de seleção era fixo no código.

**Depois:**  
- Foi movido para `config.py` como `TOURNAMENT_SIZE`, podendo ser facilmente ajustado.

**✅ Benefício:** Facilita experimentações e ajustes finos no algoritmo.

---

## 🚀 Conclusão

A refatoração resultou em um código:

✅ Mais organizado  
✅ Mais legível  
✅ Mais fácil de manter e expandir  
✅ Mais seguro com tipagem  
✅ Mais reutilizável
