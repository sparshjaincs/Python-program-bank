x=int(input())
for i in range(1,11):
	print("{0:>3}x{1:>3}={2:>3}".format(x,i,x*i),end="\n")

print("Press Enter")
input()
