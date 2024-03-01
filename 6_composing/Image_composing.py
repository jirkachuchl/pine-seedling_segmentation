from PIL import Image
import numpy as np
for k in range(1,30):

  # Number of parts in width and height
  num_parts_width = 10
  num_parts_height = 6

  # Create an empty list to store part sizes
  part_sizes = []

  # Combine image parts
  for i in range(1, num_parts_height + 1):
      for j in range(1, num_parts_width + 1):
          # Load image part
          part_path = f"/content/gdrive/MyDrive/leden/{k}/cast_{i}_{j}.jpg"
          part = Image.open(part_path)

          # Get the size of the current part
          part_width, part_height = part.size
          part_sizes.append((part_width, part_height))

  # Compute the maximum dimensions for all parts
  max_width = max([size[0] for size in part_sizes])
  max_height = max([size[1] for size in part_sizes])

  # Create an empty array for the full image
  full_img = np.zeros((max_height * num_parts_height, max_width * num_parts_width, 3), dtype=np.uint8)

  # Combine image parts
  for i in range(1, num_parts_height + 1):
      for j in range(1, num_parts_width + 1):
          # Load image part
          part_path = f"/content/gdrive/MyDrive/leden/{k}/cast_{i}_{j}.jpg"
          part = Image.open(part_path)

          # Compute position for the current part
          x = (j - 1) * max_width
          y = (i - 1) * max_height

          # Resize or crop the part if necessary
          if part.size != (max_width, max_height):
              part = part.resize((max_width, max_height))

          # Convert the part to a NumPy array
          part_array = np.array(part)

          # Insert the part into the full image
          full_img[y:y + max_height, x:x + max_width] = part_array

  # Save the combined image
  output_path = f"/content/gdrive/MyDrive/leden/vystup/{k}_cast.png"
  Image.fromarray(full_img).save(output_path)
  print(f"{k} is done")
