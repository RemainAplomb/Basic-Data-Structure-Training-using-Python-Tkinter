"""
    NAME : DIBANSA , RAHMANI P.
    COURSE-SECTION = BSCPE 2-2
    SUBJECT : DATA STRUCTURES AND ALGORITHM
"""

# First, the program will be importing the class that I have made specifically for this program
from arrayY import *

# Then, we would be calling the arrayY class.
ar = arrayY()

# To make sure that the program keeps on iterating, the program will use while loop that is set to True
while True:
    # Here the program will be printing the menu that contains all possible commands that the program could process.
    print ( "==============================" )
    print ( "            MENU              " )
    print ( "==============================" )
    print ( "  1. Insert at Beginning. " )
    print ( "  2. Insert in Between. " )
    print ( "  3. Insert at End. " )
    print ( "  4. Linear Search. " )
    print ( "  5. Binary Search. " )
    print ( "  6. Delete " )
    print ( "  7. Exit. " )
    print ( "==============================" )
    # The program would then call the display function present within the arrrayY class to print out the elements within the array.
    ar.display()
    print ( "==============================" )
    # Afterwards, the program would ask for the user's choice of action.
    choice = eval ( input ( " Enter your choice : " ) )
    # Depending on the user's inputted choice of action, the program will execute a certain process.
    if choice == 1 :
        user_input = eval ( input ( " Enter an integer : " ) )
        ar.insert_at_beg ( user_input )
    elif choice == 2 :
        user_input = eval ( input ( " Enter an integer : " ) )
        indx = eval ( input ( " Enter the index : " ) )
        ar.insert_in_between ( indx , user_input )
    elif choice == 3 :
        user_input = eval ( input ( " Enter an integer : " ) )
        ar.insert_at_end ( user_input )
    elif choice == 4 :
        element = eval ( input ( " Enter the element that you want to search for : " ) )
        ar.linear_search ( element )
    elif choice == 5 :
        element = eval ( input ( " Enter the element that you want to search for : " ) )
        ar.binary_search ( element )
    elif choice == 6 :
        element = eval ( input ( " Enter the element that you want to delete : " ) )
        ar.delete ( element )
    elif choice == 7 :
        break
    
