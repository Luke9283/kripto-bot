import requests
import time
import random

# --- TVOJI PODACI ---
MY_REF_LINK = "https://99faucet.com/?r=20929"
FAUCETPAY_EMAIL = "OVDE_UPIŠI_SVOJ_MEJL@gmail.com" # Stavi svoj FaucetPay mejl!

def pokreni_claim():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
        "Mozilla/5.0 (Linux; Android 10; K) Chrome/119.0.0.0 Mobile"
    ]
    session = requests.Session()
    headers = {"User-Agent": random.choice(user_agents), "Referer": MY_REF_LINK}
    
    try:
        response = session.post("https://99faucet.com/verify.php", data={
            "address": FAUCETPAY_EMAIL,
            "method": "faucetpay"
        }, headers=headers)
        if response.status_code == 200:
            print("Isplata poslata!")
    except:
        print("Greška.")

if __name__ == "__main__":
    for i in range(5):
        pokreni_claim()
        time.sleep(10)
