import pygame
import random
from classes.cell import Cell
from classes.snakeLinkedList import SnakeLinkedList

pygame.init() #khỏi tạo game

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 400
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Linked List')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("None", 25)
score_font = pygame.font.SysFont("None", 35)


# our snake consist of block(x,y) of the linked_list I have make
def our_snake(snake_block, snake_list):
    temp = snake_list.head_cell
    while temp is not None:
        if temp is snake_list.head_cell:
            pygame.draw.rect(dis, red, [temp.Xcord, temp.Ycord, snake_block, snake_block])
        else:
            pygame.draw.rect(dis, green, [temp.Xcord, temp.Ycord, snake_block, snake_block])
        temp = temp.next_cell


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    mes_x = int(dis_width / 6)
    mes_y = int(dis_height / 3)
    dis.blit(mesg, [mes_x, mes_y])


# Keep the game run until you lose
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = SnakeLinkedList() #Khởi tạo con rắn
    Length_of_snake = 1 #Chiều dài ban đầu của rắn

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        # while game is over choose whether play again or quit
        while game_close == True:
            dis.fill(black)
            message("Enter C to play again, Enter Q to exit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        #cắn tường sẽ chết
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # thay đổi vị trí con rắn dựa vào key nhấn
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # vẽ thức ăn
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        
        # thêm vào
        snake_cell = Cell(x1, y1)
        snake_List.at_end(snake_cell.Xcord, snake_cell.Ycord)

        if snake_List.count_cell() > Length_of_snake:
            snake_List.del_at_end()

        # tạo cái đầu
        our_snake(snake_block, snake_List)

        # render tất cả
        pygame.display.update()

        # Ăn thức ăn sẽ dài thêm 1 cục
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            # keep trak of the snake lenght
            snake_List.at_end(snake_cell.Xcord, snake_cell.Ycord)
            Length_of_snake += 1

        # Frame per second
        clock.tick(snake_speed)
    pygame.quit()
    quit()

if __name__ == '__main__':
        gameLoop()