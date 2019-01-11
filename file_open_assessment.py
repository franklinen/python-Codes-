fh = open('romeo.txt')
lword = []
for line in fh:
	line.rstrip()
	words = line.split()
	for word in words:
		if word not in lword:  
			lword.append(word)
			lword.sort()
print lword
	