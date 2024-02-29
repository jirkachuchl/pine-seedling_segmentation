import cv2
import numpy as np
import csv
import os


# Load the CSV file containing the image names and corner coordinates
csv_file_path = "C:/path/to/your/csv/with/coordinates/coordinates.csv"

# Set the path to the folder containing the images
images_folder_path = "C:/path/to/your/folder/with/images"

# Set the path to the folder for the transformed image results
results_folder_path = "C:/path/to/your/output/folder"


############################### Functions ##################################
# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    #next(csvreader)  # Skip the header row
    for row in csvreader:
        # Get the image name and corner coordinates from the current row
        image_name = row[0]
        corner1 = tuple(map(int, row[1].split(', ')))
        corner2 = tuple(map(int, row[2].split(', ')))
        corner3 = tuple(map(int, row[3].split(', ')))
        corner4 = tuple(map(int, row[4].split(', ')))

        # Construct the image path
        image_path = os.path.join(images_folder_path, image_name)

        # Load the image
        image = cv2.imread(image_path)

        # Calculate the dimensions of the planter
        planter_width = max(corner2[0] - corner1[0], corner3[0] - corner4[0])
        planter_height = max(corner4[1] - corner1[1], corner3[1] - corner2[1])

        # Define the surrounding area
        surrounding_pixels = 400

        # Define the source and destination points for perspective transformation
        src_points = np.float32([corner1, corner2, corner3, corner4])
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
        transformed_image_path = os.path.join(results_folder_path, image_name.split('.')[0] + '_transformed.png')
        # Save the transformed image
        cv2.imwrite(transformed_image_path, transformed_image)
############################### /Functions ##################################
