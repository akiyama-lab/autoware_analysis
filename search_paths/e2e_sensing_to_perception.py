#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from caret_analyze import Architecture

architecture_path = os.getenv(
    "ARCHITECTURE_FILE_PATH", "/home/akilab/autoware_analysis/architecture.yaml"
)
arch = Architecture("yaml", architecture_path)

paths = arch.search_paths(
    "/sensing/lidar/top/velodyne_ros_wrapper_node",
    "/perception/object_recognition/detection/centerpoint/lidar_centerpoint",
    "/perception/object_recognition/prediction/map_based_prediction",
)

for path in paths:
    path.summary.pprint()
    print("")
