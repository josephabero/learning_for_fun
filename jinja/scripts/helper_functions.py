import jinja2

def get_jinja_environment(template):
	file_loader = jinja2.FileSystemLoader(searchpath=template)
	return jinja2.Environment(loader=file_loader)

def write_to_file(content, output_file):
	""" Writes string to file
	"""
	with open(output_file, 'w') as file:
		file.write(content)