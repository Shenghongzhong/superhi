from art import Artwork
from PIL import ImageDraw
import os
import random

class CirclesArtwork(Artwork):
  def generate(self):
    drawer = ImageDraw.Draw(self.img)

    for (x, y) in self.get_random_points():
      color = self.get_color_at_point(x, y)

      radius = random.randint(2, 10)

      drawer.ellipse([
        (x - radius, y - radius),
        (x + radius, y + radius)
      ], fill=color)


if __name__ == "__main__":
  print("generating an artwork from circles.py")
  os.makedirs("test", exist_ok=True)
  filepath = os.path.join("test", "circles.png")
  
  art = CirclesArtwork()
  art.save_to_file(filepath)