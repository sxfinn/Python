number = input('shuzi')
c = 1 if number == 2 else 2
print(c)
n = 0
while n < 10:
    if n % 3 == 0:
        print(n)
    else:
        print(n+1)
    n += 1
