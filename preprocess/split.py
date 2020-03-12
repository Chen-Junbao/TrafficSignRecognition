import shutil


def split():
	"""
	Split the dataset
	:return: 9 slices
	"""
	prefix = '000'
	split_number = 0
	for i in range(43):
		if i < 10:
			prefix = '0000'
		else:
			prefix = '000'
		# make corresponding directories before run it
		shutil.move('/data/train/' + prefix + str(i), '/data/train/split' + str(split_number))
		if i != 0 and i % 5 == 0:
			split_number += 1


def restore():
	"""
	Restore the dataset
	:return: the original dataset with 43 classes
	"""
	prefix = '/000'
	split_number = 0
	for i in range(43):
		if i < 10:
			prefix = '/0000'
		else:
			prefix = '/000'
		# make corresponding directories before run it
		shutil.move('/data/train/split' + str(split_number) + prefix + str(i), '/data/train/')
		if i != 0 and i % 5 == 0:
			# Delete split directories
			shutil.rmtree('/data/train/split' + str(split_number))
			split_number += 1



if __name__ == "__main__":
	restore()