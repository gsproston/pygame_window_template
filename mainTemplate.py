import pygame
import windowTemplate as window

# global constants
FPS = 60

# global variables
bShutdown = False

# returns true if this takes a turn
def processClick():
  x = pygame.mouse.get_pos()[0]
  y = pygame.mouse.get_pos()[1]
  return False
    
def listenOnEvents():
  global bShutdown, bWhiteTurn
  for event in pygame.event.get(): #runs when an event occurs
    if event.type == pygame.QUIT: #quit called
      bShutdown = True #end loop
    elif event.type == pygame.MOUSEBUTTONDOWN: #mouse clicked
      processClick()
    elif event.type == pygame.KEYDOWN: #key has been pressed
      if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        bShutdown = True #end loop  
    
if __name__ == "__main__":
  pygame.init()
  window.init()
  clock = pygame.time.Clock()

  #main game loop
  while (not bShutdown):
    listenOnEvents()
    clock.tick(FPS) #update x times a second, determines FPS

  #main loop ends, exit
  pygame.quit()