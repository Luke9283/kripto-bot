import requests
import concurrent.futures

# TVOJ GMAIL JE SPREMAN
MAIL = "blazarevic@gmail.com"

SAJTOVI = [
    "https://99faucet.com/api/v1/faucet/claim",
    "https://viefaucet.com/api/v1/faucet/claim",
    "https://bfaucet.xyz/api/v1/faucet/claim"
]

def napadni(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    try:
        r = requests.post(url, data={"email": MAIL, "method": "FaucetPay"}, headers=headers, timeout=15)
        print(f"BUM! Sajt {url} odgovorio sa: {r.status_code}")
    except:
        print(f"Sajt {url} poklekao pod pritiskom!")

def main():
    print(f"POKREĆEM ZEMLJOTRES ZA: {MAIL}")
    # ThreadPoolExecutor udara na sve sajtove odjednom!
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(napadni, SAJTOVI)

if __name__ == "__main__":
    main()
