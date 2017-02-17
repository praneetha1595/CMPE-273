import subprocess
import re


ips=[["23.23.255.255","us-east-1",""],[ "52.14.64.0","us-east-2",""],["50.18.56.1","us-west-1",""],["35.160.63.253","us-west-2",""],["52.222.9.163","us-gov-west-1",""],["52.60.50.0","ca-central-1",""],["34.248.60.213","eu-west-1",""],["35.156.63.252","eu-central-1",""],["52.56.34.0","eu-west-2",""],["13.112.63.251","ap-northeast-1",""],["52.78.63.252","ap-northeast-2",""],["46.51.216.14","ap-southeast-1",""],["13.54.63.252","ap-southeast-2",""],["35.154.63.252","ap-south-1",""],["52.67.255.254","sa-east-1",""]]
for i in range(len(ips)):
	ping = subprocess.Popen(["ping", "-c", "1", ips[i][0]],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
	out, error = ping.communicate()
	ips[i][2]=int(re.search('Average = ([^ms]+)',out.decode("utf-8")).group(1))

ips.sort(key=lambda x: x[2])
print(ips[0],end=" ")
print("-smallest average latency")
for i in range(1,len(ips)-1):
	print(ips[i])
print(ips[len(ips)-1],end=" ")
print("-largest average latency")