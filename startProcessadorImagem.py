from __future__ import print_function
from projeto import Projeto
from imutils.video import VideoStream
import argparse
import time
from processadorImagem2 import Processador_Dois

#comando = python3 startProjeto.py -o /home/pi/Desktop/2019-04-17_06-03-55.jpg -d 27

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True, 
        help="path to output directory to store snapshots")
ap.add_argument("-d", "--distance", type=float, default=5,
        help="distance in cm. Default value 5cm")

args = vars(ap.parse_args())
path = args["output"]
distance = args["distance"]

print("[INFO] path: ", path)
print("[INFO] distance: %.1f cm" % distance)
processador = Processador_Dois(path, distance)
processador.imageProcessor()

