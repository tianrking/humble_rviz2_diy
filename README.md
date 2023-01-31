
# humble_rviz2_diy

## Build

```bash
git clone AA ~/AA
cd ~/AA 
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
```

## Create Project

ros2 pkg create w0x7ce_rviz2 --build-type ament_python

cd w0x7ce_rviz2 && mkdir urdf 
touch w0x7ce_rviz2_fishbot_base.urdf

## Struct

```txt
├── fishbot_description
│   ├── __init__.py
├── package.xml
├── setup.cfg
├── setup.py
└── urdf
    └── fishbot_base.urdf
```
