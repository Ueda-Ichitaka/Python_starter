from tkinter import *
from math import pow, log

class App(Frame):
    def __init__(self, parent, **kw):
        Frame.__init__(self, parent, **kw)
        self.canvasHeight = 600
        self.canvasWidth = 800
        self.parent = parent
        self.configure(**kw)
        self.grid()        
        self.createWidgets()

        

    def createWidgets(self):
        self.btnPlot = Button(self, text = "Plot function", command = self.plot)
        self.txbFkt = Entry(self)
        self.cnvPlot = Canvas(self, width = self.canvasWidth, height = self.canvasHeight, bg = "#e3e3e3")

        self.btnPlot.grid(column = 5, row = 7, padx = 15, pady = 15)
        self.txbFkt.grid(column = 5, row = 6, padx = 15, pady = 15)
        self.cnvPlot.grid(column = 5, row = 5, padx = 15, pady = 15)

        self.cnvPlot.create_line(0, 0, self.canvasWidth, 0, fill = "#000000", width = 5)
        self.cnvPlot.create_line(0, 0, 0, self.canvasHeight, fill = "#000000", width = 5)
        self.cnvPlot.create_line(self.canvasWidth, self.canvasHeight, self.canvasWidth, 0, fill = "#000000", width = 0)
        self.cnvPlot.create_line(self.canvasWidth, self.canvasHeight, 0, self.canvasHeight, fill = "#000000", width = 0)
        
    def plot(self):
        for x in range(1, self.canvasWidth):
            self.y = self.canvasHeight - (log(x, float(self.txbFkt.get())) * 10)
            self.cnvPlot.create_line(x, self.y, x + 1, self.y, fill = "#000000", width = 1)
            print(x, self.y)

def main():
    root = Tk()
    root.title("Test Window")
    app = App(root, width = 800, height = 600, relief = SUNKEN, bd = 1, padx = 50, pady = 50)
    app.grid()
    root.mainloop()


if __name__ == '__main__':
    main()
