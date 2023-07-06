# Create ROS2 workspace
Usually, we create a folder as the workspace of ROS2 with name `ros2_ws`.
```
mkdir ros2_ws
```
We create a `src` folder inside the `ros2_ws` to store all the packages we write in the future.
```
cd ros2_ws
mkdir src
```
For the first time, run `colcon build`. This will generate some folders `build`, `install` and `log` in the workspace.  

Imagine when we created a program in our workspace and we want to run this anywhere that we want.  
In this case, we need to source the `local_setup.bash` or `setup.bash` file in the `install` folder so that it can be located.  
Open the `.bashrc` file:
```
cd
gedit /bashrc
```
and then source the `setup.bash` file by adding a newline
```
source PATH_TO_YOUR_WORKSPACE/ros2_ws/install/setup.bash
```

# Create a package
To create a package, first go to `src` folder where we will write our package.
```
cd ros2_ws/src
```
Then, using the `ros2 pkg create` to create the package.  
If you want to create a `Python` package:
```
ros2 pkg create package_name --build-type ament_python --dependencies rclpy
```
If you want to create a `C++` package:
```
ros2 pkg create package_name --build-type ament_cpp --dependencies rclcpp
```


