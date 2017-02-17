import psutil
import collections
import operator
import csv
import sys
proc_names = {}
x=0
i=0
proc_details={}
count={}
for c in sorted(psutil.net_connections(kind='inet'), key=lambda p: p.pid):

	if c.raddr:
		proc_details[i]=[c.pid,c.laddr[0],c.raddr[0],c.status]
		i=i+1
output = []

for i in proc_details:
	if proc_details[i][0] not in output:
		output.append(proc_details[i][0])
		count[output.index(proc_details[i][0])]=1
	else:
		count[output.index(proc_details[i][0])]=count[output.index(proc_details[i][0])]+1
	
for i in range(0,len(output)):
	output[i]=[output[i],count[i]]
output=sorted(output,key=operator.itemgetter(1),reverse=True)
p=0
for j in range(0,len(output)):
	for i in range(0,len(proc_details)):
		if output[j][0]==proc_details[i][0]:
			proc_names[p]=proc_details[i]				
			p=p+1

writer=csv.writer(sys.stdout)
writer.writerow(["pid","laddr","raddr","status"])
for key, value in proc_names.iteritems():
    writer.writerow(value)

