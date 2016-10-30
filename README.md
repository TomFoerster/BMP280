Python BMP280
===================

Python library for accessing temperature and pressure measurments of BMP280 chip

Tested with Adafruit BMP280 temperature pressure sensors: https://www.adafruit.com/products/2651

Code used as a base:
https://github.com/gradymorgan/node-BMP280
https://github.com/adafruit/Adafruit_Python_BMP

Installation
------------
To install run the setup.py file.
(e.g. sudo python setup.py install)

e.g. usage:
-----------
import BMP280.BMP280 as BMP280
sensor=BMP280.BMP280()
sensor.read_temperature_pressure()

**See example file placed in ./examples/ for more guidance**

Options for Usage
-----------------
(e.g. sensor=BMP280.BMP280(modep=BMP280_LOWPOWER)

###SETTINGS FOR TEMPERATURE OVERSAMPLING
(OVER x2 SAMPLE NO USE FOR PRESSURE ACCURANCY)
modet=
BMP280_T_O1            x1  Sample
BMP280_T_O2            x2  Sample
BMP280_T_O4            x4  Sample
BMP280_T_O8            x8  Sample
BMP280_T_O16           x16 Sample


###PRESSURE OVERSAMPLING MODES
modep=
BMP280_ULTRALOWPOWER   x1  Sample
BMP280_LOWPOWER        x2  Sample
BMP280_STANDARD        x4  Sample
BMP280_HIGHRES         x8  Sample
BMP280_ULTRAHIGHRES    x16 Sample


###FILTER SETTINGS        >=75% STEP_RESPONCE AFTER SAMPLE
BMP280_FILTER_OFF      1
BMP280_FILTER_2        2
BMP280_FILTER_4        5
BMP280_FILTER_8        11
BMP280_FILTER_16       22


Functions:
----------
_load_calibration(self)
_set_filter(self)
_load_datasheet_calibration(self)
read_raw_temp_pressure(self)
read_temperature_pressure(self)
read_altitude(self, sealevel_pa=101325.0)
read_sealevel_pressure(self, altitude_m=0.0)


#HAVE FUN USING THIS LIBRARY



