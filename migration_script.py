import mysql.connector
from mysql.connector import Error

from discord import SyncWebhook # type: ignore
from datetime import datetime
connection_destination_db = mysql.connector.connect(
            host='',  
            database='pg_service_rnd',  
            user='',
            password=''
)

connection_source_db = mysql.connector.connect(
            host='',  
            database='',  
            user='',
            password=''
)


def message_send_to_discord():
    try:
        webhook_url = "https://discord.com/api/webhooks/1288828610026672200/l7T-5Z9KXnYXEsrXxm5pJ_ExkD906qC6XicL83JzZL7AdDZhocp072LbrBgCR_Oek0Q8"
        webhook = SyncWebhook.from_url(webhook_url)
        message = f"Data process successful\nCurrent time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        webhook.send(message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")



def get_total_iteration():
    try:
        cursor = connection_source_db.cursor()
        query = """
        SELECT COUNT(id) FROM pg_service.challan c WHERE  c.challan_generation_status = 1 AND c.transaction_date < CURDATE();
        """
        cursor.execute(query)
        records = cursor.fetchall()[0][0]
        return records
    except Exception as E:
        print(str(E))


def call_stored_procedure():
    try:
        
        iteration = get_total_iteration()
        if connection_destination_db.is_connected():
            cursor = connection_destination_db.cursor()

            for i in range(0,iteration):
                cursor.callproc('challan_data_migration_procedure')
                for result in cursor.stored_results():
                    print(result.fetchall())  
            # Fetch results (if any)
            

            print("Stored procedure called successfully.")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection_destination_db.is_connected():
            message_send_to_discord()
            cursor.close()
            connection_destination_db.close()
            print("MySQL connection closed.")

# Call the function to execute the procedure
if __name__ == "__main__":
    call_stored_procedure()
