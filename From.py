fhand = raw_input("Enter file name: ")
fh = open(fhand)
count = 0
for line in fh:
	words = line.split()	
	if line.startswith("From "):
		twoo = words[1]	
		print twoo
		count = count + 1
print twoo
print count

