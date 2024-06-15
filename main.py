import requests
import time
from datetime import datetime
from config import API_KEY

headers = {
    'Authorization': f"Bearer {API_KEY}",
}

def get_plan():
    return requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers)

def ttt():
    return datetime.now().time().strftime("%H:%M:%S")

print(f"{ttt()} Démarage")
old = get_plan()
print(f"{ttt()} OLD ->", old.text)
while True :
    print(f"\r{ttt()} Recherche", end='', flush=True)
    new = get_plan()
    if(old.text != new.text):
        print(f"\n{ttt()} NEW ->", new.text)
        break
    else:
        old = new
        time.sleep(1.5)
plan_id = new.json()[0]['id']
response = requests.get(f"https://shiftheroes.fr/api/v1/plannings/{plan_id}/shifts", headers=headers)
shifts = response.json()
for item in shifts:
    print(f"{ttt()} ID : {item['id']}  Places : {item['seats_taken']}/{item['seats']}")
    response = requests.post(f"https://shiftheroes.fr/api/v1/plannings/{plan_id}/shifts/{item['id']}/reservations", headers=headers)
    print(response.text)
