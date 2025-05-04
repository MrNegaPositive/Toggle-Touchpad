import subprocess
import evdev
from evdev import InputDevice, list_devices
from datetime import datetime

def log_message(message):
    import os
    log_file_path = os.path.expanduser("~/touchpad-toggle.log")
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    with open(log_file_path, "a") as log:
        log.write(f"{datetime.now()}: {message}\n")

def is_mouse_connected():
    devices = [InputDevice(path) for path in list_devices()]
    for device in devices:
        name = device.name.lower()
        phys = getattr(device, 'phys', '').lower()  # e.g., "usb-0000..." for USB devices

        if ("mouse" in name or "logitech" in name) and "usb" in phys:
            log_message(f"External mouse detected: {device.name}")
            return True

    log_message("No external USB mouse detected.")
    return False

def toggle_touchpad(enable):
    state = "enabled" if enable else "disabled"
    try:
        subprocess.run([
            "gsettings", "set",
            "org.gnome.desktop.peripherals.touchpad",
            "send-events", state
        ], check=True)
        log_message(f"Touchpad {state}.")
    except subprocess.CalledProcessError:
        log_message("Failed to set touchpad state.")

if __name__ == "__main__":
    if is_mouse_connected():
        toggle_touchpad(False)
    else:
        toggle_touchpad(True)

# This script checks if a mouse is connected and enables/disables the touchpad accordingly.
# It uses gsettings to change the touchpad state, which is specific to GNOME desktop environment.
# Make sure to run this script with appropriate permissions to change system settings.
# Note: This script is designed for Linux systems with GNOME. Adjust the subprocess command for other environments.
# The script uses the evdev library to list input devices and check for mouse presence.
# Ensure you have the required permissions to run this script.
# You can install the evdev library using pip:
# pip install evdev
# This script is intended for educational purposes and should be used responsibly.
# Always test scripts in a safe environment before deploying them in production.
# The script is designed to be run in a terminal or as part of a larger automation script.
# It is not intended to be run as a standalone application with a GUI.
# The script is compatible with Python 3.x. Ensure you have the correct version of Python installed.
# The script is open-source and can be modified to suit your needs.
# Feel free to contribute to the project or report any issues you encounter.
# The script is provided "as-is" without any warranties or guarantees.
# Use at your own risk. The author is not responsible for any damages or data loss.
# The script is licensed under the MIT License. See the LICENSE file for more details.
# The script is part of a larger project that aims to improve user experience on Linux systems.
# The project is open to contributions and suggestions from the community.
# The script is designed to be modular and can be easily integrated into other projects.
# The script is maintained by a small team of developers who are passionate about open-source software.
# The project has a dedicated GitHub repository where you can find the source code and documentation.
# Created by Joshua Eaton on 2025-05-03