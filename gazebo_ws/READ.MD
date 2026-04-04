# know your distro
lsb_release -a

# check the distro is active
echo $ROS_DISTRO

# update packages
sudo apt update


# Install and Sanity Check missed ths 's' in first installation
sudo apt install ros-humble-gazebo-ros-pkgs

# Gazebo multi-robot simulator, version 11.10.2
gazebo --version


# Now launch the empty Gazebo world to confirm everything is wired up correctly
ros2 launch gazebo_ros gazebo.launch.py

#check the ros2 topic list 

# TurtleBot3 packages. This is the robot model we'll load into Gazebo.
sudo apt install ros-humble-turtlebot3-gazebo

# TurtleBot3 comes in 3 models — burger, waffle, and waffle_pi. We need to tell ROS which one to use. Set the model to burger:
export TURTLEBOT3_MODEL=burger

# now open gazebo with turtlebot3
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py




# open new terminal and launch data visualization.
sudo apt install ros-humble-turtlebot3
# launch RVIZ
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_bringup rviz2.launch.py


# install keyboard
sudo apt install ros-humble-teleop-twist-keyboard


# sometime due to speed the robot not visible in that case we need to reset the values
# resets the entire simulation back to its initial state — all models, positions, and velocities back to zero.

source /opt/ros/humble/setup.bash
ros2 service call /reset_simulation std_srvs/srv/Empty


# keys to understand
i Forward
, Backward
j Rotate left 
l Rotate right
u Forward + left diagonal
o Forward + right diagonal
m Backward + left diagonal
. Backward + right diagonal
k Stop