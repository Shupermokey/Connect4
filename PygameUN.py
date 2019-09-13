import numpy as np 
import pygame
import sys
import os
import math

ROW = 6
COLUMN = 7 
purple = (128,0,128)
rec_size = 50



def create_board():
	board = np.zeros((ROW,COLUMN))
	return board

def drop_piece(board,row,col, huuuuh):
	board[row][col]=huuuuh


def is_valid_location(board, col):
	return board[ROW-1][col] ==0

def get_net_open_row(board, col):
	for r in range(ROW):
		if board[r][col] == 0:
			return r

def print_board(board):
	print(np.flip(board,0))

def winning_move(board, huuuuh):
	for c in range(COLUMN-3):
		for r in range(ROW):
			if board[r][c] == huuuuh and board[r][c+1]==huuuuh and board[r][c+2] == huuuuh and board[r][c+3] == huuuuh:
				return True

	for c in range(COLUMN):
		for r in range(ROW-3):
			if board[r][c] == huuuuh and board[r+1][c]==huuuuh and board[r+2][c] == huuuuh and board[r+3][c] == huuuuh:
				return True

	for c in range(COLUMN-3):
		for r in range(ROW-3):
			if board[r][c] == huuuuh and board[r+1][c+1]==huuuuh and board[r+2][c+2] == huuuuh and board[r+3][c+3] == huuuuh:
				return True
	for c in range(COLUMN-3):
		for r in range(3,ROW):
			if board[r][c] == huuuuh and board[r-1][c+1]==huuuuh and board[r-2][c+2] == huuuuh and board[r-3][c+3] == huuuuh:
				return True



def draw_board(board):
	for c in range(COLUMN):
		for r in range(ROW):
			pygame.draw.rect(screen,(0,150,125), (c*S_S, r*S_S+S_S, S_S, S_S))
			pygame.draw.circle(screen, (0,0,0), (int(c*S_S+S_S/2), int(r*S_S+S_S+S_S/2)), rad)

	for c in range(COLUMN):
		for r in range(ROW):
			if board[r][c] == 1:
				pygame.draw.circle(screen, (255,0,0), (int(c*S_S+S_S/2), height- int(r*S_S+S_S/2)) ,rad)
			elif board[r][c] ==2:
				pygame.draw.circle(screen, (255,255,0), (int(c*S_S+S_S/2),height - int(r*S_S+S_S/2)) ,rad)
	pygame.display.update()

board = create_board()
print(board)
game_over = False
turn = 0

pygame.init()

S_S = 100
rad = int(S_S/2 - 5)

width = COLUMN * S_S
height = (ROW+1)*S_S

size = (width, height)



screen = pygame.display.set_mode(size)
screen.fill(purple)
draw_board(board)

pygame.display.update()
myfont = pygame.font.SysFont("monospace",75)


while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen,(0,0,0),(0,0, width,S_S))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen,(255,0,0),(posx, int(S_S/2)), rad)
			else:
				pygame.draw.circle(screen,(255,255,0),(posx, int(S_S/2)), rad)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen,(0,0,0),(0,0, width,S_S))
			#print(event.pos)
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/S_S))

				if is_valid_location(board, col):
					row = get_net_open_row(board,col)
					drop_piece(board, row, col, 1)
					if winning_move(board,1):
						label = myfont.render("Player 1 WINS!!",1,(255,0,0))
						screen.blit(label,(40,10))
						game_over = True

			else: 
				posx = event.pos[0]
				col = int(math.floor(posx/S_S))

				if is_valid_location(board, col):
					row = get_net_open_row(board,col)
					drop_piece(board, row, col, 2)
					if winning_move(board,2):
						label = myfont.render("Player 2 WINS!!",1,(255,0,0))
						screen.blit(label,(40,10))
						game_over = True

			draw_board(board)

			turn = turn +1
			turn = turn % 2
			if game_over:
				pygame.time.wait(3000)





	





