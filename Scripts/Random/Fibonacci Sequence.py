x = 1
y = 0
n = int(input("Enter a number of times to sequence: "))
i = 0
while i<n:
    z=y+x
    y = x
    print(x)
    x = z
    i+=1