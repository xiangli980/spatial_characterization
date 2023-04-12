import cv2
import numpy as np
import glob
import re



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


if __name__== "__main__":

    # find largest contour in the mask
    img = cv2.imread("./output/wsis/mask/2_6063_A_0045149.png")
    label_img = label(image)
    regions = regionprops(label_img) 
    areas = [prop.area for prop in regions]
    largest_comp = areas.index(max(areas))      
    label = regions[largest_comp].label
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    mask[label_img == label] = 1

    # save the mask
        
    if self.save_mask:
        cv2.imwrite("%s/mask/%s.png" % (output_dir, wsi_name), self.wsi_mask * 255) 