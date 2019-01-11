list = [ ] 
while True:
	inp = raw_input('Enter a number: ')
	if inp == 'done': break
	value = float(inp)
	list.append(value)
	
Average = sum(list)/len(list)
print Average