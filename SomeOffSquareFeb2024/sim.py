import random,csv


def getPointInSquare():
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    return [x,y]

def inSquare():
    pointA = getPointInSquare()
    pointB = getPointInSquare()

    midpoint = [(pointA[0] + pointB[0])/2,(pointA[1] + pointB[1])/2]
    radius = (((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)**(1/2))/2
    dist = min([1-midpoint[0],midpoint[0],1-midpoint[1],midpoint[1]])

    #print (f'{tuple(pointA)},{tuple(pointB)}')
    #print (tuple(midpoint))
    return dist>radius

def getMidpoint():
    pointA = getPointInSquare()
    pointB = getPointInSquare()

    midpoint = [(pointA[0] + pointB[0])/2,(pointA[1] + pointB[1])/2]

    return midpoint



countM = []
countP = []
size=100000
     
     
for i in range(1,size+1):
    m = getMidpoint()
    

    p = getPointInSquare()
    countM.append(m)
    countP.append(p)

with open("midpoint.csv",'w', newline='') as m,  open("point.csv","w", newline='') as p:
    wm  = csv.writer(m)
    wp = csv.writer(p)
    wm.writerows(countM)
    wp.writerows(countP)

        


   


