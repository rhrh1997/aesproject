#!/usr/bin/python

import argparse 
import sys


inverse_substitutions = (
	['0x52', '0x09', '0x6A', '0xD5', '0x30', '0x36', '0xA5', '0x38', '0xBF', '0x40', '0xA3', '0x9E', '0x81', '0xF3', '0xD7', '0xFB'],
	['0x7C', '0xE3', '0x39', '0x82', '0x9B', '0x2F', '0xFF', '0x87', '0x34', '0x8E', '0x43', '0x44', '0xC4', '0xDE', '0xE9', '0xCB'],
	['0x54', '0x7B', '0x94', '0x32', '0xA6', '0xC2', '0x23', '0x3D', '0xEE', '0x4C', '0x95', '0x0B', '0x42', '0xFA', '0xC3', '0x4E'],
	['0x08', '0x2E', '0xA1', '0x66', '0x28', '0xD9', '0x24', '0xB2', '0x76', '0x5B', '0xA2', '0x49', '0x6D', '0x8B', '0xD1', '0x25'],
	['0x72', '0xF8', '0xF6', '0x64', '0x86', '0x68', '0x98', '0x16', '0xD4', '0xA4', '0x5C', '0xCC', '0x5D', '0x65', '0xB6', '0x92'],
	['0x6C', '0x70', '0x48', '0x50', '0xFD', '0xED', '0xB9', '0xDA', '0x5E', '0x15', '0x46', '0x57', '0xA7', '0x8D', '0x9D', '0x84'],
	['0x90', '0xD8', '0xAB', '0x00', '0x8C', '0xBC', '0xD3', '0x0A', '0xF7', '0xE4', '0x58', '0x05', '0xB8', '0xB3', '0x45', '0x06'],
	['0xD0', '0x2C', '0x1E', '0x8F', '0xCA', '0x3F', '0x0F', '0x02', '0xC1', '0xAF', '0xBD', '0x03', '0x01', '0x13', '0x8A', '0x6B'],
	['0x3A', '0x91', '0x11', '0x41', '0x4F', '0x67', '0xDC', '0xEA', '0x97', '0xF2', '0xCF', '0xCE', '0xF0', '0xB4', '0xE6', '0x73'],
	['0x96', '0xAC', '0x74', '0x22', '0xE7', '0xAD', '0x35', '0x85', '0xE2', '0xF9', '0x37', '0xE8', '0x1C', '0x75', '0xDF', '0x6E'],
	['0x47', '0xF1', '0x1A', '0x71', '0x1D', '0x29', '0xC5', '0x89', '0x6F', '0xB7', '0x62', '0x0E', '0xAA', '0x18', '0xBE', '0x1B'],
	['0xFC', '0x56', '0x3E', '0x4B', '0xC6', '0xD2', '0x79', '0x20', '0x9A', '0xDB', '0xC0', '0xFE', '0x78', '0xCD', '0x5A', '0xF4'],
	['0x1F', '0xDD', '0xA8', '0x33', '0x88', '0x07', '0xC7', '0x31', '0xB1', '0x12', '0x10', '0x59', '0x27', '0x80', '0xEC', '0x5F'],
	['0x60', '0x51', '0x7F', '0xA9', '0x19', '0xB5', '0x4A', '0x0D', '0x2D', '0xE5', '0x7A', '0x9F', '0x93', '0xC9', '0x9C', '0xEF'],
	['0xA0', '0xE0', '0x3B', '0x4D', '0xAE', '0x2A', '0xF5', '0xB0', '0xC8', '0xEB', '0xBB', '0x3C', '0x83', '0x53', '0x99', '0x61'],
	['0x17', '0x2B', '0x04', '0x7E', '0xBA', '0x77', '0xD6', '0x26', '0xE1', '0x69', '0x14', '0x63', '0x55', '0x21', '0x0C', '0x7D'],
)

