#nested list sum for instance 

def nested_sum(l):
	total = 0
	count = 0
	for i in l:
		if isinstance(i,list):
			total = total + nested_sum(i)
			
		else:
			total = total + i
			
	return total
