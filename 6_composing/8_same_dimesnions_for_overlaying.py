import os
from PIL import Image

def add_black_strip(image_path, output_path, strip_width, strip_height, position):
    image = Image.open(image_path)
    
    if position == 'top':
        black_strip = Image.new("RGB", (image.width, strip_height), color="black")
        combined_image = Image.new("RGB", (image.width, image.height + strip_height))
        combined_image.paste(black_strip, (0, 0))
        combined_image.paste(image, (0, strip_height))
    elif position == 'left':
        black_strip = Image.new("RGB", (strip_width, image.height), color="black")
        combined_image = Image.new("RGB", (image.width + strip_width, image.height))
        combined_image.paste(black_strip, (0, 0))
        combined_image.paste(image, (strip_width, 0))
    elif position == 'right':
        black_strip = Image.new("RGB", (strip_width, image.height), color="black")
        combined_image = Image.new("RGB", (image.width + strip_width, image.height))
        combined_image.paste(black_strip, (image.width, 0))
        combined_image.paste(image, (0, 0))
    elif position == 'bottom':
        black_strip = Image.new("RGB", (image.width, strip_height), color="black")
        combined_image = Image.new("RGB", (image.width, image.height + strip_height))
        combined_image.paste(black_strip, (0, image.height))
        combined_image.paste(image, (0, 0))
    
    combined_image.save(output_path)

input_foder = "D:/path/to/your/composed/images/"
output_folder = "D:/path/to/your/output/images/"

for k in range(1, 2):
    add_black_strip(input_foder + f"{k}_200_right.png", output_folder + f"{k}_200_right.png", 200, 0, 'left')
    add_black_strip(input_foder + f"{k}_400_right.png", output_folder + f"{k}_400_right.png", 400, 0, 'left')
    add_black_strip(input_foder + f"{k}_400_down.png", output_folder + f"{k}_400_down.png", 0, 400, 'top')
    add_black_strip(input_foder + f"{k}_200_down.png", output_folder + f"{k}_200_down.png", 0, 200, 'top')

    print(f"{k} is done")
