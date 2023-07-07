#include "rclcpp/rclcpp.hpp"
#include "randomquotes.h"

class MyNode : public rclcpp::Node
{
public:
    // Constructor
    MyNode() : Node("cpp_test"), counter_(0)
    {
        RCLCPP_INFO(this->get_logger(), "Hello from ROS2 cpp");

        // Create a timer that print random message after 2 seconds
        timer_ = this->create_wall_timer(std::chrono::milliseconds(500),
                                         std::bind(&MyNode::timer_callback,this));
    }

private:
    void timer_callback()
    {
        counter_++;
        RCLCPP_INFO(this->get_logger(), "Hello %d",counter_);
    }

    rclcpp::TimerBase::SharedPtr timer_;
    int counter_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<MyNode>();

    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;
}