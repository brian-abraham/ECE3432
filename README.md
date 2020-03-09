## ECE3432 Team 4
This codebase is for controlling the car over WiFi using ROS

### First time setup workspace and package
```
./HW6_Setup.sh
```

### Running the Program
On the master desktop machine run:
```
roscore
```

Then in another terminal on the master desktop machine run:
```
./listener.py
```
Determine the IP of the master machine by using `ifconfig`.

On the controller machine, run:
```
export ROS_MASTER_URI:<masterIP>:11311
export ROS_IP:<masterIP>
./HW6_ControlTx.sh
```

On the Car machine, run:
```
export ROS_MASTER_URI:<masterIP>:11311
export ROS_IP:<masterIP>
./listenerPi.py
```

### Contributors
  - Brian Abraham
  - Matthew Gilrow
  - Alex Kushlan
  - Rodrigo Medeiros
