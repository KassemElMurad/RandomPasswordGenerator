



import random, sys 

A = "abcdefghijklmnopqrstuyvwxyz1234567890"  
while True:
	lengthofpassword = 12
	pw = ""

	for i in range(lengthofpassword):
		r = random.randrange(len(A))
 		pw = pw + A[r]
	print (pw)
        sys.exit()
