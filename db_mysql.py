import mysql.connector

import pandas as pd


def connect_database():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*******",
    database="test_1_magally"
    )

    mycursor = mydb.cursor()
    return mycursor, mydb

def create_table_uge():
    mycursor, mydb = connect_database()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS UGE (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            scenario TEXT NOT NULL,
            test TEXT NOT NULL, 
            cat TEXT,
            agr TEXT,
            orig TEXT, 
            n_ugts TEXT,  
            objet_du_test TEXT
        )
    """

    mycursor.execute(create_table_query)
    mydb.commit()
    mydb.close()

create_table_uge()

def create_table_ugts():
    mycursor, mydb = connect_database()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS UGTS (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            scenario TEXT NOT NULL,
            test TEXT NOT NULL, 
            cat TEXT,
            agr TEXT,
            orig TEXT, 
            n_ugts TEXT,  
            objet_du_test TEXT
        )
    """

    mycursor.execute(create_table_query)
    mydb.commit()
    mydb.close()

create_table_ugts()

def insert_test_uge(scenario, test, cat, agr, orig, n_ugts, objet_du_test):

    mycursor, mydb = connect_database()

    query = """
    INSERT INTO UGE(scenario, test, cat, agr, orig, n_ugts, objet_du_test)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    val = scenario, test, cat, agr, orig, n_ugts, objet_du_test

    mycursor.execute(query, val)
    mydb.commit()
    mydb.close()

def insert_test_ugts(scenario, test, cat, agr, orig, n_ugts, objet_du_test):

    mycursor, mydb = connect_database()

    query = """
    INSERT INTO UGTS(scenario, test, cat, agr, orig, n_ugts, objet_du_test) VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    val = scenario, test, cat, agr, orig, n_ugts, objet_du_test

    mycursor.execute(query, val)
    mydb.commit()
    mydb.close()

def get_all_tests_uge(): 

    mycursor, mydb = connect_database()

    statement = 'SELECT id, scenario, test, cat, agr, orig, n_ugts, objet_du_test FROM UGE'
    mycursor.execute(statement)
    items = mycursor.fetchall()
    return items

def get_all_tests_ugts(): 

    mycursor, mydb = connect_database()

    statement = 'SELECT id, scenario, test, cat, agr, orig, n_ugts, objet_du_test FROM UGTS'
    mycursor.execute(statement)
    items = mycursor.fetchall()
    return items

def search_test_uge(test):

    mycursor, mydb = connect_database()
    
    statement = 'SELECT id, scenario, test, cat, agr, orig, n_ugts, objet_du_test FROM UGE WHERE test=%s'
    item = mycursor.execute(statement, (test,))
    items = mycursor.fetchall()
    return items


def delete_test_uge(test_id): 

    mycursor, mydb = connect_database()

    query = "DELETE FROM UGE WHERE id = %s"
    mydb.execute(query, (test_id,))
    mydb.commit()
    mydb.close()

def delete_test_ugts(test_id): 

    mycursor, mydb = connect_database()

    query = "DELETE FROM UGTS WHERE id = %s"
    mycursor.execute(query, (test_id,))
    mydb.commit()
    mydb.close()

def delete_test_ugts_title(test_title): 

    mycursor, mydb = connect_database()

    query = "DELETE FROM UGTS WHERE test = %s"
    mycursor.execute(query, (test_title,))
    mydb.commit()
    mydb.close()

def update_test_uge(test_id, new_scenario, new_test, new_cat, new_agr, new_orig, new_n_ugts, new_objet_du_test):

    mycursor, mydb = connect_database()

    query = "UPDATE UGE SET scenario=%s, test=%s, cat=%s, agr=%s, orig=%s, n_ugts=%s, objet_du_test=%s WHERE ID=%s"

    mycursor.execute(query, (new_scenario, new_test, new_cat, new_agr, new_orig, new_n_ugts, new_objet_du_test, test_id)) 
    mydb.commit()
    mydb.close()

