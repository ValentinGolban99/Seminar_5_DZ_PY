
def move_us(user, candies):
    us = int(input(f"{user} возьмите конфеты(не более 28): "))
    if us <= 28:
        candies -= us
        print(f"Осталось {candies} конфет.")
    if candies <= 0:
        print(f"Победил: {user}")
    else:
        return candies

    

user_1 = str(input('Игрок 1: '))
user_2 = str(input('Игрок 2: '))
candies = 150

while candies >= 0:
    candies_one = move_us(user_1, candies)
    candies = move_us(user_2, candies_one)

# Тут я как то недомудрил и сам себя успел несколько раз позапутывать.
# Не совсем правильно работающий код. Решил пока оставить.


