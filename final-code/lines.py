from art import Artwork
from PIL import ImageDraw
import os
import random
import math

class LinesArtwork(Artwork):
  def generate(self):
    drawer = ImageDraw.Draw(self.img)

    for (x, y) in self.get_random_points():
      color = self.get_color_at_point(x, y)

      length = random.randint(2, 10)
      angle = random.uniform(0, 3.141)

      sx = length * math.sin(angle)
      sy = length * math.cos(angle)

      drawer.line([
        (x - sx, y - sy),
        (x + sx, y + sy)
      ], fill=color)


if __name__ == "__main__":
  print("generating an artwork from lines.py")
  os.makedirs("test", exist_ok=True)
  filepath = os.path.join("test", "lines.png")
  
  art = LinesArtwork()
  art.save_to_file(filepath)