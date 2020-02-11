
def get_file_extension(path):
	paths = path.split('.')
	if len(paths) > 0:
		return paths[-1]
	raise Exception("File doesnt have any extensions")