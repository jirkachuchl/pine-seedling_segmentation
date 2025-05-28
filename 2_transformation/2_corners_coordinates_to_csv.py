# -*- coding: utf-8 -*-

##################### Function ###############################
import cv2
import pandas as pd
import os

def process_image(image_path):
    # List to store clicked coordinates
    clicked_coordinates = []

    # Extract the image name from the path
    image_name = os.path.basename(image_path)

    # Mouse click function
    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # If a button is clicked
            print(f'{x}, {y}')
            clicked_coordinates.extend([x, y])  # Append individual x and y coordinates

    # Image reading
    image = cv2.imread(image_path)

    # Windows creation for image displaying
    cv2.namedWindow('Obrazek', cv2.WINDOW_NORMAL)  # Použití normálního okna

    # Assigning a function to handle the mouse click event
    cv2.setMouseCallback('Obrazek', mouse_callback)

    # Image display
    cv2.imshow('Obrazek', image)
    cv2.waitKey(0)

    # Closing the window
    cv2.destroyAllWindows()

    # Create a DataFrame with dynamic column names based on the number of clicked points
    data = [[image_name] + clicked_coordinates]  # Convert the list to a DataFrame row
    df = pd.DataFrame(data)

    return df
##################### /Function ###############################

######### Example usage in a loop for processing multiple images #############

result_df = pd.DataFrame()  # Initialize an empty DataFrame to store the results

# set the range of numbers of processed images
for i in range(1,4):
    image_path = f"C:/path/to/your/image/{i}.png" #path to the images where i as number
    df = process_image(image_path)
    result_df = pd.concat([result_df, df], ignore_index=True)


# Save the final DataFrame to a CSV file, you have to set the output path for csv
result_df.to_csv("C:/path/to/your/output/csvfile/coordinates.csv", index=False,header=False)

# Print the final DataFrame
print("Clicked Coordinates Table for All Images:")
print(result_df)
