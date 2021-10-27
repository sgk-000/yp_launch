import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
                name='tf2_ros_fp_laser',
                package='tf2_ros',
                executable='static_transform_publisher',
                output='screen',
                arguments=['0', '0', '0', '0.0', '0.0', '0.0', 'base_footprint', 'laser'],
            ),
    ])