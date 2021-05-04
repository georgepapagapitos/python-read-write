import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://wallpapercave.com/wp/Qsbbfie.png")

print(f"Status code: {r.status_code}")

image = Image.open(BytesIO(r.content))

path = "./image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Error saving image.")
