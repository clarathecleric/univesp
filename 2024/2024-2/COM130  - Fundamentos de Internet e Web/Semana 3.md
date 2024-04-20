#### COM130 - Fundamentos de Internet e Web

## 3. Fundamentos do WWW

### 3.1 A World Wide Web (WWW)

**Como surgiu a WWW?**

A World Wide Web (WWW) foi idealizada pelo cientista da computação britânico Tim Berners-Lee na década de 80, enquanto trabalhava no CERN. Ele buscava facilitar o gerenciamento e compartilhamento de informações entre cientistas através de um sistemas descentralizado, que permitisse que as informações fossem facilmente acessadas de qualquer lugar do mundo. Sua solução inicial foi o ENQUIRE, um sistema de hipertexto que permitia a criação de links entre arquivos, criando uma teia mundial de informações.

Ele, em parceria com seu colega Robert Cailliau, apresentaria um novo sistema de hipertexto à gerência do CERN em 1989, descrito em um documento intitulado "Information Management: A Proposal". 

A boa recepção da ideia levou Berners-Lee a dar início ao desenvolvimento da WWW, criando a linguagem de marcação HTML para a criação de documentos hipertexto e o protocolo HTTP para a transferência de informações. Este esforço resultou no lançamento do primeiro navegador web, o WorldWideWeb, em 1991, efetivamente unindo os conceitos de hipertexto e a internet. Neste mesmo período, para preencher um nicho criado por ele mesmo, ele também desenvolveu o URI (Uniform Resource Identifier), um sistema de identificação global e único de recursos que eventualmente se tornaria a URL.

Enquanto a internet já contava com alguns protocolos em 1991, como, por exemplo, o e-mail, eles apresentavam limitações. Para contorná-las, foi necessário a implementação de novos protocolos que suprissem os requisitos necessários para o acesso a links de forma simples. Entre eles encontramos o FTP, necessário para a transferência de arquivos, e o  o HTTP, para a navegação.

<br>

**Os principais componentes da Web**

A grosso modo, podemos dizer que toda a WWW é um conjunto de dados dos mais diversos tipos armazenado em servidores, podendo ser requisitados pelos usuários e aplicações. Vale lembrar, que o usuário/cliente/browser é incapaz de acessar diretamente o arquivo desejado sem primeiro pedir permissão ao servidor, que por sua vez processa a requisição e disponibiliza o arquivo desejado em questão de segundos.

Os **servidores** são um componente primordial da web, baseados em três padrões fundamentais: **URL**, **HTTP** e **HTML**. Enquanto compostos tanto por componentes de hardware e software, eles podem ser um **programa** que processa e executa as requisições dos navegadores e aplicações clientes. Um grande exemplo de um servidor web de plataforma aberta é o **Apache**, mantido pela Apache Software Foundation. Versátil e seguro, o servidor oferece recursos além do simples fornecimento de conteúdo, tendo como exemplo o módulo de ativação do suporte SSL (Security Socket Layer), que garante maior segurança à conexão, e recursos de balanceamento de carga, reescrita de URL e geolocalização baseada em IP.

O sistema de **URL** (Uniform Resource Locator"), sucessor do URI, especifica um endereço único para cada página de informação da web, indicando o objeto e o servidor em que se encontra. Ele trabalha em conjunto com o **DNS** (Domain Name System) que funciona como um registro de URLs e seus respectivos endereços IP.

O **HTTP** (Hypertext Transfer Protocol), padrão da WWW, é um protocolo cliente-servidor que permite a obtenção e inserção dos mais diferentes conteúdos em servidores web. Ele é um protocolo extensível da camada de aplicação, agindo sobre o protocolo TCP. Entretanto, é independente da camada de transporte, precisando apenas que a conexão cliente-servidor seja confiável e garanta a integridade dos arquivos transportados.

A comunicação HTTP é dividida em três etapas básicas: o estabelecimento da conexão TCP, a requisição da parte do cliente e o envio de dados da parte do servidor. A versões mais recentes do HTTP buscam trazer uma única conexão TCP de forma a melhorar seu desempenho.