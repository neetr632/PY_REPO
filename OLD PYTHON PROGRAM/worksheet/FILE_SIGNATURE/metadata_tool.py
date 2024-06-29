from PIL import Image

image = Image.open(r'C:\Users\neham\OneDrive\Pictures\Screenshots\Screenshot (22).png')
metadata = image.info
print(metadata)
