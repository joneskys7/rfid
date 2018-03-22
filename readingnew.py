import RPi.GPIO as GPIO
import SimpleMFRC522
import urllib2
import time

reader = SimpleMFRC522.SimpleMFRC522()
while True:
    try:
            id, text = reader.read()
            print(id)
            if id == 962079459598 :
                    print ("jones")
                    urllib2.urlopen("http://mycampus365.com/farmvilla/update.php?id=1").read()
                    time.sleep(1)
            elif id == 344960107451 :
                    print ("arun")
                    urllib2.urlopen("http://mycampus365.com/farmvilla/update.php?id=2").read()
                    time.sleep(1)
            elif id == 553529604598 :
                    print ("mahesh")
                    urllib2.urlopen("http://mycampus365.com/farmvilla/update.php?id=3").read()
                    time.sleep(1)
            else:
                    print ("invalid")
                    urllib2.urlopen("http://mycampus365.com/farmvilla/update.php?id=0").read()
                    time.sleep(1)
    finally:
            GPIO.cleanup()
