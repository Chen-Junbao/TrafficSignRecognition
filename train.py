from keras.models import save_model
from keras.utils import np_utils
from keras import backend as K

import os
import numpy as np
import cv2
import tensorflow as tf
import ResNet


def set_config():
	config = tf.ConfigProto(allow_soft_placement=True, device_count={'GPU': 1})
	session = tf.Session(config=config)
	K.set_session(session)


def load_data():
	"""
	Load data from files
	:return: samples and labels
	"""
	X_train = []
	y_train = []
	X_test = []
	y_test = []

	# Load training data
	path = "data/train/"
	dirs = os.listdir(path)
	for dir in dirs:
		images = os.listdir(path + dir)
		for image in images:
			X_train.append(cv2.imread(path + dir + '/' + image))
			y_train.append(int(dir))

	# Load test data
	path = "data/test/"
	with open("data/test.txt") as f:
		info = f.readline()
		while info:
			info = info.strip().split(' ')
			X_test.append(cv2.imread(path + info[0]))
			y_test.append(int(info[1]))
			info = f.readline()

	return np.array(X_train), np.array(y_train), np.array(X_test), np.array(y_test)


X_train, y_train, X_test, y_test = load_data()

batch_size = 128
class_number = 43
epoch = 10

img_rows, img_cols = 48, 48
img_channels = 3

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

y_train = np_utils.to_categorical(y_train, class_number)
y_test = np_utils.to_categorical(y_test, class_number)

model = ResNet.ResNetBuilder.build_resnet_18((img_channels, img_rows, img_cols), class_number)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=epoch, batch_size=batch_size)

accuracy = model.evaluate(X_test, y_test, batch_size=batch_size)
print(accuracy)

save_model(model, "GTSR_model_keras")