from art import Artwork
import os

print("generating images")

os.makedirs("exports", exist_ok=True)

filepath = os.path.join("exports", "export.png")

art = Artwork((2000, 2000))
art.save_to_file(filepath)