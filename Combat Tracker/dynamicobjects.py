class thing:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def get1(self):
        return self.n1

#main
objlist = []
for i in range(3):
    objlist.append(thing(1, 2))

i = objlist[0].get1()
print(i)