## 4. Criação de programas

### Programas em Python

Um programa em Python é um conjunto de instruções que são executadas em ordem:
- sequenciamento;
- estruturas de condição;
- estruturas de repetição;

### print(), input(), eval()

| Função | Definição | Exemplo |
| --- | --- | --- |
| print() | imprime o que é enviado no argumento* | >>> print('Hello world') <br> Hello world |
| input() | solicita dados do usuário no shell** | >>> nome = input('Digite seu nome:') <br> Digite seu nome: Clara <br> >>> nome <br> Clara |
| eval() | instrui a linguagem a avaliar uma string como expressão | >>> eval('3+4') <br>  7|

\* outros argumentos de *print()* são: sep='/' (separador) e end='.\n' (terminador);  
\** a função *input()* sempre retorna uma string, independentemente do valor digitado pelo usuário;

<Br>

[Exemplo: Conversão de Temperatura](Code/s4-ex1.py)

*C = input('Digite a temperatura em Celsius:')  
F = 1.8 * eval(C) + 32  
print('A temperatura é de', F, '°F')*

<br>

### Definição de funções

A linguagem Python permite que o programador crie suas próprias **funções** para facilitar a execução de uma mesma sequência de instruções várias vezes em diferentes partes do programa.

O formato geral para definição de funções em Python é:

def <nome da função> (<parâmetros>):  
&nbsp;&nbsp; <instruções com identação>
<br>&nbsp;&nbsp; ...
<br>&nbsp;&nbsp; return <valor.> (opcional)

Uma função sempre deve ser definida **antes** de ser executada. Ao usar *return*, você obtém um valor que pode ser utilizado em outras funções aritméticas, enquanto *print()* apenas exibe o resultado na tela.

<br>

[Exemplo: Média](Code/s4-ex2.py)

*def media(n1,n2):  
&nbsp;&nbsp;     m = (n1+n2)/2  
&nbsp;&nbsp;     return m*

*n1 = eval(input('Insira a nota 1:'))  
n2 = eval(input('insira a nota 2:'))  
print(media(n1,n2))*

<br>

### Documentação de programas

A documentação de um programa permite que os usuários entendam o que ele faz e que os desenvolvedores entendam como ele funciona. Ela também é crucial para o próprio autor, uma vez que registra as finalidades de partes específicas do código para referência futura.

<br>

**Comentários**

A documentação em Python geralmente é feita através de comentários, que são representados depois de # ou // (em uma única linha) ou ''' (em mais de uma linha).

\# Este é um comentário.

'''  
Este é um comentário  
que ocupa mais de uma linha.  
'''

Variáveis com nomes significativos tornam o código legível, enquanto os comentários facilitam o entendimento de partes complexas do código.

<br>

**Docstrings**

As **docstrings** são uma forma de documentação incorporada ao código Python que podem ser acessadas através da função *help()*.

\>>> help(max)
Help on built-in function max in module builtins:

max(...)  
&nbsp;&nbsp;&nbsp;max(iterable, *[, default=obj, key=func]) -> value  
&nbsp;&nbsp;&nbsp;max(arg1, arg2, *args, *[, key=func]) -> value  

&nbsp;&nbsp;&nbsp;With a single iterable argument, return its biggest item. The  
&nbsp;&nbsp;&nbsp;default keyword-only argument specifies an object to return if  
&nbsp;&nbsp;&nbsp;the provided iterable is empty.  
&nbsp;&nbsp;&nbsp;With two or more arguments, return the largest argument.

No caro de funções definidas pelo usuário, o comando *help()* resgata uma descrição genérica da função.

\>>> help(media)  
Help on function media in module __main__:

media(n1, n2)

Para exibir uma descrição mais detalhada, é necessário adicionar uma *docstring* logo abaixo do nome da função entre aspas simples (').

def media(n1,n2):  
&nbsp;&nbsp;&nbsp;'Calcula a média simples a partir de duas notas'  
&nbsp;&nbsp;&nbsp;m = (n1+n2)/2  
&nbsp;&nbsp;&nbsp;return m