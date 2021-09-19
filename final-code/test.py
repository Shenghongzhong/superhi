from art import Artwork
from blocks import BlocksArtwork
from circles import CirclesArtwork
from lines import LinesArtwork
import os

print("generating images")

os.makedirs("test", exist_ok=True)

for i in range(1, 6):
  filepath = os.path.join("test", f"grad-{i}.png")

  art = Artwork(debug=True)
  art.save_to_file(filepath)

for i in range(1, 6):
  filepath = os.path.join("test", f"blocks-{i}.png")

  art = BlocksArtwork(debug=True)
  art.save_to_file(filepath)

for i in range(1, 6):
  filepath = os.path.join("test", f"circles-{i}.png")

  art = CirclesArtwork(debug=True)
  art.save_to_file(filepath)

for i in range(1, 6):
  filepath = os.path.join("test", f"lines-{i}.png")

  art = LinesArtwork(debug=True)
  art.save_to_file(filepath)