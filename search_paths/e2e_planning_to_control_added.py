#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from caret_analyze import Architecture

architecture_path = os.getenv(
    "ARCHITECTURE_FILE_PATH", "/home/akilab/autoware_analysis/architecture.yaml"
)
arch = Architecture("yaml", architecture_path)

paths = arch.search_paths(
    "/planning/scenario_planning/lane_driving/behavior_planning/behavior_path_planner",
    # "/planning/scenario_planning/lane_driving/behavior_planning/path_with_lane_id",
    "/planning/scenario_planning/lane_driving/behavior_planning/behavior_velocity_planner",
    # "/planning/scenario_planning/lane_driving/motion_planning/obstacle_cruise_planner",
    "/planning/scenario_planning/lane_driving/motion_planning/motion_velocity_planner",
    "/planning/scenario_planning/velocity_smoother",
    "/planning/planning_validator",
    "/control/trajectory_follower/controller_node_exe",
    "/control/vehicle_cmd_gate",
)

for path in paths:
    path.summary.pprint()
    print("")
