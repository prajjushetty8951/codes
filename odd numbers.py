m = int(input())
n = int(input())
b = 1
for i in range(m , n + 1):
    if i % 2 == 1 :
        b = b * i
print(b)