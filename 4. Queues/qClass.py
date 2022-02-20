"""
    Name: DIBANSA, RAHMANI P.
    Course: BSCPE 2-2
"""

import array

#  THIS CLASS IS A REPRESENTAION OF HOW A QUEUE WOULD FUNCTION IF IT IS MADE INTO A PROGRAM
class queue :
    # HERE WE WOULD BE INITIALIZING THE DATABASE THAT WOULD CONTAIN OUR ARRAY THAT WOULD ACT AS STORAGE FOR THE QUEUED DATA.
    # THE PROGRAM WOULD ALSO BE INITIALIZING THE VARIABLE "EMPTY"
    def __init__ ( self ):
        self.arDatabase = None
        self.Empty = True

    # THIS FUNCTION LOOKS THROUGH THE ARDATABASE AND CHECKS IF THE STORAGE IS EMPTY OR NOT
    def is_empty ( self ):
        if self.arDatabase == None:
            self.Empty = True
        else:
            self.tempLen = len ( self.arDatabase )
            if self.tempLen == 0 :
                self.Empty = True
            else:
                self.Empty = False
    # THIS FUNCTION ADDS/ APPENDS AN ELEMENT INTO THE QUEUE
    def enqueue ( self, user_input ):
        self.user_input = user_input
        self.is_empty()
        if self.Empty == True :
            self.arDatabase = array.array ( "i" , [ self.user_input ] )
        else:
            self.arDatabase.append ( self.user_input )

    # THIS FUNCTION REMOVES/POPS THE FIRST ELEMENT IN THE QUEUE
    def dequeue ( self ):
        self.is_empty()
        if self.Empty == False:
            self.dequeuedValue = self.arDatabase [0]
            self.arDatabase.pop (0)
            print ( " Dequeued value : " , self.dequeuedValue )
        else:
            print ( " Queue is empty. " )

    # THIS FUNCTION DISPLAYS THE QUEUED ELEMENTS
    def display ( self ) :
        if self.arDatabase != None :
            print ( " Your Queue contains : " , end = "" )
            for i in range ( len ( self.arDatabase ) ) :
                print ( self.arDatabase[i] , end = " " )
            print ( "" )
