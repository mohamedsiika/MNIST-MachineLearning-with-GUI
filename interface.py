import pygame
from main import predict_image
black = [0, 0, 0]
purple=[68,1,84]
yellow=[248,230,33]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
draw_on = False
last_pos = (0, 0)
color = (255, 128, 0)
radius = 13
font_size = 500

#image size
width = 640
height = 640
pygame.init()
screen = pygame.display.set_mode((width*2, height))
screen.fill(white)

pygame.display.set_caption("digit guess")

pygame.font.init()


def crope(orginal):
    cropped = pygame.Surface((width-5, height-5))
    cropped.blit(orginal, (0, 0))
    return cropped


def roundline(srf, color, start, end, radius=1):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(srf, color, (x, y), radius)

def showanswer(pred):
    if pred==[0]:
        image = pygame.image.load(r'numbers\0.png')

    elif pred==[1]:
        image = pygame.image.load(r'numbers\1.png')

    elif pred==[2]:
        image = pygame.image.load(r'numbers\2.png')

    elif pred==[3]:
        image = pygame.image.load(r'numbers\3.png')

    elif pred == [4]:
        image = pygame.image.load(r'numbers\4.png')

    elif pred==[5]:
        image = pygame.image.load(r'numbers\5.png')

    elif pred==[6]:
        image = pygame.image.load(r'numbers\6.png')

    elif pred==[7]:
        image = pygame.image.load(r'numbers\7.png')

    elif pred==[8]:
        image = pygame.image.load(r'numbers\8.png')

    elif pred==[9]:
        image = pygame.image.load(r'numbers\9.png')

    screen.blit(image, (width + 2, 0))

running= True
drawing= False




while running:
    pygame.draw.line(screen, red, [width, 0], [width,height ], 8)

    for event in pygame.event.get():
         if event.type==pygame.QUIT:
             running=False

         if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
             screen.fill(white)
         if (event.type==pygame.MOUSEBUTTONDOWN and event.button != 3):
             pygame.draw.circle(screen,black, event.pos, radius)
             drawing=True
         if event.type==pygame.MOUSEBUTTONUP:
                drawing=False
                fname = "out.png"
                img = crope(screen)
                pygame.image.save(img, fname)
                pred=predict_image("out.png")
                showanswer(pred)

         if event.type==pygame.MOUSEMOTION:
             if drawing:
                 pygame.draw.circle(screen, black, event.pos, radius)
                 roundline(screen,black, event.pos, last_pos, radius)
             last_pos = event.pos





    pygame.display.update()

