from pynput import mouse
import datetime

# File to store mouse movement data
output_file = "mouse_movements.txt"
start_time = None  # To track the starting time

# Function to handle mouse movement events
def on_move(x, y):
    global start_time
    if start_time is None:
        # Record the time when the first movement occurs
        start_time = datetime.datetime.now()

    with open(output_file, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - Mouse moved to ({x}, {y})\n")
        print(f"Mouse moved to ({x}, {y})")

# Function to handle mouse click events
def on_click(x, y, button, pressed):
    global start_time
    if pressed:  # If the button is pressed
        timestamp = datetime.datetime.now()
        time_elapsed = (timestamp - start_time).total_seconds() if start_time else 0
        with open(output_file, "a") as file:
            file.write(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} - Mouse clicked at ({x}, {y})\n")
            file.write(f"Time taken before clicking: {time_elapsed:.2f} seconds\n")
        print(f"Mouse clicked at ({x}, {y})")
        print(f"Time taken before clicking: {time_elapsed:.2f} seconds")
        return False  # Stop the listener after the first click

# Listener for mouse events
def start_mouse_listener():
    print("Starting mouse tracker. Move the mouse and click the 'Login' button to stop.")
    with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
        listener.join()

# Start the program
if __name__ == "__main__":
    try:
        start_mouse_listener()
    except KeyboardInterrupt:
        print("\nMouse tracking stopped.")
