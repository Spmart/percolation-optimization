import random

FILL_RATE = 0.55

# Заполняем матрицу нулями
size = int(input("Введите размер матрицы: "))
matrix = []
for i in range(size):
    matrix.append(["0"] * size)

# print(matrix)

# Добавляем в матрицу единички, пока она не заполнится до определенного уровня
filled = 0
while (filled / (size * size)) < FILL_RATE:
    row = random.randint(0, size - 1)
    col = random.randint(0, size - 1)
    if matrix[row][col] == "0":
        matrix[row][col] = "1"
        filled+=1

# print(matrix)

# Выводим матрицу в файл, который потом можно скормить hk
with open("in", "w") as outfile:
    print(str(size) + " " + str(size), file=outfile)
    for string in matrix:
        print(" ".join(string), file=outfile)

print("Матрица сгенерирована, результат в файле in")
