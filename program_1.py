#Week 11, Program 1 - Favorite saying
#Caiden Heinrichs
#04/17/26

import tkinter

class Gui:
    def __init__(self):
        #Set up the window with a size and title
        self.window = tkinter.Tk()
        self.window.minsize(250, 100)
        self.window.title('A Good Quote')
        
        #Create the label for the quote and add it to the window
        self.quote = tkinter.Label(self.window, text ='"The cushions are the essence of the chair"')
        self.quote.pack(side='top')

        #Enter the main loop
        tkinter.mainloop()

if __name__ == '__main__':
    quoteWindow = Gui()
