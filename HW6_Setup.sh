#!/bin/sh

cd ~/
source /opt/ros/melodic/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
cd ~/catkin_ws/src
rosdep install joy
catkin_create_pkg racecar std_msgs rospy roscpp
cd ~/catkin_ws
catkin_make
. ~/catkin_ws/devel/setup.bash
roscd racecar
mkdir scripts
cd scripts
cp ~/ECE3432/HW6/talker.py ~/catkin_ws/src/racecar/scripts
#wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py
chmod +x talker.py
roscd racecar/scripts/
#wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py
cp ~/ECE3432/HW6/listener.py ~/catkin_ws/src/racecar/scripts
chmod +x listener.py
cd ~/catkin_ws
catkin_make

rosparam set joy_node/dev "/dev/input/js0" 