substitutions = (
	['0x63', '0x7C', '0x77', '0x7B', '0xF2', '0x6B', '0x6F', '0xC5', '0x30', '0x01', '0x67', '0x2B', '0xFE', '0xD7', '0xAB', '0x76'],
	['0xCA', '0x82', '0xC9', '0x7D', '0xFA', '0x59', '0x47', '0xF0', '0xAD', '0xD4', '0xA2', '0xAF', '0x9C', '0xA4', '0x72', '0xC0'],
	['0xB7', '0xFD', '0x93', '0x26', '0x36', '0x3F', '0xF7', '0xCC', '0x34', '0xA5', '0xE5', '0xF1', '0x71', '0xD8', '0x31', '0x15'],
	['0x04', '0xC7', '0x23', '0xC3', '0x18', '0x96', '0x05', '0x9A', '0x07', '0x12', '0x80', '0xE2', '0xEB', '0x27', '0xB2', '0x75'],
	['0x09', '0x83', '0x2C', '0x1A', '0x1B', '0x6E', '0x5A', '0xA0', '0x52', '0x3B', '0xD6', '0xB3', '0x29', '0xE3', '0x2F', '0x84'],
	['0x53', '0xD1', '0x00', '0xED', '0x20', '0xFC', '0xB1', '0x5B', '0x6A', '0xCB', '0xBE', '0x39', '0x4A', '0x4C', '0x58', '0xCF'],
	['0xD0', '0xEF', '0xAA', '0xFB', '0x43', '0x4D', '0x33', '0x85', '0x45', '0xF9', '0x02', '0x7F', '0x50', '0x3C', '0x9F', '0xA8'],
	['0x51', '0xA3', '0x40', '0x8F', '0x92', '0x9D', '0x38', '0xF5', '0xBC', '0xB6', '0xDA', '0x21', '0x10', '0xFF', '0xF3', '0xD2'],
	['0xCD', '0x0C', '0x13', '0xEC', '0x5F', '0x97', '0x44', '0x17', '0xC4', '0xA7', '0x7E', '0x3D', '0x64', '0x5D', '0x19', '0x73'],
	['0x60', '0x81', '0x4F', '0xDC', '0x22', '0x2A', '0x90', '0x88', '0x46', '0xEE', '0xB8', '0x14', '0xDE', '0x5E', '0x0B', '0xDB'],
	['0xE0', '0x32', '0x3A', '0x0A', '0x49', '0x06', '0x24', '0x5C', '0xC2', '0xD3', '0xAC', '0x62', '0x91', '0x95', '0xE4', '0x79'],
	['0xE7', '0xC8', '0x37', '0x6D', '0x8D', '0xD5', '0x4E', '0xA9', '0x6C', '0x56', '0xF4', '0xEA', '0x65', '0x7A', '0xAE', '0x08'],
	['0xBA', '0x78', '0x25', '0x2E', '0x1C', '0xA6', '0xB4', '0xC6', '0xE8', '0xDD', '0x74', '0x1F', '0x4B', '0xBD', '0x8B', '0x8A'],
	['0x70', '0x3E', '0xB5', '0x66', '0x48', '0x03', '0xF6', '0x0E', '0x61', '0x35', '0x57', '0xB9', '0x86', '0xC1', '0x1D', '0x9E'],
	['0xE1', '0xF8', '0x98', '0x11', '0x69', '0xD9', '0x8E', '0x94', '0x9B', '0x1E', '0x87', '0xE9', '0xCE', '0x55', '0x28', '0xDF'],
	['0x8C', '0xA1', '0x89', '0x0D', '0xBF', '0xE6', '0x42', '0x68', '0x41', '0x99', '0x2D', '0x0F', '0xB0', '0x54', '0xBB', '0x16'],
)


def setupArguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("--keysize")
	parser.add_argument("--keyfile")
	parser.add_argument("--inputfile")
	parser.add_argument("--outputfile")
	parser.add_argument("--mode")

	args = vars(parser.parse_args())
	return args

def returnInsideKeyfile(keysize, keyfileName):
	filename = keyfileName
	c = 0
	file = open(filename, "rb")
	barray = ['0x00' for i in range(keysize/8)]
	while(file.read(1) != ""):
		file.seek(c)
		barray[c] = hex(int(file.read(1).encode("hex"), 16))
		c += 1
	return barray
	
def inputFileBytes(inputfileName):
	#read in file byte by byte and store each byte as an element in an array
	filename = inputfileName
	bb = bytearray()
	c = 0
	file = open(filename, "rb")
	bb = file.read().encode("hex")
	file.seek(0)
	barray = ['0x00' for i in range(len(bb)/2+(16-len(bb)%16/2))]
	while(file.read(1) != ""):
		file.seek(c)
		barray[c] = hex(int(file.read(1).encode("hex"), 16))
		c += 1
	return barray