def update_test_ugts(test_id, new_scenario, new_test, new_cat, new_agr, new_orig, new_n_ugts, new_objet_du_test):

    mycursor, mydb = connect_database()

    query = "UPDATE UGTS SET scenario=%s, test=%s, cat=%s, agr=%s, orig=%s, n_ugts=%s, objet_du_test=%s WHERE ID=%s"

    mycursor.execute(query, (new_scenario, new_test, new_cat, new_agr, new_orig, new_n_ugts, new_objet_du_test, test_id)) 
    mydb.commit()
    mydb.close()

def create_table_version_UGE(table_name):
    mycursor, mydb = connect_database()

    query = f"""
    CREATE TABLE V_{table_name}_UGE (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        scenario TEXT NOT NULL,
        test TEXT NOT NULL, 
        cat TEXT,
        agr TEXT,
        orig TEXT, 
        n_ugts TEXT,  
        objet_du_test TEXT
        )
    """

    try:
        mycursor.execute(query)
        mydb.commit()
        print(f"Table '{table_name}' created successfully.")
    except Exception as e:
        print(f"Error creating table '{table_name}': {e}")
    finally:
        mydb.close()

def create_table_version_UGTS(table_name):
    mycursor, mydb = connect_database()

    query = f"""
    CREATE TABLE V_{table_name}_UGTS (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        scenario TEXT NOT NULL,
        test TEXT NOT NULL, 
        cat TEXT,
        agr TEXT,
        orig TEXT, 
        n_ugts TEXT,  
        objet_du_test TEXT
        )
    """

    try:
        mycursor.execute(query)
        mydb.commit()
        print(f"Table '{table_name}' created successfully.")
    except Exception as e:
        print(f"Error creating table '{table_name}': {e}")
    finally:
        mydb.close()

def search_test_ugts(test):
    mycursor, mydb = connect_database()
    
    statement = 'SELECT id, scenario, test, cat, agr, orig, n_ugts, objet_du_test FROM UGTS WHERE test=%s'
    try:
        print(f"Executing query: {statement} with test={test}")
        mycursor.execute(statement, (test,))
        items = mycursor.fetchall()
        print(f"Query result: {items}")
    except Exception as e:
        print(f"Error occurred during fetching data: {e}")
        items = None
    finally:
        mydb.close()  # Ensure the connection is closed even if an error occurs

    if items:
        return items  # Return all matching records
    else:
        return None  # Return None if no record is found

def insert_test_in_version_ugts(test_name, version_name):
    print(f"Starting insert_test_in_version_ugts with test_name={test_name}, version_name={version_name}")
    mycursor, mydb = connect_database()

    try:
        results = search_test_ugts(test_name)
        
        if results:
            for result in results:
                print(f"search_test_ugts result: {result}")
                _, scenario, test, cat, agr, orig, n_ugts, objet_du_test = result

                query = f"""
                INSERT INTO V_{version_name}_UGTS (scenario, test, cat, agr, orig, n_ugts, objet_du_test)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                values = (scenario, test, cat, agr, orig, n_ugts, objet_du_test)
                
                print(f"Executing insert query: {query}")
                print(f"With values: {values}")

                mycursor.execute(query, values)
                mydb.commit()
                print("Insert query executed and committed successfully.")
        else:
            print(f"No results found for test_name={test_name}")
    except Exception as e:
        print(f"Error occurred during inserting data: {e}")
    finally:
        mydb.close()
        print("Database connection closed.")

def get_all_tests_ugts_version(version): 

    mycursor, mydb = connect_database()

    statement = f"""SELECT id, scenario, test, cat, agr, orig, n_ugts, objet_du_test FROM V_{version}_UGTS"""
    mycursor.execute(statement)
    items = mycursor.fetchall()
    return items

def save_all_to_csv_ygts(version): 
    print(f"Version here 3: {version}")
    cursor, mydb = connect_database()

    if version == 0: 
        print(f"Version here 4: {version}")
        statement = f"""SELECT id, scenario, test, cat, agr, orig, n_ugts, objet_du_test FROM UGTS"""
    else: 
        statement = f"""SELECT id, scenario, test, cat, agr, orig, n_ugts, objet_du_test FROM V_{version}_UGTS"""
        
    excel_file_path = 'exported_data.xlsx'
    
    data_frame = pd.read_sql(statement, mydb)
    data_frame.to_excel(excel_file_path, index=False)