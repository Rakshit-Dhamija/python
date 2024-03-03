import random
import os
import time

WIDTH, HEIGHT = 20, 20
SNAKE, FOOD = 'S', 'F'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(' '.join(row))

def initialize_game():
    board = [[EMPTY]*WIDTH for _ in range(HEIGHT)]
    snake = [(HEIGHT//2, WIDTH//2)]
    board[snake[0][0]][snake[0][1]] = SNAKE
    food = None
    while food is None:
        nf = (random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1))
        food = nf if nf not in snake else None
    board[food[0]][food[1]] = FOOD
    return board, snake, food

def game_step(board, snake, food, direction):
    head = snake[0]
    if direction == 'up':
        new_head = (head[0]-1, head[1])
    elif direction == 'down':
        new_head = (head[0]+1, head[1])
    elif direction == 'left':
        new_head = (head[0], head[1]-1)
    elif direction == 'right':
        new_head = (head[0], head[1]+1)
    if (new_head[0] < 0 or new_head[0] >= HEIGHT or
        new_head[1] < 0 or new_head[1] >= WIDTH or
        board[new_head[0]][new_head[1]] == SNAKE):
        return None, None, None  # Game over
    if board[new_head[0]][new_head[1]] == FOOD:
        food = None
        while food is None:
            nf = (random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1))
            food = nf if nf not in snake else None
        board[food[0]][food[1]] = FOOD
    else:
        tail = snake.pop()
        board[tail[0]][tail[1]] = EMPTY
    snake.insert(0, new_head)
    board[new_head[0]][new_head[1]] = SNAKE
    return board, snake, food

def play_game():
    board, snake, food = initialize_game()
    direction = 'up'
    while True:
        os.system('clear')
        print_board(board)
        time.sleep(0.2)
        if direction == 'up':
            direction = 'up'
        elif direction == 'left':
            direction = 'left'
        elif direction == 'down':
            direction = 'down'
        elif direction == 'right':
            direction = 'right'
        board, snake, food = game_step(board, snake, food, direction)
        if board is None:
            break

play_game()
