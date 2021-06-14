cmake_minimum_required(VERSION 2.8.3)
project(yp_launch)


find_package(catkin REQUIRED COMPONENTS
  velodyne_driver
  velodyne_pointcloud
  urg_node
  usb_cam
)

