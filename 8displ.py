import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.IN)


def clean_all():
    GPIO.output(15, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)

def for_0():
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    
def for_1():
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)

def for_2():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)

def for_3():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)

def for_4():
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)

def for_5():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)

def for_6():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(7, GPIO.HIGH)
    
def for_7():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)

def for_8():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)

def for_9():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(7, GPIO.HIGH)
clean_all()
count = 0
try:
    while True:
        while count != 10:
            if GPIO.input(12):
                globals()[("for_{}").format(count)]()
                sleep(1)
                clean_all()
                count += 1
        count = 0

except KeyboardInterrupt:
    GPIO.cleanup()


