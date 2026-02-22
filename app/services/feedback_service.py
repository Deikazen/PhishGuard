import gspread
import json
import os
from datetime import datetime

def get_gspread_client():
 
    if os.path.exists("credentials.json"):
        return gspread.service_account(filename="credentials.json")
    
    creds_json = os.environ.get("GOOGLE_CREDENTIALS")
    if creds_json:
        creds_dict = json.loads(creds_json)
        return gspread.service_account_from_dict(creds_dict)
    
    raise Exception("Kredensial Google Sheets tidak ditemukan!")

def save_feedback_to_sheets(pesan):
    """Menyimpan pesan feedback ke baris baru di Google Sheets."""
    try:
        gc = get_gspread_client()
        
        sh = gc.open("Feedback PhishGuard") 
        worksheet = sh.sheet1 

        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        worksheet.append_row([waktu_sekarang, pesan])
        
        return True 
        
    except Exception as e:
        print(f"Error saving to Google Sheets: {e}")
        raise e 