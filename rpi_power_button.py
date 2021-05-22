import logging
import logging.handlers
import os
import subprocess
import time
import RPi.GPIO as GPIO

# config
gpio_pin = 3
poll_period_sec = 0.1
delay_before_shutdown_sec = 0.5
shutdownCommand = "shutdown -h now".split()

# raspberry pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# logging
handler = logging.handlers.WatchedFileHandler("/var/log/rpi_power_button/rpi_power_button.log")
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)


def shutdown():
    try:
        subprocess.check_output(shutdownCommand)
    except Exception as e:
        logging.exception(str(e))


def init():
    while True:
        time.sleep(poll_period_sec)
        if GPIO.input(gpio_pin) == False:
            while GPIO.input(gpio_pin) == False:
                time.sleep(delay_before_shutdown_sec)
            shutdown()


init()
