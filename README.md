# Toggle-Touchpad

IF you use a laptop with a mouse attached like me, you probably get tired of bumping the touchpad wnd accidently moving the cursor into a random spot in the middle of your code. This solves the problem by detecting if a mouse is pugged in and disables the touchpad and when you unplugg the mouse the touch pad reactivates.
Create a ne folder in your home/YOURUSERNAME and copy the toggle_touchpad.py there.

You will need to create a .service file:
BASH

sudo nano ~/.config/systemd/user/touchpad-toggle.service

Then paste this into the file (update the user ID if needed):

[Unit]
Description=Toggle touchpad based on USB mouse connection

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /home/YOUR_USERNAME_HERE/touchpad-toggle/toggle_touchpad.py
Environment=DISPLAY=:0
Environment=DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus

Next you will create a timer as follows:
BASH

sudo nano ~/.config/systemd/user/touchpad-toggle.timer

Copy and past this into the editor:

[Unit]
Description=Run touchpad toggle every 10 seconds

[Timer]
OnBootSec=10
OnUnitActiveSec=10
AccuracySec=1s
Persistent=true

[Install]
WantedBy=default.target

then bash:
systemctl --user daemon-reload
systemctl --user enable --now touchpad-toggle.timer

you should now be up and running!
