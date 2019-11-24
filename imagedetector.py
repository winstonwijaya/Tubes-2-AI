import numpy as np
import cv2 as cv
import imutils
import math

precision = 5
epsilon = 0.00000000001

class image:
    def __init__(self, name):
        self.name = name
        self.image = None
        self.contours = None
        self.propery = []
        pass
    
    def getName(self):
        return self.name
    
    def getContours(self):
        return self.contour
    
    def getLengthContours(self):
        return len(getContour())

    def inputImage(self, imageName):
        self.image = cv.imread(imageName)
    
    def outputImage(self):
        cv.imshow(self.name, self.image)
        cv.waitKey(0)
    
    def findGrayImage(self):
        temp = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        return temp

    def findContoursImage(self):
        blurred = cv.GaussianBlur(self.findGrayImage(), (5, 5), 0)
        thresh1, thresh2 = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY)
        cnts = cv.findContours(blurred.copy(), 
                            cv.RETR_LIST, 
                            cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        self.contours = cnts
        return cnts

    def findCenterContour(self, c):
        M = cv.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        return cX, cY
    
    def findAngle(p1, p2):
        return math.atan2(p1[1] - p2[1], p1[0] - p2[0]) * 180/math.pi

    def findTheNumberOfSidesContour(self, c):
        perimeter = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.05*perimeter, True)
        return len(approx)
    
    def findTheApproxPolygonContour(self, c):
        perimeter = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.05*perimeter, True)
        return approx

    def findTheAngleThreePoint(self, a, b, c):
        angle = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0])-math.atan2(a[1]-b[1], a[0]-b[0]))
        if (angle < 0):
            angle += 360
        return angle
    
    def findLengthTwoPoint(self, a, b):
        leng = math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))
        return leng

    def findTheLengthSideArrayContour(self, c):
        appr = self.findTheApproxPolygonContour(c)
        length = self.findTheNumberOfSidesContour(c)
        res = []
        for i in range(0, length):
            leng = self.findLengthTwoPoint(appr[i][0], appr[(i+1)%length][0])
            res.append(leng)
        return res

    def findTheAngleArrayContour(self, c):
        appr = self.findTheApproxPolygonContour(c)
        length = self.findTheNumberOfSidesContour(c)
        print(appr)
        res = []
        for i in range(0, length):
            # find the angle p[i], p[(i+1)%length], p[(i+2)%length]
            print(appr[(i-1)%length][0], appr[(i)%length][0], appr[(i+1)%length][0])
            res.append(self.findTheAngleThreePoint(appr[(i-1)%length][0], appr[(i)%length][0], appr[(i+1)%length][0]))
        sumAngle = (length-2)*180
        tot = 0
        for i in res:
            tot += i
        if (tot > sumAngle+precision):
            for i in range(0, length):
                res[i] = 360-res[i]
        return res

    def iterateContourInContours(self):
        it = 1
        for c in self.contours:
            cx, cy = self.findCenterContour(c)
            print(it, self.findTheNumberOfSidesContour(c))
            # print(self.findTheApproxPolygonContour(c))
            print('Angle', self.findTheAngleArrayContour(c))
            print('Side Length', self.findTheLengthSideArrayContour(c))
            cv.drawContours(self.image, [c], -1, (255, 0, 0, 1), 2)
            cv.imwrite('data-set/hasil.jpg', self.image)

if __name__ == "__main__":
    image1 = image('image1')
    inp = input()
    image1.inputImage(inp)
    t = image1.findContoursImage()
    image1.iterateContourInContours()
    image1.outputImage()

