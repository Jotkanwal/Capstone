og1 = (0, 4.00448e+09, 4.39690e+07, 4.48017e+06, 300, 0)
og2 = (0, 4.00714e+09, 4.19052e+07, 7.13633e+06, 240, 1)
og3 = (0, 4.00288e+09, 4.28653e+07, 2.88017e+06, 300, 0)
og4 = (0, 4.01120e+09, 4.85532e+07, 1.12003e+07, 300, 0)

new1 = (0, 11, 11, 0, 5)
new2 = (0, 2.97684e+07, 2.97684e+07, 2.97684e+07, 60, 4)
new3 = (0, 3.19604e+07, 3.19604e+07, 3.19604e+07, 60, 4)
new4 = (0, 3.50643e+07, 3.50643e+07, 3.50643e+07, 60, 4)

og = (og1, og2, og3, og4)
new = (new2, new2, new3, new4)

ogtimerx = 0
ogdelaysum = 0
oglastdelay = 0
ogthrough = 0
ogpacketloss = 0

newtimerx = 0
newdelaysum = 0
newlastdelay = 0
newthrough = 0
newpacketloss = 0

for i in range(4):
    ogtimerx += og[i][1]
    ogdelaysum += og[i][2]
    oglastdelay += og[i][3]
    ogthrough += og[i][4] / 10.7
    ogpacketloss += og[i][5]
    
    newtimerx += new[i][1]
    newdelaysum += new[i][2]
    newlastdelay += new[i][3]
    newthrough += new[i][4] / 10.7
    newpacketloss += new[i][5]
    print(11e+10 - new[i][2])

print(ogtimerx/4)
print(ogdelaysum/4)
print(oglastdelay/4)
print(ogthrough/4)
print(ogpacketloss/4)

print(newtimerx/4)
print(newdelaysum/4)
print(newlastdelay/4)
print(newthrough/4)
print(newpacketloss/4)