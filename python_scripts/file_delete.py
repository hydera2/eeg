
"""
Deletes files that you don't need recursively in folders
__author__: Amna Hyder
__date__: August 2018
"""

import os, sys, shutil

def remove_files_recursive(path):
	files = os.listdir(path)
	for file in files:
		if os.path.isdir(file):
			remove_files_recursive(path + file + '/')
			print('checking directory',path + file + '/')
		# elif not file.endswith('_seg.mff'):
		# 	shutil.rmtree(os.path.join(path, file))
		elif  not file.endswith('.mff') and not file.endswith('.py'):
			os.remove(os.path.join(path, file))
			print('deleting file',os.path.join(path, file))

if __name__ == '__main__' :
	print(os.getcwd())
	remove_files_recursive(os.getcwd()+'/')

