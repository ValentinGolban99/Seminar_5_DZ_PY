# Создайте программу для игры в ""Крестики-нолики"".
def print_tabl():
    print(ryad_1)
    print(ryad_2)
    print(ryad_3)

ryad_1 = [1, 2, 3]
ryad_2 = [4, 5, 6]
ryad_3 = [7, 8, 9]

user_1 = str(input('Игрок 1: '))
user_2 = str(input('Игрок 2: '))
print_tabl()

move_counter = 0
win = False
while not win:
    if move_counter == 0:
        us_1 = int(input(f"{user_1} введите куда поставить крестик: "))
        if us_1 >= 1 and us_1 <= 3:
            ryad_1.pop(us_1 - 1)
            ryad_1.insert(us_1 - 1, 'X')
            print_tabl()
        elif us_1 >= 4 and us_1 <= 6:
            ryad_2.pop(us_1 - 4)
            ryad_2.insert(us_1 - 4, 'X')
            print_tabl()
        elif us_1 >= 7 and us_1 <= 9:
            ryad_3.pop(us_1 - 7)
            ryad_3.insert(us_1 - 7, 'X')
            print_tabl()
        move_counter += 1
    elif move_counter == 1:
        us_2 = int(input(f"{user_2} введите куда поставить нолик: "))
        if us_2 >= 1 and us_2 <= 3:
            ryad_1.pop(us_2 - 1)
            ryad_1.insert(us_2 - 1, 'O')
            print_tabl()
        elif us_2 >= 4 and us_2 <= 6:
            ryad_2.pop(us_2 - 4)
            ryad_2.insert(us_2 - 4, 'O')
            print_tabl()
        elif us_2 >= 7 and us_2 <= 9:
            ryad_3.pop(us_2 - 7)
            ryad_3.insert(us_2 - 7, 'O')
            print_tabl()
        move_counter -= 1

print_tabl()



