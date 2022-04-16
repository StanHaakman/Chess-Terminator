import pygame

from chessgame.chessMatch import Match 

class ChessGame():
    def __init__(self, title:str = "Chess Terminator") -> None:
        pygame.init()
        pygame.font.init()
        
        self.title = title
        self.title_font = pygame.font.SysFont("Arial", 26)
        
        self.screen = pygame.display.set_mode((400,400))
        pygame.display.set_caption(self.title)
        
        self.running = True
        
        while self.running:
            
            self.screen.fill((255,255,255))
            title_label = self.title_font.render('Welcome to Chess Terminator', True, (3, 3, 3))
            self.screen.blit(title_label, (400 / 2 - title_label.get_width() / 2, 400 / 2 - title_label.get_height()))
            
            # All key presses recorded
            keys = pygame.key.get_pressed()
            
            # All events recorded
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    match = Match()
                    
                    match.play()
                    
            
            pygame.display.update()