
import cv2
import matplotlib.pyplot as plt
import numpy as np

def load_image(name_photo : str , cale : str = "photos_in/") -> np.ndarray:
    img = cv2.imread(cale+name_photo)
    if img is None :
        raise FileNotFoundError("Couldn't load dog.jpg - is it in the project folder?")
    return img

def show_img(img : np.ndarray, title : str ="Image") -> None :
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def gray_img(img: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def save_img(img : np.ndarray, name : str, path : str = "photos_out/") -> None :
    text : str = path + name
    cv2.imwrite(text, img)