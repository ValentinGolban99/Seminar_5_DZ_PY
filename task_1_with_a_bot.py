from random import randint
def move_bot():
    us_1 = randint(0, 28)
    return us_1


user_1 = str(input('Введите имя: '))
candies = 202
move_counter = 0
number_progress = 0
while candies > 0:
    if move_counter == 0:
        us_1 = int(input(f"{user_1} возьмите конфеты(не более 28): "))
        if us_1 <= 28:
            number_progress += 1
            move_counter += 1
            candies -= us_1
            print(f"Осталось {candies} конфет.")
        else:
            print(f"{user_1} введите число меньше или равное 28!")
            move_counter = 0
        if candies == 0:
            print(f"Победил: {user_1}. Игра закончена за {number_progress} хода(ов).")
    elif move_counter == 1:
        us_2 = move_bot()
        if us_2 <= 28:
            print(f"Bot взял: {us_2} конфет.")
            number_progress += 1
            move_counter -= 1
            candies -= us_2
            print(f"Осталось {candies} конфет.")
        else:
            print(f"Bot введите число меньше или равное 28!")
            move_counter = 1
        if candies == 0:
            print(f"Победил: Bot. Игра закончена за {number_progress} хода(ов).")
