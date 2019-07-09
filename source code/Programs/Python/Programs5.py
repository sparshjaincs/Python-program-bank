x=int(input())
c=1
for i in range(2,x//2+1):
	if x%i==0:
		c=c+1
if c==1:
	print("Prime Number")
else:
	print("Not a prime number")

print("Press Enter")
input()

