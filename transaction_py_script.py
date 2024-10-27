import mysql.connector
from mysql.connector import Error

def db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='transaction',
            user='root',
            password='ruhulamin'
        )
        return connection
    
    except Error as e:
        print(str(e))

def python_data_migration():
    try:
        connection = db_connection()
        cursor = connection.cursor()
        connection.start_transaction()
        query_a = """insert into tablea(id,email)values(82,"x77ruhul@ba-systems.com");"""
        cursor.execute(query_a)
        tablea_id = cursor.lastrowid
        print(tablea_id)
        query_child = """insert into tablea_child(id,table_a_id,info)values(5,%s,"information");"""
        cursor.execute(query_child,(tablea_id,))
        
        table_a_child_id = cursor.lastrowid
        query_child_children = """insert into tablea_child_children(id,table_a_child_children_id,info)values(2,%s,"info");"""
        cursor.execute(query_child_children,(table_a_child_id,))
        cursor = connection.cursor()
        connection.commit()
        print("Transaction successful, data inserted into all tables.")

    except Error as e:
        connection.rollback()
        print("Transaction failed, rolling back:", e)

    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")


if __name__ == "__main__":
    print(python_data_migration())
        
        


