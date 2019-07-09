def GCD(x,y):
	if y==0:
		return x
	else:
		return GCD(y,x%y)
a,b=map(int,input("Enter two integer seperated by space:").split())
print(GCD(a,b))

print("Press Enter")
input()
