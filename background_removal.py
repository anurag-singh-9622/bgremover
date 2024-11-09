from PIL import Image
from rembg import remove

def remove_bg(image):
    output = remove(image, alpha_matting=True)
    return output

def add_bg_color(foreground, color):
    background = Image.new('RGBA', foreground.size, color)
    combined = Image.alpha_composite(background, foreground)
    return combined

def add_bg_image(foreground, background):
    background = background.resize(foreground.size)
    combined = Image.alpha_composite(background.convert('RGBA'), foreground.convert('RGBA'))
    return combined