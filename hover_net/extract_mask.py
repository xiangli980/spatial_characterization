import cv2
import numpy as np
import glob
import re
from skimage.measure import label, regionprops
import matplotlib.pyplot as plt
from skimage import morphology

def simple_get_mask():
    scaled_wsi_mag = 1.25  # ! hard coded
    wsi_thumb_rgb = self.wsi_handler.get_full_img(read_mag=scaled_wsi_mag)
    gray = cv2.cvtColor(wsi_thumb_rgb, cv2.COLOR_RGB2GRAY)
    _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    mask = morphology.remove_small_objects(
        mask == 0, min_size=16 * 16, connectivity=2
    )
    mask = morphology.remove_small_holes(mask, area_threshold=128 * 128)
    mask = morphology.binary_dilation(mask, morphology.disk(10))
    return mask


# dict_roi = {}
# dict_roi['11_26609_000_009_L1_HE'] = [2, 4]
# dict_roi['11_26609_009_014 L2 HE'] = [3, 4]
# dict_roi['11_26609_022_005 L02 HE'] = [1]
# dict_roi['11_26609_029_504 L12 _ HE'] = [2,4,6]
# dict_roi['12_26609_023_516 LUNK1 HE'] = [4,7,9]
# dict_roi['12_26609_026_014 L01 HE'] = [2,6]
# dict_roi['12_26609_099_005 L02 HE'] = [1]
# #dict_roi['12_26609_099_006 L02 HE'] = [2]
# dict_roi['13_26609_033_520 L01 HE'] = [5]
# dict_roi['14_26609_025_518 L01 HE'] = [1,2,3,4]

dict_roi = {}
dict_roi['11_26609_000_009_L1_HE'] = [2, 4]


if __name__== "__main__":
    # iterate over dict_roi
    for k in dict_roi:
        labels = dict_roi[k]

        #for i, k in enumerate(dict_roi):

        # find largest contour in the mask
        img = cv2.imread("./output_neptune/thumb/{}.png".format(k))
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # print(plt.hist(gray.ravel()))
        # cv2.imwrite("./output_neptune/plot/gray.png", gray)
        _, mask = cv2.threshold(gray, 210, 255, cv2.THRESH_OTSU)
        
        # cv2.imwrite("./output_neptune/plot/mask0.png", mask)

        mask = morphology.remove_small_objects(
            mask == 0, min_size=16 * 16, connectivity=2
        )
        # mask1 = np.array(mask > 0, dtype=np.uint8)
        # cv2.imwrite("./output_neptune/plot/mask1.png", mask1*255)

        mask = morphology.remove_small_holes(mask, area_threshold=128 * 128)
        # mask2 = np.array(mask > 0, dtype=np.uint8)

        # cv2.imwrite("./output_neptune/plot/mask2.png", mask2*255)

        mask = morphology.binary_dilation(mask, morphology.disk(10)) # change from 16 to 10
        mask = np.array(mask > 0, dtype=np.uint8)
        # cv2.imwrite("./output_neptune/plot/mask.png", mask*255)
        
        #mask = cv2.imread("./output_neptune/plot/mask2.png")
        #mask = (mask[:,:,0]>127)*1
        label_img = label(mask)
        regions = regionprops(label_img) 
        # areas = [prop.area for prop in regions]
        # largest_comp = areas.index(max(areas))      
        # label = regions[largest_comp].label
        wsi_mask = np.zeros(mask.shape[:2], dtype=np.uint8)
        
        for labeli in labels:
        
            wsi_mask[label_img == labeli] = 1

                    # wsi_mask = (wsi_mask<1)*1
                    # (h,w) = wsi_mask.shape
                    # # mask the first 2/3 of the image vertically
                    # wsi_mask[:,0:int(2*w/3)] = 0
            # # show the mask
            # plt.imshow(label_img)
            # for region in regions:
            #     # get center of each region
            #     y, x = region.centroid
            #     plt.text(x, y, str(region.label), fontsize=10)
            
            # # save the plot
            # plt.savefig("./output_neptune/plot/12_26609_099_006 L02 HE.png")
            # plt.show()
        cv2.imwrite("./output_MCD/mask/{}.png".format(k), wsi_mask*255)