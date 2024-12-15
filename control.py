from pynput.mouse import Controller
from pynput.keyboard import Controller

def control_mouse():
    mouse = Controller()
    mouse.position = (380,230)

def control_keyboard():
    keyboard = Controller()
    keyboard.type("i lou janu")

control_keyboard()