import keyboard
import globals

RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
GREY = "\033[90m"    

def pause_listener():
    while True:
        keyboard.wait('p')  
        globals.paused = not globals.paused
        state = "Paused" if globals.paused else "Resumed"
        print(f"\n{YELLOW}--- {state} ---{RESET}")