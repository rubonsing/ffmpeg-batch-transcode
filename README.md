# ffmpeg-batch-transcode

A lightweight Python utility to batch transcode all video files within a folder using FFmpeg.

The relevant parameters have been optimized.

## Requirements

- [FFmpeg](https://ffmpeg.org/) must be installed on your system.  
  Download it from the [official website](https://ffmpeg.org/) and ensure the `ffmpeg` command is available in your PATH.

## Usage

1. Place the Python script (e.g., `ffmpeg-batch-transcode.py`) in a directory.
2. Inside that directory, create two subfolders: `input` and `output`.
3. Move all video files you wish to transcode into the `input`. **Only video files** should be placed there.
4. Run the script:
   ```
   python ffmpeg-batch-transcode.py
5. The script will automatically process every video from `input` and write the transcoded results to `output`.

## Example Directory Structure

After setup, your project folder should look similar to:

    your-project
    ├── ffmpeg-batch-transcode.py
    ├── input
    │   ├── vacation.mp4
    │   └── presentation.mov
    └── output
        └──(transcoded files will appear here)

