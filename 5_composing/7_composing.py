from PIL import Image
import numpy as np

for k in range(1, 2):
    # Number of parts in width and height
    num_parts_width = 9
    num_parts_height = 5

    # Create an empty list to store part images and sizes
    part_images = []
    part_sizes = []

    # Combine image parts
    for i in range(1, num_parts_height + 1):
        for j in range(1, num_parts_width + 1):
            # Load image part
            part_path = f"D:/path/to/your/parts/{k}_200_down_{i}_{j}.png"
            part = Image.open(part_path)

            # Append the part image and its size to the lists
            part_images.append(np.array(part))
            part_sizes.append(part.size)

    # Calculate the total dimensions of the resulting image
    total_width = sum([size[0] for size in part_sizes[:num_parts_width]])
    total_height = sum([size[1] for size in part_sizes[:num_parts_height]])

    # Create an empty list to store rows of the composed image
    rows = []

    # Combine image parts without resizing or cropping
    x_offset = 0

    for i in range(num_parts_height):
        # Create an empty row to store parts in the current row
        row = []

        for j in range(num_parts_width):
            # Load image part
            part_array = part_images[i * num_parts_width + j]

            # Get the dimensions of the current part
            part_height, part_width, _ = part_array.shape

            # Append the part to the current row
            row.append(part_array)

        # Concatenate the parts in the current row along the horizontal axis
        rows.append(np.concatenate(row, axis=1))

    # Concatenate the rows along the vertical axis to get the final image
    full_img = np.concatenate(rows, axis=0)

    # Save the combined image
    output_path = f"D:/path/to your/composed/output/{k}_200_down.png"
    Image.fromarray(full_img).save(output_path)
    print(f"{k} is done")
