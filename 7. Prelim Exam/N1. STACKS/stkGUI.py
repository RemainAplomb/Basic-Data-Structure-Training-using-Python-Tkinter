"""
    NAME : DIBANSA, RAHMANI P.
    NAME : BELGA, EMJAY
    COURSE : BSCPE 2-2
    ACADEMIC YEAR : 2019-2020

    PROGRAM'S SUMMARY: THIS PROGRAM WOULD MIMIC A STACK OF NOTEBOOKS THAT WOULD BE CHECKED. THIS PROGRAM RECORDS THE NAME
    OF THE NOTEBOOK'S OWNER AND ADDS THE NOTEBOOK ON THE TOP OF THE STACK. AS THE USER CHECKS THE STACK, THE NOTEBOOK AT
    THE TOP OF THE STACK WOULD BE REMOVED. FURTHERMORE, THE USER COULD ALSO OPT FOR THE 'CHECK ALL' BUTTON THAT REMOVES
    EVERY NOTEBOOK IN THE STACK. IN ADDITION, THE USER COULD ALSO PEEK AT THE NOTEBOOK ON TOP OF THE STACK.
"""

#########################
# The program would import tkinter and the class that we have made.
from tkinter import *
from tkinter import messagebox
from stkClass import *
#########################

# The program would be calling upon the stack class inside the py file name stkClass
stcks = stcks()

# This class contains our program's GUI 
class stackGUI :
    # Once the class has been called, it will immediately start loading the GUI for our program's Menu.
    def __init__ ( self ) :
        self.menu()

    # This function contains the GUI for the program's main menu.
    # Depending on the button clicked by the user, the program will execute another function.
    def menu ( self ) :
        self.m = Tk()
        self.m.geometry ( "300x400" )
        self.m.config ( background = "grey" )
        self.m.resizable ( width = False , height = False )
        self.m.title ( "Notebook Checker" )
        self.m.heading = Label ( text = "MAIN MENU" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.m.heading.pack()

        self.addBTN = Button ( self.m , font = ( "Courier" , 8 , "bold" ) , text = "Add Notebook" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.add)
        self.addBTN.place ( x = 80 , y = 80 , height = 30 )

        self.checkBTN = Button ( self.m , font = ( "Courier" , 8 , "bold" ) , text = "Check Notebook" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.check )
        self.checkBTN.place ( x = 80 , y = 140 , height = 30 )

        self.peekBTN = Button ( self.m , font = ( "Courier" , 8 , "bold" ) , text = "Peek at Notebook" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.peek )
        self.peekBTN.place ( x = 80 , y = 200 , height = 30 )

        self.checkAllBTN = Button ( self.m , font = ( "Courier" , 8 , "bold" ) , text = "Check All" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.checkAll )
        self.checkAllBTN.place ( x = 80 , y = 260 , height = 30 )

        self.exitBTN = Button ( self.m , font = ( "Courier" , 8 , "bold" ) , text = "Exit" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.ext )
        self.exitBTN.place ( x = 80 , y = 320 , height = 30 )

    # This function contains the GUI that lies after the user clicked the button 'Add notebook'.
    # This GUI would ask for the name of notebook's owner.
    def add ( self ) :
        try:
            self.m.destroy()
        except:
            pass
        self.a = Tk()
        self.a.geometry ( "300x200" )
        self.a.config ( background = "grey" )
        self.a.resizable ( width = False , height = False )
        self.a.title ( "Notebook Checker" )
        self.a.heading = Label ( text = "Add Notebook" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 14 , "bold" ) )
        self.a.heading.pack()

        self.bookOwnerText = Label ( text = " Book Owner : "  )
        self.bookOwnerText.place ( x = 115 , y = 60 )

        self.bookOwnerEntry = Text ( self.a , bd = 0 , bg = "White" , height = "2" , width = "32" , font = "Arial" )
        self.bookOwnerEntry.place ( x = 5 , y = 90 )

        self.aDoneBTN = Button ( self.a , font = ( "Courier" , 8 , "bold" ) , text = "ADD" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.aDoneClicked )
        self.aDoneBTN.place ( x = 80 , y = 150 , height = 30 )

    # Once the user of the program adds a notebook, this function would be processed.
    # This function would take the Entry that the user has inputted and would be feeding it into the addNotebook function
    # inside our program's stcks class.
    def aDoneClicked ( self ) :
        self.bookOwner = self.bookOwnerEntry.get( "0.0" , END )
        stcks.addNotebook ( self.bookOwner )
        self.a.destroy()
        self.menu()

    # This function would be processed once the user clicks the button 'Check Notebook'.
    # This function would pop up a notification asking the user if he has already checked the notebook at the top of the
    # stack. If he confirms it by clicking the button 'Yes' , the program would remove the notebook from the stack.
    # If the user clicked the button 'No', the program would not remove the notebook from the stack.
    def check ( self ) :
        self.results = stcks.peekAtNotebook() 
        if self.results != None :
            self.results += "'s"
            if messagebox.askyesno( "Checking Notebook" , self.results + " notebook is being checked." )== True :
                stcks.checkNotebook()
        else:
            if messagebox.showinfo( "Checking Notebook" , " Nothing to check at the moment. " )== True :
                pass
    # This function would be processed and executed once the user clicks the button 'Peek at Notebook'.
    # This function would pop up a messagebox containing the name of the notebook's owner that is placed at the top
    # of the stack.
    def peek ( self ) :
        self.results = stcks.peekAtNotebook()
        if self.results != None :
            self.results += "'s"
            if messagebox.showinfo( "Peeking at Notebook" , self.results + " notebook is at the top of the stack. " )== True :
                pass
        else:
            if messagebox.showinfo( "Peeking ats Notebook" , "There are no notebooks. Do you understand? " )== True :
                pass
    
    # This function would be processed and executed once the user clicks the button 'Check All'
    # This function would pop up a messagebox asking the user if he has already checked the notebooks inside the stack.
    # If he answers yes, then every notebook inside the stack will be removed.
    def checkAll ( self ) :
        self.results = stcks.checkAll()
        if self.results != None :
            if messagebox.askyesno( "Checking All Notebook" , " Have you checked these notebooks : " + self.results )== True :
                stcks.checkedAll()
        else:
            if messagebox.showinfo( "Checking All Notebook" , "There are no notebooks. Do you understand? " )== True :
                pass
    
    # This function would be processed and executed once the user clicks the button 'Exit'
    # This function destroys the GUI for the menu.
    def ext ( self ) :
        self.m.destroy()

# The program would be calling the class containing the GUI of our program.
stkGUI = stackGUI()
