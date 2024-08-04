import pygame
import random

# Инициализация всех модулей Pygame
pygame.init()

# Определение цветов в формате RGB
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Установка размеров дисплея
dis_width = 800
dis_height = 600

# Создание дисплея с заданными размерами
dis = pygame.display.set_mode((dis_width, dis_height))
# Установка заголовка окна игры
pygame.display.set_caption('Snake Game')

# Инициализация часов для контроля скорости игры
clock = pygame.time.Clock()
snake_block = 10  # Размер блока змейки
snake_speed = 15  # Скорость змейки

# Установка стиля и размера шрифта для текста
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Функция отображения счета
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Функция рисования змейки
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Функция отображения сообщения на экране
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Основной игровой цикл
def gameLoop():
    game_over = False  # Флаг окончания игры
    game_close = False  # Флаг завершения текущей игры

    x1 = dis_width / 2  # Начальная координата x головы змейки
    y1 = dis_height / 2  # Начальная координата y головы змейки

    x1_change = 0  # Изменение координаты x
    y1_change = 0  # Изменение координаты y

    snake_List = []  # Список для хранения координат тела змейки
    Length_of_snake = 1  # Начальная длина змейки

    # Генерация случайных координат для еды
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Пока игра не окончена
    while not game_over:

        while game_close == True:
            dis.fill(blue)  # Заполнение экрана синим цветом
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            # Обработка событий при завершении игры
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Завершение игры при нажатии Q
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Перезапуск игры при нажатии C
                        gameLoop()

        # Обработка событий во время игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Завершение игры при закрытии окна
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Движение влево
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:  # Движение вправо
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:  # Движение вверх
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:  # Движение вниз
                    y1_change = snake_block
                    x1_change = 0

        # Проверка на выход змейки за границы экрана
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)  # Заполнение экрана синим цветом
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])  # Рисование еды
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение змейки с самой собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Проверка на поедание еды змейкой
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)  # Управление скоростью игры

    pygame.quit()  # Завершение работы Pygame
    quit()  # Выход из программы

# Запуск игрового цикла
gameLoop()