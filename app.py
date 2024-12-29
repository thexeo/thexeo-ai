import os
import mysql.connector
from mysql.connector import Error
import requests
import torch
from bs4 import BeautifulSoup

# Connection string for MySQL
connection_string = "mysql://root:yourpassword@db:3306/"  # Adjust 'yourpassword' accordingly

# WordPress API details
wp_api_url = "https://thexeo.com/wp-json/thexeoai/v1/collectdata"

def gpu_calculate_rate():
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("CUDA is available! Using GPU.")
    else:
        device = torch.device("cpu")
        print("CUDA is not available. Using CPU.")

    # Perform a simple calculation using GPU
    x = torch.tensor([1.0], device=device)
    for _ in range(100000):  # Simple loop to simulate GPU usage
        x = x * torch.pi

    # Generate a rate value from this calculation (example)
    rate = x.item() / 10000000  
    return rate

def fetch_visitors_from_thexeo():
    url = "https://thexeo.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    total_visitors = 0  
    for script in soup.find_all('script'):
        if 'google-analytics.com' in script.get('src', ''):
            total_visitors += 100  # Mocking actual visitor count

    return total_visitors

def create_database():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="yourpassword"
        )
        cursor = conn.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS thexeoai")
        print("Database created successfully")
    except Error as e:
        print(f"Error creating database: {e}")
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

def send_data_to_wordpress(data):
    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(
            wp_api_url, 
            headers=headers, 
            json=data
        )
        response.raise_for_status()  # Will raise an exception for bad status codes
        print(f"Data sent to WordPress. Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error sending data to WordPress: {e}")

if __name__ == "__main__":
    create_database()
    
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
    
    # Send data to WordPress instead of emailing
    send_data_to_wordpress({"data": [dict(zip(['id', 'workeruser', 'rate', 'visitors'], row)) for row in results]})
    
    cursor.close()
    conn.close()
