import random

my_list = [random.randint(-100, 100) for i in range(30)]
print(my_list)
max_value = max(my_list)
print("Співпали: ")
for i in range(len(my_list) - 1):
    print(my_list[i], my_list[i + 1]) if my_list[i] < 0 and my_list[i + 1] < 0 else None
print("Максимальен значення в списку: ")
print(max_value)
print("Індекс макимального значення в списку: ")
print(my_list.index(max_value))
