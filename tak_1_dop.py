
def move_us_1(candies, move_counter = 0):
    if candies != 0:
        us_1 = int(input(f"{user_1} возьмите конфеты(не более 28): "))
        if us_1 <= 28:
            move_counter += 1
            candies -= us_1
            print(f"Осталось {candies} конфет.")
            if candies == 0:
                print(f"Победил: {user_1}")


def move_us_2(candies, move_counter = 0):
    if candies != 0:
        us_1 = int(input(f"{user_1} возьмите конфеты(не более 28): "))
        if us_1 <= 28:
            move_counter += 1
            candies -= us_1
            print(f"Осталось {candies} конфет.")
            if candies == 0:
                print(f"Победил: {user_1}")

user_1 = str(input('Игрок 1: '))
user_2 = str(input('Игрок 2: '))
candies = 2021
move_counter = 0



print(f"Игра закончена за {move_counter} хода(ов).")


