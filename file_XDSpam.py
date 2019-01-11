fname = raw_input('Enter file name: ')
fhand = open(fname)
count = 0
total = 0
for line in fhand:
	if line.startswith ('X-DSPAM-Confidence:'):
		str = 'X-DSPAM-Confidence: 0.8475'
		atpos = str.find(':')
		num = str[atpos+1: ]
		flot = float(num)
		for flot in str:
			count = count + 1
			total = total + flot
		print count
		print total
	
print 'Average: ', total/count
		