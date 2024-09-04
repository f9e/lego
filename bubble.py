from hub import light_matrix
from hub import motion_sensor
import time
import runloop

rows, cols = (5, 5)


## If the pixel is out of range
#loop it around the screen
def checkRange(pos):
    if pos > 4:
        pos -= 5
    if pos < 0:
        pos += 5
    return pos

async def main():

  xPos , yPos = (2,2)
  while True:

    # Move the pixel depending on the up face
    face = motion_sensor.up_face()
    if face == motion_sensor.FRONT:
      xPos += 1
    if face == motion_sensor.BACK:
      xPos -= 1
    if face == motion_sensor.RIGHT:
      yPos += 1
    if face == motion_sensor.LEFT:
      yPos -= 1

    # If the pixel goes off the board, replace it
    xPos = checkRange(xPos)
    yPos = checkRange(yPos)

    # set all pixels in the array to false.
    # a = [
    #    [0,0,0,0,0],
    #    [0,0,0,0,0],
    #    [0,0,0,0,0],
    #    [0,0,0,0,0],
    #    [0,0,0,0,0],
    # ]
    a = [[False for i in range(cols)] for j in range(rows)]

    # set the "on" pixel
    a[int(yPos)][int(xPos)] = True

    # update the light matrix
    for i in range(5):
        for j in range(5):
            light_matrix.set_pixel(i,j, 100 if a[i][j] else 0 )

    # Wait for 1/10th of a second
    time.sleep_ms(200)

runloop.run(main())
