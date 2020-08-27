import pygame
pygame.init()
FPS = 60
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 50)
text = font.render('image', False, (255, 255, 0))
image = pygame.Surface((text.get_width(), text.get_height()))
pygame.draw.rect(image, (0, 0, 255), (1, 1, *text.get_size()))
image.blit(text, (1, 1))
pos = (1, 1)
while True:
    image = pygame.transform.rotate(image, 0.9)
    screen.blit(image, pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(FPS)
    pygame.display.flip()


