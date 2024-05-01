#### COM130 - Fundamentos de Internet e Web

## 5. HTML5 e suas funcionalidades

### 5.1. HTML5: Hypertext Markup Language/Versão 5 

Diferentemente de seu sucessor, a principal preocupação do HTML4 era integrar outras tecnologias, como CSS e JavaScript, à manipulação de documentos HTML em detrimento da clareza e a estruturação do conteúdo para usuários e mecanismos de busca. O **HTML5**, por sua vez, priorizou a **legibilidade** e **estruturação** das páginas, introduzindo novos **elementos semânticos** que as tornariam mais acessíveis e intuitivas. Além disso, a nova versão também facilitou a reutilização de informações e a criação de códigos interoperáveis para futuros dispositivos, tornando o desenvolvimento web mais eficiente e econômico.

A estrutura básica de uma página HTML5 consiste em um conjunto de elementos organizados hierarquicamente através da lógica e da semântica. Ela segue o seguinte padrão:

1. **<\!DOCTYPE html>**: define o tipo e a versão do documento
2. **Head**: contém informações sobre o documento, como título, páginas de estilo, scripts, metadados, etc.
3. **Body**: seção que contém todos os elementos visíveis da página, como textos e conteúdos multimídia.

Abaixo estão descritas as tags que podem ser usadas para compor uma página na seção **body**:

- **Estrutura do documento**:
  - **header**: usada para representar o **cabeçalho** de uma página ou seção específica;
  - **nav**: usada para agrupar **links de navegação**, podendo conter links para outras páginas do site ou diferentes seções de uma mesma página;
  - **footer**: usada para representar o **rodapé** de uma página ou seção específica;
  
- **Grupos de conteúdo**
  - **article**: usada para representar um conteúdo autônomo dentro da página, podendo conter seu próprio cabeçalho e rodapé.
  - **section**: usada para agrupar e representar uma seção tematicamente relacionada de conteúdo, também podendo conter seu próprio cabeçalho e rodapé, assim como outros elementos HTML quando necessário;
  - **div**: usada para formatar e organizar o layout da página, dividindo-a em grupos relevantes ao desenvolvedor. Enquanto seu valor semântico é menor que o da tag section, possui maior flexibilidade no seu uso;

Dentre as outras tags originárias do HTML5 também temos a **hgroup**, que permite o agrupamento de títulos, tags de **audio** e **video**, que permitem que conteúdos multimídia sejam inseridos de forma segura, e a tag **main**, que define o conteúdo mais relevante ao tópico principal da página.