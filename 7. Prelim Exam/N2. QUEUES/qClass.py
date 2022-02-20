"""
    NAME : DIBANSA, RAHMANI P.
    NAME : BELGA, EMJAY
    COURSE : BSCPE 2-2
    ACADEMIC YEAR : 2019-2020

    PROGRAM'S SUMMARY: THIS IS A QUEUEING PROGRAM THAT MIMICS A DOCTOR'S APPOINTMENT QUEUE.
"""

# THIS NODE CLASS CONTAINS THE NAME AND CONCERN OF THE PATIENT SIGNING UP FOR A CONSULTATION. IT ALSO CONTAINS THE POINTER
# THAT LEADS TO THE NEXT NODE IN THE LINKED LIST.
class node:
    def __init__ ( self , name = None , concern = None) :
        self.name = name
        self.concern = concern
        self.next = None

# THIS CLASS CONTAINS THE FUNCTIONS THAT WOULD BE THE BACKBONE FOR THE QUEUEING PROGRAM.
class qClass:
    # HERE THE PROGRAM INITIALIZES THE HEAD OF OUR LINKED LIST
    def __init__ ( self ) :
        self.head = node()

    # THIS FUNCTION CONTAINS THE PROCESS THAT WOULD PUT THE PATIENT'S DATA INTO A NODE AND APPENDS IT INTO THE QUEUE.
    def signUp ( self , name , concern ) :
        self.name = name
        self.concern = concern
        self.newNode = node( self.name , self.concern )
        self.currentNode = self.head
        while self.currentNode.next != None:
            self.currentNode = self.currentNode.next
        self.currentNode.next = self.newNode

    # TO MAKE IT EASIER FOR ME TO CODE, I'VE ADDED THE NAME AND CONCERN OF THE PATIENT AT THE FRONT OF THE QUEUE
    # INTO A LIST THAT WOULD BE RETURNED BY THIS FUNCTION ONCE IT HAS BEEN CALLED BY THE PROGRAM.
    # THIS MAKES IT SO THAT MY BEGIN CONSULTATION FUNCTION WOULD ONLY NEED TO CONTAIN THE REMOVAL OF FIRST NODE IN THE
    # LINKED LIST.
    def enterRoom ( self ):
        self.currentNode = self.head
        self.tempList = []
        if self.currentNode.next != None:
            self.tempList.append ( self.currentNode.next.name )
            self.tempList.append ( self.currentNode.next.concern )
            return self.tempList
        else:
            return None
    # THIS FUNCTION REMOVES THE FIRST NODE OF THE QUEUE IF THE QUEUE IS NOT EMPTY.
    def beginConsultation ( self ) :
        self.currentNode = self.head
        self.tempList = []
        if self.currentNode.next != None:
            self.currentNode.next = self.currentNode.next.next
        else:
            return None
    # THIS FUNCTION RESETS THE VALUE OF THE HEAD NODE TO REMOVE ALL THE PRIOR NODES THAT THE PROGRAM HAS ADDED
    # INTO THE LIST.
    def closing ( self ):
        self.head = node()
