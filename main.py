import random

import pygame

pygame.init()

black = (0,0,0)
snake_col = (0,255,0)
red = (255,0,0)
white = (255,255,255)

dis_width = 640
dis_height = 480

display = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Loh kakoita verde")
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

font_text = pygame.font.SysFont('Arial',26,bold=True,italic=True)
score_font = pygame.font.SysFont('Arial',24,bold=True)

def Your_Score(score):
    value = score_font.render("Your score: "+ str(score), True, white)
    display.blit(value,[50,50])
def message(color,msg):
    mesg = font_text.render(msg,True,color)
    display.blit(mesg,[dis_width/2-100, dis_height/3])
def game_loop():
    game_over = False
    game_close = False
    x1 = dis_width/2
    y1 = dis_height/2
    x_change = 0
    y_change = 0
    snake_list = []
    snake_len = 1

    foodx = round(random.randrange(0,dis_width - snake_block)/10.0) * 10.0
    foody = round(random.randrange(0,dis_height - snake_block)/10.0) * 10.0

    while not game_over:
        while game_close == True:
            display.fill(black)
            message(white,"Game was stopped")
            Your_Score(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_KP_ENTER:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change -= snake_block
                    x_change = 0
                if event.key == pygame.K_a:
                    x_change -= snake_block
                    y_change = 0
                if event.key == pygame.K_s:
                    y_change += snake_block
                    x_change = 0
                if event.key == pygame.K_d:
                    x_change += snake_block
                    y_change = 0
            if event.type == pygame.QUIT:
                game_over = True
        if x1 < 0 or x1 >= dis_width or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x_change
        y1 += y_change
        display.fill(black)
        pygame.draw.rect(display,red,[foodx,foody,snake_block,snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)

        snake_list.append(snake_Head)
        if len(snake_list) > snake_len:
            del snake_list[0]
        for x in snake_list:
            pygame.draw.rect(display, snake_col, [x[0],x[1],snake_block,snake_block])
        Your_Score(snake_len - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_len += 1

        #pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()
game_loop()