import sqlite3

def create_table():
    db = sqlite3.connect('database_magally.db')
    query = """
    CREATE TABLE if not exists UGE 
    (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    scenario TEXT NOT NULL,
    test TEXT NOT NULL, 
    cat TEXT,
    agr TEXT,
    orig TEXT, 
    n_ugts TEXT,  
    objet_du_test TEXT
    )
    """

    cur = db.cursor()
    cur.execute(query)
    db.close()

create_table()

def create_table_ugts():
    db = sqlite3.connect('database_magally.db')
    query = """
    CREATE TABLE if not exists UGTS 
    (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    scenario TEXT NOT NULL,
    test TEXT NOT NULL, 
    cat TEXT,
    agr TEXT,
    orig TEXT, 
    n_ugts TEXT,  
    objet_du_test TEXT
    )
    """

    cur = db.cursor()
    cur.execute(query)
    db.close()

create_table_ugts()

def insert_test(scenario, test, cat, agr, orig, n_ugts, objet_du_test):
    db = sqlite3.connect('database_magally.db')
    query = """
    INSERT INTO UGE(scenario, test, cat, agr, orig, n_ugts, objet_du_test)
    VALUES (?,?,?,?,?,?,?)
    """

    cur = db.cursor()
    cur.execute(query, (scenario, test, cat, agr, orig, n_ugts, objet_du_test))
    db.commit()
    db.close()
    print('terminé')

def insert_test_ugts(scenario, test, cat, agr, orig, n_ugts, objet_du_test):
    db = sqlite3.connect('database_magally.db')
    query = """
    INSERT INTO UGTS(scenario, test, cat, agr, orig, n_ugts, objet_du_test)
    VALUES (?,?,?,?,?,?,?)
    """

    cur = db.cursor()
    cur.execute(query, (scenario, test, cat, agr, orig, n_ugts, objet_du_test))
    db.commit()
    db.close()
    print('terminé')

def get_all_tests(): 
    db = sqlite3.connect('database_magally.db')
    statement = 'SELECT id, scenario, test, cat, agr, orig, n_ugts, objet_du_test FROM UGE'
    cur = db.cursor()
    items = cur.execute(statement)
    itemss = (i for i in items)
    return itemss

def search_test(test):
    db = sqlite3.connect('database_magally.db')
    statement = 'SELECT id, scenario, test, cat, agr, orig, n_ugts, objet_du_test FROM UGE WHERE test=?'
    cur = db.cursor()
    item = cur.execute(statement, (test,))
    itemss = (i for i in item)
    return itemss 

def search_test_ugts(test):
    try:
        # Automatically manage the database connection and cursor
        with sqlite3.connect('database_magally.db') as db:
            cur = db.cursor()
            statement = 'SELECT id, scenario, test, cat, agr, orig, n_ugts, objet_du_test FROM UGTS WHERE test = ?'
            cur.execute(statement, (test,))
            items = cur.fetchall()
            return items
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def get_all_tests_ugts(): 
    db = sqlite3.connect('database_magally.db')
    statement = 'SELECT id, scenario, test, cat, agr, orig, n_ugts, objet_du_test FROM UGTS'
    cur = db.cursor()
    items = cur.execute(statement)
    itemss = (i for i in items)
    return itemss

def delete_test(test_id): 
    db = sqlite3.connect('database_magally.db')
    query = "DELETE FROM UGE WHERE id = ?"
    db.execute(query, (test_id,))
    db.commit()
    db.close()

def delete_test_ugts(test_id): 
    db = sqlite3.connect('database_magally.db')
    query = "DELETE FROM UGTS WHERE id = ?"
    db.execute(query, (test_id,))
    db.commit()
    db.close()

def update_test(test_id, new_scenario, new_test, new_cat, new_agr, new_orig, new_n_ugts, new_objet_du_test):
    db = sqlite3.connect('database_magally.db')
    query = "UPDATE UGE SET scenario=?, test=?, cat=?, agr=?, orig=?, n_ugts=?, objet_du_test=? WHERE ID=?"
    cur = db.cursor()
    cur.execute(query, (new_scenario, new_test, new_cat, new_agr, new_orig, new_n_ugts, new_objet_du_test, test_id)) 
    db.commit()
    db.close()

def update_test_ugts(test_id, new_scenario, new_test, new_cat, new_agr, new_orig, new_n_ugts, new_objet_du_test):
    db = sqlite3.connect('database_magally.db')
    query = "UPDATE UGTS SET scenario=?, test=?, cat=?, agr=?, orig=?, n_ugts=?, objet_du_test=? WHERE ID=?"
    cur = db.cursor()
    cur.execute(query, (new_scenario, new_test, new_cat, new_agr, new_orig, new_n_ugts, new_objet_du_test, test_id)) 
    db.commit()
    db.close()


