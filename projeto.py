from __future__ import print_function
from PIL import Image
from PIL import ImageTk
import tkinter as tki
import threading
import datetime
import imutils
import os
import cv2 as cv
import time
import RPi.GPIO as GPIO
from processadorImagem2 import Processador_Dois
#from concretefactory.ultrasonicSensorFactory import UltrasonicSensorFactory

class Projeto:
    def __init__(self, vs, outputPath):
        self.vs = vs
        self.outputPath = outputPath
        self.frame = None
        self.thread = None
        self.stopEvent = None
        self.distance = None
        self.triggerPort = 18
        self.echoPort = 27
        self.sensor = None
        self.root = tki.Tk()
        self.panel = None

        btn = tki.Button(self.root, text="Take picture", command=self.takePicture)
        btn.pack(side="bottom", fill="both", expand="yes",
                padx=10, pady=10)

        #self.sensor = UltrasonicSensorFactory.createSensor("HYSRF05")
        #Biblioteca de Junior Porem não estou utilizando
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.triggerPort, GPIO.OUT)
        GPIO.setup(self.echoPort, GPIO.IN)
        

        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.start()

        self.root.wm_title("Projeto ESP203")
        self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)

    def videoLoop(self):
        try:
            while not self.stopEvent.is_set():
                self.frame = self.vs.read()
                self.frame = imutils.resize(self.frame, width=300)

                image = cv.cvtColor(self.frame, cv.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image=image)

                if self.panel is None:
                    self.panel = tki.Label(image=image)
                    self.panel.image = image
                    self.panel.pack(side="left", padx=10, pady=10)

                else:
                    self.panel.configure(image=image)
                    self.panel.image = image

        except RuntimeError as e:
            print("[INFO] caught a RuntimeError")

    def takePicture(self):
        ts = datetime.datetime.now()
        formattedTS = ts.strftime("%Y-%m-%d_%H-%M-%S")
        filename = "{}.jpg".format(formattedTS)
        path = os.path.sep.join((self.outputPath, filename))
        cv.imwrite(path, self.frame.copy())
        
        print("[INFO] saved {}".format(filename))
        
        GPIO.output(self.triggerPort, GPIO.HIGH)
        time.sleep(0.00001)
        
        GPIO.output(self.triggerPort, GPIO.LOW)
        start = time.time()

        while GPIO.input(self.echoPort)==0:
                start = time.time()
                print("start: ", start)

        while GPIO.input(self.echoPort)==1:
                stop = time.time()
                print("stop: ", stop)
                
        t_transcorrido=stop-start
        
        print(t_transcorrido)
        
        distance = (t_transcorrido * 17000)
        
        print("[INFO] distance %.1f cm" % distance)
        # Distancia da foto das moedas 27 cm.
        #Fotos na area de trabalho
        processador = Processador_Dois(path, distance)
        processador.imageProcessor()

    def onClose(self):
        print("[INFO] closing")
        self.stopEvent.set()
        self.vs.stop()
        GPIO.cleanup()
        self.root.quit()
