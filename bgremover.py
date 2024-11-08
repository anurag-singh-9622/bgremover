# prompt: refactor above code

from rembg import remove
from PIL import Image
# pip install rembg  # Uncomment this line if you haven't installed rembg

input_path = 'clgot.jpg'
output_path = input_path.split('.')[0] + '_bgremoved.png'

try:
    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path)
    # Image.open("clgot.png")
except FileNotFoundError:
    print(f"Error: Input file '{input_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")