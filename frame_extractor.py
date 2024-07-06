import os
from typing import Optional

import cv2
import argparse

def extract_frames(video_path: str, dest_dir: str, start_time: Optional[float] = None, end_time: Optional[float] = None) -> None:
    # Create the destination directory if it does not exist
    os.makedirs(dest_dir, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    # Convert start and end time to frames
    if start_time is not None and start_time >= 0:
        start_frame = int(start_time * 60 * fps)
    else:
        start_frame = 0

    if end_time is not None and end_time >= 0:
        end_frame = int(end_time * 60 * fps)
    else:
        end_frame = total_frames

    # Check if the frame numbers are within the valid range
    if start_frame < 0 or start_frame >= total_frames:
        print("Error: Start time is out of range")
        return

    if end_frame <= start_frame or end_frame > total_frames:
        print("Error: End time is out of range")
        return

    # Set the current frame position to the start frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    frame_count = start_frame
    while frame_count < end_frame:
        ret, frame = cap.read()
        if not ret:
            break

        frame_name = os.path.join(dest_dir, f"frame_{frame_count:06d}.jpg")
        cv2.imwrite(frame_name, frame)
        frame_count += 1

    cap.release()
    print(f"Frames extracted to {dest_dir}")

def parse_time_string(time_str: str) -> float:
    """Convert a time string in 'minutes.seconds' format to minutes as a float."""
    minutes, seconds = map(float, time_str.split('.'))
    return minutes + (seconds / 60)

def main() -> None:
    parser = argparse.ArgumentParser(description="Extract frames from a video file.")
    parser.add_argument("video_path", type=str, help="Path to the video file")
    parser.add_argument("dest_dir", type=str, help="Destination directory to save frames")
    parser.add_argument("--all", action="store_true", help="Extract all frames")
    parser.add_argument("--from", type=str, help="Start time in minutes.seconds format or 'start' to indicate the beginning", dest="start_time")
    parser.add_argument("--to", type=str, help="End time in minutes.seconds format or 'end' to indicate the end", dest="end_time")

    args = parser.parse_args()

    if args.start_time == "start":
        start_time = 0.0
    elif args.start_time:
        start_time = parse_time_string(args.start_time)
    else:
        start_time = None

    if args.end_time == "end":
        end_time = None
    elif args.end_time:
        end_time = parse_time_string(args.end_time)
    else:
        end_time = None

    if args.all:
        start_time, end_time = None, None

    extract_frames(args.video_path, args.dest_dir, start_time, end_time)

if __name__ == "__main__":
    main()
