ros2 run smart_school attendance_server



# ros2 interface
ros2 pkg create smart_school_interfaces
rm -rf include/ src/

mkdir srv


#package.xml
<builtool_depned> rosidl_default_generators </buildtool_depend>
<exec_depend> rosidl_default_runtime </exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>