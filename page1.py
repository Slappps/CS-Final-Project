import tkinter as tk
import tkinter.font as tkFont

class Page1:
    def __init__(self, root):
        #setting title
        root.title("NewZity Bank")
        #setting window size
        width=340
        height=440
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg = 'green')

        self.GLabel_882=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        self.GLabel_882["font"] = ft
        self.GLabel_882["fg"] = "#333333"
        self.GLabel_882["justify"] = "center"
        self.GLabel_882["text"] = "Bank"
        self.GLabel_882.place(x=120,y=20,width=86,height=30)
        #username
        self.GLineEdit_138=tk.Entry(root)
        self.GLineEdit_138["borderwidth"] = "5px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_138["font"] = ft
        self.GLineEdit_138["fg"] = "#333333"
        self.GLineEdit_138["justify"] = "center"
        self.GLineEdit_138.config(text='asdasdasdasd')
        self.GLineEdit_138.place(x=90,y=110,width=160,height=30)
        #password
        self.GLineEdit_868=tk.Entry(root)
        self.GLineEdit_868["borderwidth"] = "5px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_868["font"] = ft
        self.GLineEdit_868["fg"] = "#333333"
        self.GLineEdit_868["justify"] = "center"
        self.GLineEdit_868["text"] = ""
        self.GLineEdit_868.place(x=90,y=180,width=163,height=30)

        self.GButton_43=tk.Button(root)
        self.GButton_43["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_43["font"] = ft
        self.GButton_43["fg"] = "#000000"
        self.GButton_43["justify"] = "center"
        self.GButton_43["text"] = "Sign In"
        self.GButton_43.place(x=90,y=250,width=70,height=25)
        self.GButton_43["command"] = lambda: self.p1ButtonPress(name='signIn')

        GButton_410=tk.Button(root)
        GButton_410["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_410["font"] = ft
        GButton_410["fg"] = "#000000"
        GButton_410["justify"] = "center"
        GButton_410["text"] = "sign up"
        GButton_410.place(x=180,y=250,width=70,height=25)
        GButton_410["command"] = lambda: self.p1ButtonPress(name='signUp')

        self.GLabel_739=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_739["font"] = ft
        self.GLabel_739["fg"] = "#333333"
        self.GLabel_739["justify"] = "center"
        self.GLabel_739["text"] = "Username"
        self.GLabel_739.place(x=130,y=80,width=70,height=25)
        self.GLabel_739.configure(borderwidth=5)

        self.GLabel_491=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_491["font"] = ft
        self.GLabel_491["fg"] = "#333333"
        self.GLabel_491["justify"] = "center"
        self.GLabel_491["text"] = "Password"
        self.GLabel_491.place(x=130,y=150,width=70,height=25)
        self.GLabel_491.configure(borderwidth=5)




if __name__ == "__main__":
    root = tk.Tk()
    app = Page1(root)
    root.mainloop()
