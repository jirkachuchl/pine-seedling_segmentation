# RGB acquisition for each pine seedling | [code](./RGB_acquisition.py)
This Python script processes a range of images, extracting RGB values and saving the results to CSV files.

## Usage
In this code you should fill only range of your images (+1) and path to output folder and path to images which you transformed (step 2) ans path to images with mask (step 7)
```python
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
