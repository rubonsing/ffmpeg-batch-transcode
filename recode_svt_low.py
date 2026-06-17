# Copyright (c) 2026 rubonsing
# SPDX-License-Identifier: MIT

import subprocess
import os

input_dir = "input"
output_dir = "output"

def run_test(ref, dis):
    cmd_head = "ffmpeg -hide_banner -i " + ref + " -i " + dis + \
        """ -lavfi "[0:v]settb=AVTB,setpts=PTS-STARTPTS[ref];\
        [1:v]settb=AVTB,setpts=PTS-STARTPTS[dis];[ref][dis]"""
    
    cmd1 = cmd_head + """libvmaf=n_threads=16:shortest=true:model=version=vmaf_4k_v0.6.1"  -f null -"""
    cmd2 = cmd_head + """ssim=shortest=true"  -f null -"""
    cmd3 = cmd_head + """psnr=shortest=true"  -f null -"""
    cmd4 = cmd_head + """xpsnr=shortest=true"  -f null -"""
    subprocess.run(cmd1, check=True)
    subprocess.run(cmd2, check=True)
    subprocess.run(cmd3, check=True)
    subprocess.run(cmd4, check=True)

for filename in os.listdir(input_dir):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".mp4")

    #output_path = "output/test.mp4"
    print(f"\ntranscoding: {input_path} → {output_path}\n")
    cmd = [
        "ffmpeg", "-hide_banner", "-i", input_path,
        #"-ss", "00:00:00",
        #"-to", "00:05:00",
        #"-vf", "zscale=w=1920:h=1080:filter=lanczos,fps=30",
        "-c:v", "libsvtav1",
        "-svtav1-params", "preset=8:profile=0:tune=2:crf=40:keyint=600",
        "-map", "0",
        "-map", "-0:d",
        "-c:a:1", "copy",
        output_path
    ]
    subprocess.run(cmd, check=True)
    #run_test(input_path, output_path)

print("\nall transcode complete\n")
