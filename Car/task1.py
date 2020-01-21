from rplidar import RPLidar,RPLidarException
from time import sleep
from math import floor

PORT_NAME = '/dev/ttyUSB0'


def run(dis):
    lidar = RPLidar(PORT_NAME)
    try:
        c=0
        for scan in lidar.iter_scans():
            c=0
            d=0
            for (_, angle, distance) in scan:
                if floor(angle)>=178 and floor(angle)<=182 and distance!=0:
                    #print(floor(distance))
                    c=c+1
                    d=d+floor(distance)
                else:
                    continue
                if c!=0:
                    if d/c<=dis:
                        return 1
    except RPLidarException:
        return 0
    lidar.stop()
    lidar.disconnect()  
    

#run(10)