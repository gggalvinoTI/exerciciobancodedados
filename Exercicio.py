import sqlite3
conexao = sqlite3.connect('BancoDeDados')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
###cursor.execute('CREATE TABLE Alunos(Id INT, Nome VARCHAR(100), Idade INT (100), Curso VARCHAR(100) );')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior
#cursor.execute('INSERT INTO Alunos(Id,Nome,Idade,Curso) VALUES(1,"Eduardo Gomes","25","Administração" )')
#cursor.execute('INSERT INTO Alunos(Id,Nome,Idade,Curso) VALUES(2,"Camila Oliveira","27","Psicologia" )')
#cursor.execute('INSERT INTO Alunos(Id,Nome,Idade,Curso) VALUES(3,"Ellen Fernandez","23","Direito" )')
#cursor.execute('INSERT INTO Alunos(Id,Nome,Idade,Curso) VALUES(4,"Talita Vieira","21","Nutrição" )')
#cursor.execute('INSERT INTO Alunos(Id,Nome,Idade,Curso) VALUES(5,"Leonardo Nogueira","28","Matemática" )')

#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados:
    print (alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT nome,idade FROM alunos where Idade >20')
for alunos in dados:
    print (alunos)

#alterar curso dos aluno para engenharia
cursor.execute('UPDATE alunos SET curso = "Engenharia" WHERE nome = "Talita Vieira"') 
cursor.execute('UPDATE alunos SET curso = "Engenharia" WHERE nome = "Ellen Fernandez"') 
#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')
for aluno in dados:
    print(aluno)

#d) Contar o número total de alunos na tabela
cursor.execute('SELECT COUNT(*) FROM alunos')
total_alunos = cursor.fetchone()[0]
print("Total de alunos:", total_alunos)
    
 #4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade = "32" WHERE nome = "Camila Oliveira"')

#b) Remova um aluno pelo seu ID.  
cursor.execute('DELETE FROM alunos where Id=1') 

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes (Id INT, Nome VARCHAR(100), Idade INT (100), Saldo FLOAT(100) );')
cursor.execute('INSERT INTO clientes(Id,Nome,Idade,Saldo) VALUES(1,"Roberto Lara","25","1250,00" )')
cursor.execute('INSERT INTO clientes(Id,Nome,Idade,Saldo) VALUES(2,"Peterson Alves","45","12,01" )')
cursor.execute('INSERT INTO clientes(Id,Nome,Idade,Saldo) VALUES(3,"Tiago Iork","24","188,90" )')
cursor.execute('INSERT INTO clientes(Id,Nome,Idade,Saldo) VALUES(4,"Leandro Hasun","58","670,40" )')
cursor.execute('INSERT INTO clientes(Id,Nome,Idade,Saldo) VALUES(5,"Daniel Oliveira","36","726,70" )')
cursor.execute('INSERT INTO clientes(Id,Nome,Idade,Saldo) VALUES(6,"Fernando ALmeida","47","5698,65" )')
cursor.execute('INSERT INTO clientes(Id,Nome,Idade,Saldo) VALUES(7,"Geraldo Rodrigues","28","56,98" )')
cursor.execute('INSERT INTO clientes(Id,Nome,Idade,Saldo) VALUES(8,"Laercio Santos","71","93,04" )')
cursor.execute('INSERT INTO clientes(Id,Nome,Idade,Saldo) VALUES(9,"Lucas Morais","48","23,05" )')
cursor.execute('INSERT INTO clientes(Id,Nome,Idade,Saldo) VALUES(10,"Juliano Silveira","64","81250,00" )')
conexao.commit()
conexao.close()