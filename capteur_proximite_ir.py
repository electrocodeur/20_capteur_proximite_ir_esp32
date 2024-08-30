from machine import Pin
import time

SENSOR_PIN = 23 

ir_sensor = Pin(SENSOR_PIN, Pin.IN)

while True:
    sensor_state = ir_sensor.value()

    if sensor_state == 0:
        print("Obstacle !!")
    else:
        pass

    time.sleep_ms(200)
