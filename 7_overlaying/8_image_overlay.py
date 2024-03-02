
import numpy as np
from PIL import Image

def overlay_images(image_paths, output_path):
    # Load the images into NumPy arrays
    images = [np.array(Image.open(path)) for path in image_paths]
    
    # Create a black background image
    result_image = np.zeros_like(images[0])
    
    # Iterate through each pixel in each image
    for image in images:
        # Find non-black pixels in the current image
        non_black_pixels = np.any(image != [0, 0, 0], axis=-1)
        
        # Replace corresponding pixels in the result image
        result_image[non_black_pixels] = image[non_black_pixels]
    
    # Convert the NumPy array back to a PIL Image
    result_image = Image.fromarray(result_image, 'RGB')
    
    # Save or display the resulting image
    result_image.save(output_path)

# Example usage
image_paths = [
    f"C:/path/to/your/input/1_image.png",
    f"C:/path/to/your/input/2_image.png",
    f"C:/path/to/your/input/3_image.png",
    f"C:/path/to/your/input/4_image.png",
    f"C:/path/to/your/input/5_image.png"
]

output_path = "C:/path/to/your/output/image.png"
overlay_images(image_paths, output_path)
