library(png)

for(k in 1:2) {
  ################## Settings ##################################################
  #Loading an image
  basic_folder <- "C:/path/to/your/folder/with/your/images"     #Set path to your folder
  img <- readPNG(paste0(basic_folder,"name",k , ".png"))        #Set logic to name images in your folder
  output_folder <- "C:/path/to/your/folder/for/output/images"   #Set path to folder for you output images
  
  # size of cutted parts
  part_width <- 600   #Set the width of the part
  part_height <- 600  #Set the height of the part
  
  ################## Settings ##################################################
  
  #Dimension of the image
  width <- dim(img)[2]
  height <- dim(img)[1]
  
  #Number of parts in lenght and height of image
  num_parts_width <- ceiling(width / part_width)
  num_parts_height <- ceiling(height / part_height)
  
  # Cutting the image 
  for (i in 1:num_parts_height) {
    for (j in 1:num_parts_width) {
      
      #Calculation of position of each part
      x <- (j - 1) * part_width + 1
      y <- (i - 1) * part_height + 1
      w <- min(part_width, width - x + 1)
      h <- min(part_height, height - y + 1)
      
      #Save the current part
      part <- img[y:(y + h - 1), x:(x + w - 1), ]
      writePNG(part, paste0(output_folder,"/",k,"_part_", i, "_", j, ".png"))
    }
  }
  
  ############# Adjusted for starting from 400 pixels to the right #############
  
  # Number of parts in lenght and height of image
  num_parts_width <- ceiling((width - 400) / part_width)  
  num_parts_height <- ceiling(height / part_height)
  
  # Cutting the image
  for (i in 1:num_parts_height) {
    for (j in 1:num_parts_width) {
      #Calculation of position of each part
      x <- (j - 1) * part_width + 1 + 400
      y <- (i - 1) * part_height + 1
      w <- min(part_width, width - x + 1)
      h <- min(part_height, height - y + 1)
      
      #Save the current part
      part <- img[y:(y + h - 1), x:(x + w - 1), ]
      writePNG(part, paste0(output_folder,"/",k,"/400_right_", i, "_", j, ".png"))
    }
  }
  
  ############# Adjusted for starting from 200 pixels to the right #############
  
  # Number of parts in lenght and height of image
  num_parts_width <- ceiling((width - 200) / part_width)
  num_parts_height <- ceiling(height / part_height)
  
  # Cutting the image
  for (i in 1:num_parts_height) {
    for (j in 1:num_parts_width) {
      #Calculation of position of each part
      x <- (j - 1) * part_width + 1 + 200  
      y <- (i - 1) * part_height + 1
      w <- min(part_width, width - x + 1)
      h <- min(part_height, height - y + 1)
      
      #Save the current part
      part <- img[y:(y + h - 1), x:(x + w - 1), ]
      writePNG(part, paste0(output_folder,"/",k,"/200_right_", i, "_", j, ".png"))
    }
  }
  
  ############# Adjusted for starting from 400 pixels down #####################
  
  # Number of parts in lenght and height of image
  num_parts_width <- ceiling(width / part_width)
  num_parts_height <- ceiling((height - 400) / part_height) 
  
  # Cutting the image
  for (i in 1:num_parts_height) {
    for (j in 1:num_parts_width) {
      #Calculation of position of each part
      x <- (j - 1) * part_width + 1
      y <- (i - 1) * part_height + 1 + 400
      w <- min(part_width, width - x + 1)
      h <- min(part_height, height - y + 1)
      
      #Save the current part
      part <- img[y:(y + h - 1), x:(x + w - 1), ]
      writePNG(part, paste0(output_folder,"/",k,"/400_down_", i, "_", j, ".png"))
    }
  }
  
  ############# Adjusted for starting from 200 pixels down #####################
  
  # Number of parts in lenght and height of image
  num_parts_width <- ceiling(width / part_width)
  num_parts_height <- ceiling((height - 200) / part_height) 
  
  # Cutting the image
  for (i in 1:num_parts_height) {
    for (j in 1:num_parts_width) {
      #Calculation of position of each part
      x <- (j - 1) * part_width + 1
      y <- (i - 1) * part_height + 1 + 200 
      w <- min(part_width, width - x + 1)
      h <- min(part_height, height - y + 1)
      
      #Save the current part
      part <- img[y:(y + h - 1), x:(x + w - 1), ]
      writePNG(part, paste0(output_folder,"/",k,"/200_down_", i, "_", j, ".png"))
    }
  }
}
