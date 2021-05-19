class t():
    def __init__(self):
        self.a=None
        self.b=None
        self.c=None

temp=t()

s=set([temp.a,temp.b,temp.c])

count=1
for k in s:
    te=temp
    te.k=count
    count+=1

print(temp.a)