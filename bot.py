import requests
import time
import random

# --- TVOJI PODACI ---
MY_REF_LINK = "https://99faucet.com/?r=20929"
# OVDE UPIŠI SVOJ PRAVI MEJL IZMEĐU NAVODNIKA
FAUCETPAY_EMAIL = "TVOJ_MEJL@gmail.com" 

def pokreni_claim():
    # Različiti uređaji da te sajt ne provali
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36"
    ]
    
    # Nasumična pauza pre klika (između 10 i 30 sekundi)
    cekanje = random.randint(10, 30)
    print(f"Čekam {cekanje} sekundi pre klika...")
    time.sleep(cekanje)

    session = requests.Session()
    headers = {
        "User-Agent": random.choice(user_agents),
        "Referer": MY_REF_LINK
    }
    
    try:
        # Slanje zahteva sajtu
        response = session.post("https://99faucet.com/verify.php", data={
            "address": FAUCETPAY_EMAIL,
            "method": "faucetpay"
        }, headers=headers, timeout=15)
        
        if response.status_code == 200:
            print(f"USPEH: Isplata poslata na {FAUCETPAY_EMAIL}!")
        else:
            print(f"Sajt vratio grešku: {response.status_code}")
    except Exception as e:
        print(f"Greška u konekciji: {e}")

# --- GLAVNI DEO KOJI POKREĆE SVE ---
if __name__ == "__main__":
    # Bot će uraditi 2 klika u jednom krugu (jedan krug je 5 minuta)
    for i in range(2):
        print(f"Pokrećem pokušaj broj {i+1}...")
        pokreni_claim()
        # Kratka pauza između dva klika unutar istog kruga
        time.sleep(random.randint(5, 10))
