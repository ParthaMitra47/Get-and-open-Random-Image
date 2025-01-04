import requests
import os

def fetch_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"Image saved to {save_path}")
        os.startfile(save_path)  # Automatically opens the image file
    else:
        print(f"Error: {response.status_code}")


image_url = "https://picsum.photos/200"

#path where to save file
save_path = "C:\Users\name\Desktop\image.jpeg" 
fetch_image(image_url, save_path)

