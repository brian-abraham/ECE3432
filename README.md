## ECE3432 Team 4
This codebase is for controlling the car over WiFi using ROS

### First time setup workspace and package
```
./HW5_Setup.sh
./HW6_Setup.sh
```

### Running the Program
On the talker machine run:
```
roscore
```

Then in another terminal on the talker machine run:
```
./listener.py
```
Determine the IP of the talker machine by using `ifconfig`.

On the listener machine, run:
```
export ROS_MASTER_URI:<talkerIP>:11311
export ROS_IP:<talkerIP>
./listenerPi.py
```

### Contributors
  - Brian Abraham
  - Matthew Gilrow
  - Alex Kushlan
  - Rodrigo Medeiros
