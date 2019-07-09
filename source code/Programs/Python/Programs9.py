x=str(int(input()))
if ord(x[0])>49 and ord(x[0])<57:
	print("positive")
elif ord(x[0])==48:
	print("Zero")
else:
	print("Negative")


print("Press Enter")
input()