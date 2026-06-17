# Copyright (c) 2026 rubonsing
# SPDX-License-Identifier: MIT

import subprocess
import os

input_dir = "input"
output_dir = "output"

for filename in os.listdir(input_dir):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".mp4")
    print(f"\ntranscoding:{input_path} → {output_path}\n")
    cmd = [
        "ffmpeg", "-hide_banner", "-i", input_path,
        #"-ss", "00:00:00",
        #"-to", "00:05:00",
        #"-vf", "zscale=w=1728:h=1080:filter=lanczos,fps=30",
        "-c:v", "libsvtav1",
        "-svtav1-params", "preset=5:profile=0:tune=2:crf=45:keyint=600",
        "-map", "0",
        "-map", "-0:d",
        "-c:a:1", "copy",
        output_path
    ]
    subprocess.run(cmd, check=True)

print("\nall transcode complete\n")
