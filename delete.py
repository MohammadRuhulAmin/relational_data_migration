import mysql.connector
from mysql.connector import Error

connection_destination_db = mysql.connector.connect(
            host='localhost',  
            database='cdc_db',  
            user='root',
            password='ruhulamin'
);


def delete_process():
    try:
        cursor = connection_destination_db.cursor()
        query = """SELECT id,COUNT(id) FROM cdc_db.pg_wallet_payment_log
                GROUP BY id
                HAVING COUNT(id)>1"""
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record[0],record[1])
            query_delete = """delete from cdc_db.pg_wallet_payment_log where id = %s  limit 1;"""
            cursor.execute(query_delete,(record[0],))
            print("Deleted: ", record[0])
            connection_destination_db.commit()
            
        
    except Exception as E:
        print(str(E))
        

if __name__ == "__main__":
    delete_process()