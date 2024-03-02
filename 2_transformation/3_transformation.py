# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:55:57 2024

@author: jirka
"""

import cv2
import numpy as np
import csv
import os


# Load the CSV file containing the image names and corner coordinates
csv_file_path = "D:/jirka/Documents/skola/Ing/DP/DP_poznamky_a_skripty/real_postup/postup/transformed/coordinates.csv"

# Set the path to the folder containing the images
images_folder_path = "D:/jirka/Documents/skola/Ing/DP/DP_poznamky_a_skripty/real_postup/postup/corrected"

# Set the path to the folder for the transformed image results
results_folder_path = "D:/jirka/Documents/skola/Ing/DP/DP_poznamky_a_skripty/real_postup/postup/transformed"

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  # Assuming comma as the delimiter
    # next(csvreader)  # Skip the header row if there is one
    for row in csvreader:
        # Get the image name and corner coordinates from the current row
        image_name = row[0]
        corners = [(int(row[i]), int(row[i+1])) for i in range(1, len(row), 2)]

        # Construct the image path
        image_path = os.path.join(images_folder_path, image_name)

        # Load the image
        image = cv2.imread(image_path)

        # Calculate the dimensions of the planter
        planter_width = max(corners[1][0] - corners[0][0], corners[2][0] - corners[3][0])
        planter_height = max(corners[3][1] - corners[0][1], corners[2][1] - corners[1][1])

        # Define the surrounding area
        surrounding_pixels = 400

        # Define the source and destination points for perspective transformation
        src_points = np.float32(corners)
        dst_points = np.float32([[surrounding_pixels, surrounding_pixels],
                                 [planter_width + surrounding_pixels, surrounding_pixels],
                                 [planter_width + surrounding_pixels, planter_height + surrounding_pixels],
                                 [surrounding_pixels, planter_height + surrounding_pixels]])

        # Calculate the perspective transformation matrix
        transformation_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

        # Apply the perspective transformation to the image
        transformed_image = cv2.warpPerspective(image, transformation_matrix,
                                                (planter_width + 2 * surrounding_pixels,
                                                 planter_height + 2 * surrounding_pixels))

        # Calculate the scale factor for displaying the image
        scale_factor = min(1.0, 800 / transformed_image.shape[1], 600 / transformed_image.shape[0])

        # Resize the image for display
        resized_image = cv2.resize(transformed_image, None, fx=scale_factor, fy=scale_factor)

        # Create a window to display the image
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

        # Show the image in the window
        cv2.imshow("Image", resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Construct the transformed image path
        transformed_image_path = os.path.join(results_folder_path, f'{image_name.split(".")[0]}_transformed.png')
        
        # Save the transformed image
        cv2.imwrite(transformed_image_path, transformed_image)
