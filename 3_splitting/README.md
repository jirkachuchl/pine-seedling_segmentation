# Image splitting script | [code](./4_Splitting_images_on_parts.R)

This R script uses the `png` library to partition images into smaller parts. It's designed to cut images into specified parts and save them to an output folder.

The script includes an example loop for processing multiple images in folder.
In this code, you have to set paths:

path to the folder with image you want to split (basic_folder)
path to the output folder where the splitted parts will be (output_folder)
dimensions of the resulting parts (width and height)

## Example usage
```R
for(k in 1:number of your images) {
  #Loading an image
  basic_folder <- "C:/path/to/your/folder/with/your/images"     #Set path to your folder
  img <- readPNG(paste0(basic_folder,"name",k , ".png"))        #Set logic to name images in your folder
  output_folder <- "C:/path/to/your/folder/for/output/images"   #Set path to folder for you output images
  
  # size of cutted parts
  part_width <- 600   #Set the width of the part
  part_height <- 600  #Set the height of the part

