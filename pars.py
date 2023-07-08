from bs4 import BeautifulSoup
from urlib.request import urlopen
import requests


group_id = '6121396'
access_token = 'vk1.a.gSEyIt-pAWkxCThAX1O2JbLKrPFJny8Btyuzlj4urbFOEmF35alnDZxjxOy66yh5zadoGgvrtLxS1zZnW2rId5TcALW8GbFNYOHi1HD43Cwt60bF6QR_9ZE0iKzkr2g9_dYnGO7js3zQfx9M27r5kIQAu67IC_REZ95szDyWbKr-BGGNVsbx5WCbEGkO1_ZjiDaTA9cDy9xPlDI6CuC0Qg' 
#мой

#cообществ"vk1.a.Mro2GuCly-fjpf8vtq5BEJP3_TO1040E42Ek4-jOLYAFY7LdT9KeG028jVjLwCE8eakUwq8ugwM7Mez9q3bSU_FjDCru8Jnz1-BLUCXI8LEl_EkV9aOzttYdGD9miNS8_bDqIhupLGM8_Iv9LlnJfSh7naFogl9lvsIeIV8uoXXJTp7Bc0fCFDR5fc7IHas5NvjfJrOgcFCdPOzH_eusbA"
url = f"https://api.vk.com/method/groups.getMembers?group_id={group_id}&access_token={access_token}&v=5.131"

response = requests.get(url)
data = response.json()

if "response" in data:
    members_count = data["response"]["count"]
    members = data["response"]["items"]

soup = BeautifulSoup(str(data), "html.parser")

print(f"Количество участников: {members_count}")
print("Список участников:")
for member in members:
    member_id = soup.find(text=str(member))
    print(member_id)

else:
    print("Ошибка при получении данных")ю
