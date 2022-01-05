x = 1
y = 1

n = int(input())
str = input()

i = 0

while i <= len(str) :
    if str[i] == 'L' and y != 1 :
        y -= 1
    elif str[i] == 'R' and y != n :
        y += 1
    elif str[i] == 'U' and x != 1 :
        x -= 1
    elif str[i] == 'D' and x != n :
        x += 1
    i += 2

print(x, y)

