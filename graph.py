class graph1:
    def __init__(self):
        self.graph1 = { 1 : [ 2 , 3 ] ,
                        2 : [ 4 ] ,
                        3 : [ 6 ] ,
                        4 : [ 5 ] ,
                        5 : [ 2 ] ,
                        6 : [ 4 , 7 ] ,
                        7 : [ ] }
        self.startingPoint = 1

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

    def useDFS(self, node = 1, visited = []):
        self.node = node
        self.visited = visited
        if self.node not in self.visited:
            self.visited.append( self.node )
            for nde in self.graph1[ self.node ] :
                self.useDFS( nde , self.visited )
        return self.visited

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

class graph2:
    def __init__(self):
        self.graph2 = { "A" : [ "B" ] ,
                        "B" : [ "E" ] ,
                        "E" : [ "C" , "D" ],
                        "C" : [] ,
                        "D" : [] }

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

    def useDFS(self, node = "A", visited = []):
        self.node = node
        self.visited = visited
        if self.node not in self.visited:
            self.visited.append( self.node )
            for nde in self.graph2[ self.node ] :
                self.useDFS( nde , self.visited )
        return self.visited

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
    
graph1 = graph1()
print( graph1.useDFS() )
print( graph1.searchGraph1(7) )

graph2 = graph2()
print( graph2.useBFS() )
print( graph2.searchGraph2("E") )

while True:
    print( "====================================\n" )
    print( "               MENU \n" )
    print( "====================================\n" )
    print( "  [1] Perform Depth First Traversal \n" )
    print( "  [2] Perform Breadth First Traversal\n")
    print( "  [3] Search Graph 1 ( DFS ) \n " )
    print( "  [4] Search Graph 2 ( BFS ) \n " )
    print( "  [5] Exit \n " )
    print( "====================================\n" )
    choice = eval( input ( " What is your choice : " ) )
    if choice == 1 :
        print( "====================================\n" )
        print( "       Choose a graph to DFT       \n" )
        print( "====================================\n" )
        print( "  [1] Graph 1 \n" )
        print( "  [2] Graph 2 \n" )
        print( "====================================\n" )
        choice2 = eval( input ( " What is your choice : " ) )
        print( "====================================\n" )
        if choice2 == 1:
            print( " The result is : " + str(graph1.useDFS()) )
        if choice2 == 2:
            print( " The result is : " + str(graph2.useDFS()) )
    elif choice == 2 :
        print( "====================================\n" )
        print( "       Choose a graph to BFT       \n" )
        print( "====================================\n" )
        print( "  [1] Graph 1 \n" )
        print( "  [2] Graph 2 \n" )
        print( "====================================\n" )
        choice2 = eval( input ( " What is your choice : " ) )
        print( "====================================\n" )
        if choice2 == 1:
            print( " The result is : " + str(graph1.useBFS()) )
        if choice2 == 2:
            print( " The result is : " + str(graph2.useBFS()) )
    elif choice == 3:
        print( "====================================\n" )
        vertex = eval ( input ( " Enter a vertex : " ))
        print( "====================================\n" )
        print( " The result is : " + str( graph1.searchGraph1() ) )
        print( "====================================\n" )
    elif choice == 4:
        print( "====================================\n" )
        vertex = eval ( input ( " Enter a vertex : " ))
        print( "====================================\n" )
        print( " The result is : " + str( graph2.searchGraph2() ) )
        print( "====================================\n" )
    elif choice == 5:
        break
    else:
        print ( " Error : Invalid Input " )
            
