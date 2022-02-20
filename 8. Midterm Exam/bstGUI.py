"""
    NAME : DIBANSA, RAHMANI P.
    NAME : BELGA, EMJAY
    COURSE-SECTION : BSCPE 2-2

    PROGRAM'S SUMMARY : THIS IS A BINARY SEARCH TREE PROGRAM. THE PROGRAM CAN ; DO INSERTION, DO SEARCHING, DELETE,
    CLEAR THE BST, SEARCH FOR MINIMUM VALUE, SEARCH FOR MAXIMUM VALUE, FIND THE SUCCESSOR OF A NODE, AND FIND THE
    PREDECESSOR OF A NODE.
"""

# THESE ARE OUR MODULES THAT WE WOULD BE USING
from tkinter import *
from tkinter import messagebox                                              
from tkinter import ttk

# THIS IS THE BASIC NODE CLASS THAT WOULD BE THE FOUNDATION OF THE BINARY SEARCH TREE.
class node:
    def __init__ ( self , data = None ) :
        self.data = data
        self.parent = None
        self.right = None
        self.left = None

# THIS IS THE CLASS THAT CONTAINS THE FUNCTIONS OF THE BINARY SEARCH TREE
class BST :
    def __init__ ( self ) :
        self.bstRoot = None

    # THIS FUNCTION RESETS THE BSTROOT VARIABLE BACK TO NONE
    def clear ( self ) :
        self.bstRoot = None
        print ( " The BST has been successfully cleared. " )

    # THIS FUNCTION INSERTS AN ELEMENT/VALUE INTO THE BINARY SEARCH TREE
    def insert ( self , data ) :
        self.data = data
        self.newNode = node ( self.data )
        self.currentNode = self.bstRoot
        if self.bstRoot == None:
            self.bstRoot = node ( self.data )
        else:
            while True:
                if self.data > self.currentNode.data:
                    if self.currentNode.right == None:
                        self.currentNode.right = self.newNode
                        self.currentNode.right.parent = self.currentNode
                        print( " right" )
                        return True
                    else:
                        self.currentNode = self.currentNode.right
                        print ( " move to right" )
                elif self.data < self.currentNode.data:
                    if self.currentNode.left == None:
                        self.currentNode.left = self.newNode
                        self.currentNode.left.parent = self.currentNode
                        print ( " left " )
                        return True
                    else:
                        self.currentNode = self.currentNode.left
                        print( " move to left " )
                elif self.data == self.currentNode.data:
                    return False

    # THIS FUNCTION TRUE IF THE ELEMENT INPUTTED IS INSIDE THE LIST, AND WOULD RETURN FALSE IF OTHERWISE.
    def search ( self , data ):
        self.data = data
        self.currentNode = self.bstRoot
        if self.bstRoot == None:
            print ( " The BST is currently empty. " )
            return None
        else:
            while self.currentNode != None:
                if self.data == self.currentNode.data:
                    return True
                elif self.data > self.currentNode.data:
                    self.currentNode = self.currentNode.right
                elif self.data < self.currentNode.data:
                    self.currentNode = self.currentNode.left
            return False

    # THIS FUNCTION RETURNS THE MINIMUM VALUE THAT IS INSIDE THE BINARY SEARCH TREE.
    def minimum ( self ) :
        self.currentNode = self.bstRoot
        if self.bstRoot == None:
            print ( " The BST is currently empty. " )
            return None
        else:
            while self.currentNode.left != None:
                self.currentNode = self.currentNode.left
            return self.currentNode.data
        
    # THIS FUNCTION CONTAINS THE MAXIMUM VALUE THAT IS INSIDE THE BINARY SEARCH TREE.
    def maximum ( self ) :
        self.currentNode = self.bstRoot
        if self.bstRoot == None:
            print ( " The BST is currently empty. " )
            return None
        else:
            while self.currentNode.right != None:
                self.currentNode = self.currentNode.right
            return self.currentNode.data

    # THIS FUNCTION RETURNS THE LEFT AND RIGHT CHILDREN OF THE INPUTTED ELEMENT.
    # BTW, THE FUNCTION WOULD RETURN NONE IF THE BINARY SEARCH TREE IS EMPTY.
    # FURTHERMORE, IF THE ELEMENT INPUTTED CANNOT BE FOUND INSIDE THE BST, THE PROGRAM WOULD RETURN FALSE.
    def successor ( self , data ) :
        self.data = data
        self.currentNode = self.bstRoot
        if self.bstRoot == None:
            print ( " The BST is currently empty. " )
            return None
        else:
            while self.currentNode != None:
                if self.data == self.currentNode.data:
                    self.tempList = []
                    if self.currentNode.left == None:
                        self.tempList.append( None )
                    else:
                        self.tempList.append( self.currentNode.left.data )

                    if self.currentNode.right == None:
                        self.tempList.append( None )
                    else:
                        self.tempList.append( self.currentNode.right.data ) 
                    return self.tempList
                elif self.data > self.currentNode.data:
                    self.currentNode = self.currentNode.right
                elif self.data < self.currentNode.data:
                    self.currentNode = self.currentNode.left
            return False

    # THIS FUNCTION IS ABLE TO RETURN THE PARENT VALUE OF THE INPUTTED ELEMENT.
    def predecessor ( self , data ) :
        self.data = data
        self.targetNode = self.nodeSearch( self.data )
        if self.targetNode == None:
            return None
        elif self.targetNode == False:
            return False
        else:
            return self.targetNode.parent.data

    # THIS FUNCTION RETURNS THE NODE OF THE GIVEN ELEMENT.        
    def nodeSearch ( self , data ):
        self.data = data
        self.currentNode = self.bstRoot
        if self.bstRoot == None:
            return None
        else:
            while self.currentNode != None:
                if self.data == self.currentNode.data:
                    return self.currentNode
                elif self.data > self.currentNode.data:
                    self.currentNode = self.currentNode.right
                elif self.data < self.currentNode.data:
                    self.currentNode = self.currentNode.left
            return False

    # THIS FUNCTION RETURNS THE NUMBER OF CHILDREN THE GIVEN NODE HAS
    def numberOfChildren ( self , nocNode ) :
        self.nocNode = nocNode
        self.nChildren = 0
        if self.nocNode.left != None:
            self.nChildren += 1
        if self.nocNode.right != None:
            self.nChildren += 1
        return self.nChildren
        
    # THIS FUNCTION IS ABLE TO REMOVE/DELETE A NODE FROM THE BINARY SEARCH TREE.
    def delete ( self, data ) :
        self.data = data
        self.toDeleteNode = self.nodeSearch( self.data )
        self.currentNode = self.bstRoot

        if self.bstRoot == None:
            print ( " The Binary Search Tree is empty. " )
            return None
        elif self.toDeleteNode == False:
            print ( " The element you want to delete is nowhere to be found. " )
            return False
        elif self.toDeleteNode.parent == None:
            print ( " You can't delete the root node.")
            return -1
        else:
            self.nChildren = self.numberOfChildren( self.toDeleteNode )

            if self.nChildren == 0:
                self.currentNode = self.toDeleteNode.parent
                if self.toDeleteNode.data > self.currentNode.data:
                    self.currentNode.right = None
                else:
                    self.currentNode.left = None
            elif self.nChildren == 1:
                self.parentNode = self.toDeleteNode.parent
                if self.toDeleteNode.left != None:
                    self.toDeleteNodeChild = self.toDeleteNode.left
                elif self.toDeleteNode.right != None:
                    self.toDeleteNodeChild = self.toDeleteNode.right

                self.toDeleteNodeChild.parent = self.parentNode

                if self.toDeleteNode.data > self.parentNode.data:
                    self.parentNode.right = self.toDeleteNodeChild
                else:
                    self.parentNode.left = self.toDeleteNodeChild
            elif self.nChildren == 2:
                self.currentNode = self.toDeleteNode.right
                if self.currentNode.left != None:
                    while self.currentNode.left != None:
                        self.currentNode = self.currentNode.left
                self.currentNode.left = self.toDeleteNode.left
                self.currentNode.parent = self.toDeleteNode.parent
                if self.toDeleteNode.data > self.toDeleteNode.parent.data:
                    self.toDeleteNode.parent.right = self.currentNode
                else:
                    self.toDeleteNode.parent.left = self.currentNode
                    
