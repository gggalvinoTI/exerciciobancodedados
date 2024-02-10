import sqlite3
conexao = sqlite3.connect('BancoDeDados')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
###cursor.execute('CREATE TABLE Alunos(Id INT, Nome VARCHAR(100), Idade INT (100), Curso VARCHAR(100) );')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior
#cursor.execute('INSERT INTO Alunos(Id,Nome,Idade,Curso) VALUES(1,"Eduardo Gomes","25","Administração" )')
cursor.execute('INSERT INTO Alunos(Id,Nome,Idade,Curso) VALUES(2,"Camila Oliveira","27","Psicologia" )')
cursor.execute('INSERT INTO Alunos(Id,Nome,Idade,Curso) VALUES(3,"Ellen Fernandez","23","Direito" )')
cursor.execute('INSERT INTO Alunos(Id,Nome,Idade,Curso) VALUES(4,"Talita Vieira","21","Nutrição" )')
cursor.execute('INSERT INTO Alunos(Id,Nome,Idade,Curso) VALUES(5,"Leonardo Nogueira","28","Matemática" )')
conexao.commit()
conexao.close()