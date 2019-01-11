fname = raw_input('Enter file name: ')
if len(fname) == 0:
	fname = 'mbox-short.txt'
fhand = open(fname)
for line in fhand: 
	line = line.upper().rstrip()
	print line