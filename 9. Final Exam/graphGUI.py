"""
    NAME : DIBANSA, RAHMANI P.
    NAME : BELGA, EMJAY
    COURSE : BSCPE 2-2
    ACADEMIC YEAR : 2019-2020

    PROGRAM'S SUMMARY: THIS PROGRAM HAS TWO CUSTOMIZED GRAPHS THAT WOULD NEED TO BE PROCESSED USING THE GRAPH DATA STRUCTURE. THRE PROGRAM COULD;
        PERFORM DEPTH FIRST TRAVERSE, BREADTH FIRST TRAVERSE, SEARCHING USING BFS, AND SEARCHING USING DFS.
"""

# THESE ARE OUR MODULES THAT WE WOULD BE USING
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk


# THE CLASS GRAPH1 CONTAINS ALL OF THE NECESSARY FUNCTIONS RELATED TO THE FIRST GRAPH
class graph1:
    # WE WOULD FIRST INITIALIZE OUR GRAPH AND ITS STARTING POINT
    def __init__(self):
        self.graph1 = { 1 : [ 2 , 3 ] ,
                        2 : [ 4 ] ,
                        3 : [ 6 ] ,
                        4 : [ 5 ] ,
                        5 : [ 2 ] ,
                        6 : [ 4 , 7 ] ,
                        7 : [ ] }
        self.startingPoint = 1

    # THIS FUNCTION WOULD TRAVERSE THIS GRAPH USING BREADTH FIRST
    def useBFS(self):
        self.visited = []
        self.queue = [ self.startingPoint ]
        while self.queue:
            self.node = self.queue.pop(0)
            if self.node not in self.visited:
                self.visited.append( self.node )
                self.neighbours = self.graph1[ self.node ]

                for neighbour in self.neighbours:
                    self.queue.append( neighbour )
        return self.visited

    # THIS FUNCTION WOULD TRAVERSE THIS GRAPH USING DEPTH FIRST
    def useDFS(self, node = 1, visited = []):
        self.node = node
        self.visited = visited
        if self.node not in self.visited:
            self.visited.append( self.node )
            for nde in self.graph1[ self.node ] :
                self.useDFS( nde , self.visited )
        return self.visited

    # THIS FUNCTION WOULD SEARCH THE GRAPH USING DFS
    def searchGraph1 (self, vertex ):
        self.node = 1
        self.visited = []
        self.vertex = vertex
        self.queue = [1]
        while self.queue:
            self.node = self.queue.pop(0)
            if self.node not in self.visited:
                self.visited.append( self.node )
                if int(self.vertex) == int(self.node):
                    return True
                for nde in self.graph1[ self.node ] :
                    self.queue.append( nde)
        return False

# THIS CLASS CONTAINS ALL THE NECESSARY FUNCTIONS FOR THE SECOND GRAPH
class graph2:
    # WE WOULD INITIALIZE OUR GRAPH
    def __init__(self):
        self.graph2 = { "A" : [ "B" ] ,
                        "B" : [ "E" ] ,
                        "E" : [ "C" , "D" ],
                        "C" : [] ,
                        "D" : [] }

    # THIS FUNCTION WOULD TRAVERSE THE SECOND GRAPH USING THE BREADTH FIRST METHOD
    def useBFS(self):
        self.startingPoint = "A"
        self.visited = []
        self.queue = [ self.startingPoint ]
        while self.queue:
            self.node = self.queue.pop(0)
            if self.node not in self.visited:
                self.visited.append( self.node )
                self.neighbours = self.graph2[ self.node ]

                for neighbour in self.neighbours:
                    self.queue.append( neighbour )
        return self.visited

    # THIS FUNCTION WOULD TRAVERSE THE SECOND GRAPH USING THE DEPTH FIRST METHOD
    def useDFS(self, node = "A", visited = []):
        self.node = node
        self.visited = visited
        if self.node not in self.visited:
            self.visited.append( self.node )
            for nde in self.graph2[ self.node ] :
                self.useDFS( nde , self.visited )
        return self.visited

    # THIS FUNCTION WOULD SEARCH IF THE GIVEN VERTEX IS PRESENT IN THE GRAPH
    def searchGraph2(self, vertex):
        self.startingPoint = "A"
        self.vertex = vertex
        self.visited = []
        self.queue = [ self.startingPoint ]
        while self.queue:
            self.node = self.queue.pop(0)
            if self.node not in self.visited:
                if self.node == self.vertex:
                    return True
                self.visited.append( self.node )
                self.neighbours = self.graph2[ self.node ]

                for neighbour in self.neighbours:
                    self.queue.append( neighbour )
        return False

