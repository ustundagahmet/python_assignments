sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

str_sudoku = str(sudoku)
vir = str_sudoku.replace(",", " ")
parantez = vir.replace("[", "")
son = parantez.replace("]", "")

a = 0
b = 7
for i in range(1, 28):
    print(son[a:b], end = "")
    if i % 3 != 0:
        print(" | ", end = "")
    a += 9
    b += 9
    if i % 3 == 0:
        print()
    if i % 9 == 0:
        print("- " * 14) 