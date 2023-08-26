CONSIDERAÇÕES INICIAIS:

Por ser um Desafio Nacional, fiz o projeto 100% em português exceto por esse arquivo o "README" o qual o nome só fica estiloso em inglês hahaha.

Não vou mentir que no inicio tive muitas ideias e foi difícil saber por onde começar, por isso decidi primeiro focar especificamente em realizar tudo que foi Pedido. Porém agora que a parte essencial do Projeto está pronta, tanto eu quanto  o público pode se sentir a vontade para contribuir com Ideias no GitHub.

Neste video você encontrará um resumo do que tem aqui e algumas informações extras: https://vimeo.com/858088676/c12470a5c6


OBJETIVO DO PROGRAMA:

Imagine que você está fazendo o software de uma empresa para liberar o acesso aos funcionários para dentro e fora da empresa, é como se fosse aquelas catracas automáticas nos prédios só que ao passar pela catraca o funcionário precisar interagir com o Display, nesse display será mostrada 3 opções. a opção de cadastro para caso o funcionário seja novo, e opção de sair e entrar, vale lembrar que o funcionário não pode entrar de novo se ele já entrou, e não pode sair se já saiu. o Código deve ter essa lógica e também deve ter um banco de dados que registre os clientes cadastrados nas empresas, que registre também as entradas e as saídas e a duração entre uma entrada e um saída que é o que podemos chamar de Operação, essse banco de dados irá servir para o administrador e o time de análise de dados e tanto de desenvolvimento no futuro para fazer novas implementações. Vale ressaltar que esse banco irá sempre armazenar os dados em ordem sequencial independente se o a execução do código parou ou não, ou seja a cada funcionário que passa pela catraca é um ciclo de execução novo.

ORGANIZAÇÃO DOS ARQUIVOS E EXPLICAÇÃO LÓGICA


funcionario.py : Começarei por esse arquivo pois ele é bem simple, a ideia é criar uma classe que possa fornecer atributos para os nossos objetos, dentre eles: nome,sobrenome,cpf

banco.py : Tendo sqlite3 iremos iniciar e nos conectar com o banco 'empresa.db' e iremos definir um cursor para os nosso futuros comandos SQL

migracao.py: O arquivo migracao é um complemento de banco.py nele você poderá ter as tabelas do nosso banco, ao total são 4 tabelas. Dentre elas, funcionarios, registro_entrada, registro_saida, operacao. Esse será o primeiro arquivo a ser executado antes do Menu.py. A ideia de separar as tabelas e o banco em arquivos separados é para não precisar comentar as tabelas toda vezes que você quiser executar o código do zero e resetar o banco. Porém isso não é tão necessário para vocês já que configurei o Docker para executar automaticamente o migracao.py

menu.py: Nele iremos dar aos boas vindas com o nosso Menu, ele irá exibir 3 opções a primeira irá usar a função adicionaFuncionario() e o retorno da funcão será armazenada na váriável funcionario, o retorno será um objeto então iremos fazer um Insert na tabela funcionarios que irá receber os atributos do funcionario, um atributo para cada coluna. em seguida iremos consultar os dados desse funcionario por meio de um select e a variavel resultado irá receber as colunas desse select como uma tupla, onde cada posição é um atributo, dessa forma  você terá um print confirmando a entrada do funcionario no sistema. A Opção 2 irá ativiar a funcão entrada e a 3 a funcão saída, as quais serão explicadas no último arquivo

tratamentoDeErros.py: A ideia desse arquivo é tratar entrada inválidas, com auxilio de expressões regulares conseguir validar um CPF de forma que ele tennha os caracter: .- e o número suficiente de digitos. Nesse mesmo arquivo temos uma função para trtar nomes, o nome não pode receber números e não pode ser menor que 4 caracters, e respondendo sua pergunta... eu não conheço ninguém que tenha nome com 3 Letras

funcoesGerenciamento.py: Aqui é o ponto quente do código, onde temos toda a lógica essencial. irei dividir cada função em parágrafos...

Começaremos pela função adicionaFuncionario(), perceba que ela é bem simples, já comentamos sobre, ela produz um objeto com base nas entradas do usuário, cada variavel é enviada como atributo, e note que estou usando as funções de tratamento.

consultaEntradasSaidasPorFuncionario(): Faz uma consulta que calcula o número de entradas e saídas de um determinado funcionario

Agora vamos para entrada(), na entrada e tanto quanto a saida temos duas validações para fazer, a primeira é se o CPF digitado pelo funcionario está no banco de dados, fazer isso por meio de uma consulta SQL, que irá procurar o CPF digitado, caso tenha uma tabela como retorno o resultado que recebe o conteúdo da nossa consulta será verdadeira logo podemos fazer um if resultado que é a mesma coisa se resultado é True para a máquina(boolean), feito isso vamos fazer a segunda validação, A segunda validação se trata sobre o funcionario não poder entra duas vezes seguidas sabemos que enquanto o funcinário estiver dentro da operação o numero de entradas será 1 unidade maior que o número de saida apenas, e quando ele estiver fora da operação o número de saidas e entradas serão iguais, então tiramos a conclusão que na próxima entrada se o número de entradas já for maior que o número de saidas então devemos barrar essa próxima entrada. Para isso utilizaremos a função consultaEntradaSaidasPorfuncionario() ela irá retornar a quantidade de cada e duas váriaveis irão armazenar  uma cada uma, no else em diante temos a inserção da data e hora atual e id do funcionario na tabela de registro_entrada.

