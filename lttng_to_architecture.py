#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path

from caret_analyze import Architecture

lttng_dir_path = os.getenv("LTTNG_DIR_PATH")

if not lttng_dir_path:
    # measurementディレクトリ内でタイムスタンプが最新のものを選択
    measurement_dir = Path("/home/akilab/autoware_analysis/measurement")
    if measurement_dir.exists() and measurement_dir.is_dir():
        lttng_dir_path = max(
            measurement_dir.iterdir(),
            key=lambda p: p.stat().st_mtime if p.is_dir() else 0,
        )
    else:
        raise FileNotFoundError(
            "LTTNG_DIR_PATH is not set and no valid measurement directory found."
        )
print(f"LTTNG_DIR_PATH: {lttng_dir_path}")

arch = Architecture("lttng", str(lttng_dir_path))

architecture_path = os.getenv(
    "ARCHITECTURE_FILE_PATH", "/home/akilab/autoware_analysis/architecture.yaml"
)
print(f"ARCHITECTURE_FILE_PATH: {architecture_path}")

arch.export(architecture_path, force=True)
print(f"{lttng_dir_path} -> {architecture_path}")
