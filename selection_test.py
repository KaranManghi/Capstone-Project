a=[1,0,2,3,5,6,10,-1]

first=min(a[0],a[1])
second=max(a[0],a[1])

for i in range(2,len(a)):
    if a[i] <first:
        temp=first
        first=a[i]
        second=temp
    
    elif a[i]>first and a[i]<second:
        second=a[i]

print(first)
print(second)