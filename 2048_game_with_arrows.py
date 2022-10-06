import random
import turtle
arrow=turtle.Screen()
''' this function controls the movement of the tiles. It moves them up,down arrow,left,right based on the input'''
def upward(Matrix):
        i=0
        for j in range(0,4):
            if Matrix[i][j]!=0 or Matrix[i+1][j]!=0 or Matrix[i+2][j]!=0 or Matrix[i+3][j]!=0:# This if stametent basically checks if there is atleast one number that is not zero in the column
                if Matrix[i][j]==0:#this if statement is true only if the first number in a given column of j is zero
                    while Matrix[i][j]==0:
                        Matrix[i][j]=Matrix[i+1][j]
                        Matrix[i+1][j]=Matrix[i+2][j]#the following statments basically shifts every number upward and inserts zero at the end
                        Matrix[i+2][j] = Matrix[i+3][j]
                        Matrix[i+3][j]=0
                    #* print("THis is the first if",Matrix)
                if Matrix[i+1][j]==0 and (Matrix[i+2][j]!=0 or Matrix[i+3][j]!=0):#this if statement is true only if the second number in a given column j is zero and the other numbers under ihave aleast one non-zero value
                    while Matrix[i+1][j]==0:
                        Matrix[i+1][j]=Matrix[i+2][j]
                        Matrix[i+2][j]=Matrix[i+3][j]
                        Matrix[i+3][j]=0
                    #* delete to see print("This is the Second if",Matrix)
                if Matrix[i+2][j]==0 and (Matrix[i+3][j]!=0):#this if statement is true only if the third number in the column is zero and the number under it is not zero
                    while Matrix[i+2][j]==0:
                        Matrix[i+2][j]=Matrix[i+3][j]
                        Matrix[i+3][j]=0
                    #* delete to see print("This is the third if",Matrix)
        i=0
        for j in range(0,4): #This part addes two numbers if they are identical
            if Matrix[i][j]==Matrix[i+1][j]:#if the first and second number in the colomn are identical 
                Matrix[i][j]=Matrix[i][j]+Matrix[i+1][j]#multiply it by 2 
                Matrix[i+1][j]=Matrix[i+2][j]#and shift upward
                Matrix[i+2][j]=Matrix[i+3][j]
                Matrix[i+3][j]=0
            if Matrix[i+1][j]==Matrix[i+2][j]:#if the number second and third number in  the colomn j are identical
                Matrix[i+1][j]=Matrix[i+1][j]+Matrix[i+2][j]#multiply it by 2 
                Matrix[i+2][j]=Matrix[i+3][j]#and shift upward
                Matrix[i+3][j]=0
            if Matrix[i+2][j]==Matrix[i+3][j]:
                Matrix[i+2][j]=Matrix[i+2][j]+Matrix[i+3][j]
                Matrix[i+3][j]=0
                        
                        

def doarrowward(Matrix):      
        i=0
        for j in range(0,4):
            if Matrix[i][j]!=0 or Matrix[i+1][j]!=0 or Matrix[i+2][j]!=0 or Matrix[i+3][j]!=0:# This if stametent basically checks if there is atleast one number that is not zero in the column
                if Matrix[i+3][j]==0:
                    while Matrix[i+3][j]==0:#if the last number in the given column is zero
                        Matrix[i+3][j]=Matrix[i+2][j]#shift until the last number is not zero
                        Matrix[i+2][j]=Matrix[i+1][j]
                        Matrix[i+1][j]=Matrix[i][j]
                        Matrix[i][j]=0
                   #* print("This is the first if stament",Matrix)
                if Matrix[i+2][j]==0 and (Matrix[i+1][j]!=0 or Matrix[i][j]!=0):#if the third number is zero and one of the numbers above it is a non-zero
                    while Matrix[i+2][j]==0:
                        Matrix[i+2][j]=Matrix[i+1][j]
                        Matrix[i+1][j]=Matrix[i][j]
                        Matrix[i][j]=0
                    #*print("THis is the second if statment",Matrix)

                if Matrix[i+1][j]==0 and Matrix[i][j]!=0:#if the second number in a given column is zero while the number above is non-zero
                    while Matrix[i+1][j]==0:
                        Matrix[i+1][j]=Matrix[i][j]
                        Matrix[i][j]=0
                   #* print("THis is the third if statment",Matrix)
        i=0
        for j in range(0,4):
            if Matrix[i+3][j]==Matrix[i+2][j]:
                Matrix[i+3][j]=Matrix[i+3][j] + Matrix[i+2][j]
                Matrix[i+2][j]=Matrix[i+1][j]
                Matrix[i+1][j]=Matrix[i][j]
                Matrix[i][j]=0
            if Matrix[i+2][j]==Matrix[i+1][j]:
                Matrix[i+2][j]=Matrix[i+2][j]+Matrix[i+1][j]
                Matrix[i+1][j]=Matrix[i][j]
                Matrix[i][j]=0
            if Matrix[i+1][j]==Matrix[i][j]:
                Matrix[i+1][j]=Matrix[i+1][j]+Matrix[i][j]
                Matrix[i][j]=0
            
