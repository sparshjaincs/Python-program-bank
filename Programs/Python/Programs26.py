class complex:
	def __init__(self,r=0,i=0):
		self.real=r
		self.img=i
	def input(self):
		self.real=int(input("Enter real :"))
		self.img=int(input("Enter imag :"))
	def display(self):
		if self.img<0:
			print("{}-i{}".format(self.real,abs(self.img)))
		else:
			print("{}+i{}".format(self.real,self.img))
	def addition(self,c):
		return complex(self.real+c.real,self.img+c.img)
c1=complex()
c1.input()
c1.display()
c2=complex()
c2.input()
c2.display()
c3=c1.addition(c2)
c3.display()	


print("Press Enter")
input()
