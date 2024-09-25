import color_sensor
import color
from hub import port, light
import runloop
import time

async def main():

    # loop forever
    while True:

        # Get the current color once
        current_color = color_sensor.color(port.E)

        # If the color is known
        if current_color != color.UNKNOWN:

            # Make the power light match
            light.color(light.POWER, current_color)

        # print the number
        print(current_color)

        # Wait for 1/20th of a second
        time.sleep_ms(50)

runloop.run(main())
