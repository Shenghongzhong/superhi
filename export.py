from art import make_art
import  os

print("Generating images")
#first 255 is bold red
#second 255 is full green
#third 0 is blue
#fourth255 is full alpha transparency
os.makedirs('exports',exist_ok=True)


filepath = os.path.join('exports', "export.png")
make_art(filepath)

