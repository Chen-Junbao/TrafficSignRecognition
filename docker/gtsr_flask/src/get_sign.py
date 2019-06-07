def get_sign():
    """
	Read traffic sign information from file
	:return: Traffic information
	"""
    info = []
    with open('sign.txt', encoding='UTF-8') as f:
        line = f.readline()
        while line:
            info.append(line.strip())
            line = f.readline()

    return info