#include "rclcpp/rclcpp.hpp"


class HelloWorldNode : public rclcpp::Node // MODIFY NAME
{
public:
    HelloWorldNode() : Node("hello_world_name") // MODIFY NAME
{
}


private:

};


int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<HelloWorldNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}