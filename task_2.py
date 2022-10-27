# Создайте программу для игры в ""Крестики-нолики"".
def print_tabl():
    print(ryad_1)
    print(ryad_2)
    print(ryad_3)

def win_1():
    if ryad_1 == ['X', 'X', 'X']:
        return True
def win_2():
    if ryad_2 == ['X', 'X', 'X']:
        return True
def win_3():
    if ryad_3 == ['X', 'X', 'X']:
        return True
def win_4():
    if ryad_1[2] == ['X'] and ryad_2[1] == ['X'] and ryad_3[0] == ['X']:
        return True
def win_5():
    if ryad_1[0] == ['X'] and ryad_2[0] == ['X'] and ryad_3[0] == ['X']:
        return True
def win_6():
    if ryad_1[0] == ['X'] and ryad_2[1] == ['X'] and ryad_3[2] == ['X']:
        return True
def win_7():
    if ryad_1[1] == ['X'] and ryad_2[1] == ['X'] and ryad_3[1] == ['X']:
        return True
def win_8():
    if ryad_1[2] == ['X'] and ryad_2[2] == ['X'] and ryad_3[2] == ['X']:
        return True
def win_11():
    if ryad_1 == ['O', 'O', 'O']:
        return True
def win_22():
    if ryad_2 == ['O', 'O', 'O']:
        return True
def win_33():
    if ryad_3 == ['O', 'O', 'O']:
        return True
def win_44():
    if ryad_1[2] == ['O'] and ryad_2[1] == ['O'] and ryad_3[0] == ['O']:
        return True
def win_55():
    if ryad_1[0] == ['O'] and ryad_2[0] == ['O'] and ryad_3[0] == ['O']:
        return True
def win_66():
    if ryad_1[0] == ['O'] and ryad_2[1] == ['O'] and ryad_3[2] == ['O']:
        return True
def win_77():
    if ryad_1[1] == ['O'] and ryad_2[1] == ['O'] and ryad_3[1] == ['O']:
        return True
def win_88():
    if ryad_1[2] == ['O'] and ryad_2[2] == ['O'] and ryad_3[2] == ['O']:
        return True

ryad_1 = [1, 2, 3]
ryad_2 = [4, 5, 6]
ryad_3 = [7, 8, 9]

user_1 = str(input('Игрок 1: '))
user_2 = str(input('Игрок 2: '))
print_tabl()

move_counter = 0
win = False
while not win:
    win = win_1() or win_2() or win_3() or win_4() or win_5() or win_6() or win_7() or win_8()
    if win == True:
        print(f'Победил игрок: {user_1}')
        break
    win = win_11() or win_22() or win_33() or win_44() or win_55() or win_66() or win_77() or win_88()
    if win == True:
        print(f'Победил игрок: {user_2}')
        break
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


# Знаю что получилось очень грамоздко)))
# Уверен что можно было намного красивие и грамотнее написать код, но получилось пока только так.


