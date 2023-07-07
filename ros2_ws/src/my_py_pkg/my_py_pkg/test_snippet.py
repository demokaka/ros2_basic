#!/usr/bin/env python3
import rclpy
from rclpy.node import Node



class HelloWorld(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("hello_world!") # MODIFY NAME


def main(args=None):
    rclpy.init(args=args)
    node = HelloWorld() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()