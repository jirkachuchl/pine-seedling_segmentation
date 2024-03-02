# RGB acquisition for each pine seedling | [code](./RGB_acquisition.py)
This Python script processes a range of images, extracting RGB values and saving the results to CSV files.

## Usage
In this code you should fill only range of your images (+1) and path to output folder and path to images which you transformed (step 2) ans path to images with mask (step 7)
```python
############################# LOADINGS  #####################################
#Set range of your images
for u in range(1,2):
    
    # Path to output image folder
    output_name = f"C:/path/to/output/folder//{u}_RGB.csv"
    
    # Path to image without mask (transformed non-splitted image)
    image1_path = f"C:/path/to/your/transformed/{u}_transformed.png"
    image1 = cv2.imread(image1_path)
    
    # Path to image with segmented pines
    image_path = f"C:/path/to/your/segmented/images/{u}_overlayed.png"
    image = cv2.imread(image_path)
```
First, the window with transformed, non-segmented image will appear. Here you need to click on corners, so the code could calculate the dimensions of each cell in the planter.
Than you will close the window CORNERS, and the window TERMINAL will appear. Here you will click on the terminals of each pine. After you close this window, thw code will calculate average gb for each pine and saves it in the csv.
