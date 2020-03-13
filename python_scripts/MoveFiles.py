"""
Moves files recursively from one folder to the next
__author__: Amna Hyder
__date__: August 2018
"""

# import os
# for root, dirs, files in os.walk("/mydir"):
#     for file in files:
#         if file.endswith(".txt"):
#              print(os.path.join(root, file))

# import os, shutil

# # First, create a list and populate it with the files
# # you want to find (1 file per row in myfiles.txt)
# files_to_find = []
# with open('myfiles.txt') as fh:
#     for row in fh:
#         files_to_find.append(row.strip)

# # Then we recursively traverse through each folder
# # and match each file against our list of files to find.
# for root, dirs, files in os.walk('C:\\'):
#     for _file in files:
#         if _file in files_to_find:
#             # If we find it, notify us about it and copy it it to C:\NewPath\
#             print 'Found file in: ' + str(root)
#             shutil.copy(os.path.abspath(root + '/' + _file), 'C:\\NewPath\\')

import os, sys, shutil

def move_files_recursive(path):
	path3 = "/Volumes/Seagate Backup Plus Drive/Hyperscanning/Data_edited/edf"
	files = os.listdir(path)
	for file in files:
		if os.path.isdir(file):
			move_files_recursive(path + file + '/')
			print('checking directory',path + file + '/')
			path2 = os.path.join(path, file)
			os.chdir(path2)
			files2 = os.listdir(path2)
			for file2 in files2:
				if file2.endswith('.edf'):
					#or file2.endswith('.edf')
					try:
						shutil.copyfile(os.path.join(path2, file2),os.path.join(path3,file2))
						#print(os.path.join(path2, file2))
					except IOError: 
						continue
						print(os.path.join(path2, file2))
						print(path)
					os.chdir(path)

if __name__ == '__main__' :
	print(os.getcwd())
	move_files_recursive(os.getcwd()+'/')
