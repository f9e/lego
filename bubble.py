from hub import light_matrix
from hub import motion_sensor
import time
import random
import runloop

rows, cols = (5, 5)

async def main():

  pos = 12
  while True:

    # Move the pixel depending on the up face
    face =  motion_sensor.up_face()
    if face == motion_sensor.FRONT:
      pos+=5
    if face == motion_sensor.BACK:
      pos-=5
    if face == motion_sensor.RIGHT:
      pos+=1
    if face == motion_sensor.LEFT:
      pos-=1      
    if pos > 24:
        pos -= 25
    if pos < 0:
        pos += 25

    # set the array to be empty
    a = [[0 for i in range(cols)] for j in range(rows)]

    # map the pixel based on the number
    a[int(pos%5)][int(pos/5)] = True

    # update the light matrix
    for i in range(5):
        for j in range(5):
            light_matrix.set_pixel(i,j, 100 if a[i][j] else 0 )

    # Wait for 1/10th of a second
    time.sleep_ms(100)

runloop.run(main())
