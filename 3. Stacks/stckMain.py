# THE PROGRAM WOULD FIRST IMPORT EVERYTHING INSIDE THE .PY FILE NAME STCKCLASS
from stckClass import *

# AFTERWARDS, THE PROGRAM WOULD CALL UPON THE CLASS INSIDE THE IMPORTED .PY FILE
stk = stck()

# THIS WHILE LOOP CONTAINS THE GENERAL FLOW OF THE PROGRAM AND IS MOSTLY SELF EXPLANATORY SINCE IT IS VERY SIMPLE 
while True:
    print ( "" )
    print ( " push <value> " )
    print ( " pop " )
    print ( " quit " )
    stk.display()
    print ( "" )
    user_command = str ( input ( " What would you like to do ? " ) )
    # THIS PROCESS SPLITS THE USER'S COMMAND AND TAKES THE NECESSARY DATA THAT WOULD NEED TO BE PROCESSED
    commandInList = user_command.split( " " )
    choice = commandInList[0].lower()
    # THESE ARE THE POSSIBLE COMMANDS THAT THE PROGRAM COULD PROCESS.
    if choice == "quit" :
        break
    elif choice == "pop" :
        stk.pop()
    elif choice == "push" :
        try:
            pushInt = int ( commandInList[1] )
            stk.push ( pushInt )
        except:
            print ( " Oops!Something went wrong while pushing an item into the stack. " )
    else:
        print ( " Error: Can't recognize the user's command. " )

