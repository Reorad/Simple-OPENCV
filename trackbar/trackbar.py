from input_output import i_o_func as io
import cv2 as cv
import numpy as np



# SWITCH = "0: OFF  1: ON"

def nothing(_):
    pass


def create_trackbars(window: str) -> None:
    cv.namedWindow(window)  
    for channel in ("R", "G", "B"):
        cv.createTrackbar(channel, window, 0, 255, nothing)
    # cv.createTrackbar(SWITCH, window, 0, 1, nothing)


def run_trackbar(image_name : str, resulting_image_name : str) -> None:
    original_img = io.load_image(image_name)
    create_trackbars(resulting_image_name)

    while True:
        r = cv.getTrackbarPos("R", resulting_image_name)
        g = cv.getTrackbarPos("G", resulting_image_name)
        b = cv.getTrackbarPos("B", resulting_image_name)
        # s = cv.getTrackbarPos(SWITCH, resulting_image_name)

        # if s == 0:
        #     drawn_on_screen = original_img
        # else:
        array_of_rgb_pixels = np.full_like(original_img, (b, g, r))  
        drawn_on_screen = cv.add(original_img, array_of_rgb_pixels)            

        cv.imshow(resulting_image_name, drawn_on_screen)
        if cv.waitKey(1) & 0xFF == 27:  # ESC
            break
        
    cv.destroyAllWindows()