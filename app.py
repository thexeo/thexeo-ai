import os
import mysql.connector
from email.message import EmailMessage
import smtplib
import torch
import requests
from bs4 import BeautifulSoup

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
    rate = x.item() / 10000000  # Bu sadece bir örnek, gerçek kullanımda rate hesaplama algoritmanız olacak
    return rate

def fetch_visitors_from_thexeo():
    # This is a mock function. In reality, you would need to find or implement a way to get visitor data from Google Analytics
    # Here's a simple example using BeautifulSoup to fetch some data from the website (not actual GA data)
    url = "https://thexeo.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Mock data since real-time GA data isn't directly accessible via scraping
    # You would need to authenticate and use Google Analytics API for real data
    total_visitors = 0  # Here you might parse out a number from the page or get it from GA API
    for script in soup.find_all('script'):
        if 'google-analytics.com' in script.get('src', ''):
            # Example: Parsing some data from GA script - this is extremely simplified
            total_visitors += 100  # Mocking actual visitor count

    return total_visitors

def insert_to_db(rate, visitors):
    conn = mysql.connector.connect(
        host="db",
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE']
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO worker (id, workeruser, rate, visitors) VALUES (%s, %s, %s, %s)", 
                   (None, 'exampleuser', rate, visitors))  # id otomatik artacak
    conn.commit()
    cursor.close()
    conn.close()

def send_email(data):
    msg = EmailMessage()
    msg.set_content(str(data))
    msg['Subject'] = 'Worker Data'
    msg['From'] = os.environ['MAIL_USERNAME']
    msg['To'] = 'thexeo@thexeo.com'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ['MAIL_USERNAME'], os.environ['MAIL_PASSWORD'])
        smtp.send_message(msg)

if __name__ == "__main__":
    rate = gpu_calculate_rate()
    visitors = fetch_visitors_from_thexeo()
    insert_to_db(rate, visitors)
    conn = mysql.connector.connect(
        host="db",
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE']
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, workeruser, rate, visitors FROM worker")
    results = cursor.fetchall()
    send_email(results)
    cursor.close()
    conn.close()