tempoExpediente(): é uma função que retorna uma variavel que recebe uma consulta essa consulta tem uma estrutura que consegue pegar a data maxima de entrada e saida e subtrair as duas em segundos, lembrando que a data máxima é a sempre a mais recente, então mesmo que  funcionário já tenha feito várias operações ele sempre irá pegar a última. Lembrando que como estatmos usando duas tabelas precisamos pegar o id do funcionario em cada tabela como parametro, assim teremos dois parametros

Agora vamos para saida(). O processo de validação é a mesma ideia, a diferença está somente na segunda validação, pois enquanto o funcinario esta na operação a saida sempre vai ser uma unidade menor que a entrada e após ele sair da operação as duas irão se igualar então se na proxima saida o número de entradas e saidas forem iguais, essa saida deve ser barrada. Outra diferença da saida é o final além de adicionarmos os dados da data e hora de saida e id do funcionario na tabela de registro_saida, Também temos uma variavel que irá receber o tempeExpediente em segundos. Note que esse segundos estão em uma tupla que por sua vez está em uma lista, por isso para descompactar usamos "seguundos = diferenca[0][0]" e após isso convertemos esse valor extraido para float. Por fim adicionamos essa diferença de segundos como um parte do registro de uma operação realizada na tabela operacao que estará conectada com o funcionário.

COMO EXECUTA O PROGRAMA

Utilizei o Dockerfile assim você irá conseguir rodar o projeto  sem precisar baixar todas as ferramentas que usei como Python e pycharme por exemplo
Siga esse passo a passo:
1 - Faça um gitclone do meu repositório na sua máquina, use este link: https://github.com/Levi-cell/W5iDesafio/tree/main/GerenciadorDeAcesso
2 - Abra o CMD no local da em que você baixou os arquivos 
3 - Faça o seguinte comando python menu.py
4 - Se sinta a vontade para interagir 

COMO ACESSAR O BANCO DE DADOS

Caso queira acessar o banco de dados você terá que instalar o Python no seu computador se você tiver Windows a própria microsoft store disponibilizará, é só baixar e abrir o Python Idle e após clonar o respositorio, baixe o sqlitebroswer neste link: https://sqlitebrowser.org/. Como IDE recomendo o Pycharm. em algum lugar desse readme deixarei umas consultas. Quando você executar o programa ele irá liberar um arquivo.db que é o seu banco de dados provavelmente será "empresa.db" abra o sqlite e vá em open database após ir pro caminho desse arquivo abra o arquivo.db, você poderá visualizar o banco de dados logo em seguida, caso queira praticar consultas vá para execute sql. Vale lembrar que o SQLlite possui algumas limitações, em consultas mais complexas ele não consegue conhectar as chaves estrangeiras e acaba por duplicando os dados. Recomendo usar o MySQL caso você tenha mais tempo de fazer o projeto, pode usar o banco do seu gosto também, esse projeto também é bem comátivel pra conectar com a API flask.

CONSULTA SQL:

SELECT
    f.id_funcionario as "id do funcionario",
    f.nome as "nome do funcionario",
    SUM(o.tempo_da_operacao_em_segundos) as "Duração de todas operacoes em segundos"
FROM
    funcionarios f
INNER JOIN
    operacao o on o.codigo_funcionario = f.id_funcionario
GROUP BY
    f.id_funcionario, f.nome;



AGRADECIMENTOS:

Gostaria de Agradecer a W5i por esse desafio que por mais que pareça simples, foi muito divertido de resolver e desafiador, seria muito divertido poder enfrentar desafios como esse no dia a dia.

Lembrando que o objetivo desse programa é que ele seja usado apenas por funcionários, ou seja não é uma boa prática implementar funcionalidades de um administrador, caso um administrador queira consultar a quantidade de funcionários e dados especificos dos funcionarios o ideal é fazer uma consultaSQL. É possível sim colocar esssa opção em código por meio de consultar no programa, porém na prática todo funcionário que passasse pela catraca veria essa opção e poderia ter acesso aos dados de todos os funcionários o que é perigoso. Por isso c

Então caso vá contribuir para esse projeto, leve isso em conta, a ideia é deixar um código prático possível, quem sabe um dia poderá virar um sistema real.

MEUS CONTATOS PARA DÚVIDAS:

email: levigov21@gmail.com
número: 71994111866

OBS: Esse projeto está licenciado sob a licença MIT.
