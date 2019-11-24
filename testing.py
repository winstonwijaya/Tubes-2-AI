import numpy as np
import cv2 as cv 
import imutils

class shapeDetector:
    def __init__(self):
        pass
    
    def detect(self, c):
        perimeter = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.05*perimeter, True)
        cv.drawContours(imageInput, [approx], 0, (0, 120, 255), 10)
        print(len(approx))
        print("approx: ")
        print(approx)
        if (len(approx) == 3):
            shape = "triangle"
        elif len(approx) == 4:
            (x, y, w, h) = cv.boundingRect(approx)
            ar = w / float(h)
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        elif len(approx) == 5:
            shape = "pentagon"
        else:
            shape = "circle"
        return shape

if __name__ == "__main__":
    imageInput = cv.imread('data-set/triangle3.png')
    imageInput = cv.resize(imageInput, (300, 500))
    resized = imutils.resize(imageInput, width=300)
    ratio = imageInput.shape[0] / float(resized.shape[0])
    imageGray = cv.cvtColor(imageInput, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(imageGray, (5, 5), 0)
    thresh = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY)[1]
    cnts = cv.findContours(thresh.copy(), 
                            cv.RETR_EXTERNAL, 
                            cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = shapeDetector()
    for c in cnts:
        M = cv.moments(c)
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)
        print("shape " + shape)
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        # cv.drawContours(imageInput, [c], -1, (123, 255, 0), 3)
        cv.putText(imageInput, shape, (cX, cY), cv.FONT_HERSHEY_SIMPLEX,
		0.5, (254, 0, 255), 2)
        cv.imshow("Image", imageInput)
        cv.waitKey(0)