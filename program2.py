# IMT2019525- VIJAY JAISANKAR
# Please check IAS Implementation at ias2.py

def mod(n):
	if n>=0:
		return n 
	else:
		return -n

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a+b >=0):
	z = a+b
	z -= c
	z += mod(d)
	z <<=1
	print(z)

else:
	z = a+b
	z -= mod(c)
	z >>=2
	print(z)

