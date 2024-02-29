# Saving coordinates of corners and image Transformation
## Features
- [Coordinates of corners to csv](#Coordinates-of-corners-to-csv)
- [Image transformation](#Image-transformation)

## Coordinates of corners to csv | [code](./2_corners_coordinates_to_csv.py)

First it is necessary to save the coordinates of planter to csv. After running this sript the new window will open. You will click on  the corners in this order:
- 1st: upper left corner
- 2nd: upper right corner
- 3rd: lower right corner
- 4th: lower left corner

This script is created as loop, so insert path to directory with your images and insert range of images (+1) and it will open automatically all images in the directory
Don't forget to fill path to your output csv file.

### Example Usage

The script includes an example loop for processing multiple images.

```python
# Set the range of numbers for processed images
for i in range(1, 4):
    image_path = f"C:/path/to/your/image/{i}.png"  # Replace with the path to your images
    df = process_image(image_path)
    result_df = pd.concat([result_df, df], ignore_index=True)

# Save the final DataFrame to a CSV file
result_df.to_csv("C:/path/to/your/output/csvfile/coordinates.csv", index=False, header=False)

# Print the final DataFrame
print("Clicked Coordinates Table for All Images:")
print(result_df)
```
## Image transformation | [code](./3_transformation_by_corners_coordinates_from_CSV.py)
In this code, you only have to set paths:
- path to csv with corners coordinates (csv_file_path)
- path to the folder containing the images of planters you want to transform (images_folder_path)
- path to the folder for the transformed image results (results_folder_path)

### Example Usage
```python
# Load the CSV file containing the image names and corner coordinates
csv_file_path = "C:/path/to/your/csv/with/coordinates/coordinates.csv"

# Set the path to the folder containing the images
images_folder_path = "C:/path/to/your/folder/with/images"

# Set the path to the folder for the transformed image results
results_folder_path = "C:/path/to/your/output/folder"

