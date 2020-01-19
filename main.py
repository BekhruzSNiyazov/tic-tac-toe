import pygame
import time

pygame.init()

win = pygame.display.set_mode((620, 620))

pygame.display.set_caption("Tic Tac Toe by Bekhruz S. Niyazov")

def draw(surface, letter, position):
    if position == 1:
        if letter == "X":
            pygame.draw.line(surface, (0, 0, 255), (50, 50), (160, 160), 10)
            pygame.draw.line(surface, (0, 0, 255), (160, 50), (50, 160), 10)
        else:
            pygame.draw.circle(surface, (255, 0, 0), (100, 100), 80, 7)
    if position == 4:
        if letter == "X":
            pygame.draw.line(surface, (0, 0, 255), (50, 260), (160, 370), 10)
            pygame.draw.line(surface, (0, 0, 255), (50, 370), (160, 260), 10)
        else:
            pygame.draw.circle(surface, (255, 0, 0), (100, 310), 80, 7)
    if position == 7:
        if letter == "X":
            pygame.draw.line(surface, (0, 0, 255), (50, 470), (160, 580), 10)
            pygame.draw.line(surface, (0, 0, 255), (50, 580), (160, 470), 10)
        else:
            pygame.draw.circle(surface, (255, 0, 0), (100, 520), 80, 7)
    if position == 2:
        if letter == "X":
            pygame.draw.line(surface, (0, 0, 255), (260, 50), (370, 160), 10)
            pygame.draw.line(surface, (0, 0, 255), (260, 160), (370, 50), 10)
        else:
            pygame.draw.circle(surface, (255, 0, 0), (310, 100), 80, 7)
    if position == 5:
        if letter == "X":
            pygame.draw.line(surface, (0, 0, 255), (260, 260), (370, 370), 10)
            pygame.draw.line(surface, (0, 0, 255), (260, 370), (370, 260), 10)
        else:
            pygame.draw.circle(surface, (255, 0, 0), (310, 310), 80, 7)
    if position == 8:
        if letter == "X":
            pygame.draw.line(surface, (0, 0, 255), (260, 470), (370, 580), 10)
            pygame.draw.line(surface, (0, 0, 255), (260, 580), (370, 470), 10)
        else:
            pygame.draw.circle(surface, (255, 0, 0), (310, 520), 80, 7)
    if position == 3:
        if letter == "X":
            pygame.draw.line(surface, (0, 0, 255), (470, 50), (580, 160), 10)
            pygame.draw.line(surface, (0, 0, 255), (470, 160), (580, 50), 10)
        else:
            pygame.draw.circle(surface, (255, 0, 0), (520, 100), 80, 7)
    if position == 6:
        if letter == "X":
            pygame.draw.line(surface, (0, 0, 255), (470, 260), (580, 370), 10)
            pygame.draw.line(surface, (0, 0, 255), (470, 370), (580, 260), 10)
        else:
            pygame.draw.circle(surface, (255, 0, 0), (520, 310), 80, 7)
    if position == 9:
        if letter == "X":
            pygame.draw.line(surface, (0, 0, 255), (470, 470), (580, 580), 10)
            pygame.draw.line(surface, (0, 0, 255), (470, 580), (580, 470), 10)
        else:
            pygame.draw.circle(surface, (255, 0, 0), (520, 520), 80, 7)

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    if 5 in possibleMoves:
        move = 5
        playerMove = True
        return move

    for let in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                playerMove = True
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        playerMove = True
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        playerMove = True
        return move

    playerMove = True

    return move

def insertLetter(letter, pos):
    board[pos] = letter

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def spaceIsFree(pos):
    return board[pos] == " "

def isBoardFull(board):
	if board.count(" ") < 1:
		return True
	else:
		return False

def isWinner(bo, le):
	return (bo[7] == le and bo[8] == le and bo[9] == le) or \
	(bo[4] == le and bo[5] == le and bo[6] == le) or \
	(bo[1] == le and bo[2] == le and bo[3] == le) or \
	(bo[1] == le and bo[4] == le and bo[7] == le) or \
	(bo[2] == le and bo[5] == le and bo[8] == le) or \
	(bo[3] == le and bo[6] == le and bo[9] == le) or \
	(bo[1] == le and bo[5] == le and bo[9] == le) or \
	(bo[3] == le and bo[5] == le and bo[7] == le)

def reDrawWindow(surface):
    pygame.draw.line(surface, (255, 255, 255), (210, 10), (210, 610))
    pygame.draw.line(surface, (255, 255, 255), (420, 10), (420, 610))
    pygame.draw.line(surface, (255, 255, 255), (10, 210), (610, 210))
    pygame.draw.line(surface, (255, 255, 255), (10, 420), (610, 420))
    pygame.display.update()

board = [" " for x in range(10)]
playerMove = True

