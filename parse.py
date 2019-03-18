from PIL import Image
import hashlib

# На входе вывод из hk

# Парсим выходной файл в двумерный список.
input_matrix = []
with open("out", "r") as infile:
    time_to_read = False
    for line in infile:
        if line == " --output-- \n":
            time_to_read = True
        elif line[0:2] == "HK":
            time_to_read = False
        elif time_to_read:
            input_matrix.append(line.split())

# Проверяем, есть ли путь сверху вниз.

paths = set(input_matrix[0]) & set(input_matrix[-1])
paths.discard("0")

cluster_number = 0
if len(paths) > 0:
    print("Есть сквозной путь")
    cluster_number = str(next(iter(paths)))  # получаю ОДИН, первый элемент из сета
    print(cluster_number)


img = Image.new("RGB", (len(input_matrix), len(input_matrix)), "white")  # ТОЛЬКО ДЛЯ КВАДРАТНОЙ! Исправить.
pixels = img.load()

#md5color = hashlib.md5()
for i in range(img.size[0]):    # Для столбца
    for j in range(img.size[1]):    # Для строки
        if (input_matrix[j][i] != "0") & (input_matrix[j][i] != cluster_number):
            md5color = hashlib.md5(input_matrix[j][i].encode("utf-8"))
            #print(md5color.hexdigest()[0:6])
            pixels[i, j] = tuple(int(md5color.hexdigest()[0:6][i:i+2], 16) for i in (0, 2 ,4))
        elif input_matrix[j][i] == cluster_number:
            pixels[i, j] = (0, 0, 0)



img = img.resize((img.size[0] * 20, img.size[1] * 20))
img.show()
