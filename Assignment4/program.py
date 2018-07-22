def multiple_seven(num):
	if(num%7==0):
		return True
	else:
		return False

def multiple_thirteen(num):
	if(num%13==0):
		return True
	else:
		return False

for i in range(30,300):
	num1=multiple_seven(i)
	num2=multiple_thirteen(i)
	if(num1==True and num2==True):
		print "a-z"
	elif(num1==True):
		print "abc"
	elif(num2==True):
		print "xyz"
	else:
		print i
