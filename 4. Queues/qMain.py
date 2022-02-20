"""
    Name: DIBANSA, RAHMANI P.
    Course: BSCPE 2-2
"""
# FIRST, THE PROGRAM WOULD BE IMPORTING THE qClass THAT CONTAINS THE FUNCTIONS THAT MAKES THE PROGRAM POSSIBLE
from qClass import *

# THEN THE PROGRAM WOULD CALL UPON THE CLASS QUEUE
q = queue()

# EVERYTHING THAT IS INSIDE THIS WHILE LOOP CONTAINS THE GENERAL FLOW OF THE PROGRAM.
while True:
    print ( "" )
    print ( " enqueue <value> " )
    print ( " dequeue " )
    print ( " quit " )
    q.display()
    print ( "" )
    user_command = str ( input ( " What would you like to do ? " ) )
    # THIS PROCESS SPLITS THE USER'S COMMAND AND TAKES THE NECESSARY DATA THAT WOULD NEED TO BE PROCESSED
    commandInList = user_command.split( " " )
    choice = commandInList[0].lower()
    # THESE ARE THE POSSIBLE COMMANDS THAT THE PROGRAM COULD PROCESS.
    if choice == "quit" :
        break
    elif choice == "dequeue" :
        q.dequeue()
    elif choice == "enqueue" :
        try:
            queueInt = int ( commandInList[1] )
            q.enqueue ( queueInt )
        except:
            print ( " Oops!Something went wrong while pushing an item into the queue. " )
    else:
        print ( " Error : Can't recognize command. " )
