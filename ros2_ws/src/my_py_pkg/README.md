# Minimal code for creating a node in Python

# Minimal code Python node with OOP

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