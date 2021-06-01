import sqlite3

con = sqlite3.connect('DB.db')
cur = con.cursor()


# Get all items from DB
def getItems():
    sql = "SELECT ID, Name, Price, Category_ID, Description FROM Items"
    output = cur.execute(sql).fetchall()
    return output


# Get a specific Item from DB
def getItem(ID):
    sql = "SELECT ID, Name, Price, Category_ID, Description  FROM Items WHERE ID = ?"
    output = cur.execute(sql, (ID,)).fetchall()
    return output
