# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
from twython import TwythonStreamer

# Search terms
TERMS = '#trump, #immigration'

# Twitter application authentication
APP_KEY = 'GGjGahZ56kjEBLVXAUdllUWrO'
APP_SECRET = 'ksh52EBiJpxMv2ErSjlzwvlvwZsDQR6Zmo3PxZhjbNlC7CZpQL'
OAUTH_TOKEN = '3068198086-JkCcZtjOXtSM7iWqbZ4c0bmzjcu19KUoxdtMZcF'
OAUTH_TOKEN_SECRET = 'O9R97AXTqWbUqa8ANb8HMJQ4yylxowhcKeJXtgIPGpLov'


# Import the PCA9685 module.
import Adafruit_PCA9685

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_immigration = 600  # Max pulse length out of 4096
servo_women = 500 
servo_tech = 400

class Servo(object): 

  # Helper function to make setting a servo pulse width simpler.
  def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
    # Set frequency to 60hz, good for servos.
    pwm.set_pwm_freq(60)

  #print('Moving servo on channel 0, press Ctrl-C to quit...')
  def move_servo(channel) 
    if (channel == 0):
    # Move servo on channel O between extremes.
        pwm.set_pwm(0, 0, servo_immigration)
        time.sleep(1)
        pwm.set_pwm(0, 0, servo_min)
        time.sleep(1)
    elif (channel == 1):
        pwm.set_pwm(0, 0, servo_women)
        time.sleep(1)
        pwm.set_pwm(0, 0, servo_min)
        time.sleep(1)
    else: 
        pwm.set_pwm(0, 0, servo_tech)
        time.sleep(1)
        pwm.set_pwm(0, 0, servo_min)
        time.sleep(1)



class Twitter2RaspberryPi(TwythonStreamer):
  def on_success(self, data):
    print "on success"
    if 'text' in data:
      print "hello"
      text_body = data['text']
      print text_body
      if 'immigration' in text_body or 'immigrants' in text_body:
        print data['text'].encode('utf-8')
        print "immigration"
        servo.move_servo(0)
      if 'women' in text_body or 'prolife' in text_body:
        print data['text'].encode('utf-8')
        print "women"
        servo.move_servo(1)
      elif 'technology' in text_body or 'tech' in text_body:
        print data['text'].encode('utf-8')
        print "tech"
        servo.move_servo(1)

  def on_error(self, status_code, data):
    print status_code, data


servo = Servo()

# Create streamer
try:
  servo.set_servo_pulse() 
  stream = Twitter2RaspberryPi(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
  stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
  GPIO.cleanup()
  ss.cleanup()