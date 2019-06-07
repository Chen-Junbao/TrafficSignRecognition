import cv2
import sys
import os
import numpy as np


def rotate(path):
	"""
	Rotate the image in a small angle.
	:param path: Input image path
	:return: Rotated images
	"""
	img = cv2.imread(path)

	# center of image
	(h, w) = img.shape[:2]
	center = (w / 2, h / 2)

	# Rotate the image in 5 angles
	dst = []
	for i in range(5):
		M = cv2.getRotationMatrix2D(center, (i - 2) * 3, 1.0)
		dst.append(cv2.warpAffine(img, M, (w, h)))

	return dst


def shift(path):
	"""
	Shift the image in a small distance
	:param path: Input image path
	:return: Shifted images
	"""
	img = cv2.imread(path)

	# shape of image
	(h, w) = img.shape[:2]

	# Shift the image in 5 angles
	dst = []
	for i in range(5):
		M = np.float32([[1, 0, (i - 2) * 5], [0, 1, (i - 2) * 3]])
		dst.append(cv2.warpAffine(img, M, (w, h)))

	return dst


def augmentation_exec(path):
	"""
	Get all images, preprocess them and overwrite them.
	:param path: Dataset path
	"""
	filelist = os.listdir(path)

	for file in filelist:
		filepath = os.path.join(path, file)
		if os.path.isdir(filepath):
			augmentation_exec(filepath)
		else:
			image_rotate = rotate(filepath)
			image_shift = shift(filepath)
			for i in range(5):
				if i == 2:
					# The original image
					continue
				temp = str(filepath).split('.')
				cv2.imwrite(temp[0] + "_" + str(i) + "." + temp[1], image_rotate[i])
				cv2.imwrite(temp[0] + "-" + str(i) + "." + temp[1], image_shift[i])
