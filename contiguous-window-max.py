def TARGET_TEMP(days, temperatures):
	largesttemp_final = -274
	target_start = 0
	target_end = 0
	negsum = 0
	for i in range(0,len(temperatures)):#we check each index's right and left to determine largest contigous day's sum of temperatures possible
		largesttemp = temperatures[i]
		target_start_d = 0
		target_end_d = 0
		for d in range(i, len(temperatures)):#in this for loop we look at the right side of the index which we are looping right now. in both list when we encounter a positive first we directly add this value to the range of contigous days. if we encounter negative values first we try to sum the next occuring values until we can turn the value of negative sums to positive. if we can we add those days to contigous days
			negsum = negsum + temperatures[d]
			if negsum>=0:
				target_end_d = d
				largesttemp= largesttemp+negsum
				negsum = 0
		negsum = 0		
		for d in range(i,-1,-1):#this for loop does same with the previous loop but for left side of the index
			negsum = negsum + temperatures[d]
			if negsum>=0:
				target_start_d = d
				largesttemp= largesttemp+negsum
				negsum = 0
		negsum = 0	
		if largesttemp>largesttemp_final:#we check that for this index i value has the contigous days temperature value which is highest among other index values
			largesttemp_final = largesttemp
			target_start = target_start_d
			target_end = target_end_d
	return days[target_start], days[target_end]

print(TARGET_TEMP())#use your arrays here