# THIS CLASS CONTAINS OUR PROGRAM'S USER INTERFACE
class GUI:
    def __init__( self ):
        self.menu()

    # THIS FUNCTION WOULD CLEAR THE WIDGETS IN MENU
    def clearMenu( self):
        self.heading.destroy()
        self.insertBTN.destroy()
        self.searchBTN.destroy()
        self.minimumValueBTN.destroy()
        self.maximumValueBTN.destroy()
        self.successorBTN.destroy()
        self.predecessorBTN.destroy()
        self.deleteBTN.destroy()
        self.clearBstBTN.destroy()
        self.exitBTN.destroy()

    # THIS FUNCTION WOULD GENERATE THE WIDGETS OF MAIN MENU
    def menu( self ):
        self.heading = Label ( root , text = "MAIN MENU" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.heading.pack()

        self.insertBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "INSERT" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.insertBTN_Pressed)
        self.insertBTN.place ( x = 280 , y = 80 , height = 30 )

        self.searchBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "SEARCH" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.searchBTN_Pressed )
        self.searchBTN.place ( x = 280 , y = 140 , height = 30 )

        self.minimumValueBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "MINIMUM VALUE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.minimumValueBTN_Pressed )
        self.minimumValueBTN.place ( x = 280 , y = 200 , height = 30 )

        self.maximumValueBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "MAXIMUM VALUE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.maximumValueBTN_Pressed )
        self.maximumValueBTN.place ( x = 280 , y = 260 , height = 30 )


        self.successorBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "SUCCESSOR" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.successorBTN_Pressed)
        self.successorBTN.place ( x = 480 , y = 80 , height = 30 )

        self.predecessorBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "PREDECESSOR" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.predecessorBTN_Pressed )
        self.predecessorBTN.place ( x = 480 , y = 140 , height = 30 )

        self.deleteBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "DELETE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.deleteBTN_Pressed )
        self.deleteBTN.place ( x = 480 , y = 200 , height = 30 )

        self.clearBstBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "CLEAR BST" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.clearBstBTN_Pressed )
        self.clearBstBTN.place ( x = 480 , y = 260 , height = 30 )

        self.exitBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "Exit" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.ext )
        self.exitBTN.place ( x = 380 , y = 320 , height = 30 )

    # THIS FUNCTION CONTAINS THE WIDGETS OF THE INSERTION USER INTERFACE
    def insertBTN_Pressed(self):
        try:
            self.clearMenu()
        except:
            pass

        self.heading = Label ( root , text = "INSERTION" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.heading.pack()

        self.insertLBL = Label ( root , font = ( "Courier" , 8 , "bold" ) , width = "20", text = "ENTER AN ELEMENT :" 
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.insertLBL.place ( x = 390 , y = 120 , height = 30 )

        self.insertENTRY = Text ( root , font = ( "Courier" , 8 , "bold" ) , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.insertENTRY.place ( x = 390 , y = 180 , height = 30 )
        
        self.insertBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "INSERT" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.insertInsertBTN_Pressed )
        self.insertBTN.place ( x = 260 , y = 260 , height = 30 )

        self.goBackBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GO BACK" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.goBackBTN_Pressed )
        self.goBackBTN.place ( x = 530 , y = 260 , height = 30 )

    # THIS FUNCTION WOULD LEAD THE PROGRAM BACK TO THE MAIN MENU
    def goBackBTN_Pressed(self):
        try:
            self.heading.destroy()
            self.insertLBL.destroy()
            self.insertENTRY.destroy()
            self.insertBTN.destroy()
        except:
            pass
        try:
            self.searchLBL.destroy()
            self.searchENTRY.destroy()
            self.searchBTN.destroy()
        except:
            pass
        try:
            self.deleteLBL.destroy()
            self.deleteENTRY.destroy()
            self.deleteBTN.destroy()
        except:
            pass

        try:
            self.successorLBL.destroy()
            self.successorENTRY.destroy()
            self.successorBTN.destroy()
        except:
            pass
        try:
            self.predecessorLBL.destroy()
            self.predecessorENTRY.destroy()
            self.predecessorBTN.destroy()
        except:
            pass
        self.goBackBTN.destroy()
        self.menu()

    # THIS FUNCTION WOULD INSERT AN ELEMENT INTO THE BST
    def insertInsertBTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            self.insert_data = int(self.insertENTRY.get( "1.0" , "end-1c"))
            self.result = bst.insert( self.insert_data )
            if self.result == True:
                messagebox.showinfo( "INSERTION PROMPT" , "You have successfully added an element to the BST." )
            elif self.result == False:
                messagebox.showinfo( "INSERTION PROMPT" , "The element that you have entered is already in the BST. " )
            self.goBackBTN_Pressed()

    # THIS FUNCTION CONTAINS THE WIDGETS OF THE SEARCH USER INTERFACE
    def searchBTN_Pressed(self):
        try:
            self.clearMenu()
        except:
            pass
        self.heading = Label ( root , text = "SEARCH" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.heading.pack()

        self.searchLBL = Label ( root , font = ( "Courier" , 8 , "bold" ) , width = "20", text = "ENTER AN ELEMENT :" 
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.searchLBL.place ( x = 390 , y = 120 , height = 30 )

        self.searchENTRY = Text ( root , font = ( "Courier" , 8 , "bold" ) , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.searchENTRY.place ( x = 390 , y = 180 , height = 30 )
        
        self.searchBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "SEARCH" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.searchSearchBTN_Pressed )
        self.searchBTN.place ( x = 260 , y = 260 , height = 30 )

        self.goBackBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GO BACK" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.goBackBTN_Pressed )
        self.goBackBTN.place ( x = 530 , y = 260 , height = 30 )

    # THIS FUNCTION WOULD SEARCH FOR THE USER'S INPUTTED ELEMENT 
    def searchSearchBTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            self.result = bst.search ( int(self.searchENTRY.get( "1.0" , "end-1c")) )
            if self.result == None:
                messagebox.showinfo( "SEARCH RESULTS" , "The BST is currently empty." )
            elif self.result == True:
                messagebox.showinfo( "SEARCH RESULTS" , "The element that you are searching for is inside the BST." )
            elif self.result == False:
                messagebox.showinfo( "SEARCH RESULTS" , "The element that you are searching for cannot be found. " )
            self.goBackBTN_Pressed()

    # THIS FUNCTION WOULD DISPLAY THE MINIMUM VALUE PRESENT IN THE BST
    def minimumValueBTN_Pressed(self):
        messagebox.showinfo( "MINIMUM VALUE" , "The result is :\n" + str(bst.minimum()) )

    # THIS FUNCTION WOULD DISPLAY THE MAXIMUM VALUE PRESENT INSIDE THE BST
    def maximumValueBTN_Pressed(self):
        messagebox.showinfo( "MAXIMUM VALUE" , "The result is :\n" + str(bst.maximum()) )

    # THIS FUNCTION CONTAINS THE WIDGETS FOR THE SUCCESSOR USER INTERFACE
    def successorBTN_Pressed(self):
        try:
            self.clearMenu()
        except:
            pass
        self.heading = Label ( root , text = "LOOK FOR THE SUCCESSOR" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.heading.pack()

        self.successorLBL = Label ( root , font = ( "Courier" , 8 , "bold" ) , width = "20", text = "ENTER AN ELEMENT :" 
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.successorLBL.place ( x = 390 , y = 120 , height = 30 )

        self.successorENTRY = Text ( root , font = ( "Courier" , 8 , "bold" ) , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.successorENTRY.place ( x = 390 , y = 180 , height = 30 )
        
        self.successorBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "SEARCH" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.successorSuccessorBTN_Pressed )
        self.successorBTN.place ( x = 260 , y = 260 , height = 30 )

        self.goBackBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GO BACK" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.goBackBTN_Pressed )
        self.goBackBTN.place ( x = 530 , y = 260 , height = 30 )

    # THIS FUNCTION WOULD SEARCH FOR THE SUCCESSOR OF THE USER'S INPUTTED ELEMENT
    def successorSuccessorBTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            self.find_successor = int(self.successorENTRY.get( "1.0" , "end-1c" ))
            self.result = bst.successor( self.find_successor )
            
            if self.result == None:
                messagebox.showinfo( "Successor Prompt" , "The BST is currently empty. " )
            elif self.result == False:
                messagebox.showinfo( "Successor Prompt" , "The element that you are looking for is not in the BST." )
            else:
                try:
                    messagebox.showinfo( "Successor Prompt" , "Parent : " + str(self.find_successor) + "\n" +
                                         "Right Child : " + str(self.result[1]) + "\n" +
                                         "Left Child : " + str(self.result[0]) )
                except:
                    messagebox.showinfo( "Successor Prompt" , "Failed to display result." )
            self.goBackBTN_Pressed()

    # THIS FUNCTION CONTAINS THE WIGETS FOR THE PREDECESSOR USER INTERFACE
    def predecessorBTN_Pressed(self):
        try:
            self.clearMenu()
        except:
            pass
        self.heading = Label ( root , text = "LOOK FOR THE PREDECESSOR" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.heading.pack()

        self.predecessorLBL = Label ( root , font = ( "Courier" , 8 , "bold" ) , width = "20", text = "ENTER AN ELEMENT :" 
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.predecessorLBL.place ( x = 390 , y = 120 , height = 30 )

        self.predecessorENTRY = Text ( root , font = ( "Courier" , 8 , "bold" ) , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.predecessorENTRY.place ( x = 390 , y = 180 , height = 30 )
        
        self.predecessorBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "SEARCH" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.predecessorPredecessorBTN_Pressed )
        self.predecessorBTN.place ( x = 260 , y = 260 , height = 30 )

        self.goBackBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GO BACK" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.goBackBTN_Pressed )
        self.goBackBTN.place ( x = 530 , y = 260 , height = 30 )

    # THIS FUNCTION WOULD SEARCH FOR THE PREDECESSOR OF THE USER'S INPUTTED ELEMENT
    def predecessorPredecessorBTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            self.find_predecessor = int(self.predecessorENTRY.get( "1.0" , "end-1c" ))
            self.result = bst.predecessor( self.find_predecessor )
            if self.result == None:
                messagebox.showinfo( "Predecessor Prompt" , "The BST is currently empty. " )
            elif self.result == False:
                messagebox.showinfo( "Predecessor Prompt" , "The element that you are looking for is not in the BST." )
            elif self.result == "Invalid" :
                messagebox.showinfo( "Predecessor Prompt" , "Child : " + str(self.find_predecessor) + "\n" +
                                    "Predecessor : None " )
            else:
                try:
                    messagebox.showinfo( "Predecessor Prompt" , "Child : " + str(self.find_predecessor) + "\n" +
                                         "Predecessor : " + str(self.result) )
                except:
                    messagebox.showinfo( "Predecessor Prompt" , "Failed to display result." )
            self.goBackBTN_Pressed()


    # THIS FUNCTION CONTAINS THE WIDGETS FOR THE DELETE/REMOVE USERINTERFACE
    def deleteBTN_Pressed(self):
        try:
            self.clearMenu()
        except:
            pass

        self.heading = Label ( root , text = "DELETE/REMOVE" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.heading.pack()

        self.deleteLBL = Label ( root , font = ( "Courier" , 8 , "bold" ) , width = "20", text = "ENTER AN ELEMENT :" 
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.deleteLBL.place ( x = 390 , y = 120 , height = 30 )

        self.deleteENTRY = Text ( root , font = ( "Courier" , 8 , "bold" ) , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.deleteENTRY.place ( x = 390 , y = 180 , height = 30 )
        
        self.deleteBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "DELETE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.deleteDeleteBTN_Pressed )
        self.deleteBTN.place ( x = 260 , y = 260 , height = 30 )

        self.goBackBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GO BACK" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.goBackBTN_Pressed )
        self.goBackBTN.place ( x = 530 , y = 260 , height = 30 )

    # THIS FUNCTION WOULD DELETE THE ELEMENT GIVEN BY THE USER
    def deleteDeleteBTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            self.to_delete = int(self.deleteENTRY.get("1.0" , "end-1c"))
            self.result = bst.delete( self.to_delete )
            if self.result == True:
                messagebox.showinfo( "Removal Prompt" , "You have successfully deleted the node"  )
            elif self.result == -1:
                messagebox.showinfo( "Removal Prompt" , "You can't delete the root node." )
            elif self.result == False:
                messagebox.showinfo( "Removal Prompt" , "The element that you want to delete is not in the BST." )
            elif self.result == None:
                messagebox.showinfo( "Removal Prompt" , "The Binary Search Tree is empty." )
            self.goBackBTN_Pressed()

    # THIS FUNCTION WOULD CLEAR THE BST
    def clearBstBTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            bst.clear()
            messagebox.showinfo( "BST CLEAR PROMPT" , "You have successfully cleared the BST." )

    # THIS FUNCTION WOULD TERMINATE THE PROGRAM
    def ext(self):
        root.destroy()
            
# THE PROGRAM WOULD CALL THE BST CLASS
bst = BST()
root = Tk()
root.title( " Data Structures : BST " )
root.resizable( width = FALSE , height = FALSE )
root.geometry( "900x400" )
root.config( background = "grey" )
gui = GUI()
