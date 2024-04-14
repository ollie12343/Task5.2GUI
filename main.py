from tkinter import *
import RPi.GPIO as GPIO

# Constants
RED = 8
GREEN = 10
BLUE = 12


# Setup RPI
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

redPin = GPIO.PWM(RED, 50)
greenPin = GPIO.PWM(GREEN, 50)
bluePin = GPIO.PWM(BLUE, 50)


# TKInter setup
root = Tk()
root.title("Task 5.2C GUI")
root.geometry("225x225")

redLabel = Label(root, text="Red", anchor=W).grid(column=0, row=0, padx=10, pady=(10, 0))
redSlider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
redSlider.grid(column=1, row=0, padx=10, pady=10)
greenLabel = Label(root, text="Green", anchor=W).grid(column=0, row=1, padx=10)
greenSlider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
greenSlider.grid(column=1, row=1, padx=10)
greenLabel = Label(root, text="Blue", anchor=W).grid(column=0, row=2, padx=10, pady=(0, 10))
blueSlider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
blueSlider.grid(column=1, row=2, padx=10, pady=10)

exit_button = Button(root, text="Exit!", command=root.destroy).grid(column=1, row=3, pady=(35, 10))


def update():
    try:
        redPin.ChangeDutyCycle(redSlider.get())
        greenPin.ChangeDutyCycle(greenSlider.get())
        bluePin.ChangeDutyCycle(blueSlider.get())
        root.after(10, update)
    except AttributeError:
        pass

redPin.start(0)
greenPin.start(0)
bluePin.start(0)


root.after(50, update)
root.mainloop()

redPin.stop()
greenPin.stop()
bluePin.stop()

GPIO.cleanup()