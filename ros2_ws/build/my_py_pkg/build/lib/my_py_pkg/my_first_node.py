import rclpy
from rclpy.node import Node

def main(args=None):
    # Initialize the node
    rclpy.init(args=args)

    # Create the node
    node = Node("py_test")

    # Main execution
    node.get_logger().info(message="Hello from ROS2")

    # Spinning 
    rclpy.spin(node=node)

    # Shutdown the node
    rclpy.shutdown()

if __name__=='__main__':
    main()