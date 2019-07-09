def rec(x):
	if x==0:
		return
	else:
		print("Helloo world")
		rec(x-1)	

n=int(input("Enter the value of n: "))
rec(n)

print("Press Enter")
input()