#### COM120 - Algoritmos e Programação de Computadores II

## 3. Recursão

### 3.1. Recursão I

A **recursão** é um conceito fundamental na programação onde uma função chama a si mesma durante a sua execução, buscando resolver um problema de forma iterativa. Em resumo, é uma ação que se repete até que alcance uma condição de parada.

Na prática, a recursão ocorre da seguinte forma:

1. **Chamada inicial da função**: A função recursiva é chamada com parâmetros iniciais.

2. **Verificação do caso base**: Os parâmetros são verificados para determinar se atingiram o caso base. Se sim, a recursão para.

3. **Caso recursivo**: Se os parâmetros não atingiram o caso base, a função realiza processamento e chama a si mesma com parâmetros modificados.

4. **Subdivisão progressiva**: A função continua a chamar-se recursivamente, reduzindo o problema original em subproblemas menores a cada chamada.

5. **Convergência para o caso base**: Eventualmente, os parâmetros passados satisfazem o caso base, indicando que a recursão pode parar.
    
6. **Retorno dos resultados**: À medida que as chamadas recursivas alcançam o caso base, os resultados são combinados ou processados para produzir o resultado final da função.

7. **Desenrolamento da pilha**: Com o retorno dos resultados das chamadas recursivas, a pilha de chamadas é desenrolada progressivamente, retornando para cada chamada recursiva sua resposta, até que o resultado final seja retornado para a chamada original.

Uma das vantagens da recursão é sua capacidade de tornar o código mais limpo e legível, especialmente quando não se sabe quantas iterações serão necessárias para resolver um problema. Entretanto, ela também pode ser utilizada incorretamente, levando a problemas de desempenho e estouro de pilha quando há recursão excessiva.

O uso da recursão deve ocorrer quando não houver uma versão mais simples e não recursiva da função, e quando o problema puder ser definido recursivamente de forma natural.

É necessário definir três pontos para utilizar a recursão corretamente:

1. Definir o problema de forma recursiva
2. Definir a condição de término
3. Garantir que a cada chamada recursiva está mais próxima de satisfazer a condição de término

<br>

### 3.2. Recursão II

A escolha entre **recursão** e **iteração** depende do problema em questão e das preferências do programador. Enquanto a recursão pode deixar o  código mais conciso e legível, ela tende a ser mais lenta, tornando a iteração mais ágil.

Uma técnica utilizada para otimizar a recursão é chamada de **memoização**, que armazena em cache os resultados de chamadas prévias da função para evitar cálculos desnecessários quando uma nova função é chamada.