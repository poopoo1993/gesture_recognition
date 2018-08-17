import cv2
import os

#create folder to save the image set to train
def createDir(gesture_name):
	if not os.path.exists("gesture"):
		os.makedirs("gesture")

	if not os.path.exists("gesture/" + gesture_name):
		os.makedirs("gesture/" + gesture_name)
	else:
		os.system("rm -rf " + "gesture/" + gesture_name)
		os.makedirs("gesture/" + gesture_name)

while True:
	
	gesture_name = input("Enter the gesture name:")
	createDir(gesture_name)
	
	#1 is because I use another cam rather than the one in laptab 
	cap = cv2.VideoCapture(1)
	counter = 1
	while True:
		ret, frame = cap.read()
		image = cv2.flip(frame, 1)
		image = cv2.rectangle(image, (100, 100), (400, 400), (255,0,0), 2)
		cv2.imshow(gesture_name,image)
	
		commond = cv2.waitKey(1)
		
		if commond == 27:
			break
		elif commond == 32:
			gesture = image[100:400, 100:400]
			cv2.imwrite("gesture/" + gesture_name + "/" + 
						gesture_name +"_" + str(counter) + ".jpg", gesture)
			print("get gesture " + str(counter))
			counter = counter + 1
			if counter == 201:
				break
		
	if input("Do you want to add another gesture?(y/n)") == 'y':
		cv2.destroyAllWindows()	

	else:
		break
	
