# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np

def clip_image(background_path, mask_path, output_path):
    # Open the images
    background = Image.open(background_path)
    mask = Image.open(mask_path)

    # Convert images to NumPy arrays
    background_array = np.array(background)
    mask_array = np.array(mask)

    # Create a mask for red pixels
    red_mask = (mask_array == [255, 56, 56]).all(axis=-1)

    # Replace zeros in the background with corresponding pixels from the second image
    background_array[~red_mask] = 0

    # Create a new image from the modified background array
    clipped_image = Image.fromarray(background_array)

    # Save the result
    clipped_image.save(output_path)


for i in range(1,2):
    
    #original image path
    background_path = f"path/{i}.png" 
    
    #image with mask path
    mask_path = f"path/{i}.png" 
    
    #path for output image
    output_path = f"path/{i}.png"

    clip_image(background_path, mask_path, output_path)

