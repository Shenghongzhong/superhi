from PIL import Image   

print("hello")
#first 255 is bold red
#second 255 is full green
#third 0 is blue
#fourth255 is full alpha transparency
img = Image.new("RGBA", (500, 500),color=(255,255,0,255))

img.save("test.png")

