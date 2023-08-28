--------------------CONSIDERAÇÕES INICIAIS:-------------------------

1- Por ser um Desafio Nacional, fiz o projeto 100% em português exceto por esse arquivo o "README" o qual o nome só fica estiloso em inglês hahaha.
2- Caso você tenha dúvida em algum tópico acesse o vídeo correspondente ao tópico.

----------------------OBJETIVO DO PROGRAMA:--------------------------

Imagine que você está fazendo o software de uma empresa para liberar o acesso aos funcionários para dentro e fora da empresa, é como se fosse aquelas catracas automáticas nos prédios só que ao passar pela catraca o funcionário precisar interagir com o Display, nesse display será mostrada 3 opções. a opção de cadastro para caso o funcionário seja novo, e opção de sair e entrar, vale lembrar que o funcionário não pode entrar de novo se ele já entrou, e não pode sair se já saiu. Também deve ter um banco de dados já que o programa só ficará ativo quando alguém passar pela catraca.

viídeo: https://vimeo.com/858480157/39ced06403

---------------------ORGANIZAÇÃO DOS ARQUIVOS E EXPLICAÇÃO LÓGICA:-------------------------------


FUNCIONARIO.py

Começarei por esse arquivo pois ele é bem simple, a ideia é criar uma classe que possa fornecer atributos para os nossos objetos, dentre eles: nome,sobrenome,cpf.

BANCO.py

Tendo sqlite3 iremos iniciar e nos conectar com o banco 'empresa.db' e iremos definir um cursor para os nosso futuros comandos SQL.

MIGRACAO.py

O arquivo migracao é um complemento de banco.py nele você poderá ter as tabelas do nosso banco, ao total são 4 tabelas. Dentre elas, funcionarios, registro_entrada, registro_saida, operacao. Esse será o primeiro arquivo a ser executado antes do Menu.py. A ideia de separar as tabelas e o banco é para não precisar comentar as tabelas todas as vezes que você quiser executar o código do zero e resetar o banco. Porém isso não é tão necessário para vocês já que configurei o Docker para executar automaticamente o migracao.py.

MENU.py

Ele irá exibir 3 opções a primeira irá usar a função adicionaFuncionario() e dará um Insert na tabela funcionarios que irá receber os atributos do funcionario, um atributo para cada coluna. A Opção 2 irá ativiar a funcão entrada e a 3 a funcão saída, as quais serão explicadas no último arquivo.

TRATAMENTODEERROS.py

A ideia desse arquivo é tratar entradas inválidas como nome e CPF. 

vídeo: https://vimeo.com/858480505/539ffb39f3

FUNCOESGERENCIAMENTO.py

Aqui é o ponto onde temos toda a lógica essencial. irei dividir cada função em parágrafos...

--adicionaFuncionario(): basicamente criará nosso objeto funcionáro.

--consultaEntradasSaidasPorFuncionario(): Faz uma consulta que calcula o número de entradas e saídas de um determinado funcionario.

--entrada(): na entrada e tanto quanto a saida temos duas validações para fazer, a primeira é verificar pelo CPF se o funcionário está no banco, feito isso vamos fazer a segunda validação, A segunda validação se trata sobre o funcionario não poder entra duas vezes seguidas, sabemos que e Nº de entradas e saidas serão sempre iguais exceto quando o funcionario estiver dentro da operação, logo se na proxima entrada o número de entradas for pelo menos 1 unidade maior que o numero de saidas então essa entrada deverá ser barrada. Para isso utilizaremos a função consultaEntradaSaidasPorfuncionario() ela irá retornar a quantidade de entradas e saídas.

--tempoExpediente(): O objetivo é armazenar a diferença entra a data mais recente de entrada e a de saída de um funcionário emm segundos.

--saida(): O inicio é a mesma ideia da entrada.  a diferença está somente na segunda validação, enquanto o funcinario esta na operação a saida sempre vai ser uma unidade menor que a entrada e após ele sair da operação as duas irão se igualar então se na proxima saida o número de entradas e saidas forem iguais, essa saida deve ser barrada. Logo em seguida Também utilizamos o tempeExpediente em segundos para obter o tempo de permanência na operação.

