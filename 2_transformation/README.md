# Image Transformation
## Features
- [Coordinates of corners to csv](#Coordinates-of-corners-to-csv)
- [Image transformation](#Image-transformation)

# Coordinates of corners to csv

This Python script utilizes the OpenCV and Pandas libraries to extract clicked coordinates from images. It provides an interactive way to select points on an image using mouse clicks and saves the coordinates in a CSV file.

## Function

### process_image(image_path)

The `process_image` function allows users to interactively click on points in an image and records the coordinates. The function returns a DataFrame containing the image name and clicked coordinates.

## Example Usage

The script includes an example loop for processing multiple images. The processed coordinates are concatenated into a final DataFrame and saved to a CSV file.

```python
result_df = pd.DataFrame()  # Initialize an empty DataFrame to store the results

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

