from tkinter import *
from tkinter import messagebox
import json as js
import os


class first:
    def initial(self):
               self.fp1=open("Programs\\Questions.txt")
               
               self.re1=self.fp1.read()
               self.re1=self.re1.strip()
               self.re1=self.re1.split("\n")
               
               self.fp1.close()
    def interface(self):
               self.top=Tk()
               self.top.geometry("1350x750")
               self.top.title("Programs")
               self.top.resizable(False,False)
               self.top.configure(background="#111")
               obj1.initial()
               obj1.frames()
               obj1.label()
               obj1.text()
               obj1.button()
               self.top.mainloop()
        


    def frames(self):
               self.f1=Frame(self.top,width=1350,height=70,bg="#444",bd=0)
               self.f1.place(relx=0,rely=0)
               self.f2=Frame(self.top,width=800,height=780,bg="#111",bd=0)
               self.f2.place(relx=0,rely=.095)
                                                                       
               self.f3=Frame(self.top,width=550,height=780,bg="#333",bd=0)
               self.f3.place(relx=.59,rely=0.095)
               self.f4=Frame(self.f2,width=750,height=600,bg="#444",bd=0)
               self.f4.place(relx=.0,rely=0.1)
    def label(self):
               self. label1=Label(self.f3,text="PROGRAM",bd=0,width=10,bg="#333",fg="white",font=("Times",20,"bold underline"))
               self.label1.place(relx=.33,rely=.03)
               self.label2=Label(self.f2,text="LIST OF PROGRAM",bd=0,width=25,bg="#111",fg="white",font=("Times",20,"bold underline"))
               self.label2.place(relx=.23,rely=.03)
               self.label3=Label(self.f1,text="PYTHON PROGRAM",bd=0,width=20,bg="#444",fg="#F6F6F6",font=("Times",24,"bold underline"))
               self.label3.place(relx=.37,rely=.2)
    def text(self):
               self.t1=Text(self.f3,width=65,height=32,bd=0)
               self.t1.place(relx=.03,rely=.1)
    def button(self):
               self.button1=Button(self.f3,text="RUN",bd=0,bg="#111",fg="white",font=("Times",20,"bold"),width=10,command=obj1.run)
               self.button1.place(relx=.01,rely=.78)

               self.button2=Button(self.f3,text="CLEAR",bd=0,bg="#111",fg="white",font=("Times",20,"bold"),width=10,command=obj1.clear)
               self.button2.place(relx=.68,rely=.78)

               self.button3=Button(self.f2,text="ADD QUESTION",bd=0,bg="#333",fg="white",font=("Times",16,"bold"),width=18,command=obj1.question)
               self.button3.place(relx=.05,rely=.795)

               self.button4=Button(self.f2,text="PRINT",bd=0,bg="#333",fg="white",font=("Times",16,"bold"),width=18,command=obj1.Print)
               self.button4.place(relx=.65,rely=.795)

               self.button5=Button(self.f2,text="EDIT",bd=0,bg="#333",fg="white",font=("Times",16,"bold"),width=18,command=obj1.Edit)
               self.button5.place(relx=.35,rely=.795)

               self.button6=Button(self.f3,text="REFRESH",bd=0,bg="#111",fg="white",font=("Times",20,"bold"),width=10,command=obj1.update)
               self.button6.place(relx=.345,rely=.78)

               self.scrollbar = Scrollbar(self.f4) 
               self.scrollbar.pack( side = RIGHT, fill=Y )
               self.scrollbar1 = Scrollbar(self.f4,width=20,orient=HORIZONTAL) 
               self.scrollbar1.pack( side = BOTTOM, fill=X)
              
               self.mylist = Listbox(self.f4,width=77,height=22,selectmode=SINGLE,xscrollcommand=self.scrollbar1.set, yscrollcommand = self.scrollbar.set ,font=("Times",14,"bold"),bg="#111",fg="white") 
               for i in self.re1:
                    self.mylist.insert(END,i)
                 
               self.mylist.pack( side = LEFT, fill = BOTH ) 
               self.scrollbar.config( command = self.mylist.yview )
               self.scrollbar1.config(command=self.mylist.xview)
    def run(self):
        os.startfile("Programs\\Python\\Programs{}.py".format(self.x11))
    def clear(self):
        self.t1.delete("1.0",END)
    def question(self):
            
               self.top1=Toplevel()
               self.top1.geometry("500x700+450+30")
               self.top1.title("Add Question")
               self.top1.resizable(False,False)
               self.top1.configure(background="#111")
               self.l1=Label(self.top1,text="Write Your Question Here.",font=("times",10,"bold underline"),fg="white",bg="#111",bd=0)
               self.l1.place(relx=.05,rely=.05)
               self.l2=Label(self.top1,text="Write Your Solution Here.",font=("times",10,"bold underline"),fg="white",bg="#111",bd=0)
               self.l2.place(relx=.05,rely=.3)
               self.text1=Text(self.top1,width=63,height=8,bd=0)
               self.text1.place(relx=.0,rely=.1)
               self.text2=Text(self.top1,width=63,height=24,bd=0)
               self.text2.place(relx=.0,rely=.35)
               
               self.buttontop1=Button(self.top1,text="SUBMIT",bd=0,bg="#333",fg="white",font=("Times",20,"bold"),width=10,command=obj1.submit)
               self.buttontop1.place(relx=.02,rely=.92)
               self.buttontop2=Button(self.top1,text="RESET",bd=0,bg="#333",fg="white",font=("Times",20,"bold"),width=10,command=obj1.reset)
               self.buttontop2.place(relx=.65,rely=.92)
               self.top1.mainloop()
    def Print(self):
               self.t1.delete("1.0",END)
               self.x11=(self.mylist.curselection())
               self.x11=self.x11[0]+1
               
               self.fp4=open("Programs\\Python\\Programs{}.py".format(self.x11))
               self.READ=self.fp4.read()
               self.fp4.close()
              
               self.t1.insert(END,self.READ)
    def Edit(self):
               self.x22=self.mylist.curselection()
               self.x22=self.x22[0]+1
               self.top2=Toplevel()
               self.top2.geometry("500x700+450+30")
               self.top2.title("Add Question")
               self.top2.resizable(False,False)
               self.top2.configure(background="#111")
               self.ll1=Label(self.top2,text="Edit Your Question.",font=("times",10,"bold underline"),fg="white",bg="#111",bd=0)
               self.ll1.place(relx=.05,rely=.05)
               self.ll2=Label(self.top2,text="Edit Your Solution.",font=("times",10,"bold underline"),fg="white",bg="#111",bd=0)
               self.ll2.place(relx=.05,rely=.3)
               
               self.ttext1=Text(self.top2,width=63,height=8,bd=0)
               self.ttext1.place(relx=.0,rely=.1)
               self.ttext2=Text(self.top2,width=63,height=24,bd=0)
               self.ttext2.place(relx=.0,rely=.35)
               
               self.bbuttontop1=Button(self.top2,text="SUBMIT",bd=0,bg="#333",fg="white",font=("Times",20,"bold"),width=10,command=obj1.editsubmit)
               self.bbuttontop1.place(relx=.36,rely=.92)

               self.fp4=open("Programs\\Questions.txt")
               self.READ=self.fp4.read()
               self.READ=self.READ.strip().split("\n")
               self.ttext1.insert(END,self.READ[self.x22-1])
               self.fp4.close()
               self.fp4=open("Programs\\Python\\Programs{}.py".format(self.x22))
               self.READ1=self.fp4.read()
               self.ttext2.insert(END,self.READ1)
               self.fp4.close()
               
               
               self.top2.mainloop()
               
               
    def update(self):
               self.mylist.delete(0,END)
               self.fp1=open("Programs\\Questions.txt")
               
               self.ree1=self.fp1.read()
               self.ree1=self.ree1.strip()
               self.ree1=self.ree1.split("\n")
               
               self.fp1.close()
               for i in self.ree1:
                    self.mylist.insert(END,i)
    def submit(self):
       
               self.var1=self.text1.get("1.0",END)
               self.var2=self.text2.get("1.0",END)
            
               self.fp3=open("Programs\\index.txt")
               self.re3=self.fp3.read()
               self.re3=self.re3.strip()
               self.re3=self.re3.split("\n")
               self.inde=int(self.re3[-1])
               self.fp3=open("Programs\\index.txt","a")
               self.g=self.inde+1
               self.fp3.write("\n"+str(self.g))
               self.fp3.close()
               self.var1=self.text1.get("1.0",END)
               self.fp1=open("Programs\\Questions.txt","a")

               self.fp1.write(str(self.inde)+".   "+self.var1)
               self.fp1.close()
               self.fp1=open("Programs\\Questions.txt")
               self.re2=self.fp1.read()
               self.re2=self.re2.strip().split("\n")
               self.mylist.insert(END,str(self.re2[-1]))
               self.string1="Programs"+str(self.inde)
               self.fp2=open("Programs\\Python\\{}.py".format(self.string1),"w")
               self.var2 =self.text2.get("1.0",END)
               
               self.var2=self.var2+'\nprint("Press Enter")\ninput()'
               self.fp2.write(self.var2)
               self.fp2.close()
               self.top1.withdraw()
    def reset(self):
        self.text1.delete("1.0",END)
        self.text2.delete("1.0",END)
    def editsubmit(self):
               self.variable1=self.ttext1.get("1.0",END)
               self.variable2=self.ttext2.get("1.0",END)
               self.fp4=open("Programs\\Questions.txt")
               self.READ=self.fp4.read()
          
               self.RE=self.READ.index("{}.".format(self.x22))
               self.fp4.close()
               self.g=self.RE
               for i in self.READ[self.g:]:
                    if i!='\n':
                         self.g=self.g+1
                    else:
                         break
               self.empstr=""
               self.READ=list(self.READ)
               self.READ[self.RE:self.g+1]=self.variable1
               for i in self.READ:
                    self.empstr=self.empstr+i
               self.fp4=open("Programs\\Questions.txt","w")
               self.fp4.write(self.empstr)
               self.fp4.close()
               self.fp4=open("Programs\\Python\\Programs{}.py".format(self.x22),"w")
               self.fp4.write(self.variable2)
               self.fp4.close()
               self.top2.withdraw()
    
               
obj1=first()
obj1.interface()
