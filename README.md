# autoware_analysis

## measurements

[CARET Analysis for Autoware](https://github.com/tier4/caret_report/tree/main/sample_autoware)を参考にして、Autowareのトレースを取得します。
すべてのトレースは、`~/autoware_analysis/measurement`に保存されます。

1. `autoware`を起動

```bash
cd autoware_caret
ulimit -n 65534
source caret/setenv_caret.bash
source ./install/local_setup.bash
source ~/autoware_analysis/caret_topic_filter.bash
ros2 launch autoware_launch logging_simulator.launch.xml map_path:=$HOME/autoware_map/sample-map-rosbag vehicle_model:=sample_vehicle sensor_model:=sample_sensor_kit
```

2. `rosbag`を再生(別のターミナルで実行)

```bash
cd autoware_caret
source ./install/local_setup.bash
ros2 topic pub /vehicle/status/control_mode autoware_vehicle_msgs/msg/ControlModeReport "mode: 0" --once
ros2 bag play ~/autoware_map/sample-rosbag/ -r 0.2 -s sqlite3
```

3. `caret`でトレースを取得(別のターミナルで実行)

```bash
export ROS_TRACE_DIR=~/autoware_analysis/measurement
source caret/install/local_setup.bash
ros2 caret record -f 10000 --light
```