def leftside(Matrix):
        j=0
        for i in range(0,4):

            if Matrix[i][j]!=0 or Matrix[i][j+1]!=0 or Matrix[i][j+2]!=0 or Matrix[i][j+3]!=0:
                if Matrix[i][j]==0:
                    while Matrix[i][j]==0:
                        Matrix[i][j]=Matrix[i][j+1]
                        Matrix[i][j+1]=Matrix[i][j+2]
                        Matrix[i][j+2] = Matrix[i][j+3]
                        Matrix[i][j+3]=0
                if Matrix[i][j+1]==0 and (Matrix[i][j+2]!=0 or Matrix[i][j+3]!=0):
                    while Matrix[i][j+1]==0:
                        Matrix[i][j+1]=Matrix[i][j+2]
                        Matrix[i][j+2]=Matrix[i][j+3]
                        Matrix[i][j+3]=0
                if Matrix[i][j+2]==0 and (Matrix[i][j+3]!=0):
                    while Matrix[i][j+2]==0:
                        Matrix[i][j+2]=Matrix[i][j+3]
                        Matrix[i][j+3]=0
        j=0
        for i in range(0,4):
            if Matrix[i][j]==Matrix[i][j+1]:
                Matrix[i][j]=Matrix[i][j]+Matrix[i][j+1]
                Matrix[i][j+1]=Matrix[i][j+2]
                Matrix[i][j+2]=Matrix[i][j+3]
                Matrix[i][j+3]=0
            if Matrix[i][j+1]==Matrix[i][j+2]:
                Matrix[i][j+1]=Matrix[i][j+1]+Matrix[i][j+2]
                Matrix[i][j+2]=Matrix[i][j+3]
                Matrix[i][j+3]=0
            if Matrix[i][j+2]==Matrix[i][j+3]:
                Matrix[i][j+2]=Matrix[i][j+2]+Matrix[i][j+3]
                Matrix[i][j+3]=0
def rightside(Matrix):
        j=0
        for i in range(0,4):
            if Matrix[i][j]!=0 or Matrix[i][j+1]!=0 or Matrix[i][j+2]!=0 or Matrix[i][j+3]!=0:
                if Matrix[i][j+3]==0:
                    while Matrix[i][j+3]==0:
                        Matrix[i][j+3]=Matrix[i][j+2]
                        Matrix[i][j+2]=Matrix[i][j+1]
                        Matrix[i][j+1]=Matrix[i][j]
                        Matrix[i][j]=0
                if Matrix[i][j+2]==0 and (Matrix[i][j+1]!=0 or Matrix[i][j]!=0):
                    while Matrix[i][j+2]==0:
                        Matrix[i][j+2]=Matrix[i][j+1]
                        Matrix[i][j+1]=Matrix[i][j]
                        Matrix[i][j]=0

                if Matrix[i][j+1]==0 and Matrix[i][j]!=0:
                    while Matrix[i][j+1]==0:
                        Matrix[i][j+1]=Matrix[i][j]
                        Matrix[i][j]=0
        j=0
        for i in range(0,4):
            if Matrix[i][j+3]==Matrix[i][j+2]:
                Matrix[i][j+3]=Matrix[i][j+3] + Matrix[i][j+2]

                Matrix[i][j+2]=Matrix[i][j+1]
                Matrix[i][j+1]=Matrix[i][j]
                Matrix[i][j]=0
            if Matrix[i][j+2]==Matrix[i][j+1]:
                Matrix[i][j+2]=Matrix[i][j+2]+Matrix[i][j+1]
                Matrix[i][j+1]=Matrix[i][j]
                Matrix[i][j]=0
            if Matrix[i][j+1]==Matrix[i][j]:
                Matrix[i][j+1]=Matrix[i][j+1]+Matrix[i][j]
                Matrix[i][j]=0
                
                


'''This function displays the table in the format given'''
def table(Matrix):#error1 appends into a number
 print("***********************************************************")
 for i in range (4):
        print ("   +---------+---------+---------+---------+")
        for j in range (4):
                    print("   |",format(Matrix[i][j],"4d"),end=' ')#the format code simply gives spaces between the numbers in the table. if you change 4d to 5d the numbers will be further apart
        print("   |")
 print ("   +---------+---------+---------+---------+")
               

'''This function starts the program and checks whether or not you have won or lost '''

print("**********Welcome to the 2048 game*****************")
print("**********USE THE ARROW KEYS TO MOVE***************")
Matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]#first all the numbers in a given matrix are zero
avalible_index = [0,1,2,3]#to randomly pick an index to put the number 2 or 4 we make a list of avalible indexes in the matrix, then randomly pick two numbers from the list and take them as the index of the number we are putting
nums=[2,4]#in the game we are putting the number 4 or 2 randomly in the matrix
Matrix[random.choice(avalible_index)][random.choice(avalible_index)]=random.choice(nums)#the random.choice method randomly picks a number from the list

def main():   
        table(Matrix)
        izero = []# Here we create two empty lists this are used to find the indexes of the number zero in the matrix
        jzero = []
        count = 0
        for i in range(0,4):
            for j in range(0,4):
                if Matrix[i][j]==0:
                    count+=1
                    izero.append(i)#append the i index of the zero value to a izero
                    jzero.append(j)#append the j index of the zero value to a listoforj
        if count > 0:#meaning if there are zeros in the matrix
            if count > 1:#if there are two or more zeros
                randomindex = izero.index(random.choice(izero))
                Matrix[izero[randomindex]][jzero[randomindex]]=2
            else:
                Matrix[izero[0]][jzero[0]]=2
        else:
            print ("Game over")

        for i in range (0,4):
            for j in range (0,4):
                if Matrix[i][j]==2048:
                    print("Congartulations YOu won!!!")
                                                


main()

def move_up():
    upward(Matrix)
    main()
def move_down():
    doarrowward(Matrix)
    main()
def move_left():
    leftside(Matrix)
    main()
def move_right():
    rightside(Matrix)
    main()    
arrow.onkey(move_up,"Up")
arrow.onkey(move_down,"Down")
arrow.onkey(move_left,"Left")
arrow.onkey(move_right,"Right")
arrow.listen()
arrow.mainloop()  

