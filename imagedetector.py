import numpy as np
import cv2 as cv
import imutils
import math
import clipspy as cl

precision = 5
epsilon = 0.00000000001

SHAPES_MAP = {
    'Segitiga Lancip' : '(shape triangle_acute)',
    'Segitiga Tumpul' : '(shape triangle_obtuse)',
    'Segitiga Siku-siku' : '(shape triangle_right)',
    'Segitiga Sama Kaki dan Siku-siku' : '(shape triangle_isosceles_right)',
    'Segitiga Sama Kaki dan Tumpul' : '(shape triangle_isosceles_obtuse)',
    'Segitiga Sama Kaki dan Lancip' : '(shape triangle_isosceles_acute)',
    'Segitiga Sama Sisi' : '(shape triangle_equilateral)',
    'Jajaran Genjang Beraturan' : '(shape square)',
    'Layang-layang' : '(shape kite)',
    'Trapezium Sama Kaki' : '(shape trapezoidal_isosceles)',
    'Trapezium Rata Kanan' : '(shape trapezoidal_right)',
    'Trapezium Rata Kiri' : '(shape trapezoidal_left)',
    'Segi Lima Sama Sisi' : '(shape pentagon)',
    'Segi Enam Sama Sisi' : '(shape hexagon)',
}
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
            res.append(int((leng)/5)*5)
        return res

    def findTheAngleArrayContour(self, c):
        appr = self.findTheApproxPolygonContour(c)
        length = self.findTheNumberOfSidesContour(c)

        res = []
        for i in range(0, length):
            res.append(self.findTheAngleThreePoint(appr[(i-1)%length][0], appr[(i)%length][0], appr[(i+1)%length][0]))
            res[i] = int((res[i])/5)*5
        sumAngle = (length-2)*180
        tot = 0
        for i in res:
            tot += i
        if (tot > sumAngle+precision):
            for i in range(0, length):
                res[i] = 360-res[i]
        return res

    def iterateContourInContours(self, shape):
        matchContour = []
        fakta = []
        for c in self.contours:
            cx, cy = self.findCenterContour(c)
            tmp = []
            sisi = self.findTheLengthSideArrayContour(c)
            sudut = self.findTheAngleArrayContour(c)
            temp = "(sides "
            pertama = True
            for side in sisi:
                if (pertama):
                    pertama = False
                    temp = temp + (str(side))
                else:
                    temp = temp + (" " + str(side))
            temp = temp + ")"
            tmp.append(temp)

            temp = "(angles "
            pertama = True
            for angle in sudut:
                if (pertama):
                    pertama = False
                    temp = temp + (str(angle))
                else:
                    temp = temp + (" " + str(angle))
            temp = temp + ")"
            tmp.append(temp)

            tmpFakta = cl.findFact(tmp)
            fakta.append(tmpFakta)
            check = False

            for j in tmpFakta:
                if (SHAPES_MAP[shape] == j):
                    check = True
                    break
            
            if (check) :
                matchContour.append(c)

        for c in matchContour:
            cv.drawContours(self.image, [c], -1, (255,255,0), 10)
        
        cv.imwrite('data-set/hasil.png', self.image)
        return fakta
        

if __name__ == "__main__":
    image1 = image('image1')
    inp = input()
    image1.inputImage(inp)
    t = image1.findContoursImage()
    image1.iterateContourInContours()
    image1.outputImage()

