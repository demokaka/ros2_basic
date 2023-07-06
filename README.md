# ros2_basic
Learning ROS2 basics for beginners

# ROS2 installation
The version used in this project is ROS2 Humble
The installation follows the instruction at the [ROS2 Humble installation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html) home page

## Set locale
First run 
'locale'
to check the locale supports UTF-8. If not, run the next $ four lines:
'''
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
'''
## Setup Sources

## Install ROS 2 packages