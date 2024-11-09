from PIL import Image, ImageDraw
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

def add_text_behind(foreground, text, position, font, color):
    background = Image.new('RGBA', foreground.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(background)
    draw.text(position, text, font=font, fill=color)
    combined = Image.alpha_composite(background, foreground)
    return combined