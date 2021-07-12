print("Введіть строчку: ")
str = input()
str_out = list(str)
digit = []
chars = []
for i in str_out:
    if i.isdigit():
        digit.append(int(i))
    else:
        chars.append(i)
str_out = ''.join(chars)
print("Змінена строчка: " + str_out)
print("Створений список чисел: ", digit)

print("Змінена строчка (Верхній вегістр): ", str_out.title())

digits = []
index = 0
for i in digit:
    d_max = max(digit)
    if d_max == i:
        index += 1
        continue
    else:
        res = i**index
        digits.append(res)
    index += 1

if not digits:
    print("Список чисел пустий")
else:
    print("Максимальний елемент списку: ", d_max)
print("Отриманий список: ", digits)
