import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, pi
import random

xseries = []
yseries = []
##xseries.extend([0 for i in range(1000)])
##yseries.extend(np.linspace(-3/2*300,0,1000))
baseAngle = 39
randomFactor = 12

##angleDIFF1 = random.randrange(baseAngle-randomFactor,baseAngle+randomFactor+1)
##angleDIFF2 = random.randrange(baseAngle-randomFactor,baseAngle+randomFactor+1)

angleDIFF1 = 20
angleDIFF2 = 39

n = 10
points = 500

def form(c):
    return c*2/3

def R(c):
    return c*pi/180

def nextStep(clen=300,prevLoc = (0,0),angle=0,c=0):
    if c==n:
        return 0
    clen=form(clen)
##    R_A_D()
    angle -= angleDIFF1
    point1 = (prevLoc[0]+(sin(R(angle))*clen),prevLoc[1]+(cos(R(angle))*clen))
    xseries.extend(np.linspace(prevLoc[0],point1[0],points))
    yseries.extend(np.linspace(prevLoc[1],point1[1],points))
    nextStep(clen,point1,angle,c+1)
##    print(angle)
    angle += angleDIFF1
##    R_A_D()
    angle += angleDIFF2
    point2 = (prevLoc[0]+(sin(R(angle))*clen),prevLoc[1]+(cos(R(angle))*clen))
    xseries.extend(np.linspace(prevLoc[0],point2[0],points))
    yseries.extend(np.linspace(prevLoc[1],point2[1],points))
    nextStep(clen,point2,angle,c+1)
##    print(angle)
    angle -= angleDIFF2
nextStep()
plt.scatter(xseries,yseries,c=xseries,linewidths=0,s=0.1)
plt.show()
