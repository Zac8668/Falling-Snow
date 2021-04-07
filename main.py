import pygame, sys, random

WHITE = pygame.Color(220, 220, 220)
BLACK = pygame.Color(0, 0, 0)

class FallingSnow:
    def __init__(self):
        pygame.init()
        
        self.screen_res = [512,512]
        self.clock = pygame.time.Clock()
        self.fps = 0
        self.screen = pygame.display.set_mode(self.screen_res)
        
        self.pa = pygame.PixelArray(self.screen)
        
        self.snowflakes = []
        
    def add_snow(self, pos):
        try:
            self.snowflakes.append(pos)
            self.pa[pos[0], pos[1]] = WHITE
        except IndexError:
            print(pos)
        
    def tick(self):
        x = random.randint(1, self.screen_res[0] - 1)
        y = random.randint(0, 4)
        
        self.add_snow([x, y])
        
        for idx, snow in enumerate(self.snowflakes):
            if self.pa[snow[0], snow[1]] == self.screen.map_rgb(WHITE) and snow[1] + 1 < self.screen_res[1]:
                if self.pa[snow[0], snow[1] + 1] == self.screen.map_rgb(BLACK):
                    self.pa[snow[0], snow[1]] = BLACK
                    self.pa[snow[0], snow[1] + 1] = WHITE
                    self.snowflakes[idx] = [snow[0], snow[1] + 1]
                    
            else:
                self.snowflakes.pop(idx)

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
            self.tick()
            
            pygame.display.flip()
            self.clock.tick(self.fps)
            
render = FallingSnow()
render.mainloop()
            