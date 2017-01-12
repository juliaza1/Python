import sys
import os
import os.path
import fnmatch

def count(filename):
	aLine = 0 
	bWords = 0
	cChar = 0

	infile = open(filename, 'r')
	#counting lines
	for line in infile:
		words = line.split()
		aLine += 1
		bWords += len(words)
		cChar += len(line)
	print(aLine, '\t', bWords, '\t', cChar, '\t', filename)


def main():
	if len(sys.argv) == 2:
		count(sys.argv[1])

	elif len(sys.argv) > 1:
		try:
			for file in sys.argv[0:-1]:
				if os.path.isfile(file):
					count(file)
		except:
			print("Error file handling. Quitting...")
			sys.exit(1)

	elif sys.argv[1] == '*.py':
		pattern = '*.py'
		try:
			for file in os.listdir('.'):
				if fnmatch.fnmatch(file, pattern):
					count(file)
		except:
			print("Unknown file error. Quitting...")
			sys.exit(1)



if __name__ == '__main__':
	main()