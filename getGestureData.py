import cv2
import os

#create folder to save the image set to train
def createDir(gesture_name):
	if not os.path.exists("/gesture"):
		os.makedirs("gesture")

	if not os.path.exists("gesture/" + gesture_name):
		os.makedirs("gesture/" + gesture_name)
	else:
		os.system("rm -rf " + "gesture/" + gesture_name)
		os.makedirs("gesture/" + gesture_name)




