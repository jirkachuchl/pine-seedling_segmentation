# Bacround removal | [code](./6_mask_clip)
This Python script uses the `PIL` (Pillow) library to clip an image based on a specified mask. It replaces non-red pixels in the original image with corresponding pixels from the mask image.

## Usage
Here you need to only fill the number +1 of your images for the loop and path to you inputs and output. 
```python
for i in range(1,21):
    
    #original image path
    background_path = f"path/{i}.png" 
    
    #image with mask path
    mask_path = f"path/{i}.png" 
    
    #path for output image
    output_path = f"path/{i}.png"

    clip_image(background_path, mask_path, output_path)
```
