#Week 11, Program 2 - Fictional Address
#Caiden Heinrichs
#04/17/26

import tkinter

class Gui:
    def __init__(self):
        #Set up window with size and title
        self.window = tkinter.Tk()
        self.window.title("Fictional Address")
        self.window.minsize(500, 250)

        #Set up title and buttons
        self.address = tkinter.Label(self.window, text = 'Name: Caiden Heinrichs\nAddress: 15 Maplewood Terrace, Willow Creek, VT 05401')
        self.showInfoButton = tkinter.Button(self.window, text = 'Show Info', command = self.showInfoMethod)
        self.quitButton = tkinter.Button(self.window, text = 'Quit', command = self.quitMethod)

        #Pack buttons
        self.showInfoButton.pack(side = 'left')
        self.quitButton.pack(side = 'right')

    def showInfoMethod(self):
        self.address.pack(side = 'top')

    def quitMethod(self):
        self.window.destroy()


if __name__ == '__main__':
    window = Gui()
    window.window.mainloop()
