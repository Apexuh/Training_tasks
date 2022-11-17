a = (1, 1)
b = (2, 4)

def side(i, j):
    x1, y1 = i
    x2, y2 = j
    side = ((x2 - x1)** 2 + (y2 - y1) ** 2)** 0.5
    return side

print(side(a,b))
def gipo(side):
    gip = (side ** 2 + side ** 2) ** 0.5
    return gip
print(gipo(side(a,b)))
