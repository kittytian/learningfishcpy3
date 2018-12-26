
i = 1
n = 7  # 台阶数
while i <= 100:
    if(n % 2 == 1) and (n % 3 == 2) and (n % 5 == 4) and (n % 6 == 5):
        print(n)
    else:
        n = 7 * i
    i = i + 1
