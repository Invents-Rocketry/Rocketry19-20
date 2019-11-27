import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

# Make Panorama image from 2 consecutive images
# -----------------Find the similar cutout of both images and merge it at that point.----------------------------


test1File = 'd:/rocketry/Rocketry_2019-2020/Panorama_Merge_Test/bike1.jpg'
test2File = 'bike2.jpg'

# 1. Load 2 images
leftGray=cv2.imread(test1File,0)
rightGray=cv2.imread(test2File,0)

leftColor = cv2.imread(test1File,-1)
rightColor = cv2.imread(test2File,-1)

# 2. Take template (cropped right image) at bottom left
crop_image_dimension = 100
w,h = leftGray.shape[::-1]
template = rightGray[h-crop_image_dimension:h,0:crop_image_dimension]


cv2.imshow('template',template)
cv2.waitKey(0)



# 3. Find matching location (TOP LEFT)
method = cv2.TM_CCOEFF_NORMED

w,h = template.shape[::-1] #size of template



res = cv2.matchTemplate(leftGray,template,method)


min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) #find the global min-max location

print(cv2.minMaxLoc(res))

if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc

bottom_right = (top_left[0]+w,top_left[1]+h)
cv2.rectangle(leftGray,top_left,bottom_right,0,5)
plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(leftGray,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(method)
plt.show()


# 4. Find cut-off x-axis
cutoff_x_axis = top_left[0]

# 5. Crop left image at the cut-off x-axis
left_w, left_h = leftGray.shape[::-1]

leftImageCutoff = leftColor[0:left_h, 0:cutoff_x_axis]
merging_result = np.hstack((leftImageCutoff, rightColor))

cv2.imshow('result',merging_result)
cv2.waitKey(0)


cv2.destroyAllWindows()