# THIS CLASS CONTAINS THE PROGRAM'S USER INTERFACE
class GUI:
    def __init__(self):
        self.menu()
        
    # THIS FUNCTION CLEARS ALL THE WIDGETS IN THE MENU
    def clearMenu(self):
        self.heading.destroy()
        self.dftBTN.destroy()
        self.bftBTN.destroy()
        self.sG1BTN.destroy()
        self.sG2BTN.destroy()
        self.exitBTN.destroy()
        self.graph1BTN.destroy()
        self.graph2BTN.destroy()

    # THIS FUNCTION CONTAINS ALL OF THE WIDGETS FOR OUR PROGRAM'S MAIN MENU   
    def menu(self):
        self.graph1Image_resize = Image.open( "graph1.png" ).resize( (300 , 200), Image.ANTIALIAS )
        self.graph1Image = ImageTk.PhotoImage( self.graph1Image_resize )
        self.graph1BTN = Button ( root , image = self.graph1Image)
        self.graph1BTN.photo = self.graph1Image
        self.graph1BTN.place ( x = 20 , y = 100 )

        self.graph2Image_resize = Image.open( "graph2.png" ).resize( (300 , 200), Image.ANTIALIAS )
        self.graph2Image = ImageTk.PhotoImage( self.graph2Image_resize )
        self.graph2BTN = Button ( root , image = self.graph2Image)
        self.graph2BTN.photo = self.graph1Image
        self.graph2BTN.place ( x = 580 , y = 100 )
        
        self.heading = Label ( root , text = "MAIN MENU" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.heading.pack()

        self.dftBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "Depth First Traversal" , width = "25"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.dftBTN_Pressed)
        self.dftBTN.place ( x = 360 , y = 80 , height = 30 )

        self.bftBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "Breadth First Traversal" , width = "25"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.bftBTN_Pressed )
        self.bftBTN.place ( x = 360 , y = 140 , height = 30 )

        self.sG1BTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "Search Graph 1(DFS)" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.sG1BTN_Pressed )
        self.sG1BTN.place ( x = 380 , y = 200 , height = 30 )

        self.sG2BTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "Search Graph 2(BFS)" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.sG2BTN_Pressed )
        self.sG2BTN.place ( x = 380 , y = 260 , height = 30 )

        self.exitBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "Exit" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.ext )
        self.exitBTN.place ( x = 380 , y = 320 , height = 30 )
        
    # THIS FUNCTION CONTAINS THE WIDGETS FOR DEPTH FIRST TRAVERSAL BUTTON
    def dftBTN_Pressed(self):
        try:
            self.clearMenu()
        except:
            pass
        self.heading = Label ( root , text = "CHOOSE A GRAPH" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.heading.pack()
        
        self.graph1Image_resize = Image.open( "graph1.png" ).resize( (300 , 200), Image.ANTIALIAS )
        self.graph1Image = ImageTk.PhotoImage( self.graph1Image_resize )
        self.graph1BTN = Button ( root , image = self.graph1Image)
        self.graph1BTN.photo = self.graph1Image
        self.graph1BTN.place ( x = 20 , y = 100 )

        self.graph2Image_resize = Image.open( "graph2.png" ).resize( (300 , 200), Image.ANTIALIAS )
        self.graph2Image = ImageTk.PhotoImage( self.graph2Image_resize )
        self.graph2BTN = Button ( root , image = self.graph2Image)
        self.graph2BTN.photo = self.graph1Image
        self.graph2BTN.place ( x = 580 , y = 100 )

        self.grph1BTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GRAPH 1" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.DFTgrph1BTN_Pressed )
        self.grph1BTN.place ( x = 380 , y = 140 , height = 30 )

        self.grph2BTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GRAPH 2" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.DFTgrph2BTN_Pressed )
        self.grph2BTN.place ( x = 380 , y = 200 , height = 30 )

        self.goBackBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GO BACK" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.goBackBTN_Pressed )
        self.goBackBTN.place ( x = 380 , y = 260 , height = 30 )

    # THIS FUNCTION LEADS THE PROGRAM BACK TO THE MAIN MENU
    def goBackBTN_Pressed(self):
        try:
            self.heading.destroy()
            self.graph1BTN.destroy()
            self.graph2BTN.destroy()
            self.goBackBTN.destroy()
            self.grph1BTN.destroy()
            self.grph2BTN.destroy()
        except:
            pass
        try:
            self.searchLBL.destroy()
            self.searchENTRY.destroy()
            self.searchBTN.destroy()
            self.goBackBTN.destroy()
        except:
            pass
        self.menu()

    # THIS FUNCTION WOULD SEARCH THE FIRST GRAPH USING DFT     
    def DFTgrph1BTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            messagebox.showinfo( "GRAPH 1 DFT" , "The result is :\n" + str(graph1.useDFS()) )

    # THIS FUNCTION WOULD SEARCH THE SECOND GRAPH USING DFT
    def DFTgrph2BTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            messagebox.showinfo( "GRAPH 2 DFT" , "The result is :\n" + str(graph2.useDFS()) )

    # THIS FUNCTION WOULD SEARCH THE FIRST GRAPH USING BFT
    def BFTgrph1BTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            messagebox.showinfo( "GRAPH 1 BFT" , "The result is :\n" + str(graph1.useBFS()) )

    # THIS FUNCTION WOULD SEARCH THE SECOND GRAPH USING BFT
    def BFTgrph2BTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            messagebox.showinfo( "GRAPH 2 BFT" , "The result is :\n" + str(graph2.useBFS()) )

    # THIS FUNCTION CONTAINS THE WIDGETS FOR TRAVERSING USING BREADTH FIRST METHOD.
    def bftBTN_Pressed(self):
        try:
            self.clearMenu()
        except:
            pass
        self.heading = Label ( root , text = "CHOOSE A GRAPH" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.heading.pack()
        
        self.graph1Image_resize = Image.open( "graph1.png" ).resize( (300 , 200), Image.ANTIALIAS )
        self.graph1Image = ImageTk.PhotoImage( self.graph1Image_resize )
        self.graph1BTN = Button ( root , image = self.graph1Image)
        self.graph1BTN.photo = self.graph1Image
        self.graph1BTN.place ( x = 20 , y = 100 )

        self.graph2Image_resize = Image.open( "graph2.png" ).resize( (300 , 200), Image.ANTIALIAS )
        self.graph2Image = ImageTk.PhotoImage( self.graph2Image_resize )
        self.graph2BTN = Button ( root , image = self.graph2Image)
        self.graph2BTN.photo = self.graph1Image
        self.graph2BTN.place ( x = 580 , y = 100 )

        self.grph1BTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GRAPH 1" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.BFTgrph1BTN_Pressed )
        self.grph1BTN.place ( x = 380 , y = 140 , height = 30 )

        self.grph2BTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GRAPH 2" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.BFTgrph2BTN_Pressed )
        self.grph2BTN.place ( x = 380 , y = 200 , height = 30 )

        self.goBackBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GO BACK" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.goBackBTN_Pressed )
        self.goBackBTN.place ( x = 380 , y = 260 , height = 30 )

    # THIS FUNCTION CONTAINS THE WIDGETS FOR SEARCHING GRAPH 1 USING DFS
    def sG1BTN_Pressed(self):
        try:
            self.clearMenu()
        except:
            pass
        self.heading = Label ( root , text = "SEARCH GRAPH 1( DFS )" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.heading.pack()
        
        self.graph1Image_resize = Image.open( "graph1.png" ).resize( (300 , 200), Image.ANTIALIAS )
        self.graph1Image = ImageTk.PhotoImage( self.graph1Image_resize )
        self.graph1BTN = Button ( root , image = self.graph1Image)
        self.graph1BTN.photo = self.graph1Image
        self.graph1BTN.place ( x = 20 , y = 100 )

        self.searchLBL = Label ( root , font = ( "Courier" , 8 , "bold" ) , width = "20", text = "ENTER A VERTEX :" 
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.searchLBL.place ( x = 560 , y = 120 , height = 30 )

        self.searchENTRY = Text ( root , font = ( "Courier" , 8 , "bold" ) , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.searchENTRY.place ( x = 560 , y = 180 , height = 30 )
        
        self.searchBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "SEARCH" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.sG1SearchBTN_Pressed )
        self.searchBTN.place ( x = 430 , y = 260 , height = 30 )

        self.goBackBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GO BACK" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.goBackBTN_Pressed )
        self.goBackBTN.place ( x = 700 , y = 260 , height = 30 )

    # THIS FUNCTION WOULD SEARCH IF THE USER'S GIVEN VERTEX IS PRESENT IN GRAPH 1
    def sG1SearchBTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            messagebox.showinfo( "GRAPH 1 BFS" , "The result is :\n" + str(graph1.searchGraph1(self.searchENTRY.get( "1.0" , "end-1c"))) )

    # THIS FUNCTION WOULD SEARCH OF THE USER'S GIVEN VERTEX IS PRESENT IN GRAPH 2
    def sG2SearchBTN_Pressed(self):
        if messagebox.askyesno( "Confirmation..." , " Are you sure? " )== True :
            messagebox.showinfo( "GRAPH 2 DFS" , "The result is :\n" + str(graph2.searchGraph2(self.searchENTRY.get( "1.0" , "end-1c"))) )

    # THIS FUNCTION CONTAINS THE WIDGETS FOR SEARCHING GRAPH 2 USING BFS
    def sG2BTN_Pressed(self):
        try:
            self.clearMenu()
        except:
            pass
        self.heading = Label ( root , text = "SEARCH GRAPH 2( BFS )" , bg = "black" , fg = "white" , width = "100" , height = "2" ,
                               font = ( "Courier" , 18 , "bold" ) )
        self.heading.pack()
        
        self.graph2Image_resize = Image.open( "graph2.png" ).resize( (300 , 200), Image.ANTIALIAS )
        self.graph2Image = ImageTk.PhotoImage( self.graph2Image_resize )
        self.graph2BTN = Button ( root , image = self.graph2Image)
        self.graph2BTN.photo = self.graph2Image
        self.graph2BTN.place ( x = 20 , y = 100 )

        self.searchLBL = Label ( root , font = ( "Courier" , 8 , "bold" ) , width = "20", text = "ENTER A VERTEX :" 
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.searchLBL.place ( x = 560 , y = 120 , height = 30 )

        self.searchENTRY = Text ( root , font = ( "Courier" , 8 , "bold" ) , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" )
        self.searchENTRY.place ( x = 560 , y = 180 , height = 30 )
        
        self.searchBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "SEARCH" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.sG2SearchBTN_Pressed )
        self.searchBTN.place ( x = 430 , y = 260 , height = 30 )

        self.goBackBTN = Button ( root , font = ( "Courier" , 8 , "bold" ) , text = "GO BACK" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = self.goBackBTN_Pressed )
        self.goBackBTN.place ( x = 700 , y = 260 , height = 30 )

    # THIS FUNCTION WOULD CLOSE/ TERMINATE THE PROGRAM'S USER INTERFACE
    def ext(self):
        root.destroy()

# IN THIS BLOCK OF CODE, WE WOULD INITIALIZE OUR PROGRAM AND START THE USER INTERFACE 
graph1 = graph1()
graph2 = graph2()
root = Tk()
root.title( " Data Structures : Graph " )
root.resizable( width = FALSE , height = FALSE )
root.geometry( "900x400" )
root.config( background = "grey" )
gui = GUI()

