#author : Akib Hosen Khan


from sense_hat import SenseHat
from time import time
from time import sleep

sense = SenseHat()

temp1 = round(sense.get_temperature()*1.8 +32)
temp2 = round(sense.get_temperature())

humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())
message = 'Temperature is %d F , %d Degree , Humidity is %d percent , Pressure is %d mbars' %(temp1,temp2,humidity,pressure)


print 'temperature in Fahrenheit : ', temp1, 'F'
print 'temperature in Degree Celsius : ', temp2, 'Degree C'
print 'humidity : ', humidity, 'percent'
print 'pressure in bar : ', pressure, 'm bars' #bar is a metric unit of pressure, but is not approved as part of SI . 1 bar= 100000 pascal.

#print temp1 'F'


#baseURL = 'https://apt.thingpeak.com/update?api_key=%s' % sys.argv[1]


sense.show_message(message, scroll_speed=(0.08),text_colour=[200,0,200],back_colour= [0,0,0] )
sense.clear()                                                                                      

#back_colour= [0,0,200]