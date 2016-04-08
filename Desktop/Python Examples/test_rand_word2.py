import random
import string

x = []
for j in range(100):
	x.append(''.join(random.choice(string.letters) for i in range(20))) 
print x
