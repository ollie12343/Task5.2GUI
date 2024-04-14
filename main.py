from tkinter import *
import RPi.GPIO as GPIO

root = Tk()
root.title("Task 5.1P GUI")
root.minsize(200, 200)

LED = IntVar()


RED = 8
GREEN = 10
BLUE = 12


GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.output(RED, GPIO.LOW)
GPIO.output(GREEN, GPIO.LOW)
GPIO.output(BLUE, GPIO.LOW)


def clicked(LED):
    if LED == RED:
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(BLUE, GPIO.LOW)
        return
    if LED == GREEN:
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.LOW)
        return
    if LED == BLUE:
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(BLUE, GPIO.HIGH)
        return

# Radio Buttons - The values of the buttons correspond to the GPIO pin used
Radiobutton(root, text="Red", variable=LED, value=RED, command=lambda: clicked(LED.get())).pack(anchor=W, padx=10, pady=(20, 10))
Radiobutton(root, text="Green", variable=LED, value=GREEN, command=lambda: clicked(LED.get())).pack(anchor=W, padx=10)
Radiobutton(root, text="Blue", variable=LED, value=BLUE, command=lambda: clicked(LED.get())).pack(anchor=W, padx=10, pady=(10, 20))

exit_button = Button(root, text="Exit!", command=root.destroy).pack()

root.mainloop()

GPIO.cleanup()

