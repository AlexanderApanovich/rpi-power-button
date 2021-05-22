# pi-power-button

Python script to power on/off Raspberry PI 4

Guide for Raspberry PI 4:
1. Connect button between GPIO 3 (SCL) and ground
2. git clone https://github.com/AlexanderApanovich/rpi-power-button.git
3. cd rpi-power-button
4. sudo ./install
5. sudo crontab -e  
Add following string: @reboot python /usr/local/bin/rpi_power_button.py &

Uninstallation guide:
1. sudo crontab -e  
Remove following string: @reboot python /usr/local/bin/rpi_power_button.py &
2. cd rpi-power-button
3. sudo ./uninstall