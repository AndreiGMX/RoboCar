from rplidar import RPLidar,RPLidarException
from time import sleep
from math import radians,sin,cos,floor
import numpy as np
from Astar import astar
from Servomotor import srv
from dcmotors import p



PORT_NAME = '/dev/ttyUSB0'

val = [[],[]] #lista de valori tip lidar

#pentru ca lidarul pierde date am observat ca prima citire este foarte slaba 
def run(s):  #functie care baga valorile din lidar in lista de valori de mai sus la a 's' citire
    lidar = RPLidar(PORT_NAME)
    try:
        i=0
        for scan in lidar.iter_scans():
            if i==s:
                for (_, angle, distance) in scan:
                    if distance!=0: #floor(angle)>=145 and floor(angle)<=215 and 
                        #print(floor(angle),distance)
                        val[0].append(floor(angle))
                        val[1].append(floor(distance/100))
                    else:
                        continue
                return 1
            i=i+1
    except RPLidarException:
        return 0
    lidar.stop()
    lidar.disconnect()  


def georef(): #convertire date in matrice si executare
    #creez matricea si pun obstacolele in ea
    n=41 #n trebuie sa fie impar
    matx=np.zeros((n, n),dtype = int)

    i=int((n-1)/2)
    j=i
    matx[i][j]=8

    for s in range(len(val[0])):
        if val[1][s]!=0:
            itemp=floor(sin(radians(val[0][s]))*val[1][s])
            jtemp=floor(cos(radians(val[0][s]))*val[1][s])
            #print(i+itemp,j+jtemp)
            if abs(itemp)>i or abs(jtemp)>j:
                continue
            else:
                matx[i+itemp][j+jtemp]=1

    #print(matx)
    
    #go from->to
    start = (i, j)
    end = (i, 7)
    maze=matx.tolist()
    path = astar(maze, start, end) #folosete algoritmul Astar pentru gasire drum
    #print(path)
    #pun 2 in matrice pe tot drumul
    for i in path:
        matx[i[0]][i[1]]=2
    #pun datele si intr-un fisier
    f=open("data.txt",'w')
    np.savetxt(f, matx, fmt='%d')
    f.close()

    #ocolire
    p(45)
    
    for i in range(6,len(path)):
        x=path[i-2][0]
        y=path[i-1][0]
        z=path[i][0]
        #print(x,y,z,(x-y+y-z)/3.3,'\n')
        srv((x-y+y-z)/3.3)
        if (x-y+y-z)!=0:
            sleep(18.6/45)
        sleep(13.2/45)
    
    p(0)
    srv(0)
    sleep(0.1)


def getData(s): #primeste date
    val[0].clear()  #curata datele vechi
    val[1].clear()
    while run(s)!=1:  #baga date in lista lidar adica in val
        continue
    georef() 

def printData():
    for i in range(len(val[0])):
        print(val[0][i],val[1][i])



def main():
    getData(2)
    #printData()
    #print(len(val[0]))

if __name__ == '__main__':
    main()