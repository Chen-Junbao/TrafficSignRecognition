import cv2
import sys
import os


def preprocess(path):
	"""
	Preprocess image with GaussianBlur
	:param path: Input image path
	:return: Preprocessed image
	"""
	img = cv2.imread(path)

	# GaussianBlur
	dst = cv2.GaussianBlur(img, (5, 5), 0)

	return dst


def preprocess_exec(path):
	"""
	Get all images, preprocess them and overwrite them.
	:param path: Dataset path
	"""
	filelist = os.listdir(path)

	for file in filelist:
		filepath = os.path.join(path, file)
		if os.path.isdir(filepath):
			preprocess_exec(filepath)
		else:
			image = preprocess(filepath)
			cv2.imwrite(filepath, image)
