# Image Overlay Script

This script overlays multiple images by combining their pixels. It takes a set of input images, checks each pixel at the same coordinates in all images, and creates a new image based on the following logic:

- If all pixels are black, the script skips that pixel.
- If any image has a non-black pixel at the current coordinates, it takes the color of the first non-black pixel and writes it to the resulting image.

# Usage
In this code, you need to fill path to your input images and to your output result. This code is not in thwe form of the loop so if you can, you can easily change it
```python
# Example usage
image_paths = [
    f"D:/jirka/Documents/skola/Ing/DP/rijen_sadbovace/vystup/2/vystupy/pokus/2.png",
    f"D:/jirka/Documents/skola/Ing/DP/rijen_sadbovace/vystup/2/vystupy/pokus/3.png",
    f"D:/jirka/Documents/skola/Ing/DP/rijen_sadbovace/vystup/2/vystupy/pokus/4.png",
    f"D:/jirka/Documents/skola/Ing/DP/rijen_sadbovace/vystup/2/vystupy/pokus/5.png",
    f"D:/jirka/Documents/skola/Ing/DP/rijen_sadbovace/vystup/2/vystupy/pokus/6.png"
]

output_path = "D:/jirka/Documents/skola/Ing/DP/rijen_sadbovace/vystup/2/vystupy/pokus/_RRR_result_image.png"
overlay_images(image_paths, output_path)
```
