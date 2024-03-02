# Image composing
This codes compose parts of the splitted image together based on names of the parts and add black stripes, so images can be overlayed in the next step.

## Features
- [Composing](#composing)
- [Adding black stripes](#adding-black-stripes)

## Composing | [code](./7_composing.py)
This code compose parts of the segmented image together.

### Usage
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
## Adding black stripes | [code](./8_same_dimesnions_for_overlaying.py)
This code adds black stripes to the composed images. It is because we splitted images with some shift, and now we need to overlay images without the shift.

### Usage
In this code, you need to fill path to your folder with composed images, path to output folder where you want results, name-logic of your images and you can add range of images +1 so the loop will process your images at once.
You can also set the width or height of the black stripe and its position
```python
input_foder = "D:/path/to/your/composed/images/"
output_folder = "D:/path/to/your/output/images/"

for k in range(1, 2):
    add_black_strip(input_foder + f"{k}_200_right.png", output_folder + f"{k}_200_right.png", 200, 0, 'left')
    add_black_strip(input_foder + f"{k}_400_right.png", output_folder + f"{k}_400_right.png", 400, 0, 'left')
    add_black_strip(input_foder + f"{k}_400_down.png", output_folder + f"{k}_400_down.png", 0, 400, 'top')
    add_black_strip(input_foder + f"{k}_200_down.png", output_folder + f"{k}_200_down.png", 0, 200, 'top')
