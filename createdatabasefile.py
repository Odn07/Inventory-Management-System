from mod1 import *
import sqlite3


def sqliteDataBase(PC, PRD, QTY, CP, SP):
    Con = sqlite3.connect("sqliteDataBase.db") 
    cursor = Con.cursor()
    sqliteTable = """CREATE TABLE sqliteTable (
    PC VARCHAR(255),
    DT DATE,
    PRD VARCHAR(255),
    QTY INTEGER,
    CP INTEGER,
    SP INTEGER);"""           

    cursor.execute(sqliteTable)            
    
    Con.execute("""INSERT INTO sqliteTable VALUES (?, ?, ?, ?, ?, ?)""",(PC, date.today(), PRD, QTY, CP, SP))


    for row in cursor.execute("""SELECT * FROM sqliteTable"""):
        print(row)

    Con.commit()
    Con.close()    


sqliteDataBase(121212, "eva soap", 30, 200, 450)      