import cv2
import matplotlib.pyplot as plt
import numpy as np
from input_output import i_o_func as io



def main() -> None:
    # Normal original Image
    img : np.ndarray = io.load_image('dog.jpg')
    print(img.shape)
    io.show_img(img, "Original")

    # Gray image :
    gri :np.ndarray = io.gray_img(img)
    io.show_img(gri, "Caine gri")
    io.save_img(gri, 'caine_gri.jpg')
    


if __name__ == "__main__":
    main()