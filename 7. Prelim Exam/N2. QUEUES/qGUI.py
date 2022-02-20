"""
    NAME : DIBANSA, RAHMANI P.
    NAME : BELGA, EMJAY
    COURSE : BSCPE 2-2
    ACADEMIC YEAR : 2019-2020

    PROGRAM'S SUMMARY: THIS IS A QUEUEING PROGRAM THAT MIMICS A DOCTOR'S APPOINTMENT QUEUE.
"""

################################
# HERE THE PROGRAM WOULD BE IMPORTING ALL OF THE MODULES WITHIN TKINTER AND SPECIFICALLY IMPORT THE MESSAGEBOX FUNCTION
# OF TKINTER BECAUSE THE NEWER VERSIONS OF TKINTER REQUIRES THE PROGRAM TO IMPORT MESSAGEBOX SEPARATELY.
from tkinter import *
from tkinter import messagebox
from qClass import *
################################

# HERE THE PROGRAM WOULD BE CALLING UPON THE QCLASS FUNCTION INSIDE THE PY FILE NAMED QCLASS WHICH THE PROGRAM HAVE
# IMPORTED ABOVE.
qClass = qClass()

# THIS CLASS CONTAINS ALL GUI RELATED FUNCTIONS THAT THE PROGRAM USES.
class qGUI :
    # WHENEVER THE CLASS WOULD BE CALLED, THE FUNCTION MENU WHICH CONTAINS THE GUI FOR THE PROGRAM'S MENU WOULD BE
    # INITIALIZED.
    def __init__ ( self ) :
        self.menu()

    # THIS FUNCTION CONTAINS THE GUI FOR THE MAIN MENU OF THE PROGRAM.
    def menu ( self ) :
        self.m = Tk()
        self.m.geometry ( "300x400" )
        self.m.config ( background = "grey" )
        self.m.resizable ( width = False , height = False )
        self.m.title ( "Doctor's Queue" )
        self.m.heading = Label ( text = "MAIN MENU" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.m.heading.pack()

        self.signUpBTN = Button ( self.m , font = ( "Courier" , 8 , "bold" ) , text = "Sign Up For Doctor's Consultation" , width = "35"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.signUp)
        self.signUpBTN.place ( x = 30 , y = 80 , height = 30 )

        self.enterBTN = Button ( self.m , font = ( "Courier" , 8 , "bold" ) , text = "Enter Room" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.enter )
        self.enterBTN.place ( x = 80 , y = 140 , height = 30 )

        self.beginBTN = Button ( self.m , font = ( "Courier" , 8 , "bold" ) , text = "Begin Consultation" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.begin )
        self.beginBTN.place ( x = 80 , y = 200 , height = 30 )

        self.closingBTN = Button ( self.m , font = ( "Courier" , 8 , "bold" ) , text = "Closing time" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.closing )
        self.closingBTN.place ( x = 80 , y = 260 , height = 30 )

        self.exitBTN = Button ( self.m , font = ( "Courier" , 8 , "bold" ) , text = "Exit" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.ext )
        self.exitBTN.place ( x = 80 , y = 320 , height = 30 )

    # THIS FUNCTION WOULD BE PROCESSED ONCE THE USER CLICKS THE BUTTON 'SIGN UP FOR DOCTOR'S CONSULTATION.
    # THIS FUNCTION CONTAINS THE GUI FOR THE SIGN UP FORM OF OUR PROGRAM. 
    def signUp ( self ) :
        try:
            self.m.destroy()
        except:
            pass
        self.su = Tk()
        self.su.geometry ( "300x300" )
        self.su.config ( background = "grey" )
        self.su.resizable ( width = False , height = False )
        self.su.title ( "Doctor's Queue" )
        self.su.heading = Label ( text = "Sign Up" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 14 , "bold" ) )
        self.su.heading.pack()

        self.nameText = Label ( text = " Name : "  )
        self.nameText.place ( x = 130 , y = 60 )

        self.nameEntry = Text ( self.su , bd = 0 , bg = "White" , height = "2" , width = "32" , font = "Arial" )
        self.nameEntry.place ( x = 5 , y = 90 )

        self.concernText = Label ( text = " Concern : "  )
        self.concernText.place ( x = 125 , y = 140 )

        self.concernEntry = Text ( self.su , bd = 0 , bg = "White" , height = "3" , width = "32" , font = "Arial" )
        self.concernEntry.place ( x = 5 , y = 170 )

        self.confirmBTN = Button ( self.su , font = ( "Courier" , 8 , "bold" ) , text = "CONFIRM" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.confirmClicked )
        self.confirmBTN.place ( x = 80 , y = 250 , height = 30 )

    # THIS FUNCTION WOULD BE EXECUTED ONCE THE USER CLICKED THE CONFIRM BUTTON IN THE SIGN UP FORM.
    # THIS FUNCTION TAKES THE ENTRIES THAT CONTAINS THE PATIENT'S NAME AND CONCERN
    # THE DATA TAKEN FROM THE ENTRIES WOULD THEN BE FED INTO THE QCLASS'S SIGNUP FUNCTION
    def confirmClicked ( self ) :
        self.name = self.nameEntry.get( "0.0" , END )
        self.concern = self.concernEntry.get ( "0.0" , END )
        qClass.signUp ( self.name , self.concern )
        self.su.destroy()
        self.menu()

    # THIS FUNCTION WOULD BE PROCESSED ONCE THE USER CLICKS THE BUTTON 'ENTER ROOM'.
    # THIS FUNCTION WOULD DISPLAY ON THE SCREEN THE NAME OF THE PATIENT THAT IS ON THE FORE FRONT OF THE QUEUE.
    # IF THERE IS NO ONE IN THE QUEUE, THE PROGRAM WOULD DISPLAY A PROMPT THAT WOULD SAY SO.
    def enter ( self ) :
        self.results = qClass.enterRoom() 
        if self.results != None :
            if messagebox.showinfo( "Enter Room" , self.results[0] + " should enter the room. "  )== True :
                pass
        else:
            if messagebox.showinfo( "Enter Room" , "There are no one on the Queue. Do you understand? " )== True :
                pass
    # THIS FUNCTION WOULD BE PROCESSED ONCE THE USER CLICKS THE BUTTON 'BEGIN CONSULTATION'.
    # THIS FUNCTION POPS UP A PROMPT ASKING THE USER IF THE PATIENT WOULD BE BEGINNING THE CONSULTATION.
    # IF THE USER CLICKS 'YES', IT WOULD THEN REMOVE THE NODE THAT CONTAINS THE DATA OF THE PATIENT AT THE FRONT OF THE QUEUE
    def begin ( self ) :
        self.results = qClass.enterRoom() 
        if self.results != None :
            if messagebox.askyesno( "Begin Consultation" , "Name: " + self.results[0] + "Nature of concern: " + self.results[1]  )== True :
                qClass.beginConsultation()
        else:
            if messagebox.showinfo( "Begin Consultation" , "There are no one on the Queue. Do you understand? " )== True :
                pass
    # THIS FUNCTION WOULD BE PROCESSED ONCE THE USER CLICKS THE BUTTON 'CLOSING TIME'.
    # THIS FUNCTION POPS UP A PROMPT ASKING THE USER IF THE USER WOULD REALLY WANT TO CLOSE.
    # IF THE USER CLICKS 'YES', IT WOULD REMOVE RESET THE LINKED LIST AND REMOVE EVERYONE ON THE QUEUE
    def closing ( self ) :
        if messagebox.askyesno( "Closing" , "Are you sure you want to close? " )== True :
                qClass.closing()
    # THIS FUNCTION WOULD BE EXECUTED ONCE THE USER CLICKS THE BUTTON 'EXIT'
    # THIS FUNCTION DESTROYS THE MAIN MENU'S GUI.
    def ext ( self ) :
        self.m.destroy()

# HERE THE PROGRAM WOULD BE CALLING THE CLASS CONTAINING THE PROGRAM'S GUI.
qGUI = qGUI()
