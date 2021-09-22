from art import Artwork
import  os


print("Generating images")
#first 255 is bold red
#second 255 is full green
#third 0 is blue
#fourth255 is full alpha transparency
os.makedirs('exports',exist_ok=True)

filepath = os.path.join('exports', "export.png")
art = Artwork((2000,2000))
art.save_to_file(filepath)

