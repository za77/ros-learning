# yaml access
import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node 


def generate_launch_description():
    # Path to your config file
    config = os.path.join(
        get_package_share_directory('smart_school'),
        'config',
        'school_params.yaml'
    )
    return LaunchDescription([

        Node(
            package='smart_school',
            executable='attendance_server',
            name='attendance_server',
            parameters=[config]
        ),

        Node(
            package='smart_school',
            executable='bell_scheduler',
            name='bell_scheduler',
            parameters=[config]
        ),

        Node(
            package='smart_school',
            executable='school_monitor',
            name='school_monitor',
            parameters=[config]
        ),

    ])