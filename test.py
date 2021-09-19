from art import make_art
import  os

print("Generating images")
#first 255 is bold red
#second 255 is full green
#third 0 is blue
#fourth255 is full alpha transparency
os.makedirs('test',exist_ok=True)

for i in range(1,11):
    filepath = os.path.join('test',f"test-{i}.png")
    make_art(filepath)

