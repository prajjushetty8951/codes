n = input()
c = 0
for i in range(1,int(n) + 1):
    s = 0
    for j in str(i):
        s +=int(j)**len(str(i))
    if int(i)==s:
        print(s)