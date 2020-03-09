## ECE3432 Team 4
This codebase is for controlling the car over WiFi using ROS

### Setup workspace and package
```
./HW5_Setup.sh
```

### To Run Program
On the talker machine run:
```
roscore
```

Then in another terminal on the talker machine run:
```
./talker.py
```
Determine the IP of the talker machine by using `ifconfig`.

On the listener machine, run:
```
export ROS_MASTER_URI:<talkerIP>:11311
export ROS_IP:<talkerIP>
./listener.py
```

### Contributors
  - Brian Abraham
  - Matthew Gilrow
  - Alex Kushlan
  - Rodrigo Medeiros
