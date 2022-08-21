from PIL import Image

img_d = input("Enter the directory where the image is located.\n---> ")

img = Image.open(img_d)

print(f"\nWidth: {img.width}, height: {img.height}")

width = int(input("\nEnter the new width.\n---> "))
height = int(input("\nEnter the new height.\n---> "))

img = img.resize((width, height))

img.save("Resized Image.png")

print("\nResized Image Saved as Resized Image.png")