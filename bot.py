import requests
import time
import random

# --- TVOJI PODACI ---
MY_REF_LINK = "https://99faucet.com/?r=20929"
# Ovde obavezno stavi svoj pravi FaucetPay mejl!
FAUCETPAY_EMAIL = "UPIŠI_SVOJ_MEJL@gmail.com" 

def pokreni_claim():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) Mobile/15E148"
    ]
    session = requests.Session()
    headers = {"User-Agent": random.choice(user_agents), "Referer": MY_REF_LINK}
    
    try:
        # Čekamo malo pre klika da ne provale bota
        time.sleep(random.randint(5, 15))
        
        response = session.post("https://99faucet.com/verify.php", data={
            "address": FAUCETPAY_EMAIL,
            "method": "faucetpay"
        }, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("USPEH: Isplata poslata!")
        else:
            print(f"Status: {response.status_code}")
    except:
        print("Greška u konekciji.")

if __name__ == "__main__":
    for i in range(2):
        pokreni_claim()
        time.sleep(5)
