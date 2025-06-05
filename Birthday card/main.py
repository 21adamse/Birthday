import pygame
import time

pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")
pygame.display.update()
image1=pygame.image.load("Images/birthdaybg.jpg")
image2=pygame.image.load("Images/cake.jpg")
image3=pygame.image.load("Images/historycake.jpg")

#Resizing images

image1=pygame.transform.scale(image1,(WIDTH,HEIGHT))
image2=pygame.transform.scale(image2,(WIDTH,HEIGHT))
image3=pygame.transform.scale(image3,(WIDTH,HEIGHT))

#Selecting font and size
font1=pygame.font.SysFont("Arial",50)
font2=pygame.font.SysFont("Calibre",40)
font3=pygame.font.SysFont("Times New Roman",30)

text1=font1.render("to an amazing",True,("red"))
text2=font1.render("grandpa",True,"red")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.blit(image1,(0,0))
    screen.blit(text1,(100,100))
    screen.blit(text2,(100,150))
    pygame.display.update()
    time.sleep(3)

    screen.blit(image2,(0,0))
    pygame.display.update()
    time.sleep(3)

    screen.blit(image3,(0,0))
    pygame.display.update()
    time.sleep(3)