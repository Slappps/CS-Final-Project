import tkinter as tk
import tkinter.font as tkFont

class Page2:
    def __init__(self, root):
        #setting title
        root.title("Account")
        #setting window size
        width=340
        height=440
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)


        self.GLabel_760=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_760["font"] = ft
        self.GLabel_760["fg"] = "#333333"
        self.GLabel_760["justify"] = "center"
        self.GLabel_760["text"] = "Name"
        self.GLabel_760.place(x=0,y=0,width=86,height=30)

        self.GButton_592=tk.Button(root)
        self.GButton_592["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_592["font"] = ft
        self.GButton_592["fg"] = "#000000"
        self.GButton_592["justify"] = "center"
        self.GButton_592["text"] = "Log Out"
        self.GButton_592.place(x=260,y=10,width=70,height=25)
        self.GButton_592["command"] = lambda: self.p2ButtonPress(name='logOut')

        self.GLabel_167=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_167["font"] = ft
        self.GLabel_167["fg"] = "#333333"
        self.GLabel_167["justify"] = "center"
        self.GLabel_167["text"] = "Checking "
        self.GLabel_167.place(x=20,y=60,width=70,height=25)

        self.GLabel_866=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_866["font"] = ft
        self.GLabel_866["fg"] = "#333333"
        self.GLabel_866["justify"] = "center"
        self.GLabel_866["text"] = "Savings"
        self.GLabel_866.place(x=20,y=160,width=70,height=25)

        self.GLabel_975=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_975["font"] = ft
        self.GLabel_975["fg"] = "#333333"
        self.GLabel_975["justify"] = "center"
        self.GLabel_975["text"] = "Balance"
        self.GLabel_975.place(x=170,y=60,width=70,height=25)

        self.GLabel_534=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_534["font"] = ft
        self.GLabel_534["fg"] = "#333333"
        self.GLabel_534["justify"] = "center"
        self.GLabel_534["text"] = "Balance"
        self.GLabel_534.place(x=170,y=160,width=70,height=25)

        self.GLineEdit_347=tk.Entry(root)      # checking deposit
        self.GLineEdit_347["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_347["font"] = ft
        self.GLineEdit_347["fg"] = "#333333"
        self.GLineEdit_347["justify"] = "center"
        self.GLineEdit_347["text"] = "Deposit"
        self.GLineEdit_347.place(x=30,y=110,width=122,height=30)

        self.GLineEdit_708=tk.Entry(root) # checking withdraw
        self.GLineEdit_708["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_708["font"] = ft
        self.GLineEdit_708["fg"] = "#333333"
        self.GLineEdit_708["justify"] = "center"
        self.GLineEdit_708["text"] = "Withdraw"
        self.GLineEdit_708.place(x=180,y=110,width=120,height=30)

        self.GButton_77=tk.Button(root)
        self.GButton_77["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_77["font"] = ft
        self.GButton_77["fg"] = "#000000"
        self.GButton_77["justify"] = "center"
        self.GButton_77["text"] = "Submit"
        self.GButton_77.place(x=130,y=280,width=70,height=25)
        self.GButton_77["command"] = lambda: self.p2ButtonPress(name='submit')

        self.GLineEdit_4=tk.Entry(root) #savings deposit
        self.GLineEdit_4["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_4["font"] = ft
        self.GLineEdit_4["fg"] = "#333333"
        self.GLineEdit_4["justify"] = "center"
        self.GLineEdit_4["text"] = "placeholder"
        self.GLineEdit_4.place(x=30,y=210,width=120,height=30)

        self.GLineEdit_261=tk.Entry(root) #savings withdraw
        self.GLineEdit_261["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_261["font"] = ft
        self.GLineEdit_261["fg"] = "#333333"
        self.GLineEdit_261["justify"] = "center"
        self.GLineEdit_261["text"] = "place"
        self.GLineEdit_261.place(x=180,y=210,width=121,height=30)

        def clearP2():
            self.GLineEdit_347.delete(0, 'end')
            self.GLineEdit_708.delete(0, 'end')
            self.GLineEdit_4.delete(0, 'end')
            self.GLineEdit_261.delete(0, 'end')
            root.destroy()


        root.protocol('WM_DELETE_WINDOW', clearP2)

        self.GLineEdit_347.insert('end', 0)
        self.GLineEdit_708.insert('end', 0)
        self.GLineEdit_4.insert('end', 0)
        self.GLineEdit_261.insert('end', 0)



if __name__ == "__main__":
    root = tk.Tk()
    app = Page2(root)
    root.mainloop()
