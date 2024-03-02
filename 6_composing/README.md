# Image composing | [code](./Image_composing.py)
This code compose parts of the splitted image together based on names of the parts. 

## Usage
The code is a loop which process more images, so you need to fill rande onf the images (+1). You have to fill number of parts in width and height of image. You also need to fill path to your folders with input parts and output folder.

You have fill these rows:
```python
# row 4
for k in range(1,30):

# row 6-7
num_parts_width = 10
num_parts_height = 6

# row 17
part_path = f"/path/to/your/image_parts/{k}/part_{i}_{j}.png"

# row 55
output_path = f"/path/to/your/output/folder/{k}_cast.png"
```
