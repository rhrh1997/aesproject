#!/usr/bin/python

import argparse 

def setupArguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("--keysize")
	parser.add_argument("--keyfile")
	parser.add_argument("--inputfile")
	parser.add_argument("--outputfile")
	parser.add_argument("--mode")

	args = vars(parser.parse_args())
	return args

def returnInsideKeyfile(keyfileName):
	filename = keyfileName
	file = open(filename, "r")
	return file.read()
	
def inputFileBytes(inputfileName):
	filename = inputfileName
	file = open(filename, 'rb')
	return file.read()

if __name__ == "__main__":
	#main()
	arguments = setupArguments()
	keysize = arguments['keysize']
	keyfile = arguments['keyfile']
	inputfile = arguments['inputfile']
	outputfile = arguments['outputfile']
	mode = arguments['mode']
	#print(returnInsideKeyfile(keyfile))
	print(inputFileBytes(inputfile))




