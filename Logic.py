from page1 import *
from page2 import *
import csv
from accounts import *


class Logic(Page1, Page2):

    def __init__(self, root):

        self.__userName = ''

        self.mywindow = tk.Toplevel()
        Page2.__init__(self, self.mywindow)
        self.mywindow.withdraw()
        self.root = root
        super().__init__(root)

    def CreateWindow(self):
        '''
        Sets up page 2 and un-hides the window.
        :return: none
        '''
        try:
            self.setP2Info()
            self.mywindow.deiconify()

            # self.GLabel_p2Header.config(text = 'new text test')
        except:

            self.mywindow = tk.Toplevel()
            Page2.__init__(self, self.mywindow)
            self.setP2Info()

    def p1ButtonPress(self, name: str):
        '''
        Listens for a button press from page 1.
        :param name: This is the action key word
        :return: none
        '''

        if name == 'signIn':
            if self.checkCredentials():
                self.CreateWindow()
                self.GLineEdit_138.delete(0, 'end')
                self.GLineEdit_868.delete(0, 'end')
            else:
                print('invalid username or password')
                self.GLineEdit_138.delete(0, 'end')
                self.GLineEdit_868.delete(0, 'end')
        if name == 'signUp':
            print(self.createCredentials())
            self.GLineEdit_138.delete(0, 'end')
            self.GLineEdit_868.delete(0, 'end')

    def p2ButtonPress(self, name: str):
        '''
        Listens for a button press from page 2.
        :param name: This is the action key word
        :return: none
        '''
        if name == 'logOut':
            self.mywindow.withdraw()
            self.clearP2()
        if name == 'submit':
            self.setP2Info()

    def checkCredentials(self) -> bool:
        '''
        Checks if username and password are correct.
        :return: none
        '''
        with open('nameANDpass.csv', 'r', ) as myfile:
            content = csv.reader(myfile)
            header = myfile.readline()
            accountfound = False

            for line in content:
                try:
                    if line[0] == self.GLineEdit_138.get() and line[1] == self.GLineEdit_868.get():
                        self.__userName = line[0]
                        accountfound = True
                        print("success")
                except IndexError:
                    return accountfound

        return accountfound

    def createCredentials(self) -> str:
        '''
        Creates a new user and assigns them a default starting checking and savings value.
        :return: string detailing success or failure of creation
        '''
        # better way to use csv.writer(myfile) than swithcing it out?
        with open('nameANDpass.csv', 'r+', newline='') as myfile:
            reader = csv.reader(myfile)
            writer = csv.writer(myfile)
            header = myfile.readline()
            exists = False
            for line in reader:
                if not line:
                    continue

                if line[0] == self.GLineEdit_138.get():
                    exists = True
                    return 'account allready exists'
            if not exists:
                writer.writerow([self.GLineEdit_138.get(), self.GLineEdit_868.get(), 1, 1])
                return 'created account'  # wrote name and pass to file

    def calculate(self) -> tuple:
        '''
        Manages withdraw and deposit methods. Saves bank information to file.
        :return:Current Checking and Savings balance
        '''
        # updates and returns account balances using account class
        checking = Account(self.__userName, 0)
        savings = SavingAccount(self.__userName)

        with open('nameANDpass.csv', 'r+', newline='') as myfile:

            reader = csv.reader(myfile)
            writer = csv.writer(myfile)
            header = myfile.readline()

            content = []

            for line in reader:
                content.append(line)
                if line[0] == self.__userName:

                    CurrentChekBal = line[2]
                    CurrentSaveBal = line[3]

            # content = myfile.readlines()

            checking.set_balance(int(CurrentChekBal))
            savings.set_balance(int(CurrentSaveBal))

            try:
                checking.deposit(int(self.GLineEdit_347.get()))

                checking.withdraw(int(self.GLineEdit_708.get()))

                savings.deposit(int(self.GLineEdit_4.get()))

                savings.withdraw(int(self.GLineEdit_261.get()))
            except:
                print("enter in a number")

            CBal = checking.get_balance()
            SBal = savings.get_balance()

            # write to file
            # [john 1234 0 0 , joe 1234 0 0]


        for x in content:
            # [john,1234,0,0]
            if x[0] == self.__userName:
                x[2] = CBal
                x[3] = SBal

        with open('nameANDpass.csv', 'w', newline='') as myfile:
            writer = csv.writer(myfile)
            writer.writerow(['name', 'password', 'Checking bal', 'Savings bal'])
            writer.writerows(content)

        return CBal, SBal

    def clearP2(self):
        '''
        Clears page 2 of info
        :return: none
        '''
        self.GLineEdit_347.delete(0, 'end')
        self.GLineEdit_708.delete(0, 'end')
        self.GLineEdit_4.delete(0, 'end')
        self.GLineEdit_261.delete(0, 'end')
        self.mywindow.destroy()

    def setP2Info(self):
        '''
        puts results of calculate() on page 2
        :return:
        '''
        # call calculate function

        CBal, SBal = self.calculate()
        self.GLabel_760.config(text=self.__userName)
        self.GLabel_975.config(text=CBal)  # checking bal
        self.GLabel_534.config(text=SBal)  # savings bal

        self.GLineEdit_347.delete(0, 'end')
        self.GLineEdit_708.delete(0, 'end')
        self.GLineEdit_4.delete(0, 'end')
        self.GLineEdit_261.delete(0, 'end')

        self.GLineEdit_347.insert('end', 0)
        self.GLineEdit_708.insert('end', 0)
        self.GLineEdit_4.insert('end', 0)
        self.GLineEdit_261.insert('end', 0)


if __name__ == "__main__":
    window = tk.Tk()
    logicobject = Logic(window)
    window.mainloop()
