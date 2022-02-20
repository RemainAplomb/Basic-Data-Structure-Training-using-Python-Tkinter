
# This is a separate class that deals with the storage of data
class storage:
	def __init__( self , data=None ):
		self.data = data
		self.next = None

# This is the class for the Linked List
class LinkedList:
	# We will be initializing the storage of the linked list.
	def __init__( self ):
		self.head = storage()

	# Using this function we will be able to append a data to the linked list.
	def app ( self , data ):
		self.data = data
		self.NewStorage = storage( self.data )
		self.Current = self.head
		while self.Current.next != None:
			self.Current = self.Current.next
		self.Current.next = self.NewStorage

	# Using this function we will be counting the number of elements within the list.
	def len ( self ) :
		self.CurrentStorage = self.head
		self.NumOfElements= 0
		while self.CurrentStorage.next != None:
			self.NumOfElements += 1
			self.CurrentStorage= self.CurrentStorage.next
		return self.NumOfElements

	# Prints out the linked list in traditional Python list format. 
	def print ( self ):
		self.list = []
		self.CurrentStorage = self.head
		while self.CurrentStorage.next != None:
			self.CurrentStorage = self.CurrentStorage.next
			self.list.append( self.CurrentStorage.data )
		print( self.list )

	# This function will return  the element inside the given index.
	def take ( self , index ) :
		self.index = index
		if self.index >= self.len() or self.index < 0: 
			print( " Error : The index inputted can't be located! " )
			return None
		self.CurrentIndex = 0
		self.CurrentStorage = self.head
		while True:
			self.CurrentStorage = self.CurrentStorage.next
			if self.CurrentIndex == self.index: 
				return self.CurrentStorage.data
			self.CurrentIndex += 1

	# This function will delete the element of a given index
	def remove ( self , index ):
		self.index = index
		if self.index >= self.len() or self.index < 0: 
			print( " Error : The index given can't be located " )
			return None
		self.CurrentIndex=0
		self.CurrentStorage = self.head
		while True:
			self.LastStorage = self.CurrentStorage
			self.CurrentStorage = self.CurrentStorage.next
			if self.CurrentIndex == self.index:
				self.LastStorage.next = self.CurrentStorage.next
				return None
			self.CurrentIndex += 1


## WE WILL BE TESTING HERE THE LINKED LIST CLASS THAT WE HAVE CREATED.

# LL STANDS FOR LINKED LIST

# FIRST WE WILL BE CALLING THE CLASS
LL = LinkedList()

# SECOND, WE WILL TRY TO APPEND THE VALUES 2,4,6,8,10
LL.app(2)
LL.app(4)
LL.app(6)
LL.app(8)
LL.app(10)

# THIRD, WE WILL BE PRINTING THE LINKED LIST
LL.print()

# FOURTH, WE WILL PRINT THE ELEMENT INSIDE THE SECOND INDEX
print ( " We took : " , LL.take(1) )

# FIFTH, WE WILL TRY TO REMOVE THE ELEMENT INSIDE THE SECOND INDEX
LL.remove(1)

# LASTLY WE WILL TRY TO PRINT THE LINKED LIST AGAIN AND WE WILL USE THE LEN FUNCTION TO COUNT THE NUMBER OF ELEMENTS INSIDE THE LINKED LIST.
LL.print()
print(" The numbef of elements : " , LL.len() )