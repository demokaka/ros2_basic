# Minimal code for creating a node in Python
```
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    # Initialize the node
    rclpy.init(args=args)

    # Create the node
    node = Node("py_test")

    # Main execution


    # Spinning 
    rclpy.spin(node=node)

    # Shutdown the node
    rclpy.shutdown()

if __name__=='__main__':
    main()    
```

# Minimal code Python node with OOP
```
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__(node_name="py_test")
        self.get_logger().info(message="Hello from ROS2")

def main(args=None):
    # Initialize the node
    rclpy.init(args=args)

    # Create the node
    node = MyNode()

    # Spinning 
    rclpy.spin(node=node)

    # Shutdown the node
    rclpy.shutdown()

if __name__=='__main__':
    main()
```

# Install the executable using colcon build
First, do not forget to source the `setup.bash` file in the install folder of the workspace.  
If not, there will be no executable at the output.
```
source PATH_TO_WORKSPACE/ros2_ws/install/local_setup.bash
``` 
Now, in the `setup.py`, in the `setup` part, the `'console_scripts'`, add this line:
```
"my_first_node_exec = my_py_pkg.my_first_node:main"
```

```
setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='khanh',
    maintainer_email='khanhdinhcong99@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "my_first_node_exec = my_py_pkg.my_first_node:main"
        ],
    },
)
```
# Python version problem
We can run the Python script by command line
```
python3 my_py_node.py
```
or by making the script an executable and then running it
```
chmod +x my_py_node.py
./my_py_node.py
```

Normally, this should work in a new machine with Python version 3.10.
## Problem
If you have Python version 3.8 installed on the system by default, there will be some error messages that indicate lacks of files when you run:

```
Traceback (most recent call last):
  File "./my_first_node.py", line 2, in <module>
    import rclpy
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 49, in <module>
    from rclpy.signals import install_signal_handlers
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/signals.py", line 15, in <module>
    from rclpy.exceptions import InvalidHandle
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/exceptions.py", line 15, in <module>
    from rclpy.impl.implementation_singleton import rclpy_implementation as _rclpy
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/impl/implementation_singleton.py", line 32, in <module>
    rclpy_implementation = import_c_library('._rclpy_pybind11', package)
  File "/opt/ros/humble/lib/python3.10/site-packages/rpyutils/import_c_library.py", line 39, in import_c_library
    return importlib.import_module(name, package=package)
  File "/home/khanh/miniconda3/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ModuleNotFoundError: No module named 'rclpy._rclpy_pybind11'
The C extension '/opt/ros/humble/lib/python3.10/site-packages/_rclpy_pybind11.cpython-38-x86_64-linux-gnu.so' isn't present on the system. Please refer to 'https://docs.ros.org/en/humble/Guides/Installation-Troubleshooting.html#import-failing-without-library-present-on-the-system' for possible solutions
```

## Solution
Install the `python3.10-venv` package if it's not already installed on your system.  
Open a terminal and run the following command:

```
sudo apt install python3.10-venv
```
Create a new directory where you want to set up your Python 3.10 environment. For example:
```
mkdir mypythonenv
cd mypythonenv
```
Create a virtual environment using Python 3.10 by running the following command:
```
python3.10 -m venv myenv
```
Open your shell configuration file in a text editor
```
gedit ~/.bashrc
```

Add the following line at the end of the file:
```
alias activate_python3.10="source PATH_TO_PYTHON_ENVIRONMENT/mypythonenv/myenv/bin/activate"
```

Now, you can activate the Python 3.10 virtual environment by simply running the following command:
```
activate_python3.10
```

# Changing the arguments of ROS2 node using command line
If you want to change the name of the node, add the options `--ros-args --remap` when running
```
ros2 run my_py_pkg my_first_node_exec --ros-args --remap __node:=abc
```
Also you can change the other attributes/parameters using the same options
```
ros2 run my_py_pkg my_first_node_exec --ros-args --remap name_of_parameter:=new_name_of_parameter
```