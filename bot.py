import requests
import time
import random

# --- TVOJI PODACI ---
MY_REF_LINK = "https://99faucet.com/?r=20929"
# Tvoj ispravan FaucetPay mejl
FAUCETPAY_EMAIL = "blazarevic729@gmail.com" 

def pokreni_claim():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1"
    ]
    
    session = requests.Session()
    headers = {
        "User-Agent": random.choice(user_agents),
        "Referer": MY_REF_LINK
    }
    
    try:
        # Nasumična pauza da bi izgledalo kao da čovek klikće
        cekanje = random.randint(10, 25)
        print(f"Čekam {cekanje} sekundi...")
        time.sleep(cekanje)
        
        response = session.post("https://99faucet.com/verify.php", data={
            "address": FAUCETPAY_EMAIL,
            "method": "faucetpay"
        }, headers=headers, timeout=15)
        
        if response.status_code == 200:
            print(f"USPEH: Isplata poslata na {FAUCETPAY_EMAIL}!")
        else:
            print(f"Sajt vratio status: {response.status_code}")
    except Exception as e:
        print(f"Greška u konekciji: {e}")

# --- GLAVNI DEO KOJI POKREĆE BOTER ---
if __name__ == "__main__":
    # Bot će pokušati 2 isplate u jednom krugu (svakih 5 minuta)
    for i in range(2):
        print(f"=== Pokrećem pokušaj {i+1} ===")
        pokreni_claim()
        time.sleep(5)
