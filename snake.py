import math
import random
import pygame
pygame.init()
width = 500
height = 500
board = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
class snake:
    def __init__(self, color,x,y):
        self.color = color
        self.List = []
        self.len = 1
        self.x = x
        self.y = y
    def move(self,event, prev_key):
        x_diff = 0
        y_diff = 0
        if event.key == pygame.K_LEFT and prev_key == pygame.K_RIGHT:
            exec = prev_key
            x_diff+=10
        elif event.key == pygame.K_LEFT:
            exec = event.key
            x_diff-=10
        elif event.key == pygame.K_RIGHT and prev_key == pygame.K_LEFT:
            exec = prev_key
            x_diff-=10
        elif event.key == pygame.K_RIGHT:
            exec = event.key
            x_diff+=10
        elif event.key == pygame.K_UP and prev_key == pygame.K_DOWN:
            exec = prev_key
            y_diff+=10
        elif event.key == pygame.K_UP:
            exec = event.key
            y_diff-=10
        elif event.key == pygame.K_DOWN and prev_key == pygame.K_UP:
            exec = prev_key
            y_diff-=10
        elif event.key == pygame.K_DOWN:
            exec = event.key
            y_diff+=10

        return [x_diff, y_diff, exec]
    def dead(self):
        if self.x > width or self.x < 0 or self.y > height or self.y < 0:
            return True
        else:
            return False
    def eating_itself(self):
        if [self.x,self.y] in self.List[:-1]:
            return True
        return False
    def draw(self):
        head = 0
        for block in self.List:
            pygame.draw.rect(board, self.color, [block[0], block[1], 10,10])
            if head == len(self.List)-1:
                pygame.draw.circle(board, (0,0,0),(block[0]+3,block[1]+5),2 )
                pygame.draw.circle(board, (0, 0, 0), (block[0] + 6, block[1] + 5), 2)
            head+=1
def food(snake):
    flag = True
    while flag:
        foodx = (random.randrange(0,width-10)//10)*10
        foody = (random.randrange(0,height-10)//10)*10
        if [foodx,foody] in snake.List:
            flag=True
        else:
            flag=False
    return [foodx,foody]


def main():
    snake1 = snake((0,255,0), 220,220)
    game = True
    snake1.List.append([220,220])
    #snake length=1 and list=[]
    curr_food = food(snake1)
    gameOver=False
    moved=[0,0]
    exec = ""
    while game:
        while gameOver:
            font = pygame.font.SysFont('Arial',40)
            txt = "Game Over! Score: "+ str(snake1.len-1)
            text = font.render(txt, 1, [213,50,80])
            board.blit(text, [5,240])
            snake1.draw()
            pygame.display.update()
            game = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game=False
            if event.type == pygame.KEYDOWN:
                moved = snake1.move(event, exec)
                exec = moved[2]
        snake1.y += moved[1]
        snake1.x += moved[0]
        if snake1.dead():
            #"dead"
            gameOver=True
        if snake1.eating_itself():
            #"eating itself"
            gameOver=True
        board.fill([255,255,102])
        pygame.draw.line(board, (0,0,0), (0,0), (0,498), 2)
        pygame.draw.line(board, (0, 0, 0), (0, 0), (498, 0), 2)
        pygame.draw.line(board, (0, 0, 0), (498, 0), (498, 498), 2)
        pygame.draw.line(board, (0, 0, 0), (0, 498), (498, 498), 2)
        pygame.draw.rect(board, (50, 153, 213), [curr_food[0], curr_food[1], 10, 10])
        snake1.draw()

        pygame.display.update()
        if [snake1.x,snake1.y]==curr_food:
            snake1.len += 1
            curr_food = food(snake1)
        snake1.List.append([snake1.x, snake1.y])
        if len(snake1.List)>snake1.len:
            del snake1.List[0]
        clock.tick(15)
main()