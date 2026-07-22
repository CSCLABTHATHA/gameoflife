import random


class cell:
    all_instances = []
    
    def __init__(self,pos,life = False):
        self.pos = pos
        self.life = life


    def show(self):
        if self.life:
            return 1
        else:
            return 0


    def position(self):
        return self.pos


#grid 40x20
def surrounding(tup):
    x,y = tup
    lis = []
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            lis.append((i,j))


    del lis[4]
    for i in lis:
        for j in i:
            if j < 0:
                lis.remove(i)

    return lis


print(surrounding(3,4))


def percent(chance = input("Enter the percentage of life: ")):
    if random.randint(0,100) <= chance:
        return True
    else:
        return False


for i in range(41):
    for j in range(21):
        
        pass
