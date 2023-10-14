//IMPORT THE NECCESARY LIBRARIES
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/point_cloud2.hpp>

using namespace std;
using namespace std::chrono_literals;
using std::placeholders::_1;

// DEFINE A CLASS FOR PUBLISHING AN OCCUPANCY GRID
class remapping_nodes : public rclcpp::Node
{

private:
    // DECLARE PRIVATE MEMBERS
    rclcpp::Subscription<sensor_msgs::msg::PointCloud2>::SharedPtr sub_lidar;
    rclcpp::Publisher<sensor_msgs::msg::PointCloud2>::SharedPtr pub_lidar;

public:
    remapping_nodes() : Node("save_map")
    {
        // CREATE A SUBSCRIBER
        sub_lidar = this->create_subscription<sensor_msgs::msg::PointCloud2>(
            "/airsim_node/Drone1/lidar/MyLidar1",
            10,
            std::bind(&remapping_nodes::remapping_lidar_callback, this, _1)
        );

        // CREATE A PUBLISHER
        pub_lidar = this->create_publisher<sensor_msgs::msg::PointCloud2>("/Drone/Airsim/remapping/lidar_pointcloud", 10);
    }

    // CALLBACK FUNCTION TO GENERATE AND PUBLISH AN OCCUPANCY GRID
    void remapping_lidar_callback(const sensor_msgs::msg::PointCloud2::SharedPtr msg)
    {
        // create lidar msg
        auto lidar_msg = sensor_msgs::msg::PointCloud2();
        lidar_msg.header.stamp = rclcpp::Clock().now();
        lidar_msg.header.frame_id = "odom";
        lidar_msg.height = msg->height;
        lidar_msg.width = msg->width;
        lidar_msg.fields = msg->fields;
        lidar_msg.is_bigendian = msg->is_bigendian;
        lidar_msg.point_step = msg->point_step;
        lidar_msg.row_step = msg->row_step;
        lidar_msg.data = msg->data;
        lidar_msg.is_dense = msg->is_dense;

        pub_lidar->publish(lidar_msg);

    }


};

// MAIN FUNCTION
int main(int argc, char ** argv)
{
    // INITIALIZE THE ROS2 NODE
    rclcpp::init(argc, argv);
    auto node = std::make_shared<remapping_nodes>();
    std::cout << "Remapping Airsim nodes..." << std::endl;
    rclcpp::spin(node);
    return 0;
}
