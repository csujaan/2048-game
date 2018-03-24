import random

"""Generating initial conditions"""
def initials():
    """Creating the matrix"""
    order=input("Enter the matrix size: ")
    matrix=[[0 for column in range(order)] for row in range(order)]
    """generating initial numbers"""
    a=2**random.randint(1,2)
    b=2**random.randint(1,3)
    matrix[random.randint(order)][random.randint(order)]=a
    while (True):
        x=random.randint(order)
        y=random.randint(order)
        if matrix[x][y]==0:
            matrix[x][y]=b
            break
    """Printing the matrix"""
    for i in range(x):
        print matrix[i]



"""for generating a number at each step"""
def generate():
    while(True):
        if matrix[random.randint(order)][random.randint(order)]==0:
            matrix[random.randint(order)][random.randint(order)]=2**random.randint(1,2)
            break



"""Taking keyboard input from user"""
def swipe():
    print "\n\nEnter....\n'w' to swipe up\n's' to swipe down\n'a' to swipe left\n'd' to swipe right\n"
    swipe_value=raw_input()
    if swipe_value =='W' or swipe_value=='w':
        up_swipe()
    elif swipe_value =='S' or swipe_value=='s':
        down_swipe()
    elif swipe_value =='A' or swipe_value=='a':
        left_swipe()
    elif swipe_value =='D' or swipe_value=='d':
        right_swipe()
    else:
        print "\nPlease enter a valid choice!\n\n"



"""Up swipe function"""
def up_swipe():
    for r in range(1,order):
        for c in range(order):
            while matrix[c][r-1]==0:
                if matrix[c][r]==matrix[c][r-1] and matrix[c][r-1]!=0:
                    matrix[c][r-1]=matrix[c][r]+matrix[c][r-1]
                    matrix[c][r]=0
                if matrix[c][r-1]==0:
                    matrix[c][r-1],matrix[c][r]=matrix[c][r],matrix[c][r-1]
    generate()



"""Down swipe function"""
def down_swipe():
    for r in range(order-1):
        for c in range(order):
            while matrix[c][r-1]==0:
                if matrix[c][r]==matrix[c][r+1]:
                    matrix[c][r+1]=matrix[c][r]+matrix[c][r+1]
                    matrix[c][r]=0
                if matrix[c][r+1]==0:
                    matrix[c][r+1],matrix[c][r]=matrix[c][r],matrix[c][r+1]
    generate()

"""Left swipe function"""   
def left_swipe():



    generate()

"""Right swipe function"""
def right_swipe():



    generate()




"""Calling functions"""
initials()
swipe()
