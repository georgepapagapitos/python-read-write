import requests

param = str(input("Search for something: "))

r = requests.get(f"https://www.google.com/search?q={param}")
print(f"Status: {r.status_code}")

print(r.url)

f = open("./page.html", "w+")
f.write(r.text)

