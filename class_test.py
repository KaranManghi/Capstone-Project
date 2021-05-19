class test:
    def __init__(self,l):
        self.l=l

def change(o):
    o.l=[2,3,4]
a=test([1,2,3])
change(a)

# a.l=[2,3,4]

print(a.l)