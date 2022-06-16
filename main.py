import sys, pygame as pyg
from pygame.locals import *
from images import *
import time

#初期設定
XO = 'x'
winner = None
draw = False
width = 600
height = 600
black = (105, 105, 105)
line_color = (255,140,0)

#３目並べボード
board = [[None]*3, [None]*3, [None]*3]

#pygameウインドーウ設定
pyg.init()
fps = 30
CLOCK = pyg.time.Clock()
screen = pyg.display.set_mode((width, height+100),0,32)
pyg.display.set_caption("３目並べ")

#画像ロード、サイズ設定
opening = pyg.image.load('images/tictactoe.png')
x_img = pyg.image.load('images/x.png')
o_img = pyg.image.load('images/o.png')
x_img = pyg.transform.scale(x_img, (100,100))
o_img = pyg.transform.scale(o_img, (100,100))
opening = pyg.transform.scale(opening, (width, (height+100)))

def game_opening():
    screen.blit(opening,(0,0))
    pyg.display.update()
    time.sleep(1)
    screen.fill(black)
    pyg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)
    pyg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)
    pyg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
    pyg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)
    draw_status()

def draw_status():
    global draw
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " Win!"
    if draw:
        message = 'Draw!'
    font = pyg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 610, 500, 80))
    text_rect = text.get_rect(center=(width/2, 700-50))
    screen.blit(text, text_rect)
    pyg.display.update()

def check_win():
    global board, winner, draw
    for row in range (0,3):
        if ((board [row][0] == board[row][1] == board[row][2]) and(board [row][0] is not None)):
            winner = board[row][0]
            break

    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            winner = board[0][col]
            break

    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None):
        winner = board[0][0]

    if (board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None):
        winner = board[0][2]

    if(all([all(row) for row in board]) and winner is None ):
        draw = True
    draw_status()

def drawXO(row,col):
    global board,XO
    if row==1:
        posx = 30
    if row==2:
        posx = width/3 + 30
    if row==3:
        posx = width/3*2 + 30

    if col==1:
        posy = 30
    if col==2:
        posy = (height)/3 + 30
    if col==3:
        posy = (height)/3*2 + 30
    board[row-1][col-1] = XO
    if(XO == 'x'):
        screen.blit(x_img,(posy,posx))
        XO= 'o'
    else:
        screen.blit(o_img,(posy,posx))
        XO= 'x'
    pyg.display.update()

def userClick():
    #get coordinates of mouse click
    x,y = pyg.mouse.get_pos()

    #get column of mouse click (1-3)
    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None

    #get row of mouse click (1-3)
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
    #print(row,col)

    if(row and col and board[row-1][col-1] is None):
        global XO

        #draw the x or o on screen
        drawXO(row,col)
        check_win()

def reset_game():
    global TTT, winner,XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner = None
    board = [[None]*3,[None]*3,[None]*3]

game_opening()
#永久ゲームロープ
while(True):
    for event in pyg.event.get():
        if event.type == QUIT:
            pyg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            userClick()
            if(winner or draw):
                reset_game()

    pyg.display.update()
    CLOCK.tick(fps)

