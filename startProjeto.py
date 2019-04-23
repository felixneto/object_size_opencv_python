from __future__ import print_function
from projeto import Projeto
from imutils.video import VideoStream
import argparse
import time

#comando = python3 startProjeto.py -o /home/pi/Desktop/

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True, 
        help="path to output directory to store snapshots")
ap.add_argument("-p", "--picamera", type=int, default=-1,
        help="Whether or not the Raspberry Pi camera should be used")

args = vars(ap.parse_args())

print("[INFO] warming up camera...")
vs = VideoStream().start()
time.sleep(2.0)

pba = Projeto(vs, args["output"])
pba.root.mainloop()
