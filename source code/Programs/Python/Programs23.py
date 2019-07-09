def fact(x):
	if x==0:
		return 1
	else:
		return x*fact(x-1)
print(fact(int(input("Enter number :"))))

print("Press Enter")
input()



