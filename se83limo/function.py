import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def imshow(X, resize=None):
    im = None
    try:
        X = np.asarray(X)
    except (TypeError):
        pass
    try:
        im = Image.fromarray(np.uint8(X))
    except: print("Oops!  That was no valid array!")
    if im is not None:
        if isinstance(resize, tuple) and len(resize) == 2:
            plt.imshow(im.resize(resize))
            return im.resize(resize)
        else:
            print("no or wrong input tuble!") 
            plt.imshow(im)
            return im
    return im
    

if __name__ == "__main__":
    
    xp = np.random.randint(0,255, (2560, 2560, 3)).astype(np.uint8)
    newsize = (1000,1000)
    imshow(xp, newsize)
    #imshow("try str")
    #imshow((0,1,2,3,4,5,6,7,7,8,9,9,4,453,56,3,45,3,24,5,2,5,6,64,67,23,2,3,6,5,3), (256,2560))
    