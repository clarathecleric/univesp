#### COM120 - Algoritmos e Programação de Computadores II

## 1. Gerenciamento de memória, arquivos e depuração de programas

### 1.1. Tipos mutáveis e não mutáveis em Python 

Diferentemente de outras linguagens de programação, Python trata as **variáveis** como **objetos**, com todas as operações que as envolvem sendo feitas através de referências aos tais. Quando uma variável é declarada, o interpretador aloca espaço na memória para armazenar o objeto correspondente. Quando ela deixa de ser necessária, o espaço reservado é desalocado, ficando livre para outros usos. Isso permite que uma variável apresente valores diferentes em momentos diferentes do código.

As variáveis e seus correspondentes valores são armazenados em uma tabela de símbolos, conhecida como namespace, que permite que o interpretador procure e resgate o objeto correspondente quando uma variável é referenciada.

Em Python, temos tanto **objetos mutáveis** (list, dict, set, etc.), que podem ter seus valores alterados depois de criados, e **imutáveis** (tuple, str, int, etc.), cujos valores só podem ser definidos em sua inicialização. No caso dos mutáveis, é importante lembrar que qualquer alteração feita a um objeto afetará todas as variáveis que a ele apontam.

<br>

### 1.2. Arquivos

Os dois principais tipos de arquivo de Python são os arquivos de texto e os arquivos binários.

**Arquivos de texto** são aqueles que contém dados codificados em caracteres, que podem ser lidos e escritos pelas funções built-in do Python, como open() e readline(), normalmente sendo manipulados como strings.

Já os **arquivos binários** são aqueles que contem dados codificados em sequências de bytes e devem ser lidos e escritos utilizando funções especializadas na manipulação de arquivos binários, como as funções open() com o parâmetro "rb" (read binary) para leitura ou "wb" (write binary) para escrita.

<br>

**Sistema de arquivos**

O **sistema de arquivos** é um componente fundamental do computador, fornecendo uma interface para a criação, abertura e modificação de arquivos. Além disso, ele os organiza em uma estrutura hierárquica, composta por pastas ou diretórios. Cada diretório pode conter zero ou mais arquivos e subdiretórios, que, por sua vez, podem conter mais arquivos e diretórios.

Há duas formas de especificar o arquivo ou diretório desejado: o caminho relativo ou o caminho absoluto.

O **caminho relativo** especifica o local de um arquivo ou diretório em relação ao diretório atual, que é normalmente o diretório em que o processo foi iniciado ou o último diretório que o usuário mudou, enquanto o **caminho absoluto** especifica o local de um arquivo ou diretório em relação à raiz do sistema de arquivos. Ele sempre se inicia na raiz e descreve todo o caminho até o arquivo ou diretório desejado.

<br>

**Manipulação de arquivos**

O processamento de um arquivo em Python ocorre em três passos:

- Abertura:

A função utilizada para abrir um arquivo é a **open()** contendo dois argumentos: o **caminho** (absoluto ou relativo) e o **modo de abertura** respectivamente. Ex.: open('exemplo.txt', 'r')
  
  | modo | descrição |
  | --- |--- |
  | **r** | modo de leitura (padrão) |
  | **w** | modo de escrita (se o arquivo já existir, seu conteúdo é descartado) |
  | **a** | modo append (o conteúdo é adicionado ao final do arquivo) |
  | **r+** | modo de leitura e escrita |
  | **t** | modo texto (padrão) |
  | **b** | modo binário |

<br>

- Leitura ou escrita:
  
A tabela a seguir apresenta as principais funções de leitura e edição de arquivos em Python:

  | método | descrição|
  | --- | --- |
  | **infile.read(n)** | lê *n* caracteres do arquivo **infile** ou até que o final do arquivo seja atingido, e retorna caracteres como uma string |
  | **infile.read()** | lê caracteres do arquivo **infile** até que o final do arquivo seja atingido, e retorna caracteres como uma string |
  | **infile.readline()** | lê o arquivo **infile** até que alcance a nova linha de caracteres ou o final do arquivo (incluindo a nova linha) e retorna os caracteres como uma string |
  | **infile.readlines()** | lê o arquivo **infile** até o final do arquivo e retorna os caracteres lidos como uma lista de linhas |
  | **outfile.write(s)** | escreve a string *s* no arquivo **outfile** |

<br>

- Fechamento:
  
Por fim, após realizar a leitura ou edição necessária, usa-se a função **close()** para fechar o arquivo, assim notificando o sistema que os recursos do arquivo previamente aberto podem ser liberados.


### 1.3. Depuração

A **depuração** de programas é uma etapa importante no desenvolvimento de software, uma vez que permite encontrar e corrigir erros. Ela pode ser realizada tanto durante o desenvolvimento quanto após a sua implantação, caso ocorram erros na produção.

Os três principais tipos de erros são:

1. **Erros de sintaxe** (syntax errors): referentes às regras da linguagem de programação, eles impedem que o código seja interpretado ou compilado corretamente;
2. **Erros de execução** (runtime errors): refentes a possíveis problemas encontrados durante a execução que impedem que o código continue a ser executado;
3. **Erros de semântica** (semantic errors): referentes a erros que ocorrem quando o código é executado sem problemas aparentes, mas apresenta resultados incorretos ou inesperados, sendo assim mais difíceis de detectar.

Os **depuradores** são ferramentas que auxiliam o programados no processo da depuração, nativamente presentes em muios ambientes de desenvolvimento integrados (IDEs). Eles permitem que o programador execute o código passo a passo, inspecione valores de variáveis e defina pontos de interrupção dentro do código.

O **breakpoint** é uma técnica de depuração que interrompe a execução do código em um ponto específico, permitindo que analise o estado atual do programa e identifique possíveis erros ou bugs. Em Python, é possível inserir breakpoints diretamente no código através da função **pdb.set_trace()**.