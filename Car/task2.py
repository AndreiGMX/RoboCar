from rplidar import RPLidar,RPLidarException
from time import sleep
from math import floor
from Servomotor import srv

PORT_NAME = '/dev/ttyUSB0'



def Smart2(x):
    d=50
    da=x/10
    m=(da-d)
    #print(d,da,m)

    if m>0:
        i=1
    else:
        i=-1

    a=abs(da-d)
    if a<5:
        srv(0)
    elif a<10:
        srv(0.1*i)
    elif a<14:
        srv(0.2*i)
    elif a<17:
        srv(0.3*i)
    elif a<20:
        srv(0.4*i)
    elif a<22:
        srv(0.5*i)
    else:
        srv(0.6*i)


def run(dis):
    lidar = RPLidar(PORT_NAME)
    try:
        for scan in lidar.iter_scans():
            c=0
            d=0
            for (_, angle, distance) in scan:
                if floor(angle)>=170 and floor(angle)<=190 and distance!=0 and distance<=dis:
                    return 1
                elif floor(angle)>=210 and floor(angle)<=225 and distance!=0:
                    #print(floor(distance))
                    c=c+1
                    d=d+floor(distance)
                else:
                    continue
                if c!=0:
                    Smart2(d/c)
    except RPLidarException:
        return 0
    lidar.stop()
    lidar.disconnect()

#Smart2(20)