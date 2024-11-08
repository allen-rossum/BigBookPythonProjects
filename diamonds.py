

def main():
    print("Diamonds")

    #Display diamonds of sizes 0 through 6:
    for diamondSize in range(0,6):
        displayOutlineDiamond(diamondSize)
        print() #Print a new line
        displayFilledDiamond(diamondSize)
        print() #Print a new line


def displayOutlineDiamond(size):
    #Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1),end='') #left side space
        print('/', end = '') #left side of diamond
        print(' '* (i * 2),end='') #interior of the diamond
        print('\\') #right side of diamond

    #Display the bottom half of the diamond
    for i in range(size):
        print(' '* i,end='') #Left side space
        print('\\',end='')  #Left side of diamond
        print(' ' * ((size - i - 1)*2),end='') #interior of diamond
        print('/') #right side of diamond


def displayFilledDiamond(size):
    #Display the top half of the diamond
    for i in range(size):
        print(' ' * (size - i - 1),end='') #Left side space
        print('/' * (i+1),end='') #Left half of diamond
        print('\\'* (i+1)) #Right half of diamond

    #Display the bottom half of the diamond
        print(' ' * i,end='') #Left side space
        print('\\' * (size - i),end='') #Left side of Diamond
        print('/' * (size - i)) #Right side of diamond


#If this program was run (instead of imported),run the game:
if __name__ == '__main__':
    main()