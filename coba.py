import numpy as np
import cv2 as cv
import imutils

class shape:
    def __init__(self, name):
        self.name = name
        self.image = None
        self.contour = None
        self.propery = []
        pass
    
    def inputShape(self, imageName):
        self.image = cv.imread(imageName)
    
    def outputShape(self):
        cv.imshow(self.name, self.image)
        cv.waitKey(0)
    
    def convertToGrayImage(self):
        temp = cv.cvtColor(self.input, cv.COLOR_BGR2GRAY)
        return tmp

    def findContoursShape(self):
        blurred = cv.GaussianBlur(convertToGrayImage(self.image), (5, 5), 0)
        thresh = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY)[1]
        cnts = cv.findContours(thresh.copy(), 
                            cv.RETR_EXTERNAL, 
                            cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        self.contour = cnts

    def findCenter(self):
        M = cv.moments(self.contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        return cX, cY

    def get_angle(p1, p2):
    return math.atan2(p1[1] - p2[1], p1[0] - p2[0]) * 180/math.pi

    def findTheNumberOfSides(self):
    
    def findAngle(self):



if __name__ == "__main__":
    test = shape('shape1')
    test.inputShape('data-set/triangle3.png')
    test.outputShape()
