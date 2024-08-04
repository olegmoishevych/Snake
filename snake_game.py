import pygame, random, time
# Импортируем необходимые библиотеки: pygame для игры, random для генерации случайных чисел и time для пауз.

pygame.init()
# Инициализация всех модулей Pygame.

s, f, b = pygame.display.set_mode([400, 400]), lambda: (random.randint(0, 39) * 10, random.randint(0, 39) * 10), [(200, 200)]
# s - создаем окно размером 400x400 пикселей.
# f - lambda-функция для генерации случайных координат пищи, кратных 10.
# b - начальное положение змейки, список с одним элементом - координатами головы (200, 200).

d, a = (10, 0), f()
# d - направление движения змейки (вправо).
# a - начальная позиция пищи, сгенерированная функцией f().

while 1:
    s.fill((0, 0, 0))
    # Заполняем экран черным цветом.

    for e in pygame.event.get():
        if e.type == pygame.QUIT: exit()
        # Если событие - закрытие окна, то выходим из программы.

        if e.type == pygame.KEYDOWN:
            # Если нажата клавиша, меняем направление движения змейки в зависимости от нажатой клавиши.
            d = {(pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT)[i]: ((0, -10), (0, 10), (10, 0), (-10, 0))[i] for i in range(4)}.get(e.key, d)
            # d принимает новое значение в зависимости от нажатой клавиши: вверх, вниз, вправо или влево.

    b = [((b[0][0] + d[0]) % 400, (b[0][1] + d[1]) % 400)] + b
    # Обновляем позицию головы змейки в направлении d и добавляем ее в начало списка b.
    # Если змейка выходит за границы экрана, она появляется с противоположной стороны благодаря % 400.

    if b[0] == a: a = f()
    # Если голова змейки попадает на координаты пищи, генерируем новую еду.

    else: b.pop()
    # Если змейка не съела еду, удаляем последний элемент списка b (хвост змейки).

    if b[0] in b[1:]: break
    # Если голова змейки сталкивается с ее телом, завершаем игру.

    for p in b: pygame.draw.rect(s, (0, 255, 0), (*p, 10, 10))
    # Рисуем каждый сегмент тела змейки зеленым цветом.

    pygame.draw.rect(s, (255, 0, 0), (*a, 10, 10))
    # Рисуем еду красным цветом.

    pygame.display.flip()
    # Обновляем экран для отображения изменений.

    time.sleep(0.1)
    # Пауза на 0.1 секунды для управления скоростью игры.