def encrypt(keysize, key, inputfile):
	state = [["0"] for i in range(16)]
	print("input", inputfile)
	print("key", key)

	out = ["0x00" for i in range(len(inputfile))]
	filecursor = 0
	#need to add key expansion to create the key schedule based off the key that is given
	keyschedule = keyExpansion(key, keysize)

	if(keysize == 128):
		while(filecursor < len(inputfile)-1):
			keyindex = 0
			#transfers values from input into state
			for x in range(16):
				state[x] = inputfile[x+filecursor]
			state = addRoundKey(state, keyschedule, keyindex)
			keyindex += 4
			
			for x in range(9):
				state = subBytes(state)
				state = shiftRows(state)
				state = mixColumns(state)
				state = addRoundKey(state, keyschedule, keyindex)
				keyindex += 4
			state = subBytes(state)
			state = shiftRows(state)
			state = addRoundKey(state, keyschedule, keyindex)

			for x in range(16):
				out[x+filecursor] = state[x]

			filecursor += 16

		return out

	if(keysize == 256):
		while(filecursor < len(inputfile)-1):
			keyindex = 0
			#transfers values from input into state
			for x in range(16):
				state[x] = inputfile[x+filecursor]
			state = addRoundKey(state, keyschedule, keyindex)
			keyindex += 4
			
			for x in range(13):
				state = subBytes(state)
				state = shiftRows(state)
				state = mixColumns(state)
				state = addRoundKey(state, keyschedule, keyindex)
				keyindex += 4
			state = subBytes(state)
			state = shiftRows(state)
			state = addRoundKey(state, keyschedule, keyindex)

			for x in range(16):
				out[x+filecursor] = state[x]

			filecursor += 16
			
		return out
	return
	
def decrypt(keysize, key, inputfile):
	state = [["0"] for i in range(16)]
	print("input", inputfile)
	print("key", key)

	out = ["0x00" for i in range(len(inputfile))]
	filecursor = 0
	#need to add key expansion to create the key schedule based off the key that is given
	keyschedule = keyExpansion(key, keysize)

	if(keysize == 128):
		while(filecursor < len(inputfile)-1):
			keyindex = 0
			#transfers values from input into state
			for x in range(16):
				state[x] = inputfile[x+filecursor]
			state = addRoundKey(state, keyschedule, keyindex)
			keyindex += 4
			
			for x in range(9):
				state = invShiftRows(state)
				state = invSubBytes(state)
				state = addRoundKey(state, keyschedule, keyindex)
				state = invMixColumns(state)
				keyindex += 4
			state = invShiftRows(state)
			state = invSubBytes(state)
			state = addRoundKey(state, keyschedule, keyindex)

			for x in range(16):
				out[x+filecursor] = state[x]

			filecursor += 16
		return out

	if(keysize == 256):
		while(filecursor < len(inputfile)-1):
			keyindex = 0
			#transfers values from input into state
			for x in range(16):
				state[x] = inputfile[x+filecursor]
			state = addRoundKey(state, keyschedule, keyindex)
			keyindex += 4
			
			for x in range(13):
				state = invShiftRows(state)
				state = invSubBytes(state)
				state = addRoundKey(state, keyschedule, keyindex)
				state = invMixColumns(state)
				keyindex += 4
			state = invShiftRows(state)
			state = invSubBytes(state)
			state = addRoundKey(state, keyschedule, keyindex)

			for x in range(16):
				out[x+filecursor] = state[x]

			filecursor += 16
		return out
	
	return
		
def subBytes(state):
	#use substitution matrix to replace values in state with substition values
	for e in range(16):
		state[e] = substitutions[int(state[e][2], 16)][int(state[e][3], 16)]
	return state
	
def shiftRows(state):
	temp = ['0x00' for i in range(16)]
	#copy first 4 elements as normal
	for x in range(4):
		temp[x*4] = state[x*4]
	#perform shift algorithm on rest of list
	for e in range(1, 4):
		for f in range(4):
			temp[e+(f*4)] = state[(e+(4*(f+e)))%16]
	return temp
	
def mixColumns(state):
	#copy is a copy of the original values of state for calculation purposes
	#temp is a copy of the multiplicative values of the state values in the given matrix multiplcaiton algorithm
	copy = ['0x00' for i in range(4)]
	temp = ['0x00' for i in range(4)]

	for c in range(4):
		for r in range(4):
			copy[r] = int(state[c*4+r], 16)
			temp[r] = int(state[c*4+r], 16) << 1
			if(format(int(state[c*4+r], 16), '#010b')[2:3] == '1'):
				temp[r] = temp[r]^27
		state[c*4] = "0x{:02x}".format((temp[0]^copy[3]^copy[2]^temp[1]^copy[1])%256)
		state[1+c*4] = "0x{:02x}".format((temp[1]^copy[0]^copy[3]^temp[2]^copy[2])%256)
		state[2+c*4] = "0x{:02x}".format((temp[2]^copy[1]^copy[0]^temp[3]^copy[3])%256)
		state[3+c*4] = "0x{:02x}".format((temp[3]^copy[2]^copy[1]^temp[0]^copy[0])%256)
	return state
	
