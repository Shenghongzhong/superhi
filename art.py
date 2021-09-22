from hashlib import blake2b
from PIL import Image   
import os
import random
import colorsys
from noise import pnoise2

class Artwork():
    def __init__(self,size=(500,500), grain_level = 0.1, noise_level = 1.5, noise_shift = 2.0):
        self.img =  Image.new("RGBA", size)
        self.palette = ( 
            self.create_random_color(),
            self.create_random_color(),
            self.create_random_color(),
            self.create_random_color()
        )
        self.noise_level = noise_level
        self.noise_shift = noise_shift
        self.noise_base = random.randint(0, 999)
        self.grain_level =  grain_level
        self.generate()
    
    def generate(self):
        for x in range(self.img.width):
            for y in range(self.img.height):
                color = self.get_color_at_point(x,y)

                self.img.putpixel((x,y), color)

    def make_grain(self):
        if self.grain_level >0:
            return random.uniform(-0.5 * self.grain_level, 0.5 * self.grain_level)
        else:
            return 0
    
    def make_noise(self, px, py):
        return self.noise_level * pnoise2(
            px * self.noise_shift, 
            py * self.noise_shift, 
            base=self.noise_base)

    def get_color_at_point(self,x,y):
        (tl, tr, bl, br) = self.palette

        px = x / self.img.width
        py = y / self.img.height

        grain_x = self.make_grain()
        grain_y = self.make_grain()

        noise_x = self.make_noise(px, py)
        noise_y = self.make_noise(px, py)

        grad1 = self.mix(tl, tr, px + grain_x + noise_x)
        grad2 = self.mix(bl, br, px + grain_y + noise_y)

        grad = self.mix(grad1, grad2, py + grain_y + noise_y)

        return grad

    def mix(self, color1, color2, mixer):
        (r1, g1, b1, a1) = color1
        (r2, g2, b2, a2) = color2

        mixer = max(0, min(mixer, 1))


        return (
            self.mix_channel(r1, r2, mixer),
            self.mix_channel(g1, g2, mixer),
            self.mix_channel(b1, b2, mixer),
            self.mix_channel(a1, a2, mixer)
        )
    
    def mix_channel(self, c1, c2, mixer):
        return int(c1 + (c2 - c1) * mixer)

    def create_random_color(self):
        h = random.uniform(0, 1)
        s = random.uniform(0.5, 1)
        v= random.uniform(0.9, 1)

        (r,g,b) = colorsys.hls_to_rgb(h,s,v)

        r  = int(r *255)
        g = int(g *255)
        b = int(b *255) 
        
        return (r,g,b,255)

    def save_to_file(self,filepath):
        self.img.save(filepath)


if __name__ == "__main__":
    print("Generating artwork from art.py")
    os.makedirs('test', exist_ok=True)
    filepath = os.path.join('test','art.png')

    art = Artwork()
    art.save_to_file(filepath)