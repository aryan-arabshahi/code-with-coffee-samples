import numpy as np
import cv2
from mss import mss
from PIL import Image
import keyboard
from time import sleep


WINDOW_DETAILS = {
    'top': 200,
    'left': 0,
    'width': 800,
    'height': 400,
}


def main():
    screen = mss()
    while True:
        count = 0
        cropped_screen_shot = screen.grab(WINDOW_DETAILS)
        cropped_image = np.array(Image.frombytes(
            'RGB',
            (cropped_screen_shot.width, cropped_screen_shot.height),
            cropped_screen_shot.rgb
        ))

        gray_image = cv2.cvtColor(cropped_image[220:260, 110:270], cv2.COLOR_BGR2GRAY)

        th, threshed = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU) 
        contours = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2] 

        if len(contours) >= 1:
            keyboard.press('space')

        # cv2.imshow('cropped_image', cropped_image)
        # cv2.imshow('danger_zone', np.array(gray_image))
        cv2.imshow('contours', np.array(threshed))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