def invSubBytes(state):
	#use substitution matrix to replace values in state with substition values
	for e in range(16):
		state[e] = inverse_substitutions[int(state[e][2], 16)][int(state[e][3], 16)]
	return state
	
def invShiftRows(state):
	temp = ['0x00' for i in range(16)]
	#copy first 4 elements as normal
	for x in range(4):
		temp[x*4] = state[x*4]
	#perform shift algorithm on rest of list
	for e in range(1, 4):
		for f in range(4):
			temp[(e+(4*(f+e)))%16] = state[e+(f*4)]
	return temp
	
def invMixColumns(state):
	#copy is a copy of the original values of state for calculation purposes
	#temp is a copy of the multiplicative values of the state values in the given matrix multiplcaiton algorithm
	copy = ['0x00' for i in range(4)]
	temp = ['0x00' for i in range(4)]

	for c in range(4):
		for r in range(4):
			copy[r] = int(state[c*4+r], 16)
			temp[r] = int(state[c*4+r], 16) << 1
			if(format(int(state[c*4+r], 16), '#010b')[2:3] == '1'):
				temp[r] = temp[r]^27
		state[c*4] = "0x{:02x}".format((temp[0]^copy[3]^copy[2]^temp[1]^copy[1])%256)
		state[1+c*4] = "0x{:02x}".format((temp[1]^copy[0]^copy[3]^temp[2]^copy[2])%256)
		state[2+c*4] = "0x{:02x}".format((temp[2]^copy[1]^copy[0]^temp[3]^copy[3])%256)
		state[3+c*4] = "0x{:02x}".format((temp[3]^copy[2]^copy[1]^temp[0]^copy[0])%256)
	return state


def addRoundKey(state, keyschedule, keyindex):
	for e in range(16):
		bs = int(state[e], 16)
		bk = int(keyschedule[e/4+keyindex][e%4], 16)
		bs = bs ^ bk
		state[e] = "0x{:02x}".format(bs)
	return state

def keyExpansion(key, keysize):
	nk = keysize/32
	if(keysize == 128):
		nr = 10
	else:
		nr = 14
	i = 0
	rcon = ["0x01", "0x02", "0x04", "0x08", "0x10", "0x20", "0x40", "0x80", "0x1b", "0x36"]
	mschedule = [["0x00"]*4 for x in range(4*(nr+1))]
	while(i < nk):
		mschedule[i] = [key[i*4], key[i*4+1], key[i*4+2], key[i*4+3]]
		i += 1
	i = nk

	while(i < 4*(nr+1)):
		temp = mschedule[i-1]
		if(i%nk == 0):
			temp = subWord(rotWord(temp))
			temp[0] = "0x{:02x}".format(int(temp[0], 16)^int(rcon[i/nk-1], 16))
		elif((nk > 6) and (i%nk == 4)):
			temp = subWord(temp)
		for x in range(4):
			mschedule[i][x] = "0x{:02x}".format(int(mschedule[i-nk][x], 16)^int(temp[x], 16))
		i += 1
	return mschedule

def subWord(word):
	for e in range(4):
		word[e] = substitutions[int(word[e][2], 16)][int(word[e][3], 16)]
	return word

def rotWord(word):
	arr = ['0x00' for i in range(4)]
	for e in range(3):
		arr[e] = word[e+1]
	arr[3] = word[0]
	return arr
	
if __name__ == "__main__":
	#main()
	arguments = setupArguments()
	keysize = arguments['keysize']
	keyfile = arguments['keyfile']
	inputfile = arguments['inputfile']
	outputfile = arguments['outputfile']
	mode = arguments['mode']

	if None in (keysize, keyfile, inputfile, outputfile, mode):
		print("Required arguments missing")
		sys.exit()
	#print(returnInsideKeyfile(keyfile))

	if(mode == 'encrypt'):
		print(encrypt(int(keysize), returnInsideKeyfile(int(keysize), keyfile), inputFileBytes(inputfile)))
	elif(mode == 'decrypt'):
		decrypt(int(keysize), returnInsideKeyfile(int(keysize), keyfile), inputFileBytes(inputfile))
	else:
		print('invalid mode')

