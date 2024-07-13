from hub import light_matrix
from hub import motion_sensor
import time
import random
import runloop

# initalize the array
a = [[0]*5] * 5

async def main():
  while True:
    
    # TOP = 0 or false
    if motion_sensor.up_face():

        # creaet a random array
        for i in range(5):
            a[i] = [random.randint(0,100) for _ in range(5)]

        # update the light matrix
        for i in range(5):
            for j in range(5):
                light_matrix.set_pixel(i,j,a[i][j])

        # Wait for 1/10th of a second
        time.sleep_ms(100)

runloop.run(main())
