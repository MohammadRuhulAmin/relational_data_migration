import mysql.connector
from mysql.connector import Error
import time 
from discord import SyncWebhook # type: ignore
from datetime import datetime
connection_destination_db = mysql.connector.connect(
            host='',  
            database='',  
            user='',
            password=''
)

def count_records():
    try:
        query = """select count(id) from pg_service_rnd.challan;"""
        cursor = connection_destination_db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()[0][0]
        return records 
    except Exception as E:
        print(str(E))

def message_send_to_discord():
    try:
        migrated_records = count_records()
        webhook_url = ""
        webhook = SyncWebhook.from_url(webhook_url)
        message = f"\nCurrent time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')},Current challan records migration: ${migrated_records} "
        webhook.send(message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")
        

if __name__ == "__main__":
    message_send_to_discord()
    
    

