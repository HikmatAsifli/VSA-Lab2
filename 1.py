n = int(input("Bir reqem girin: "))
b = list(range(n))
print('B:',b)
k=0
for x in b:
    if x%2!=0:
        k+=x
print(k)