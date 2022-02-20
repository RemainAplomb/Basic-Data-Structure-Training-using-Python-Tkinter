"""
    NAME : DIBANSA , RAHMANI P.
    COURSE-SECTION = BSCPE 2-2
    SUBJECT : DATA STRUCTURES AND ALGORITHM
"""

import array # We will be importing the built in array in python

class arrayY:
    # Here we will be initializing the array's database to None so that it would be easier to tell if the array's database is empty or not
    def __init__ ( self ) : 
        self.arDatabase = None

    # This function would input the user's inputted integer at the very beginning. If the array's database is equals to None, it would create it and add the element that the user have inputted.
    # Otherwise, it would proceed to just insert the user's input at index 0
    def insert_at_beg ( self, user_input ) :
        self.user_input = user_input
        if self.arDatabase == None:
            self.arDatabase = array.array ( "i" , [ user_input ] )
        else:
            self.arDatabase.insert ( 0 , self.user_input )

    # This function would be taking the user's desired integer and index and would act the same way as the insert_at_beg function.
    # The only difference is that the user could add the integer in his desired index.
    def insert_in_between ( self, indx , user_input ) :
        self.user_input = user_input
        self.indx = indx
        if self.arDatabase == None:
            print ( " Oops! The index that you have inputted exceeds the possible index present. " )
        elif self.indx > len ( self.arDatabase) :
            print ( " Oops! The index that you have inputted exceeds the possible index present. " )
        else:
            self.arDatabase.insert ( self.indx , self.user_input )

    # This function would be appending  the user's input into the array if the array's database has already been created.
    # Otherwise, the program would create the array's database and add the user's input.
    def insert_at_end ( self , user_input ) :
        self.user_input = user_input
        if self.arDatabase == None:
            self.arDatabase = array.array ( "i" , [ user_input ] )
        else:
            self.arDatabase.append ( self.user_input )

    # This function would be iterating every index to search for the user's inputted element.
    # If the program sees that the inputted element matches with the element within the array's database, it would print the index.
    def linear_search ( self , element ) :
        self.element = element
        self.found = False
        if self.arDatabase != None:
            for i in range ( len ( self.arDatabase ) ) :
                if self.arDatabase[i] == self.element :
                    print ( " The element you are looking for is at index : " , i )
                    self.found = True
                    break
            if self.found == False:
                print ( " Oops! The element you are looking for cannot be found! " )

    # This function employs the binary search formula to effectively and efficiently find the inputted element.
    def binary_search ( self , element ) :
        self.tempList = []
        self.element = element
        self.found = False
        self.stop = 0
        if self.arDatabase != None :
            for i in range ( len ( self.arDatabase ) ) :
                self.tempList.append ( self.arDatabase[i] )
            self.tempList.sort()
            self.arDatabase = array.array ( "i" , self.tempList )
            self.low = 0
            self.high = len ( self.arDatabase ) + 1 
            while self.found == False:
                self.mid = int ( ( self.low + ( self.high - self.low ) ) / 2 )
                if self.mid > ( len ( self.arDatabase ) + 1 ) :
                    self.linear_search ( self.element )
                    break
                elif self.stop == 500 :
                    self.linear_search ( self.element )
                    break
                else:
                    if self.arDatabase[ self.mid ] == self.element :
                        print ( " The element you are looking for is at index : " , self.mid )
                        break
                    elif self.arDatabase[ self.mid ] > self.element :
                        self.stop += 1
                        self.high = self.mid - 1
                    elif self.arDatabase[ self.mid ] < self.element :
                        self.stop += 1
                        self.high = self.mid + 1
    # This function is self explanatory and very simple. It just takes the user's inputted element and deletes it using the '.remove' function of the built-in array that we are using
    def delete ( self, element ) :
        self.element = element
        if self.arDatabase != None :
            try:
                self.arDatabase.remove ( self.element )
            except:
                print ( " Oops! The program can't delete the element that you want to delete. " )

    # This function displays the elements within the array's database.
    def display ( self ) :
        if self.arDatabase != None :
            print ( " Your array contains : " , end = "" )
            for i in range ( len ( self.arDatabase ) ) :
                print ( self.arDatabase[i] , end = " " )
            print ( "" )


                
            
