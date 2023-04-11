import cv2
import numpy as np


if __name__== "__main__":
    img = cv2.imread("./output/wsis/mask/2_6063_A_0045149.png")
    # msk = np.zeros((1500, 1494, 3))
    # print(img[589:,:,:].shape)
    # img[589:,:,:] = msk[:,:,:]
    cv2.imwrite("./output/wsis/mask/2_6088_A_0037218.png", img)
    