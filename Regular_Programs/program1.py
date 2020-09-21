# IMT2019525 - VIJAY JAISANKAR
# Please see IAS Computer Implementation at ias1.py

def mod(n):
	if n>=0:
		return n
	else:
		return -n

a = int(input())
b = int(input())

if (a - mod(b) >= 0):
	c = a - mod(b)
	c >>= 2
	print(c)

else:
	c = a - mod(b)
	c <<= 1
	print(c)



