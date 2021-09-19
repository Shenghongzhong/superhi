from PIL import Image   

def make_art(filepath):
    img = Image.new("RGBA", (500, 500),color=(255,255,0,255))
    img.save(filepath)