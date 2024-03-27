from rplidar import RPLidar, RPLidarException

import numpy as np

lidar = RPLidar('com8')

lidar.__init__('com8', 256000, 3, None)

lidar.connect()

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

try:
    
    for i, scan in enumerate(lidar.iter_scans()):
        for d in scan:
            
            if 330 <= d[1] <= 360 or 0 <= d[1] <= 30:  
                
                flag = 0
                   
                # d[2] : Distance of the measurement
                if (d[2]/10) <= 100:
                    
                    flag += 1  # Her tamamlanışta flag değeri artırılır
                    
                    if d[1] == 360:
                        if flag != 0:
                            print("Engel Var!")
                        else:
                            print("Engel Yok!")

        if False:
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
            break
except KeyboardInterrupt as err:
    print('key board interupt')
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()

except RPLidarException as err:
    print(err)
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
except AttributeError:
    print('hi attribute error')