vídeo: https://vimeo.com/858481603/8197e60580

----------------COMO EXECUTA O PROGRAMA:----------------

Utilizei o Dockerfile assim você irá conseguir rodar o projeto  sem precisar baixar todas as ferramentas que usei como Python e pycharme por exemplo
Siga esse passo a passo:
1 - Faça um gitclone do meu repositório na sua máquina, use este link: https://github.com/Levi-cell/W5iDesafio.git

2 - Abra o CMD no local da em que você baixou os arquivos. 

3 - Não esqueça de usar o comando cd GerenciadorDeAcesso.

4 - Faça o seguinte comando python menu.py

5 - Se sinta a vontade para interagir.

Observação: caso delete o banco de dados, antes de rodar python menu.py faça o comando: python migracao.py

vídeo: https://vimeo.com/858489837/76b11cbe78

--------------COMO ACESSAR O BANCO DE DADOS:----------------

Caso queira acessar o banco de dados você terá que instalar o Python no seu computador se você tiver Windows a própria microsoft store disponibilizará, é só baixar e abrir o Python Idle e após clonar o respositorio, baixe o sqlitebroswer neste link: https://sqlitebrowser.org/.

Como IDE recomendo o Pycharm. 

vídeo: https://vimeo.com/858490833/2206774df2

vídeo continuação: https://vimeo.com/858497308/a07d06d7fb

---------------CONSULTA SQL INTERMEDIARIAS:----------------------

SELECT
    f.id_funcionario as "id do funcionario",
    f.nome as "nome do funcionario",
    SUM(o.tempo_da_operacao_em_segundos)/60 as "Duração de todas operacoes em minutos"
FROM
    funcionarios f
INNER JOIN
    operacao o on o.codigo_funcionario = f.id_funcionario
GROUP BY
    f.id_funcionario, f.nome;

//

SELECT f.nome,
       re.data_hora_entrada
       FROM registro_entrada re
INNER JOIN funcionarios f on f.id_funcionario = re.codigo_funcionario
where nome = 'Levi';

//

SELECT f.nome,
       rs.data_hora_saida
       FROM registro_saida rs
INNER JOIN funcionarios f on f.id_funcionario = rs.codigo_funcionario
where nome = 'Levi';

//

SELECt f.nome as 'Funcionario',
       SUM(o.tempo_da_operacao_em_segundos)/60 as 'Tempo total trabalhado na empresa em segundos'
       FROM funcionarios f 
INNER JOIN operacao o on f.id_funcionario = o.codigo_funcionario
WHERE nome = 'Levi'
 GROUP BY nome;
    

------------------- CONSULTAS SQL SIMPLES:--------------------


SELECT * FROM registro_entrada

SELECT * FROM registro_saida

Select * FROM funcionarios


-----------------AGRADECIMENTOS:-----------------------

Gostaria de Agradecer a W5i por esse desafio que por mais que pareça simples, foi muito divertido de resolver e desafiador.

Lembrando que o objetivo desse programa é que ele seja usado apenas por funcionários, ou seja não é uma boa prática implementar funcionalidades de um administrador, caso um administrador queira consultar a quantidade de funcionários e dados especificos dos funcionarios o ideal é fazer uma consultaSQL. É possível sim colocar esssa opção em código por meio de consultar no programa, porém na prática todo funcionário que passasse pela catraca veria essa opção e poderia ter acesso aos dados de todos os funcionários o que é perigoso.

Então caso vá contribuir para esse projeto, leve isso em conta, a ideia é deixar um código o mais prático possível, quem sabe um dia poderá virar um sistema real.

MEUS CONTATOS PARA DÚVIDAS:

email: levigov21@gmail.com
número: 71994111866

OBS: Esse projeto está licenciado sob a licença MIT.
