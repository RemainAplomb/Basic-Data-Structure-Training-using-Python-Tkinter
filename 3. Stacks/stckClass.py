"""
    Name: DIBANSA, RAHMANI P.
    Course: BSCPE 2-2
"""
# THE PROGRAM WOULD IMPORT THE BUILT IN ARRAY OF PYTHON
import array

# THIS CLASS MIMICS HOW STACKS WORKS USING THE BUILT IN ARRAY OF THE PYTHON
class stck :
    # THE INIT FUNCTION INITIALIZES THE DATABASE THAT WOULD CONTAIN THE ELEMENTS WITHIN THE PROGRAM'S STACK
    def __init__ ( self ):
        self.arDatabase = None
        self.Empty = True

    # THIS FUNCTION CHECKS IF THE QUEUE IS EMPTY OR NOT
    def is_empty ( self ):
        if self.arDatabase == None:
            self.Empty = True
        else:
            self.tempLen = len ( self.arDatabase )
            if self.tempLen == 0 :
                self.Empty = True
            else:
                self.Empty = False
    # THIS FUNCTION ADDS ANOTHER ELEMENT INTO THE STACK
    def push ( self, user_input ):
        self.user_input = user_input
        self.is_empty()
        if self.Empty == True :
            self.arDatabase = array.array ( "i" , [ self.user_input ] )
        else:
            self.arDatabase.append ( self.user_input )

    # THIS FUNCTION REMOVES THE LAST ITEM IN THE STACK
    def pop ( self ):
        self.is_empty()
        if self.Empty == False:
            self.poppedValue = self.arDatabase [ ( len ( self.arDatabase ) - 1 ) ]
            self.arDatabase.pop ( len ( self.arDatabase) - 1 )
            print ( " Popped value : " , self.poppedValue )
        else:
            print ( " Stack is empty. " )

    # THIS FUNCTION DISPLAYS THE ITEMS INSIDE THE STACK
    def display ( self ) :
        if self.arDatabase != None :
            self.n = len ( self.arDatabase ) - 1
            print ( " Your stack contains : ")
            for i in range ( len ( self.arDatabase ) ) :
                print ( "                       " , self.arDatabase[ self.n ] )
                self.n -= 1
            print ( "" )
        
