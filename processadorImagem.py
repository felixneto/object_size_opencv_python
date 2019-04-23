class Processador:
    def __init__(self, inputPath, distance):
        self.vs = vs
        self.inputPath = inputPath
        self.distance = distance

    def imageProcessor(self):
		image = cv2.imread(self.inputPath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
		
        
