#### COM120 - Algoritmos e Programação de Computadores II

## 2. Programação orientada a objetos e modularização

### 2.1. Programação orientada a objetos I

A **programação estruturada** é um paradigma de programação que se baseia em **estruturas de sequência**, **seleção** e **repetição** para escrever programas, frequentemente utilizando **funções** para modularizar e reutilizar o código, facilitando sua manutenção. É uma técnica de extrema importância na programação, servindo de base para outros paradigmas, como a programação orientada a objetos.

Na **programação orientada a objetos**, todos os dados e procedimentos são encapsulados em um único elemento, o **objeto**. A comunicação entre tais objetos ocorre através da troca de mensagens, caracterizando a execução do programa. Em contrapartida, na programação estruturada, a comunicação entre procedimentos se dá por meio da passagem de parâmetros.

Um **objeto** é uma instância de uma classe que mais se aproxima de uma entidade do mundo real. Possui **estados** (dados) e **comportamentos** (ações que podem ser executadas).

Uma **classe** é uma **representação abstrata** de um conjunto de objetos que possuem atributos e comportamentos similares. Ela descreve o a estrutura e comportamento de seus objetos em linhas gerais.

[Exemplo](code/s2-ex1.py)

<br>

### 2.2. Programação orientada a objetos II

A **sobrecarga de operadores** permite definir operadores que possam ser usados de formas diferentes em diferentes classes através da implementação de métodos especiais. Ela permite o desenvolvimento de um código mais limpo e conciso, permitindo o uso dos operados ao invés do uso explícito de métodos.

| operador | método | número | list e str |
| --- | --- | --- | --- |
| **x + y** | x.\_\_add__(y) | adição | concatenação |
| **x - y** | x.\_\_sub__(y) | subtração | - |
| **x * y** | x.\_\_mul__(y) | multiplicação | auto-concatenação |
| **x / y** | x.\_\_truediv__(y) | divisão | - |
| **x // y** | x.\_\_floordiv__(y) | divisão inteira | - |
| **x % y** | x.\_\_mod__(y) | módulo | - |
| **x == y** | x.\_\_eq__(y) | igual | igual | 
| **x != y** | x.\_\_ne__(y) | diferente | diferente 
| **x > y** | x.\_\_gt__(y) | maior | maior |
| **x >= y** | x.\_\_ge__(y) | maior ou igual | maior ou igual |
| **x < y** | x.\_\_lt__(y) | menor | menor |
| **x <= y** | x.\_\_le__(y) | menor ou igual | menor ou igual |
| **repr(x)** | x.\_\_repr__(y) | representação canônica da str | representação canônica da str |
| **str(x)** | x.\_\_str__(y) | representação informal da str | representação informal da str |
| **len(x)** | x.\_\_len__(y) | - | tamanho da coleção |
| **\<type>(x)** | \<type>.\_\_init__(x) | construtor | construtor |


Outra característica essencial da programação orientada a objetos é a **herança**, uma técnica que permite reutilizar ou alterar métodos de classes já existentes, adicionando novos atributos e métodos para adaptá-las para seu novo uso. Isso se dá a partir da criação de uma **superclasse**, classe básica composta por funcionalidades genéricas comuns às classes consequentes, e a partir dela uma ou mais **subclasses**, classe derivada que pode, além de adicionar novos atributos e métodos, sobrescrever os atuais para fornecer funcionalidades específicas. Diz-se então, que uma subclasse herda suas características da superclasse.

[Exemplo](code/s2-ex2.py)