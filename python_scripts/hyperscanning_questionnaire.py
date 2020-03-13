"""
Creates a questionnaire on python for subjects 

__author__: Amna Hyder
__date__: August 2018
"""

import csv
import os
from tabulate import tabulate


def valid_input(num_text):
	if num_text.isdigit():
		num = int(num_text)
		return num >= 1 and num <= 5
	return False

if __name__ == '__main__':

	os.system('clear')

	likert = tabulate([[1, 2, 3, 4, 5]], headers=['Not at All', 'A Little', 'Moderately', 'Quite a Bit', 'Extremely'])
	#a name for the subject file
	trial = raw_input('Name this file: ')
	#put the questions
	questions = ['Interested', 'Distressed', ' Excited', 'Upset', 'Strong', 'Guilty', 'Scared', 'Hostile','Enthusiastic','Proud']
	answers = [] 
	for numb in range (1,7):
		curr_answers = []
		os.system('clear')
		for question in questions:
			print('\n'*2)
			print('\t Please indicate the extent to which you feel the following terms from 1 to 5.')
			print('\n'*8)
			print('\t \t \t \033[1m \t \t' + question + '\033[0m')
			print('\n'*4)
			print(likert)
			print('\n'*2)
			user_input =  raw_input("response: \t")
			#get them within a certain range
			while not valid_input(user_input):
				print("You must enter a number from 1 to 5 (i.e. 0,1,2...)")
				user_input =  raw_input("response: \t")
			curr_answers.append(user_input)
			os.system('clear')
		answers.append(curr_answers)
		os.system('clear')	
		print('\n'*10)
		print(" \t \t \t BREAK - PLEASE HAND LAPTOP TO RESEARCH ASSISTANT")
		user_input =  raw_input()


	with open(trial + '.csv', 'wb') as myfile:
	    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	    wr.writerow(questions)
	    for answer_set in answers:
	    	wr.writerow(answer_set)





