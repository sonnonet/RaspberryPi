import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 23

GPIO.setup(PIR_PIN, GPIO.IN)

try: 
    print "PIR Module Test (Ctrl +C to exit)"
    time.sleep(2)
    print "Ready"

    while True:
        if GPIO.input(PIR_PIN):
            t = time.localtime()
            print "%d:%d:%d Motion Detected!" % (t.tm_hour, t.tm_min, t.tm_sec)
            time.sleep(0.05)

except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()
