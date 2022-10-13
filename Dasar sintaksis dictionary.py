"""
Dasar sintaksis dictionary
"""

users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "sincere@aprl.biz",
    "adress": {
        "street": "Amarilis 3",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
    }
}
print(users)
print(users["name"])
print(users["username"])
print(users["email"])
print(users["adress"])
print(users["adress"]["street"])

print("\nUbah Format JSON")
import json
result = json.dumps(users)
print(type(result))
print(result)

with open('result.json', 'w') as file:
    json.dump(users, file)


