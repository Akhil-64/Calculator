from tkinter import *

def iCalc(source,side):
    storeObj=Frame(source,borderwidth=4,bd=4,bg="powder blue")
    storeObj.pack(side=side,expand=YES,fill=BOTH)
    return storeObj


def button(source,side,text,command=None):
    storeObj=Button(source,text=text,command=command,activebackground="pink")
    storeObj.pack(side=side,expand=YES,fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add("*Font","arial 30 bold")
        self.pack(expand=YES,fill=BOTH)
        self.master.title("CALCULATOR")

        display=StringVar()
        Entry(self,relief=SUNKEN,textvariable=display,justify="right",bd=30,bg="powder blue").pack(side=TOP,expand=YES,fill=BOTH)
        #relief=raised,sunken,flat,ridge,groove
        for clearBut in (["CE"],["C"]):
            erase=iCalc(self,TOP)
            for ichar in clearBut:
                button(erase,LEFT,ichar,lambda storeObj=display,q=ichar:storeObj.set(" "))
            
        for number in ("789/","456*","123-","0.+"):
            functionNum=iCalc(self,TOP)
            for equals in number:
                button(functionNum,LEFT,equals,lambda storeObj=display,q=equals:storeObj.set(storeObj.get()+q))
        EqualsButton=iCalc(self,TOP)
        for equals in "=":
            if equals=="=":
                bEquals=button(EqualsButton,RIGHT,equals)
                bEquals.bind("<ButtonRelease-1>",lambda e,s=self,storeObj=display:s.calc(storeObj),"+")
            else:
                bEquals=button(EqualsButton,RIGHT,equals,
                               lambda storeObj=display,s="%s"%Equals:storeObj.set(storeObj.get()+s))

    def calc(self,display):
        try:
           display.set(eval(display.get()))
        except:
           display.set("ERROR")


        
if __name__=="__main__":
    app().mainloop()
    
