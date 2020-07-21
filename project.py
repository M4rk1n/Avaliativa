import sqlite3
banco = sqlite3.connect('banco.db')

1
print("Bem-Vindo ao sistema UniSuporte!")

opcao = input('''[1] Cadatrar Cliente
[2] Atualizar
[3] Listar Computadores
[4] Remover 




''')

sql = banco.cursor()

if opcao == "1":
    cliente = input("Digite o NOME DO CLIENTE: ")
    relato = input("Oque esta acontecendo? ")
    
    
    sql.execute(f"INSERT INTO Clientes (NOME, RELATO, STA) VALUES ('{cliente}','{relato}', 'Na fila' ) ")
    print("Cliente cadastrado!")
    banco.commit()

if opcao == "2":
    id=int(input("DIGITE O ID DO COMPUTADOR: "))
    op2 = input("[1]Manutençao [2]Concluido: ")
    if op2 == "1":
        sql.execute(f"UPDATE Clientes SET STA = 'Manutençao' WHERE id = {id}")
        banco.commit()
        print("Status Atualizado com sucesso!") 
    elif op2 == "2":
        sql.execute(f"UPDATE Clientes SET STA = 'Concluido' WHERE id = {id}")
        banco.commit()
        print("Status Atualizado com sucesso!") 



if opcao == "3":
    stats = int(input("[1]Na fila [2]Manutençao [3]Concluido: "))
    if stats == 1:
        sql.execute(f"SELECT * FROM Clientes WHERE STA = 'Na fila'")
        print(sql.fetchall())
    elif stats == 2:
        sql.execute(f"SELECT * FROM Clientes WHERE STA = 'Manutençao'")
        print(sql.fetchall())
    elif stats == 3:
        sql.execute(f"SELECT * FROM Clientes WHERE STA = 'Concluido'")
        print(sql.fetchall())


if opcao == "4":
    id=int(input("DIGITE O ID DO COMPUTADOR: "))
    sql.execute(f"DELETE  FROM Clientes WHERE ID = '{id}'")
    print("Cliente removido com sucesso!")
    banco.commit()

