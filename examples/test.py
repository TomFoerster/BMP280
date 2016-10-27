#!/usr/bin/python
import time
import BMP280.BMP280 as BMP280
#setting timeout for 7 hours
timeout = time.time() + 60*60*7
file = open('measurements.csv','a')
sensor = BMP280.BMP280(modep=BMP280.BMP280_ULTRAHIGHRES,modet=BMP280.BMP280_T_O2,filter=BMP280.BMP280_FILTER_OFF,address=BMP280.BMP280_I2CADDR)
#writing to csv file every 30 seconds
while True:
	t,p = sensor.read_temperature_pressure()
        out=(str(time.time()) + ',' + str(t) + ',' + str(p) + '\n')
        file.write(out)
        print(out)
        time.sleep(1)
        if time.time() > timeout:
                file.close()
                break

