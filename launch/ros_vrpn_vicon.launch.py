import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import yaml

def get_params(package, file, name):
    path = os.path.join(get_package_share_directory(package) + file)

    with open(path, "r") as file:
        params = yaml.safe_load(file)[name]["ros__parameters"]
    return params

def generate_launch_description():
    model_name = LaunchConfiguration('model_name')
    model_name_arg = DeclareLaunchArgument(
        'model_name',
        default_value='atn_holybro'
    )

    params = get_params(
        "ros_vrpn", "/config/asl_vicon.yaml", "ros_vrpn_client"
    )
    params["object_name"] = model_name
    params["vrpn_server_ip"] = "10.10.10.5"

    return LaunchDescription(
        Node(
            package="ros_vrpn",
            executable="ros_vrpn_client",
            namespace=object,
            output="screen",
            parameters=[params],
        )
    )
