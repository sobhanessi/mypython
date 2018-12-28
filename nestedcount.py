#nested list count for instance

def nested_count(l):
	
	count = 0
	
	for i in l:
		if isinstance(i,list):
			
			count = count + nested_sum(i)
		else:
			
			count = count + 1
			
	return count
