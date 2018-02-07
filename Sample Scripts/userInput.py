import sys
import calendar
import hashlib
from tkinter import *


class UI(Frame):
    def __init__(self, parent, **kw):
        Frame.__init__(self, parent, **kw)
        self.canvasHeight = 600
        self.canvasWidth = 800
        self.parent = parent
        self.configure(**kw)
        self.grid()        
        self.createWidgets()

    def createWidgets(self):
        self.txbA11 = Entry(self)
        self.txbA12 = Entry(self)
        self.txbA13 = Entry(self)
        self.txbA21 = Entry(self)
        self.txbA22 = Entry(self)
        self.txbA23 = Entry(self)
        self.txbA31 = Entry(self)
        self.txbA32 = Entry(self)
        self.txbA33 = Entry(self)

        self.txbB11 = Entry(self)
        self.txbB12 = Entry(self)
        self.txbB13 = Entry(self)
        self.txbB21 = Entry(self)
        self.txbB22 = Entry(self)
        self.txbB23 = Entry(self)
        self.txbB31 = Entry(self)
        self.txbB32 = Entry(self)
        self.txbB33 = Entry(self)

        self.btnMul = Button(self, text = "A * B", command = self.mul)
        self.btnAdd = Button(self, text = "A + B", command = self.add)
        self.btnSub = Button(self, text = "A - B", command = self.sub)
        self.btnSwitch = Button(self, text = "<->", command = self.switch)

        self.lblA = Label(self, text = "A")
        self.lblB = Label(self, text = "B")
        
        self.txbA11.grid(column = 1, row = 2, padx= 15, pady = 15)
        self.txbA12.grid(column = 2, row = 2, padx= 15, pady = 15)
        self.txbA13.grid(column = 3, row = 2, padx= 15, pady = 15)
        self.txbA21.grid(column = 1, row = 3, padx= 15, pady = 15)
        self.txbA22.grid(column = 2, row = 3, padx= 15, pady = 15)
        self.txbA23.grid(column = 3, row = 3, padx= 15, pady = 15)
        self.txbA31.grid(column = 1, row = 4, padx= 15, pady = 15)
        self.txbA32.grid(column = 2, row = 4, padx= 15, pady = 15)
        self.txbA33.grid(column = 3, row = 4, padx= 15, pady = 15)

        self.txbB11.grid(column = 5, row = 2, padx= 15, pady = 15)
        self.txbB12.grid(column = 6, row = 2, padx= 15, pady = 15)
        self.txbB13.grid(column = 7, row = 2, padx= 15, pady = 15)
        self.txbB21.grid(column = 5, row = 3, padx= 15, pady = 15)
        self.txbB22.grid(column = 6, row = 3, padx= 15, pady = 15)
        self.txbB23.grid(column = 7, row = 3, padx= 15, pady = 15)
        self.txbB31.grid(column = 5, row = 4, padx= 15, pady = 15)
        self.txbB32.grid(column = 6, row = 4, padx= 15, pady = 15)
        self.txbB33.grid(column = 7, row = 4, padx= 15, pady = 15)

        self.btnSwitch.grid(column = 4, row = 3, padx = 15, pady = 15)
        self.btnMul.grid(column = 4, row = 4, padx = 15, pady = 15)
        self.btnAdd.grid(column = 4, row = 5, padx = 15, pady = 15)
        self.btnSub.grid(column = 4, row = 6, padx = 15, pady = 15)
        
        self.lblA.grid(column = 2, row = 1, padx = 15, pady = 15)
        self.lblB.grid(column = 6, row = 1, padx = 15, pady = 15)

    def initMatrices(self):
        self.A = [[float(self.txbA11.get()), float(self.txbA12.get()), float(self.txbA13.get())],
                 [float(self.txbA21.get()), float(self.txbA22.get()), float(self.txbA23.get())],
                 [float(self.txbA31.get()), float(self.txbA32.get()), float(self.txbA33.get())]]

        self.B = [[float(self.txbB11.get()), float(self.txbB12.get()), float(self.txbB13.get())],
                 [float(self.txbB21.get()), float(self.txbB22.get()), float(self.txbB23.get())],
                 [float(self.txbB31.get()), float(self.txbB32.get()), float(self.txbB33.get())]]

        self.result = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def mul(self):
        self.initMatrices()
        for i in range(len(self.A)):
            for j in range(len(self.B[0])):
                for k in range(len(self.B)):
                    self.result[i][j] += self.A[i][k] * self.B[k][j]

        print()
        for r in self.result:
            print(r)
        print()
        
    def add(self):
        self.initMatrices()
        for i in range(len(self.A)):
            for j in range(len(self.B[0])):
                self.result[i][j] = self.A[i][j] + self.B[i][j]

        print()        
        for r in self.result:
            print(r)
        print()

    def sub(self):
        self.initMatrices()
        for i in range(len(self.A)):
            for j in range(len(self.B[0])):
                self.result[i][j] = self.A[i][j] - self.B[i][j]

        print()                
        for r in self.result:
            print(r)
        print()

    def switch(self):
        self.initMatrices()
        self.txbA11.delete(0, END)
        self.txbA12.delete(0, END)
        self.txbA13.delete(0, END)
        self.txbA21.delete(0, END)
        self.txbA22.delete(0, END)
        self.txbA23.delete(0, END)
        self.txbA31.delete(0, END)
        self.txbA32.delete(0, END)
        self.txbA33.delete(0, END)
        self.txbB11.delete(0, END)
        self.txbB12.delete(0, END)
        self.txbB13.delete(0, END)
        self.txbB21.delete(0, END)
        self.txbB22.delete(0, END)
        self.txbB23.delete(0, END)
        self.txbB31.delete(0, END)
        self.txbB32.delete(0, END)
        self.txbB33.delete(0, END)

        self.txbA11.insert(0, self.B[0][0])
        self.txbA12.insert(0, self.B[0][1])
        self.txbA13.insert(0, self.B[0][2])
        self.txbA21.insert(0, self.B[1][0])
        self.txbA22.insert(0, self.B[1][1])
        self.txbA23.insert(0, self.B[1][2])
        self.txbA31.insert(0, self.B[2][0])
        self.txbA32.insert(0, self.B[2][1])
        self.txbA33.insert(0, self.B[2][2])
        self.txbB11.insert(0, self.A[0][0])
        self.txbB12.insert(0, self.A[0][1])
        self.txbB13.insert(0, self.A[0][2])
        self.txbB21.insert(0, self.A[1][0])
        self.txbB22.insert(0, self.A[1][1])
        self.txbB23.insert(0, self.A[1][2])
        self.txbB31.insert(0, self.A[2][0])
        self.txbB32.insert(0, self.A[2][1])
        self.txbB33.insert(0, self.A[2][2])

        self.initMatrices()
    
