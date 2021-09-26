import cv2
import matplotlib.pyplot as plt

def denoise(image, kernel_type, **kwargs):
    if kernel_type == 'box':
        imOu = cv2.blur(image, kwargs['ksize'])
    elif kernel_type == 'median':
        imOu = cv2.medianBlur(image, kwargs['ksize'])
    elif kernel_type == 'gaussian':
        imOu = cv2.GaussianBlur(image, kwargs['ksize'], 0)
    else:
        print('Operation not implemented')
    return imOu


    


