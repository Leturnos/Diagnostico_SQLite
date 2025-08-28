import sqlite3
conn = sqlite3.connect("testeIA.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Chance (
            id INTEGER PRIMARY KEY,
            garganta INT, 
            febre INT, 
            espirros INT, 
            tosse INT,
            fg INT,
            fe INT,
            ft INT
        )
''')
cursor.execute("SELECT COUNT(*) FROM Chance")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO Chance (id, garganta, febre, espirros, tosse, fg, fe, ft) VALUES (1, 10, 15, 75, 35, 30, 90, 20)")
    conn.commit()

while True:
    Garganta = input("Você está com dor de Garganta? (s/n) >")
    if Garganta !="s" and Garganta != "n":
        print("Resposta inválida, por favor digite s para sim e n para não")
        continue
    Febre = input("Você está com febre? (s/n) >")
    if Febre !="s" and Febre != "n":
        print("Resposta inválida, por favor digite s para sim e n para não")
        continue
    Espirros = input("Você está espirrando? (s/n) >")
    if Espirros !="s" and Espirros != "n":
        print("Resposta inválida, por favor digite s para sim e n para não")
        continue
    Tosse = input("Você está tossindo? (s/n) >")
    if Tosse !="s" and Tosse != "n":
        print("Resposta inválida, por favor digite s para sim e n para não")
        continue
    break
    
cursor.execute("SELECT * FROM Chance")
pesos = cursor.fetchone()
# O pesos[0] seria o id
peso_garganta = pesos[1]
peso_febre = pesos[2]
peso_espirros = pesos[3]
peso_tosse = pesos[4]
peso_fg = pesos[5]
peso_fe = pesos[6]
peso_ft = pesos[7]

chance = 0
fg = False
fe = False
ft = False

if Febre == "s" and Garganta == "s":
    chance += peso_fg
    fg = True
if Febre == "s" and Espirros == "s":
    chance += peso_fe
    fe = True
if Febre == "s" and Tosse == "s":
    chance += peso_ft
    ft = True

if Garganta == "s" and fg == False:
    chance += peso_garganta
if Febre == "s" and fg == False and fe == False and ft == False:
    chance += peso_febre
if Espirros == "s" and fe == False:
    chance += peso_espirros
if Tosse == "s" and ft == False:
    chance += peso_tosse

if chance >= 50:
    print(f"{chance}%, Você está resfriado")
else:
    print(f"{chance}%, Você não está resfriado")

while True:
    acertei = input("Eu acertei o diagnóstico? (s/n) >")
    if acertei == "s":
        print("Obrigado pelo retorno")
        conn.close()
        exit()
    elif acertei == "n":
        print("Ok, vou ajustar os pesos...")
        if Febre == "s" and Garganta == "s":
            cursor.execute("UPDATE Chance SET fg = ? WHERE id = 1", (peso_fg - 2,))
            
        if Febre == "s" and Espirros == "s":
            cursor.execute("UPDATE Chance SET fe = ? WHERE id = 1", (peso_fe - 2,))

        if Febre == "s" and Tosse == "s":
            cursor.execute("UPDATE Chance SET ft = ? WHERE id = 1", (peso_ft - 2,))

        if Garganta == "s" and fg == False:
            cursor.execute("UPDATE Chance SET garganta = ? WHERE id = 1", (peso_garganta - 2,))

        if Febre == "s" and fg == False and fe == False and ft == False:
            cursor.execute("UPDATE Chance SET febre = ? WHERE id = 1", (peso_febre - 2,))

        if Espirros == "s" and fe == False:
            cursor.execute("UPDATE Chance SET espirros = ? WHERE id = 1", (peso_espirros - 2,))

        if Tosse == "s" and ft == False:
            cursor.execute("UPDATE Chance SET tosse = ? WHERE id = 1", (peso_tosse - 2,))
            
        conn.commit()
        print("Pesos ajustados com sucesso, obrigado pelo retorno")
        break
    else:
        print("Resposta inválida, por favor digite s para sim e n para não")
        continue