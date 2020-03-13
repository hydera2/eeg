"""
Changes triggers for evt files
__author__: Amna Hyder
__date__: August 2018
"""
import os
import csv


if __name__ == '__main__':

	files = filter(lambda x: 'txt' in x, os.listdir(os.getcwd()))
	print(files)
	for f in files:
		# see if need to rename
		with open(f) as t:
			table = csv.reader(t, delimiter='\t')
			new_table = []
			for line in table:
				if 'Code' in line: 
					new_table.append(line)
					continue
				trigger = line[3]
				line[3] = trigger.replace('Trigger - ', '')
				if 'gcmp' in line[3]: line[2] = 3
				elif 'gcoo' in line[3]: line[2] = 2
				elif 'gree'
				in line[3]: line[2] = 1
				new_table.append(line)
			writer = csv.writer(open('clean_' + f, 'w'), delimiter='\t')
			for i in new_table: print(i)
			writer.writerows(new_table)

