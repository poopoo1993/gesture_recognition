import tensorflow as tf
import numpy as np
import os, glob, cv2
import sys, argparse


sess = tf.Session()
saver = tf.train.import_meta_graph('model.meta')
# Step-2: Now let's load the weights saved using the restore method.
saver.restore(sess, tf.train.latest_checkpoint('./'))

# Accessing the default graph which we have restored
graph = tf.get_default_graph()

cap = cv2.VideoCapture(1)
cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("frame",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
while True:
	ret, frame = cap.read()
	frame = cv2.flip(frame,1)
	cv2.rectangle(frame, (50, 50), (350, 350), (255,0,0), 2)
	image = frame[50:350,50:350]
	image = cv2.flip(image,1)
	image = cv2.resize(image, (150, 150),0,0, cv2.INTER_LINEAR)
	images = []
	images.append(image)
	images = np.array(images, dtype=np.uint8)
	images = images.astype('float32')
	images = np.multiply(images, 1.0/255.0)
	x_batch = images.reshape(1, 150, 150, 3)
	y_pred = graph.get_tensor_by_name("y_pred:0")

	## Let's feed the images to the input placeholders
	x= graph.get_tensor_by_name("x:0")
	y_true = graph.get_tensor_by_name("y_true:0")
	y_test_images = np.zeros((1, len(os.listdir('gesture'))))
	classes = os.listdir('gesture')
	### Creating the feed_dict that is required     to be fed to calculate y_pred 
	feed_dict_testing = {x: x_batch, y_true: y_test_images}
	result=sess.run(y_pred, feed_dict=feed_dict_testing)
	result=result.tolist()
	
	for i in range(len(result[0])):
		image = cv2.putText(frame, str(classes[i])+':' + str("%2.1f0"%result[0][i]), (50, 80+30*i), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)
	cv2.imshow("frame", frame)
	if cv2.waitKey(1) == 27:
		break
