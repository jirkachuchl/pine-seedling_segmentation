# Segmentation of pine seedling 
This algoritmus is slightly modified algoritmus YOLOv7 branch u7 (https://github.com/WongKinYiu/yolov7.git) 
The usage is described in the directory

## Modifications
There are only few modifications
### 1. Making the resulting mask opaque | modifications are in this part of algoritmus: [code](./yolov7-u7-seg/seg/utils/segment/plots.py)
Here the alpha is set to 1, so resulting mask will have only one opaque colour

'''python
###########################    set alpha to 1    ###############################

def plot_masks(img, masks, colors, alpha=1):

########################### // set alpha to 1 // ###############################
'''

### 2. Setting a mask colour | modifications are in this part of algoritmus: [code](./yolov7-u7-seg/seg/utils/plots.py)
Here the color RGB HEXCODE is used for setting a colour of mask

'''python
     hex = matplotlib.colors.TABLEAU_COLORS.values()
    ####################################### set your own colors for mask ######################### 
    hexs = ('FF3838', 'FF3838', 'FF3838', 'FF3838', 'FF3838', 'FF3838', 'FF3838', 'FF3838', 'FF3838', 'FF3838')
    # original hexs
    # '''
    hexs = ('FF3838', 'FF9D97', 'FF701F', 'FFB21D', 'CFD231', '48F90A', '92CC17', '3DDB86', '1A9334', '00D4BB',
    '2C99A8', '00C2FF', '344593', '6473FF', '0018EC', '8438FF', '520085', 'CB38FF', 'FF95C8', 'FF37C7')
    '''
    ####################################### //set your own colors for mask //######################
'''

### 3. Turning of the bounding box | modifications are in this part of algoritmus: [code](./yolov7-u7-seg/seg/utils/plots.py)
Here the part of the code is turned of, so the bounding box won't be displayed in the resulting image

'''python
      # Add one xyxy box to image with label
  ################ set this part of for turning of the boinding box #############
      '''
        if self.pil or not is_ascii(label):
            self.draw.rectangle(box, width=self.lw, outline=color)  # box
            if label:
                w, h = self.font.getsize(label)  # text width, height
                outside = box[1] - h >= 0  # label fits outside box
                self.draw.rectangle(
                    (box[0], box[1] - h if outside else box[1], box[0] + w + 1,
                     box[1] + 1 if outside else box[1] + h + 1),
                    fill=color,
                )
                # self.draw.text((box[0], box[1]), label, fill=txt_color, font=self.font, anchor='ls')  # for PIL>8.0
                self.draw.text((box[0], box[1] - h if outside else box[1]), label, fill=txt_color, font=self.font)
        else:  # cv2
            p1, p2 = (int(box[0]), int(box[1])), (int(box[2]), int(box[3]))
            cv2.rectangle(self.im, p1, p2, color, thickness=self.lw, lineType=cv2.LINE_AA)
            if label:
                tf = max(self.lw - 1, 1)  # font thickness
                w, h = cv2.getTextSize(label, 0, fontScale=self.lw / 3, thickness=tf)[0]  # text width, height
                outside = p1[1] - h >= 3
                p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
                cv2.rectangle(self.im, p1, p2, color, -1, cv2.LINE_AA)  # filled
                cv2.putText(self.im,
                            label, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2),
                            0,
                            self.lw / 3,
                            txt_color,
                            thickness=tf,
                            lineType=cv2.LINE_AA)
      '''
  ################ //set this part of for turning of the boinding box// #############
    
