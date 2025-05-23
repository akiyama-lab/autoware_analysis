# autoware_analysis

## measurements

[CARET Analysis for Autoware](https://github.com/tier4/caret_report/tree/main/sample_autoware)を参考にして、Autowareのトレースを取得します。
すべてのトレースは、`~/autoware_analysis/measurement`に保存されます。

1. `autoware`を起動

```bash
cd autoware
ulimit -n 65534
source ~/caret/setenv_caret.bash
source ./install/local_setup.bash
source ~/autoware_analysis/caret_topic_filter.bash
ros2 launch autoware_launch logging_simulator.launch.xml map_path:=$HOME/autoware_map/sample-map-rosbag vehicle_model:=sample_vehicle sensor_model:=sample_sensor_kit
```

2. `rosbag`を再生(別のターミナルで実行)

```bash
cd autoware
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

## transform

[lttng_to_architecture.py](https://github.com/akiyama-lab/autoware_analysis/blob/main/lttng_to_architecture.py)でLttngからArchitectureファイルに変換します。

環境変数`LTTNG_TRACE_DIR`や`ARCHITECTURE_FILE_PATH`で、パスを指定することができます。
指定がない場合、lttngトレースデータはmeasurementフォルダでタイムスタンプが最新のものを、Architectureファイルは`/home/akilab/autoware_analysis/architecture.yaml`が指定されます。
