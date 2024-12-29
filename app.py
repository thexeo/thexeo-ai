import os
import mysql.connector
from mysql.connector import Error
from email.message import EmailMessage
import smtplib
import torch
import requests
from bs4 import BeautifulSoup

# Connection string assuming MySQL is running locally or on the same network
connection_string = "mysql://root:yourpassword@db:3306/"  # Adjust 'yourpassword' accordingly

def gpu_calculate_rate():
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("CUDA is available! Using GPU.")
    else:
        device = torch.device("cpu")
        print("CUDA is not available. Using CPU.")

    # GPU ile basit bir hesaplama yapalım
    x = torch.tensor([1.0], device=device)
    for _ in range(100000):  # Basit bir döngü ile GPU kullanımı simülasyonu
        x = x * torch.pi

    # Bu hesaplama sonucundan bir rate değeri üretelim (örnek olarak)
    rate = x.item() / 10000000  
    return rate

def fetch_visitors_from_thexeo():
    url = "https://thexeo.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    total_visitors = 0  
    for script in soup.find_all('script'):
        if 'google-analytics.com' in script.get('src', ''):
            total_visitors += 100  

    return total_visitors

def create_database_and_table():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="yourpassword"
        )
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS thexeoai")
        cursor.execute("USE thexeoai")
        
        # Create table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS worker (
            id INT AUTO_INCREMENT PRIMARY KEY,
            workeruser VARCHAR(255),
            rate FLOAT,
            visitors INT
        )
        """)
        print("Database and table created successfully")
    except Error as e:
        print(f"Error creating database or table: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def insert_to_db(rate, visitors):
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="yourpassword",
            database="thexeoai"
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO worker (workeruser, rate, visitors) VALUES (%s, %s, %s)", 
                       ('exampleuser', rate, visitors))
        conn.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"Error inserting data: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def send_email(data):
    msg = EmailMessage()
    msg.set_content(str(data))
    msg['Subject'] = 'Worker Data'
    msg['From'] = os.environ['MAIL_USERNAME']
    msg['To'] = 'your_email@example.com'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ['MAIL_USERNAME'], os.environ['MAIL_PASSWORD'])
        smtp.send_message(msg)

if __name__ == "__main__":
    create_database_and_table()
    rate = gpu_calculate_rate()
    visitors = fetch_visitors_from_thexeo()
    insert_to_db(rate, visitors)
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="yourpassword",
        database="thexeoai"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, workeruser, rate, visitors FROM worker")
    results = cursor.fetchall()
    send_email(results)
    cursor.close()
    conn.close()
