import random

FILL_RATE = 0.55


def count_filled(matrix):
    count = 0.0
    for row in matrix:
        count += row.count("1")
    return count

# Заполняем матрицу нулями
size = int(input("Введите размер матрицы: "))
matrix = []
for i in range(size):
    matrix.append(["0"] * size)

# print(matrix)

# Добавляем в матрицу единички, пока она не заполнится до определенного уровня
# ОЧЕНЬ МЕДЛЕННО. На 800 уже валится намертво
while (count_filled(matrix) / (size * size)) < FILL_RATE:
    row = random.randint(0, size - 1)
    col = random.randint(0, size - 1)
    matrix[row][col] = "1"

# print(matrix)

# Выводим матрицу в файл, который потом можно скормить hk
with open("in", "w") as outfile:
    print(str(size) + " " + str(size), file=outfile)
    for string in matrix:
        print(" ".join(string), file=outfile)

print("Матрица сгенерирована, результат в файле in")