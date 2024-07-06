# Video Frame Extractor

This is a small Python CLI program to extract frames from a video file. You can specify the video file path, the destination directory, and choose to extract all frames or just the frames from a specific segment of the video.

## 1. Requirements

- Python 3.x
- OpenCV (cv2)
- argparse

You can install the required libraries using pip:

```sh
pip install opencv-python argparse
```

## 2. Usage

### 2.1. Extract All Frames

Extract `all` frames from the video:

```sh
python frame_extractor.py.py path/to/video path/to/destination --all
```

### 2.2. Extract Frames from a Specific Segment

Extract frames from a specific time segment (e.g., from 1 minute 30 seconds to 2 minutes 45 seconds):

```sh
python extract_frames.py path/to/video path/to/destination --from=1.30 --to=2.45
```

Extract frames from the `start` (beginning) of the video to a specific time:

```sh
python extract_frames.py path/to/video path/to/destination --from=start --to=2.45
```

Extract frames from a specific time to the `end` of the video:

```sh
python extract_frames.py path/to/video path/to/destination --from=1.30 --to=end
```

## 3. Options

- `video_path`: Path to the video file (e.g., `video`)
- `dest_dir`: Destination directory to save extracted frames
- `--all`: Extract all frames
- `--from`: Start time in `minutes.seconds` format or `start` to indicate the beginning
- `--to`: End time in `minutes.seconds` format or `end` to indicate the end

## 4. Error Handling

The script will print an error message if the video file cannot be opened. It will also check if the specified start and end times are within the valid range and are non-negative, printing an error message if they are not.

## 5. Example

Extract frames from example.mp4 between 1 minute 10 seconds and 2 minutes 30 seconds, and save them to frames/ directory:

```sh
python extract_frames.py example.mp4 frames --from=1.10 --to=2.30
```

## 6. License

This project is licensed under the MIT [License](./LICENSE) - see the LICENSE file for details.
