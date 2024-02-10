import sqlite3
conexao = sqlite3.connect('BancoDeDados')
cursor = conexao.cursor()
#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE Alunos(Id INT, Nome VARCHAR(100), Idade INT (100), Curso VARCHAR(100) );')
conexao.commit()
conexao.close()