def fact(x):
	if x==0:
		return 1
	else:
		return x*fact(x-1)
z=int(input())
print(fact(z))
		

print("Press Enter")
input()