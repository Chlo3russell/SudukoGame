import pygame


sizeX, sizeY = 600, 800

pygame.font.init()

# window size
board = pygame.display.set_mode((sizeX, sizeY))
# name of the window
pygame.display.set_caption("Sudoku Solver")

# predefined grid
# 0 represents an empty cell
grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


# fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

#glonbal variables for grid position and value
x = 0
y = 0
sizeOfCell = sizeX / 9
valueToPlace = 0


def createBoard():
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
                # colour numbers already given
                pygame.draw.rect(board, (173, 216, 230), (i * sizeOfCell, j * sizeOfCell, sizeOfCell + 1, sizeOfCell + 1))
                # fill cells with given board
                #.render takes parameters: text, antialiasing, color
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                # blit takes parameters: surface, text, position
                # position is calculated by multiplying cell size with row and column index
                board.blit(text1, (i * sizeOfCell + 15, j * sizeOfCell + 15))
    # display the grid like a traditional sudoku board       
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(board, (0, 0, 0), (0, i * sizeOfCell), (sizeX, i * sizeOfCell), thick)
        pygame.draw.line(board, (0, 0, 0), (i * sizeOfCell, 0), (i * sizeOfCell, sizeX), thick)  


'''
Function to get the coordinates of the cell clicked
:param pos: position of the mouse click
:return: row and column of the cell clicked
'''
def getCoords(pos):
    
    global x, y
    x = int(pos[0] // sizeOfCell)
    y = int(pos[1] // sizeOfCell)
    return x, y

# hightlight the cell clicked
def highlightCell():
    for i in range(2):
        # draw horizontal and vertical lines to highlight the cell
        # .line takes parameters: surface, color, start position, end position, width of line
        pygame.draw.line(board, (255, 0, 0), (x * sizeOfCell - 3, (y + i) * sizeOfCell), (x * sizeOfCell + sizeOfCell + 3, (y + i) * sizeOfCell), 7)
        pygame.draw.line(board, (255, 0, 0), ((x + i) * sizeOfCell, y * sizeOfCell), ((x + i) * sizeOfCell, y * sizeOfCell + sizeOfCell), 7)



def raiseError(errorType):
    if errorType == 1:
        text = font2.render("Error: Number cannot be zero", 1, (255, 0, 0))
    elif errorType == 2:
        text = font2.render("Error: Invalid Input", 1, (255, 0, 0))
    elif errorType == 3:
        text = font2.render("Error: Wrong number moron", 1, (255, 0, 0))
    board.blit(text, (10, 550))

def displayNum(value):
    text1 = font1.render(str(valueToPlace), 1, (0, 0, 0))
    board.blit(text1, (x * sizeOfCell + 15, y * sizeOfCell + 15))    

def checkValid(grid, row, col, num):
    # Check if the number is already in the row
    for i in range(9):
        if grid[row][i] == num:
            return False
    # Check if the number is already in the column
    for i in range(9):
        if grid[i][col] == num:
            return False
    # Check if the number is already in the 3x3 subgrid
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True










run = True
flag1 = 0
flag2 = 0

createBoard()

while run:
    board.fill((255, 255, 255))


    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # if the window is closed, exit the loop
        if event.type == pygame.QUIT:
            run = False  
        # Get the mouse position to insert number    
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            getCoords(pos)
        # Get the number to be inserted if key pressed    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1    
            # Check if the number pressed is between 1 and 9
            if event.key == pygame.K_1:
                valueToPlace = 1
            if event.key == pygame.K_2:
                valueToPlace = 2    
            if event.key == pygame.K_3:
                valueToPlace = 3
            if event.key == pygame.K_4:
                valueToPlace = 4
            if event.key == pygame.K_5:
                valueToPlace = 5
            if event.key == pygame.K_6:
                valueToPlace = 6 
            if event.key == pygame.K_7:
                valueToPlace = 7
            if event.key == pygame.K_8:
                valueToPlace = 8
            if event.key == pygame.K_9:
                valueToPlace = 9  
            # if the number is zero, raise an error
            if event.key == pygame.K_0:
                raiseError(1)
               
    createBoard()  
    if flag1 == 1:
        highlightCell()     
    if flag2 == 1:      
        # need to implement the backtracking algorithm here
        continue 
    if valueToPlace != 0:            
        displayNum(valueToPlace)
   
        if checkValid(grid, int(x), int(y), valueToPlace) == True:
            grid[int(x)][int(y)]= valueToPlace
            flag1 = 0
        else:
            grid[int(x)][int(y)]= 0
            raiseError(3)   
        valueToPlace = 0    
      
     

    # Update window
    pygame.display.update()  

# Quit pygame window    
pygame.quit()


