"""
    NAME : DIBANSA, RAHMNI P
    SECTION : BSCPE 2-2
"""

# WE WILL BE USING THE BUILT IN ARRAY OF PYTHON
import array as asArray

# THE PROGRAM WOULD ASK FORR THE INTEGERS THAT WOULD BE PUT INSIDE THE ARRAY
# EXAMPLE INPUT : 1,2,3,4,5,6
integers = eval ( input ( " Enter the integers you want to put inside your array : " ) )

integers2 = list ( integers )
integers2.sort()

# THE PROGRAM WOULD INITIALIZE THE BUILT IN ARRAY 
MyArray = asArray.array ( "i" , integers )
MyArrayBinary = asArray.array ( "i" , integers2 )

searchNum = eval ( input ( " Enter the integer that you would like to search for : " ) )

# Linear SEARCH
print ( " Your Linear Array : " , end = " " )
for i in range ( len ( MyArray) ):
    print ( MyArray[i] , end = " " )
print ( "" )
for i in range ( len ( MyArray) ) :
    if searchNum == MyArray[i] :
        print ( " The index of " , searchNum , " is " , i , "." )
        break

# Binary SEARCH
print ( " Your Binary Array : " , end = " " )
for i in range ( len ( MyArrayBinary) ):
    print ( MyArrayBinary[i] , end = " " )
print ( "" )

# THIS FOLLOWING BLOCK OF CODE WILL SEARCH USING THE BINARY SEARCH METHOD
high = int ( MyArrayBinary[ len ( MyArrayBinary ) - 1 ] )
low = searchNum
mid = int (( high - low ) / 2 )
temp = str( mid )
mid = int ( temp[0] )
found = False
while found == False:
    if MyArrayBinary[mid] == searchNum:
        print ( " The index of " , searchNum , " is " , mid )
        found = True
    elif MyArrayBinary[mid] > searchNum:
        mid  -= 1
    elif MyArrayBinary[mid] < searchNum:
        mid += 1