while not isBoardFull(board):
    if pygame.event.get(pygame.QUIT):
        break

    events = pygame.event.get()
    for event in events:
        if event == pygame.QUIT:
            pygame.quit()

    if playerMove:
        if not isWinner(board, "O"):
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                try:
                    pos = list(pos)
                    if pos[0] < 210:
                        if pos[1] < 210:
                            if spaceIsFree(1):
                                draw(win, "X", 1)
                                insertLetter("X", 1)
                                playerMove = False
                        if pos[1] > 210 and pos[1] < 420:
                            if spaceIsFree(4):
                                draw(win, "X", 4)
                                insertLetter("X", 4)
                                playerMove = False
                        if pos[1] >= 420:
                            if spaceIsFree(7):
                                draw(win, "X", 7)
                                insertLetter("X", 7)
                                playerMove = False

                    if pos[0] > 210 and pos[0] < 420:
                        if pos[1] < 210:
                            if spaceIsFree(2):
                                draw(win, "X", 2)
                                insertLetter("X", 2)
                                playerMove = False
                        if pos[1] > 210 and pos[1] < 420:
                            if spaceIsFree(5):
                                draw(win, "X", 5)
                                insertLetter("X", 5)
                                playerMove = False
                        if pos[1] >= 420:
                            if spaceIsFree(8):
                                draw(win, "X", 8)
                                insertLetter("X", 8)
                                playerMove = False

                    if pos[0] > 420:
                        if pos[1] < 210:
                            if spaceIsFree(3):
                                draw(win, "X", 3)
                                insertLetter("X", 3)
                                playerMove = False
                        if pos[1] > 210 and pos[1] < 420:
                            if spaceIsFree(6):
                                draw(win, "X", 6)
                                insertLetter("X", 6)
                                playerMove = False
                        if pos[1] > 420:
                            if spaceIsFree(9):
                                draw(win, "X", 9)
                                insertLetter("X", 9)
                                playerMove = False
                except: pass
        else:
            l = "O"
            if board[7] == l and board[8] == l and board[9] == l:
                pygame.draw.line(win, (255, 255, 255), (20, 520), (600, 520), 5)
            if board[4] == l and board[5] == l and board[6] == l:
                pygame.draw.line(win, (255, 255, 255), (20, 310), (600, 310), 5)
            if board[1] == l and board[2] == l and board[3] == l:
                pygame.draw.line(win, (255, 255, 255), (20, 100), (600, 100), 5)
            if board[1] == l and board[4] == l and board[7] == l:
                pygame.draw.line(win, (255, 255, 255), (100, 20), (100, 600), 5)
            if board[2] == l and board[5] == l and board[8] == l:
                pygame.draw.line(win, (255, 255, 255), (310, 20), (310, 600), 5)
            if board[3] == l and board[6] == l and board[9] == l:
                pygame.draw.line(win, (255, 255, 255), (520, 20), (520, 600), 5)
            if board[1] == l and board[5] == l and board[9] == l:
                pygame.draw.line(win, (255, 255, 255), (20, 20), (600, 600), 5)
            if board[3] == l and board[5] == l and board[7] == l:
                pygame.draw.line(win, (255, 255, 255), (600, 20), (20, 600), 5)
            time.sleep(0.5)

    if not playerMove:
        if not isWinner(board, "X"):
            move = compMove()
            if move == 0:
                time.sleep(1)
                break
            else:
                draw(win, "O", move)
                insertLetter("O", move)
                playerMove = True
                computerMove = False
        else:
            l = "X"
            if board[7] == l and board[8] == l and board[9] == l:
                pygame.draw.line(win, (255, 255, 255), (20, 520), (600, 520), 5)
            if board[4] == l and board[5] == l and board[6] == l:
                pygame.draw.line(win, (255, 255, 255), (20, 310), (600, 310), 5)
            if board[1] == l and board[2] == l and board[3] == l:
                pygame.draw.line(win, (255, 255, 255), (20, 100), (600, 100), 5)
            if board[1] == l and board[4] == l and board[7] == l:
                pygame.draw.line(win, (255, 255, 255), (100, 20), (100, 600), 5)
            if board[2] == l and board[5] == l and board[8] == l:
                pygame.draw.line(win, (255, 255, 255), (310, 20), (310, 600), 5)
            if board[3] == l and board[6] == l and board[9] == l:
                pygame.draw.line(win, (255, 255, 255), (520, 20), (520, 600), 5)
            if board[1] == l and board[5] == l and board[9] == l:
                pygame.draw.line(win, (255, 255, 255), (20, 20), (600, 600), 5)
            if board[3] == l and board[5] == l and board[7] == l:
                pygame.draw.line(win, (255, 255, 255), (600, 20), (20, 600), 5)
            time.sleep(0.5)

    if isBoardFull(board):
        time.sleep(1)
        break

    reDrawWindow(win)

pygame.quit()