class App():
    def __init__(self):
        return
    
    def Calendar(self):
        yy = int(input("Enter year: "))
        mm = int(input("Enter month: "))
        print()
        print(calendar.month(yy, mm))

    def Hash(self):
        filename = input("Enter path to file: ")
        h = hashlib.sha1()
        with open(filename, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
        print()
        print("SHA1 Checksum:", h.hexdigest())
        print()

    def Matrix(self):
        root = Tk()
        root.title("Matrix Calc")
        ui = UI(root)
        ui.grid()
        root.mainloop()

    def mainloop(self):
        while(True):
            print("0: Exit")
            print("1: Hello")
            print("2: Calendar")
            print("3: Hash")
            print("4: Matrix")
            print("5: leer")
            print("6: leer")
            print("7: leer")
            print("8: leer")
            print("9: leer")

            mode = input("Choose a mode: ")

            if(mode == str(0)):
                exit()
            if(mode == str(1)):
                print("Hello World")
            if(mode == str(2)):
                self.Calendar()
            if(mode == str(3)):
                self.Hash()
            if(mode == str(4)):
                self.Matrix()
            if(mode == str(5)):
                pass
            if(mode == str(6)):
                pass
            if(mode == str(7)):
                pass
            if(mode == str(8)):
                return
            if(mode == str(9)):
                pass

def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()    
