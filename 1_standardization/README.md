# ImageJ Macro Script for White Reference Standardization |[code](./1_IMAGEJ_white_correction.ijm)

This ImageJ Macro script is designed for standardizing images using a white reference region of interest (ROI). Follow the steps below to use the script:

## Instructions

1. **Create a Region of Interest (ROI):**
   - Manually create a ROI around your white reference area in the image.

2. **Update Output File Path:**
   - Open the script and locate the line: `outputFilePath = "D:/path/to/output.png"`.
   - Replace `"D:/path/to/output.png"` with the desired path and filename for the standardized output image.

3. **Run the Macro:**
   - Execute the script in ImageJ.

4. **Review Output:**
   - The script will calculate mean intensity values for each color channel in the ROI.
   - It will then normalize the image based on these values to achieve white reference standardization.

5. **Save Result:**
   - The standardized image will be saved to the specified output file path.
