#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import random

# import sys


# sys.path.append("~/Documents/ros2_basic/ros2_ws/src/my_py_pkg/my_py_pkg")
# import randomquotes as rqus

class MyNode(Node):
    def __init__(self):
        super().__init__(node_name="py_test")
        self.get_logger().info(message="Hello from ROS2")

        # Create a timer that generate a random message after 2.0 sec
        self.create_timer(2.0, callback=self.timer_callback)

    def timer_callback(self):
        # self.get_logger().info(message=rqus.randomquotes())
        self.get_logger().info(message=str(random.random()))

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