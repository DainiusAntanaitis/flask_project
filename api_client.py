import requests
import time

# Šiek tiek palaukiame, kad serveris spėtų pilnai pasileisti
time.sleep(5)

BASE_URL = "http://api-server:5000"

def get_users():
    try:
        response = requests.get(f"{BASE_URL}/users")
        print("Visi vartotojai:", response.json())
    except Exception as e:
        print("Klaida jungiantis prie serverio:", e)

def add_user(name, email):
    try:
        payload = {"name": name, "email": email}
        response = requests.post(f"{BASE_URL}/users", json=payload)
        print("Naujas vartotojas:", response.json())
    except Exception as e:
        print("Klaida jungiantis prie serverio:", e)

if __name__ == "__main__":
    get_users()
    add_user("Petras", "petras@example.com")
    get_users()