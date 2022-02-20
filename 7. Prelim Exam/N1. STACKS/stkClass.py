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

# This stack class mimics a stack of notebooks.
class stcks:
    # The program would be initializing the allocated storage for the notebook's stack and the truth value
    # of isStackEmpty.
    def __init__( self ) :
        self.stackStorage = []
        self.isStackEmpty = True

    # This function checks if the stack is empty or not.
    # The program would be updating the truth value of isStackEmpty depending on the result of the process.
    def is_empty ( self ) :
        self.tempLen = len ( self.stackStorage )
        if self.tempLen == 0:
            self.isStackEmpty = True
        else:
            self.isStackEmpty = False

    # This function adds another book on top of the stack.
    def addNotebook ( self , ownerName ) :
        self.ownerName = ownerName
        self.stackStorage.append ( self.ownerName )

    # If the notebook stack isn't empty, this function would remove the last added notebook in the stack.
    def checkNotebook ( self ) :
        self.is_empty()
        if self.isStackEmpty == True:
            return None
        else:
            self.stackStorage.pop ( len ( self.stackStorage ) - 1 )

    # If the notebook stack isn't empty, this function would take the name of the owner of the last inputted
    # notebook in the stack, and the program would return the name of the notebook's owner back to wherever it has
    # been called.
    def peekAtNotebook ( self ) :
        self.is_empty()
        if self.isStackEmpty == True:
            return None
        else:
            self.notebookOwner = self.stackStorage[ len ( self.stackStorage ) - 1 ]
            return self.notebookOwner

    # If the notebook stack isn't empty, this function would take all the names of the notebook owners and record it
    # following the order of the stack.
    def checkAll ( self ) :
        self.is_empty()
        if self.isStackEmpty == True:
            return None
        else:
            self.result = ""
            self.tempStackStorage = self.stackStorage.copy()
            for i in range ( len ( self.tempStackStorage ) ) :
                if i != ( len( self.tempStackStorage) - 1 ) :
                    self.result += self.tempStackStorage[i] + ", "
                else:
                    self.result += self.tempStackStorage[i] + "."
            return self.result

    # This is an extension of the checkAll function above, all this does is remove all the elements within the
    # program's stack.
    def checkedAll ( self ) :
        self.stackStorage = []
    
