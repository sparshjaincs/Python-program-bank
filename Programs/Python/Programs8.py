x,y,z=map(int,input("Enter three integers seperated by space:").split())
if x>y and y>z:
	print(x)
elif y>z:
	print(y)
else:
	print(z)

print("Press Enter")
input()