"""
    NAME : DIBANSA , RAHMANI P.
    COURSE-SECTION = BSCPE 2-2
    SUBJECT : DATA STRUCTURES AND ALGORITHM
"""
class ArList:
    # Here we will be initializing the list that would acty as our array
    def __init__ ( self ) :
        self.array = []

    # This function would print the array if called
    def display ( self ) :
        print ( self.array )

    # This function appends an element in the array
    def append ( self , user_input ) :
        self.user_input = user_input
        try:
            self.array += [self.user_input]
        except:
            print ( " Error : You can only append one element at a time. " )
        

    # This function is able to add a number of elements to the list
    def extend ( self , user_input ) :
        self.user_input = user_input
        try:
            for i in range ( len ( self.user_input ) ) :
                self.array += [ self.user_input[i] ]
        except:
            self.array += [ self.user_input ]


    # This function can insert an element to the user's desired index
    def insert ( self , index , user_input ) :
        self.temporary_array = []
        self.user_input = user_input
        self.index = index
        for i in range ( len ( self.array ) + 1 ) :
            if i == self.index :
                self.temporary_array += [ self.user_input]
                try:
                    self.temporary_array += [ self.array[i] ]
                except:
                    pass
            else:
                try:
                    self.temporary_array += [ self.array[i] ]
                except:
                    pass

        self.array = self.temporary_array

    # This function can remove the desired element of the user.
    def remove ( self , user_input ) :
        self.temporary_array = []
        self.user_input = user_input
        self.UIindx = self.indx( self.user_input )
        for i in range ( len ( self.array ) ) :
            if i != self.UIindx :
                self.temporary_array += [ self.array[i] ]
        self.array = self.temporary_array

    # This function returns the index of the element inputted by the user.
    def indx ( self , user_input ) :
        self.user_input = user_input
        self.nthCount = 0
        for i in range ( len ( self.array ) ) :
            if self.user_input == self.array[i]:
                return self.nthCount
            self.nthCount += 1

    # This function will count the number of times the given element occured.         
    def count ( self , user_input) :
        self.user_input = user_input
        self.occurence = 0
        for i in range ( len ( self.array ) ) :
            if self.array[i] == self.user_input:
                self.occurence += 1
        return self.occurence

    # This function is able to remove the element in a certain index.
    def pop ( self , index ) :
        self.temporary_array = []
        self.index = index
        for i in range ( len ( self.array ) ) :
            if i != self.index :
                self.temporary_array += [ self.array[i] ]
        self.array = self.temporary_array

    # This function reverses the arrangements of elements in the array
    def reverse ( self ) :
        self.temporary_array = []
        self.lenArray = len ( self.array ) - 1
        for i in range ( len ( self.array ) ) :
            self.temporary_array.append( self.array [ self.lenArray ] )
            self.lenArray -= 1
        self.array = self.temporary_array

    # This function sorts the array.
    def sort ( self ) :
        self.sorting_temporary_array = []
        self.nOccurence = 0
        for i in range ( len ( self.array ) ) :
            self.nOccurence = 0
            try:
                self.nOccurence = self.count( min(self.array) )
                for n in range ( self.nOccurence ) :
                    self.sorting_temporary_array += [ min(self.array) ]

                for n in range ( self.nOccurence ) :
                    self.remove( min(self.array) )

            except:
                pass
        self.array = self.sorting_temporary_array            

    # This function would simply remove every element in the array.
    def clear ( self ) :
        self.array = []


# Here the program would call the class that I have made.
array = ArList()

# In this section the program will be appending the numbers one to four into the array.
array.append ( 1 )
array.append ( 2 )
array.append ( 3 )
array.append ( 4 )
array.display()

# Here the program will be asking for the elements that the user wants to add into the list.
user_input = eval ( input ( " Input the integers you want to extend to the array : " ))
array.extend ( user_input )
array.display()

# Here the program the element to be inserted into the array and the index where it will be placed.
user_input = eval ( input ( " Input the element you want to insert : " ) )
index = int ( input ( " Enter the index you want to input it into : " ) )
array.insert ( index , user_input )
array.display()

# Here the program would be removing the element desired by the host.
user_input = eval ( input ( " Enter the element that you want to remove : " ) )
array.remove ( user_input )
array.display()

# Here the program will print the index of the element that the user is looking for.
user_input = eval ( input ( " What element do you want to look for ? " ) )
index = array.indx ( user_input )
print ( " The index of " , user_input , " is : " , index )

# Here the program would be counting the number of times the user's input occured.
user_input = eval ( input ( " What element do you want to count the number of occurence? " ) )
print ( " The number of " , user_input , " in the array : " , array.count( user_input ) )

# Here the program will be removing the element in the index given
user_input = eval ( input ( " What index do you want to pop ? " ) )
array.pop ( user_input )
array.display()

# Here the program will reverse the elements in the list
array.reverse()
array.display()

# Here the elements in the array will be sorted.
array.sort()
array.display()

# Here the program will clear the elements inside the array.
array.clear()
array.display()

        
