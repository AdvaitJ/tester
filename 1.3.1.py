import os 

for i in range(1,255):
			a = os.popen("ping -c 1 10.11.1." + str(i))
			for line in a.readlines():
				#print(line)
				if("1 received" in line):
					print("10.11.1." + str(i))
