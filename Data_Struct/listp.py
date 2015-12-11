name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
names=dict()
for line in handle:
    line=line.strip()
    if line.startswith('From'):
        temp=line.split()
        names[temp[1]]=names.get(temp[1],0)+1
high = 0
highest=list()
for name in names:
    if names[name]>high:
    	highest.append(name)
        high=names[name]
print highest[len(highest)-1],high
