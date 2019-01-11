fname = raw_input('Enter filename: ')
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
count = 0
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1
print line

print 'Subject line count is:', count	


