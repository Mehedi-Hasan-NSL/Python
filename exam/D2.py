import os 

"""
commands to create directories in this directory
mkdir test
cd test
mkdir {1..5}
cd 1
touch txt 
touch test.txt
mkdir a
cd a
touch a_test.txt
"""

def get_list_of_filename_dir(dir):
	child_dirs = os.listdir(dir)
	all_list = list()

	for child in child_dirs:
		path = dir + "/" + child
		#print(path)
		if os.path.isdir(path):
			all_list.append(path)
			all_list = all_list + get_list_of_filename_dir(path)
		else:
			all_list.append(path)
	return all_list

#print(*get_list_of_filename_dir())
## "./1/D/test" have multiple directoreis with subdirectories

for path in get_list_of_filename_dir("./1/D/test"):
	print(path)