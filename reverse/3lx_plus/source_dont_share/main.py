from random import randrange


def reshape(lst, n):
    return [lst[i*n:(i+1)*n] for i in range(len(lst)//n)]
xored = [62, 103, 76, 56]


flag = "CTF{V1rtual3_Mash1n3s_ar3_B3autiful}"
numbers = reshape([ord(i) for i in flag], 9)
# print(numbers)
#65536 <- 16
#4,294,967,295 <- 32
for i in range(1, 4):
    for j in range(3):
        k = [randrange(1, 100), randrange(1, 100)]
        # print((numbers[i][3 * j] * k[0] + numbers[i][3 * j + 1] * k[1]) < 65536)
        answ = ((numbers[i][3 * j] * k[0] + numbers[i][3 * j + 1] * k[1]) - numbers[i][3 * j + 2]) ^ xored[i - 1]
        print(f"(x{3 * j + i *9} * {k[0]} + x{3 * j + 1+ i *9} * {k[1]}) - x{3 * j + 2+ i *9} == {answ} ^ {xored[i - 1]},")#^ {xored[i - 1]}

    for j in range(3):
        # print(numbers[i][j], numbers[i][3+j], numbers[i][6+j])
        answ = ((numbers[i][j] + numbers[i][3+j]) * numbers[i][6+j]) ^ xored[i - 1]
        # print((numbers[0][j] + numbers[0][3+j]) * numbers[0][6+j] < 65536)
        print(f"(x{j+ i *9} + x{3+j+ i *9}) * x{6+j+ i *9} == {answ} ^ {xored[i - 1]},")

    #!--------------!
    answ = (numbers[i][0] + numbers[i][4] - numbers[i][8]) ^ xored[i - 1]
    print(f"x{0 + i *9} + x{4 + i *9} - x{8+ i *9} == {answ} ^ {xored[i - 1]},")
    #!-------------!

    k = [randrange(1, 100)]
    while (numbers[i][2] * numbers[i][4] * k[0]) >= 65536:
        k = [randrange(1, 100)]
    answ = ((numbers[i][2] * numbers[i][4] * k[0]) - numbers[i][6]) ^ xored[i - 1]
    print(f"({k[0]} * x{2+ i *9} * x{4+ i *9}) - x{6+ i *9} == {answ} ^ {xored[i - 1]},")
    print(f"BLOCK {i} END\n\n\n\n")