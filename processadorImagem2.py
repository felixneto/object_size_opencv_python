import cv2
import os
import datetime
import numpy

class Processador_Dois:
    
    def __init__(self, inputPath, distance):
        self.inputPath = inputPath
        self.distance = distance #In milimiters
        self.focalLength = 4 #In milimiters the focal length of logitech c510
        self.sensorWidth = 3.58 #In milimiters the sensor wide of logitech c510 
        self.sensorHeight = 2.02 #In milimiters the sensor high of logitech c510 

    def imageProcessor(self):
	    image = cv2.imread(self.inputPath, cv2.IMREAD_COLOR)
	    imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	    metodo = cv2.THRESH_BINARY_INV
	    ret, imgBinarizada = cv2.threshold(imgray, 127, 255, metodo)
	    e = numpy.ones((3,3), numpy.uint8)
	    imgTratada = cv2.morphologyEx(imgBinarizada, cv2.MORPH_CLOSE, e)
	    imgTratada = cv2.erode(imgTratada, e, iterations = 1)
	    imgSegmentada = cv2.Canny(imgTratada, 100, 200)
	    
	    
	    modo = cv2.RETR_TREE
	    metodo = cv2.CHAIN_APPROX_SIMPLE
	    _, contornos, hierarquia = cv2.findContours(imgSegmentada, modo, metodo)
	    	    
	    diretorio = os.path.dirname(self.inputPath)
	    ts = datetime.datetime.now()
	    formattedTS = ts.strftime("%Y-%m-%d_%H-%M-%S")
	    filename = "{}.bmp".format(formattedTS)
	    
	    path = os.path.sep.join((diretorio, filename))
	    
	    imageHeight, imageWidth, channels = image.shape
	    
	    for objeto in contornos:
	        rect = cv2.boundingRect(objeto)
	        x,y,w,h = rect
	        countour = cv2.contourArea(objeto, True)

	        if(countour < 0): continue

	        if (w > 50 or h > 50):
                    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
                    objectWidth = (w*self.distance*self.sensorWidth)/(self.focalLength*imageWidth)
                    objectHeight = (h*self.distance*self.sensorHeight)/(self.focalLength*imageHeight)
                    objectArea = objectHeight*objectWidth
                    cv2.putText(image, 'A: %.2f mm' % objectArea, (x+w+10, y+h), 0, 0.3,(0,255,0))
                    print(objectArea)
	    
	    cv2.imwrite(path, image)
	    cv2.imshow("Imagem Segmentada", imgSegmentada)
	    cv2.imshow("Imagem", image)

	    cv2.waitKey(0)
	    cv2.destroyAllWindows()
