############################# LIBRARIES #####################################

import csv
import cv2
import numpy as np

############################# FUNCTIONS #####################################

# Functions for mouse clicking on corners
def mouse_callback_c(event, x, y, flags, param):
    global x1, y1, coordinates_list
    if event == cv2.EVENT_LBUTTONDOWN:  # If the mouse was clicked...
        print(f'Souřadnice pixelu: ({x}, {y})')
        if x1 is None and y1 is None:  # If the first coordinate is not set
            x1, y1 = x, y
        else:
            coordinates_list.extend([x1, y1, x, y])  # Append the coordinates (x1, y1, x2, y2) to the list
            x1, y1 = None, None  # Reset the temporary variables for the next pair of coordinates
            
# Functions for mouse clicking on terminals
def mouse_callback_t(event, x, y, flags, param):
    global terminals_list
    if event == cv2.EVENT_LBUTTONDOWN:  # Pokud bylo stisknuto tlačítko myši
        print(f'Souřadnice pixelu: ({x}, {y})')
        terminals_list.append((x, y))  # Append the clicked coordinates to the list

# Function for creating imaginary grid
def split_area_into_cells(area, rows, columns):                                # Function for calculating area of planter cell
    x_min, y_min, x_max, y_max = area
    cell_width = (x_max - x_min) / columns
    cell_height = (y_max - y_min) / rows

    cells = []
    for row in range(rows):
        for col in range(columns):
            cell_x_min = x_min + col * cell_width
            cell_y_min = y_min + row * cell_height
            cell_x_max = cell_x_min + cell_width
            cell_y_max = cell_y_min + cell_height
            cell = (cell_x_min, cell_y_min, cell_x_max, cell_y_max)
            cells.append(cell)

    return cells

# Functions for counting clicking in the cell
def count_points_in_cells(points, cells):                                      # Function for counting terminals in the cell based on their coordinates
    counts = [0] * len(cells)                                                  
    for idx, cell in enumerate(cells):
        x_min, y_min, x_max, y_max = cell
        count = 0
        for x, y in points:
            if x_min <= x <= x_max and y_min <= y <= y_max:
                count += 1
        counts[idx] = count
    return counts

# Function for calculating average colour
def calculate_average_color(image, center_x, center_y, diameter):              # # Function to calculate average RGB values and HEX code for a given point
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.circle(mask, (center_x, center_y), diameter // 2, 255, -1)

    roi = cv2.bitwise_and(image, image, mask=mask)

    # Find non-black pixels in the ROI
    non_black_pixels = roi[np.any(roi != [0, 0, 0], axis=-1)]

    # If there are no non-black pixels, return [0, 0, 0] (black color)
    if len(non_black_pixels) == 0:
        return np.array([0, 0, 0]), '#000000'

    # Calculate the average RGB value for non-black pixels
    average_rgb = np.mean(non_black_pixels, axis=0)
    average_hex = '#{:02x}{:02x}{:02x}'.format(int(average_rgb[2]), int(average_rgb[1]), int(average_rgb[0]))

    return average_rgb, average_hex



    ############################# LOADINGS  #####################################

#Set range of your images
for u in range(1,31):
    
    # Path to output image folder
    output_name = f"C:/path/to/output/folder//{u}_RGB.csv"
    
    # Path to image without mask (transformed non-splitted image)
    image1_path = f"C:/jirka/Documents/skola/mvp/monca_sadbovace_svetlo/yolo_casti_masky/nove_puvodni/{u}.png"
    image1 = cv2.imread(image1_path)
    
    # Path to image with mask 
    image_path = f"D:/jirka/Documents/skola/mvp/monca_sadbovace_svetlo/slunce_orez/spojene_masky/vystup_{u}.png"
    image = cv2.imread(image_path)

    ############################# PLANTER CORNERS ###############################

    x1, y1 = None, None
    coordinates_list = []

    cv2.namedWindow('CORNERS', cv2.WINDOW_NORMAL)            # create windows for image displaying
    cv2.setMouseCallback('CORNERS', mouse_callback_c)        # Mouse click function 
    cv2.imshow('CORNERS', image1)                            # Image displaying
    cv2.waitKey(0)
    cv2.destroyAllWindows()                                  # Close the window


    x1, y1 = coordinates_list[:2]                           # Extract the (x1, y1) coordinates
    x2, y2 = coordinates_list[2:]                           # Extract the (x2, y2) coordinates
    
    # Calculate x_min, y_min, x_max, y_max based on (x1, y1) and (x2, y2)
    x_min = min(x1, x2)
    y_min = min(y1, y2)
    x_max = max(x1, x2)
    y_max = max(y1, y2)
    area = (x_min, y_min, x_max, y_max)
    coordinates_list.append(area)

    # List to store the coordinates
    terminals_list = []
    cv2.namedWindow('Terminals', cv2.WINDOW_NORMAL)         # create windows for terminals marking
    cv2.setMouseCallback('Terminals', mouse_callback_t)     # Mouse click function 
    cv2.imshow('Terminals', image)                          # Image displaying
    cv2.waitKey(0)
    cv2.destroyAllWindows()                                 # Close the window 
 
    ############################# CALCULATIONS #############################

    # Read areas from the CSV file
    areas = [(x1,y1,x2,y2)]
         
    # Split each area into cells
    rows = 6
    columns = 10
    target_rows = rows*columns
    area_cells = [split_area_into_cells(area, rows, columns) for area in areas]

    # Count the number of points in each cell of each area
    results = [count_points_in_cells(terminals_list, cells) for cells in area_cells]
    counts = []
    for sublist in results:
        counts.extend(sublist)
       
    # Get average RGB values and HEX codes for each area around the defined points
    diameter = int(min((((x_max - x_min) / columns)/2),(((y_max - y_min) / rows)/2)))
    average_rgbs = []
    hex_codes = []

    for point in terminals_list:
        center_x, center_y = point
        average_rgb, hex_code = calculate_average_color(image, center_x, center_y, diameter)
        average_rgbs.append(average_rgb)
        hex_codes.append(hex_code)

    ############################# CREATING OUTPUT ###############################

    output = [[i + 1, counts[i]] for i in range(60)]

    avg_index = 0  # Index for average_rgbs list
    hex_index = 0  # Index for hex_codes list

    for i in range(60):
        value = output[i][1]
        
        if value == 0: 
            continue
        elif value == 1:
            output[i].extend(average_rgbs[avg_index])
            output[i].extend([hex_codes[hex_index]])
            avg_index += 1
            hex_index += 1
        
    # Printing the new list
    for row in output:
        print(row)

    # File name and path for the CSV file
    # Writing the list of lists to the CSV file
    with open(output_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(output)



    ############################### TURNING TABLE #########################
    data = []
    with open(output_name, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)

    # Reverse the order of rows
    reversed_data = list(reversed(data))

    # Add row numbers to each row and update them based on the new order
    for i, row in enumerate(reversed_data):
        row[0] = str(i + 1)

    with open(output_name, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        
        # Write the reversed data with updated row numbers
        for row in reversed_data:
            csv_writer.writerow(row)
            
    print(f"Data has been written to {output_name} successfully.")
