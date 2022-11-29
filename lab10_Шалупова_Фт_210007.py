sum = int(input("Введите сумму в рублях: "))
while sum <= 1:
           print("Число должно быть больше 1")
           sum = int(input("Введите сумму в рублях: "))
           break
print("Ваши купюры: ")
k = 128
while 2 <= (k := k // 2):
    n, sum = divmod(sum, k)
    if n > 0:
        print(n, k)
