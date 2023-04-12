import cv2
import numpy as np
import glob
import re

if __name__== "__main__":
    input_dir = './dataset/tile'
    patterning = lambda x: re.sub("([\[\]])", "[\\1]", x)
    file_path_list = glob.glob(patterning("%s/*" % input_dir))
    file_path_list.sort()  # ensure same order
    assert len(file_path_list) > 0, 'Not Detected Any Files From Path'

    # img = cv2.imread("./output/wsis/mask/2_6063_A_0045149.png")
    # msk = np.zeros((1500, 1494, 3))
    # print(img[589:,:,:].shape)
    # img[589:,:,:] = msk[:,:,:]
    # cv2.imwrite("./output/wsis/mask/2_6088_A_0037218.png", img)
    
