import re
fname='regex_sum_210717.txt'
handle=open(fname)
lst=list()
for lines in handle:
	lst=lst+re.findall('[0-9]+',lines)
total=0
for numbers in lst:
	total=total+int(numbers)
print 'Total no. of elements are',len(lst)
print 'Sum is',total
