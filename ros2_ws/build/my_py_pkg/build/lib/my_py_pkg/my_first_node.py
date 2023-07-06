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