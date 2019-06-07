import sys

from preprocess import preprocess_exec
from augmentation import augmentation_exec

if __name__ == "__main__":
	preprocess_exec(sys.argv[1])
	augmentation_exec(sys.argv[1])
	print("Finish!")
