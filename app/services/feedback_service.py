from pandas._libs.hashtable import mode
import csv
import os
from datetime import datetime
from app.models.model_loader import CSV_FILE

def init_csv():
    if not os.path.isfile(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8' ) as file:
            writer = csv.writer(file)
            writer.writerow(['Tanggal & Waktu', 'Pesan Feedback'])

def save_feedback_to_csv(pesan: str) -> bool:
    try:
        this_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(CSV_FILE, mode='a', newline='', encoding='utf-8' ) as file:
            writer = csv.writer(file)
            writer.writerow([this_time, pesan])
        return True
    except Exception as e:
        print(f"Error saving to CSV: {e}")
        return False
