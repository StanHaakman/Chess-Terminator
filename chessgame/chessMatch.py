import numpy as np
import pygame

from .chessBoard import Board

class Match:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        self.running = True
        
        # game board is a matrix of pieces and empty spaces
        self.board = Board()
        self.board.create_board()
        self.board.add_pieces()
        
    def play(self):
        while self.running:
            # Pygame background fill
            self.screen.fill((255, 255, 255))
            
            # All key presses recorded
            keys = pygame.key.get_pressed()
            
            # All events recorded
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            pygame.display.update()

    def swap(self, loc_a, loc_b):
        if self.board[loc_b[0]][loc_b[1]] != 0:
            return -1
        self.board[loc_a[0]][loc_a[1]], self.board[loc_b[0]][loc_b[1]] = self.board[loc_b[0]][loc_b[1]], self.board[loc_a[0]][loc_a[1]]

    def destroy(self, loc_a, loc_b):
        if self.board[loc_a[0]][loc_a[1]] == 0 or self.board[loc_b[0]][loc_b[1]] == 0:
            return -1
        self.board[loc_a[0]][loc_a[1]], self.board[loc_b[0]][loc_b[1]] = 0, self.board[loc_a[0]][loc_a[1]]

    def set_piece(self, piece, location):
        # TODO: Place the piece on the location in the matrix
        return -1
