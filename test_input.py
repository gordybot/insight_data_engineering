#!/usr/bin/python3

import sys


# Driver function.
def main():
	print('Number of arguments:', len(sys.argv), 'arguments.')
	print('Argument List:', str(sys.argv) )
	if len(sys.argv) < 4:
		print('Need one input and two output file names, e.g.: ')
		print('h1b_thing infile outfile1 outfile2')
	else:
		in_filename = sys.argv[1]
		#outfile_jobs = './output/top_10_occupations.txt'
		#outfile_states = './output/top_10_states.txt'
		outfile_jobs = sys.argv[2]
		outfile_jobs = sys.argv[3]

		var_descriptors = [['work','state'],['poc_code'],['status']]

if __name__=='main':
	main()
